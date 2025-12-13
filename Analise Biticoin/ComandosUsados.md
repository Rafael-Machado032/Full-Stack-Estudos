## Configurar o ambiente virtual

### 1. Criar o ambiente virtual
No diretório do projeto:
```bash
python -m venv venv
```

### 2. Ativar o ambiente virtual
- Windows (CMD):
```bash
venv\Scripts\activate
```
- Windows (PowerShell):
```powershell
.\venv\Scripts\Activate.ps1
```
- macOS / Linux:
```bash
source venv/bin/activate
```

## Instalar dependências
Instale FastAPI, Uvicorn e outras bibliotecas necessárias:
```bash
pip install "fastapi[standard]" uvicorn requests pandas
```

## Estrutura e primeiro arquivo FastAPI
Crie a pasta `backend` e o arquivo `backend/main.py`:

Estrutura:
```
backend/
    └─ main.py
```

Conteúdo de `backend/main.py`:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
        return {"message": "Hello, World!"}
```

## Executar o servidor
No terminal (com o ambiente ativado), execute:
```bash
uvicorn backend.main:app --reload
```

O que significam os parâmetros:
- `backend.main`: arquivo `main.py` dentro da pasta `backend`.
- `:app`: variável `app` exposta pelo FastAPI.
- `--reload`: reinicia automaticamente ao salvar alterações.

(Se desejar, especifique host/porta: `--host 127.0.0.1 --port 8000`)

## Instalar a biblioteca de gráficos

```bash
npm install react-plotly.js plotly.js-dist
```

```bash
npm i --save-dev @types/react-plotly.js
```

**Nota:** Este comando instala os tipos TypeScript para `react-plotly.js`, necessário para melhor autocompletar e verificação de tipos em projetos TypeScript.


## Execultar Servidores

**Back End**
Execulta na pasta raiz
```bash

venv\Scripts\activate

uvicorn backend.main:app --reload

```
**Front End**
Execulta na pasta frontend
```bash

    npm run dev
    
```
