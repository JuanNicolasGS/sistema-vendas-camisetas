# Deploy na Vercel - Passo a Passo

## Sim, a Vercel suporta Flask!

A Vercel funciona perfeitamente com Flask usando a estrutura serverless. Preparei todos os arquivos necessários.

## Passo a Passo para Deploy

### 1. Preparar o Código
✅ Já criei o arquivo `vercel.json` com as configurações
✅ Já criei a pasta `api/` com o arquivo necessário

### 2. Criar Conta na Vercel
1. Acesse [vercel.com](https://vercel.com)
2. Faça login com GitHub (recomendado)
3. É gratuito para projetos pessoais

### 3. Conectar ao GitHub
1. Suba seu código para um repositório GitHub
2. Na Vercel, clique "Import Project"
3. Conecte seu repositório do GitHub

### 4. Configurar Variáveis de Ambiente
Na Vercel, vá em Settings > Environment Variables e adicione:

- `SESSION_SECRET`: sua chave secreta
- `FORM_PASSWORD`: senha do formulário
- `GOOGLE_CREDENTIALS`: JSON das credenciais
- `GOOGLE_SHEET_NAME`: nome da planilha

### 5. Deploy Automático
- A Vercel fará o deploy automaticamente
- Cada commit no GitHub atualiza automaticamente

## Alternativas Mais Simples

### Render (Recomendado para Flask)
- Melhor suporte para Flask
- Setup mais simples
- Gratuito: 750 horas/mês

### PythonAnywhere
- Especializado em Python
- Interface web simples
- 1 app gratuita

### Replit Deployments (Mais Fácil)
- Clique em "Deploy" na interface do Replit
- Zero configuração
- Funciona imediatamente

## Minha Recomendação

Para você como estudante:

1. **Primeiro teste**: Use Replit Deployments (clique em Deploy)
2. **Para aprender**: Use Render (render.com)
3. **Para portfólio**: Use Vercel (vercel.com)

Qual opção prefere testar primeiro?