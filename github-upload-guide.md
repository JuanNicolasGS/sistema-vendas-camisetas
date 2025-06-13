# Como Subir para GitHub - Método Download/Upload

## Arquivos Principais do Projeto

Certifique-se de incluir estes arquivos no GitHub:

### Arquivos Essenciais:
- `app.py` - Aplicação principal Flask
- `main.py` - Ponto de entrada
- `templates/index.html` - Interface do usuário
- `static/style.css` - Estilos responsivos
- `config.py` - Configurações

### Arquivos para Deploy:
- `vercel.json` - Configuração Vercel
- `api/index.py` - Adaptador serverless
- `requirements_github.txt` - Dependências (renomeie para requirements.txt)

### Documentação:
- `README.md` - Documentação do projeto
- `.gitignore` - Arquivos a ignorar
- `.env.example` - Exemplo de variáveis

## Passo a Passo:

1. **Download**: No Replit, clique (...) → "Download as zip"
2. **Extrair**: Descompacte o arquivo no computador
3. **Renomear**: `requirements_github.txt` → `requirements.txt`
4. **Upload no GitHub**: 
   - Vá para seu repositório
   - Clique "Add file" → "Upload files"
   - Arraste todos os arquivos
   - Commit: "Sistema de vendas de camisetas completo"

## Após Upload:

Deploy imediato disponível em:
- Vercel.com (conecte repositório)
- Render.com (conecte repositório)
- Railway.app (conecte repositório)

Todas as plataformas detectarão automaticamente que é um projeto Flask.