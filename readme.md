# Gestion événement 

## Description

Ce projet est une application C qui permet de gérer des événement (mariage, anniversaire,cinéma). Il utilise Python pour générer des graphiques à partir de données stockées dans une base de données MySQL.

## Installation

1. Installer pip : `sudo apt install python3-pip`
2. Installer plotly: `pip install plotly`
3. Installer python-dev : `sudo apt-get install python-dev python3.10-dev`
4. Installer mysql-connector : `pip install mysql-connector-python`
5. Recréer la base de données pour l'adapter au projet grâce au fichier `event.sql`

## Exécution

1. Compiler le code dans le terminal taper `make`
2. Exécuter le programme : `./Gestion`
3. Supprimer les fichier .O : `make clean`

Le programme va se connecter à la base de données MySQL, récupérer les données nécessaires, les traiter en utilisant Python pour générer les graphiques, et les afficher à l'utilisateur.

Assurez-vous que la base de données MySQL est en cours d'exécution avant d'exécuter le programme.
