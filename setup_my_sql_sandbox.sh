#!/bin/bash

# Met à jour la liste des paquets
echo "Mise à jour de la liste des paquets..."
apt update

# Installe le paquet mysql-server
echo "Installation de mysql-server..."
apt install -y mysql-server

# Vérifie l'installation de MySQL
echo "Vérification de l'installation de MySQL..."
mysql_version=$(mysql --version)
if [[ $? -eq 0 ]]; then
    echo "MySQL a été installé avec succès : $mysql_version"
else
    echo "L'installation de MySQL a échoué."
    exit 1
fi

# Démarre le service MySQL
echo "Démarrage du service MySQL..."
service mysql start

# Vérifie si le service MySQL a démarré correctement
if [[ $? -eq 0 ]]; then
    echo "Le service MySQL a démarré avec succès."
else
    echo "Le service MySQL a échoué à démarrer."
    exit 1
fi

# Connexion à MySQL via la ligne de commande
echo "Connexion à MySQL en tant que root..."
mysql -uroot -e "quit"

if [[ $? -eq 0 ]]; then
    echo "Connexion réussie à MySQL."
else
    echo "Échec de la connexion à MySQL."
    exit 1
fi

echo "La sandbox MySQL est prête à l'emploi !"
