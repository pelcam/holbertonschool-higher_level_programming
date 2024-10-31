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

# Installation des dépendances nécessaires pour MySQLdb
echo "Installation des dépendances pour MySQLdb..."
apt install -y python3-dev libmysqlclient-dev zlib1g-dev
if [[ $? -eq 0 ]]; then
    echo "Les dépendances ont été installées avec succès."
else
    echo "Échec de l'installation des dépendances pour MySQLdb."
    exit 1
fi

# Installation du module MySQLdb
echo "Installation du module MySQLdb..."
pip3 install mysqlclient==2.0.*
if [[ $? -eq 0 ]]; then
    echo "Module MySQLdb installé avec succès."
else
    echo "Échec de l'installation de MySQLdb."
    exit 1
fi

# Vérification de l'installation de MySQLdb
echo "Vérification de l'installation de MySQLdb..."
python3 -c "import MySQLdb; assert MySQLdb.version_info >= (2, 0), 'MySQLdb version is not 2.0.x'; print('MySQLdb version:', MySQLdb.version_info)"
if [[ $? -eq 0 ]]; then
    echo "MySQLdb est installé avec la version attendue."
else
    echo "MySQLdb n'est pas installé correctement."
    exit 1
fi

# Installation du module SQLAlchemy
echo "Installation du module SQLAlchemy..."
pip3 install SQLAlchemy==1.4.*
if [[ $? -eq 0 ]]; then
    echo "Module SQLAlchemy installé avec succès."
else
    echo "Échec de l'installation de SQLAlchemy."
    exit 1
fi

# Vérification de l'installation de SQLAlchemy
echo "Vérification de l'installation de SQLAlchemy..."
python3 -c "import sqlalchemy; assert sqlalchemy.__version__.startswith('1.4'), 'SQLAlchemy version is not 1.4.x'; print('SQLAlchemy version:', sqlalchemy.__version__)"
if [[ $? -eq 0 ]]; then
    echo "SQLAlchemy est installé avec la version attendue."
else
    echo "SQLAlchemy n'est pas installé correctement."
    exit 1
fi

echo "La sandbox MySQL et les modules MySQLdb et SQLAlchemy sont prêts à l'emploi !"
