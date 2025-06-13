# 👕 Sistema de Registro de Vendas de Camisetas

Uma aplicação web Flask completa para registrar vendas de camisetas com integração automática ao Google Sheets.

[![Deploy](https://img.shields.io/badge/Deploy-Vercel-black)](https://vercel.com/new/clone?repository-url=https://github.com/SEU-USUARIO/sistema-vendas-camisetas)
[![Deploy](https://img.shields.io/badge/Deploy-Render-46E3B7)](https://render.com/deploy)

## 🚀 Demo

[Ver aplicação funcionando](https://SEU-DEPLOY-URL.vercel.app)

## 📱 Totalmente Responsivo

Funciona perfeitamente em:
- 📱 Smartphones
- 💻 Tablets  
- 🖥️ Desktops

## Características

- Interface em português com design responsivo
- Campos simplificados: nome, tamanho, quantidade, valor, status de pagamento e método
- Métodos de pagamento: Cartão, Pix e Dinheiro Físico
- Proteção por senha
- Integração automática com Google Sheets
- Cálculo automático do valor total

## Campos do Formulário

1. **Senha** - Para autenticação
2. **Nome do Cliente** - Nome completo do cliente
3. **Tamanho da Camiseta** - PP, P, M, G, GG, XGG
4. **Quantidade** - Número de camisetas
5. **Valor Unitário** - Preço por camiseta em R$
6. **Status do Pagamento** - Pago ou Não Pago
7. **Método de Pagamento** - Cartão, Pix ou Dinheiro Físico

## Configuração no Replit

### 1. Configuração do Google Sheets

#### Passo 1: Criar um Projeto no Google Cloud
1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto ou selecione um existente
3. Ative a API do Google Sheets:
   - Vá para "APIs e Serviços" > "Biblioteca"
   - Procure por "Google Sheets API"
   - Clique em "Ativar"

#### Passo 2: Criar uma Conta de Serviço
1. No Google Cloud Console, vá para "APIs e Serviços" > "Credenciais"
2. Clique em "Criar Credenciais" > "Conta de serviço"
3. Preencha os dados:
   - Nome: `vendas-camisetas`
   - Descrição: `Conta para registro de vendas`
4. Clique em "Criar e continuar"
5. Pule as permissões opcionais
6. Clique em "Concluído"

#### Passo 3: Gerar Chave JSON
1. Na lista de contas de serviço, clique na conta criada
2. Vá para a aba "Chaves"
3. Clique em "Adicionar chave" > "Criar nova chave"
4. Selecione "JSON" e clique em "Criar"
5. Baixe o arquivo JSON (será usado nas variáveis de ambiente)

#### Passo 4: Criar e Compartilhar a Planilha
1. Crie uma nova planilha no [Google Sheets](https://sheets.google.com)
2. Nomeie como "Vendas de Camisetas" (ou outro nome de sua preferência)
3. Copie o email da conta de serviço (encontrado no arquivo JSON baixado)
4. Compartilhe a planilha com este email, dando permissão de "Editor"

### 2. Configuração das Variáveis de Ambiente no Replit

1. No seu projeto Replit, vá para a aba "Secrets" (ícone de cadeado)
2. Adicione as seguintes variáveis:

#### SESSION_SECRET
- **Nome:** `SESSION_SECRET`
- **Valor:** Uma string aleatória para segurança (ex: `minha-chave-super-secreta-123456`)

#### FORM_PASSWORD
- **Nome:** `FORM_PASSWORD`
- **Valor:** A senha que será usada para acessar o formulário (ex: `admin123`)

#### GOOGLE_CREDENTIALS
- **Nome:** `GOOGLE_CREDENTIALS`
- **Valor:** Todo o conteúdo do arquivo JSON baixado, em uma única linha
- **Exemplo:**
```json
{"type": "service_account", "project_id": "seu-projeto", "private_key_id": "123abc", "private_key": "-----BEGIN PRIVATE KEY-----\nSUA_CHAVE_AQUI\n-----END PRIVATE KEY-----\n", "client_email": "vendas-camisetas@seu-projeto.iam.gserviceaccount.com", "client_id": "123456789", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/vendas-camisetas%40seu-projeto.iam.gserviceaccount.com"}
```

#### GOOGLE_SHEET_NAME
- **Nome:** `GOOGLE_SHEET_NAME`
- **Valor:** Nome exato da sua planilha (ex: `Vendas de Camisetas`)

### 3. Executar a Aplicação

1. Clique no botão "Run" no Replit
2. A aplicação estará disponível na URL mostrada no painel direito
3. Use a senha configurada em `FORM_PASSWORD` para acessar o formulário

## Estrutura da Planilha

Quando a primeira venda for registrada, a planilha será automaticamente configurada com os seguintes cabeçalhos:

| Data/Hora | Nome do Cliente | Tamanho | Quantidade | Valor Unitário | Valor Total | Status Pagamento | Método de Pagamento |
|-----------|-----------------|---------|------------|----------------|-------------|------------------|-------------------|

## Solução de Problemas

### Erro de Credenciais do Google
- Verifique se o arquivo JSON foi copiado corretamente para `GOOGLE_CREDENTIALS`
- Confirme que a conta de serviço tem acesso à planilha
- Certifique-se de que a API do Google Sheets está ativada

### Erro de Planilha Não Encontrada
- Verifique se o nome em `GOOGLE_SHEET_NAME` corresponde exatamente ao nome da planilha
- Confirme que a planilha foi compartilhada com o email da conta de serviço

### Senha Incorreta
- Verifique se a senha está configurada corretamente em `FORM_PASSWORD`
- A senha é case-sensitive (diferencia maiúsculas de minúsculas)

## Segurança

- Nunca compartilhe suas credenciais do Google
- Use senhas fortes para `FORM_PASSWORD` e `SESSION_SECRET`
- As credenciais são armazenadas com segurança nas variáveis de ambiente do Replit

## Personalização

Para personalizar a aplicação:

1. **Alterar cores:** Edite o arquivo `static/style.css`
2. **Modificar campos:** Edite `templates/index.html` e `app.py`
3. **Adicionar validações:** Modifique a função de validação em `app.py`

## Suporte

Se encontrar problemas:
1. Verifique os logs no console do Replit
2. Confirme que todas as variáveis de ambiente estão configuradas
3. Teste a conexão com a planilha através do endpoint `/health`