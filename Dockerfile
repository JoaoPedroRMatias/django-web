FROM python:3.10.10-alpine3.17

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos do diretório do host para o diretório de trabalho
COPY . /app

# Instala as dependências
RUN pip install -r requirements.txt

# Define a porta em que a aplicação irá rodar
EXPOSE 8000

# Define o comando para rodar a aplicação
CMD ["python", "manage.py", "runserver"]