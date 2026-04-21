# Imagem base oficial do Python
FROM python:3.10-slim

# Evita arquivos .pyc e buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Copia dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o projeto
COPY . .

# Comando padrão
CMD ["python", "main.py"]