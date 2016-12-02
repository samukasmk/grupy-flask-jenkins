# define a imagem oficial do python como base
FROM python:3.5

# copia todos arquivos do projeto para o container /ap//
COPY . /app

# define a pasta de execução do docker (tipo: cd /app)
WORKDIR /app

# instala as dependencias do projeto
RUN pip install -r requirements.txt

# define o comando que rodará no container
CMD [ "python", "./app.py" ]

# para buildar esse container use o comando:
### docker build -t <docker username>/<docker repo>:<docker tag> .
### exemplo:
### docker build -t samukasmk/grupy-flask-jenkins:latest .

# para enviar essa imagem gerada ao docker hub
### docker login
### docker push <docker username>/<docker repo>:<docker tag>
# exemplo
### docker push samukasmk/grupy-flask-jenkins:latest

# para executar esse projeto na sua maquina
### docker run -p 80:80 samukasmk/grupy-flask-jenkins:latest
