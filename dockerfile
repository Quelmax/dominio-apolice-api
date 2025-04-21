# Use imagem oficial do Python
FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta que o Uvicorn vai escutar
EXPOSE 80

# Comando para rodar a API FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
