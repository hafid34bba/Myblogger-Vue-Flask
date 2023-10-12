# Utiliser une image de Node.js LTS
FROM node:lts-alpine as build-stage

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier 'package.json' et 'package-lock.json'
COPY package*.json ./

# Installer les dépendances
RUN npm install

# Copier les fichiers du projet
COPY . .

# Construire l'application
RUN npm run build

# Deuxième étape : Utiliser un serveur HTTP léger pour servir l'application
FROM nginx:stable-alpine as production-stage

# Copier les fichiers de build depuis la première étape
COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exposer le port 80
EXPOSE 80

# Commande par défaut
CMD ["nginx", "-g", "daemon off;"]
