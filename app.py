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
        
        # Open the spreadsheet by name
        sheet_name = os.environ.get("GOOGLE_SHEET_NAME", "Vendas de Camisetas")
        try:
            spreadsheet = client.open(sheet_name)
        except Exception as e:
            logging.error(f"Error opening spreadsheet '{sheet_name}': {e}")
            return False, f"Planilha '{sheet_name}' não encontrada. Verifique o nome e as permissões."
        
        worksheet = spreadsheet.sheet1
        
        # Prepare data row
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row_data = [
            timestamp,
            sale_data['customer_name'],
            sale_data['tshirt_size'],
            sale_data['quantity'],
            sale_data['unit_price'],
            sale_data['total_price'],
            sale_data['payment_status'],
            sale_data['payment_method']
        ]
        
        # Add header row if sheet is empty
        if len(worksheet.get_all_records()) == 0:
            header_row = [
                "Data/Hora",
                "Nome do Cliente",
                "Tamanho",
                "Quantidade",
                "Valor Unitário",
                "Valor Total",
                "Status Pagamento",
                "Método de Pagamento"
            ]
            worksheet.append_row(header_row)
        
        # Add the data
        worksheet.append_row(row_data)
        logging.info(f"Successfully added sale record to Google Sheets")
        return True, "Venda registrada com sucesso"
        
    except Exception as e:
        sheet_name = os.environ.get("GOOGLE_SHEET_NAME", "Vendas de Camisetas")
        logging.error(f"Error adding sale to sheet: {e}")
        if "insufficient authentication scopes" in str(e).lower():
            return False, "Erro de permissões. Verifique se a API do Google Drive está ativada e a planilha foi compartilhada corretamente."
        elif "not found" in str(e).lower():
            return False, f"Planilha '{sheet_name}' não encontrada. Verifique o nome exato da planilha."
        else:
            return False, f"Erro ao registrar venda: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Verify password
            password = request.form.get('password')
            required_password = os.environ.get("FORM_PASSWORD", "admin123")
            
            if password != required_password:
                flash("Senha inválida. Tente novamente.", "error")
                return render_template('index.html')
            
            # Validate required fields
            required_fields = ['customer_name', 'tshirt_size', 'quantity', 'unit_price', 'payment_method', 'payment_status']
            field_names = {
                'customer_name': 'Nome do Cliente',
                'tshirt_size': 'Tamanho da Camiseta',
                'quantity': 'Quantidade',
                'unit_price': 'Valor Unitário',
                'payment_method': 'Método de Pagamento',
                'payment_status': 'Status do Pagamento'
            }
            for field in required_fields:
                if not request.form.get(field):
                    flash(f"Por favor, preencha o campo {field_names[field]}.", "error")
                    return render_template('index.html')
            
            # Calculate total price
            quantity = int(request.form.get('quantity', 0))
            unit_price = float(request.form.get('unit_price', 0))
            total_price = quantity * unit_price
            
            # Prepare sale data
            sale_data = {
                'customer_name': request.form.get('customer_name'),
                'tshirt_size': request.form.get('tshirt_size'),
                'quantity': quantity,
                'unit_price': unit_price,
                'total_price': total_price,
                'payment_method': request.form.get('payment_method'),
                'payment_status': request.form.get('payment_status')
            }
            
            # Add to Google Sheets
            success, message = add_sale_to_sheet(sale_data)
            
            if success:
                flash("Venda registrada com sucesso!", "success")
                return redirect(url_for('index'))
            else:
                flash(f"Erro ao registrar venda: {message}", "error")
                return render_template('index.html')
                
        except ValueError as e:
            flash("Por favor, digite números válidos para quantidade e valor.", "error")
            return render_template('index.html')
        except Exception as e:
            logging.error(f"Error processing form: {e}")
            flash("Ocorreu um erro ao processar sua solicitação. Tente novamente.", "error")
            return render_template('index.html')
    
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
