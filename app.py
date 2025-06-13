import os
import logging
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")

# Google Sheets configuration
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def get_google_sheets_client():
    """Initialize Google Sheets client using service account credentials"""
    try:
        # Get credentials from environment variable
        creds_json = os.environ.get("GOOGLE_CREDENTIALS")
        if not creds_json:
            raise ValueError("GOOGLE_CREDENTIALS environment variable not set")
        
        # Parse JSON credentials
        creds_info = json.loads(creds_json)
        credentials = Credentials.from_service_account_info(creds_info, scopes=SCOPES)
        
        # Initialize gspread client
        client = gspread.authorize(credentials)
        return client
    except Exception as e:
        logging.error(f"Error initializing Google Sheets client: {e}")
        return None

def add_sale_to_sheet(sale_data):
    """Add sale data to Google Sheets"""
    try:
        client = get_google_sheets_client()
        if not client:
            return False, "Falha ao conectar com Google Sheets"

        sheet_name = os.environ.get("GOOGLE_SHEET_NAME", "Vendas de Camisetas")
        spreadsheet = client.open(sheet_name)
        worksheet = spreadsheet.sheet1

        # Prepara a linha de dados para inserir
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        row_data = [
            timestamp,
            sale_data['customer_name'],
            sale_data['tshirt_size'],
            sale_data['quantity'],
            sale_data['unit_price'],
            sale_data['total_price'],
            "Pago",  # Status de pagamento
            sale_data['payment_method']
        ]

        # Define o cabeçalho esperado
        expected_header = [
            "Data/Hora", "Nome do Cliente", "Tamanho", "Quantidade",
            "Valor Unitário", "Valor Total", "Status Pagamento", "Método de Pagamento"
        ]

        try:
            first_row = worksheet.row_values(1)
        except gspread.exceptions.APIError:
            first_row = []

        # CORREÇÃO DE INDENTAÇÃO: A verificação agora acontece fora do 'try'
        if first_row != expected_header:
            if first_row:
                worksheet.delete_rows(1)
            worksheet.insert_row(expected_header, 1)

        # Adiciona a nova linha de venda (APENAS UMA VEZ)
        worksheet.append_row(row_data)
        logging.info("Successfully added sale record to Google Sheets")
        return True, "Venda registrada com sucesso"

    except Exception as e:
        logging.error(f"Error adding sale to sheet: {e}")
        return False, f"Erro ao registrar venda: {str(e)}"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # --- 1. Coleta e valida os dados do formulário ---
            customer_name = request.form.get('customer_name')
            tshirt_size = request.form.get('tshirt_size')
            quantity = int(request.form.get('quantity', 0))
            payment_method = request.form.get('payment_method')
            unit_price = float(request.form.get('unit_price', 0))

            if not all([customer_name, tshirt_size, quantity > 0, payment_method]):
                flash('Erro: Todos os campos devem ser preenchidos corretamente.', 'error')
                return redirect(url_for('index'))

            # --- 2. Prepara os dados da venda ---
            sale_data = {
                'customer_name': customer_name,
                'tshirt_size': tshirt_size,
                'quantity': quantity,
                'unit_price': unit_price,  
                'total_price': quantity * unit_price,
                'payment_method': payment_method,
                'payment_status': "Pago"
            }

            # --- 3. Chama a função para adicionar na planilha ---
            success, message = add_sale_to_sheet(sale_data)
            
            if success:
                flash(message, 'success')
            else:
                flash(message, 'error')

        except Exception as e:
            # Captura qualquer outro erro inesperado e informa o usuário
            flash(f'Ocorreu um erro inesperado no processamento: {e}', 'error')
        
        return redirect(url_for('index'))

    # Se o método for GET, apenas renderiza a página
    return render_template('index.html')


@app.route('/health')
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# Vercel entry point
def handler(environ, start_response):
    return app(environ, start_response)

# For local development
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
