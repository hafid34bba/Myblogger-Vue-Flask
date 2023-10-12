# Utilisez une image Python officielle comme image de base
FROM python:3.9

# Répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu du répertoire courant dans le conteneur à /app
COPY . /app

# Installez Flask et les autres dépendances
RUN pip install -r requirements.txt

RUN pip install gunicorn
# Exposez le port sur lequel l'application fonctionnera
EXPOSE 5000

# Commande pour lancer Gunicorn et servir l'application Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_dep_app()"]