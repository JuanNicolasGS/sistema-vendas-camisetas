# Solução para Erro 404 - Deploy Flask

## Problema Identificado
O erro 404 NOT_FOUND na Vercel acontece porque a configuração serverless não está correta para Flask.

## Solução 1: Corrigir Vercel (Atualizado)

Já atualizei os arquivos:
- `vercel.json` - Nova configuração
- `app.py` - Adicionado handler para Vercel

### Passos para Re-deploy:
1. Faça commit das mudanças no GitHub
2. A Vercel vai fazer re-deploy automaticamente
3. Aguarde 2-3 minutos

## Solução 2: Render (Recomendado para Flask)

O Render funciona melhor com Flask. Use esta configuração:

### Deploy no Render:
1. Acesse render.com
2. "New Web Service"
3. Conecte seu repositório GitHub
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Environment**: Python 3

### Variáveis de Ambiente (Render):
- `SESSION_SECRET`: sua chave secreta
- `FORM_PASSWORD`: senha do formulário
- `GOOGLE_CREDENTIALS`: JSON das credenciais (uma linha)
- `GOOGLE_SHEET_NAME`: nome da planilha

## Solução 3: Railway (Alternativa)

1. Acesse railway.app
2. "Deploy from GitHub"
3. Conecte repositório
4. Configure variáveis de ambiente
5. Deploy automático

## Arquivos Preparados

Todos os arquivos necessários já estão prontos:
- `requirements_github.txt` (renomeie para requirements.txt)
- `render.yaml` - Configuração Render
- `vercel.json` - Configuração Vercel corrigida
- `app.py` - Com handler Vercel

## Recomendação

Use o **Render** para deploy de Flask - é mais confiável e específico para aplicações Python web.