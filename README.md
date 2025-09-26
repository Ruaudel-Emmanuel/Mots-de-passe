🛡️ Générateur de Mots de Passe avec Historique
À propos de ce projet
Ce projet est un outil de bureau simple, léger et efficace, conçu pour générer des mots de passe aléatoires et robustes. Son interface graphique intuitive permet de créer des mots de passe personnalisés et de les sauvegarder localement dans un fichier texte pour en garder une trace sécurisée.

L'objectif est de fournir une solution "hors ligne" pour la création et la gestion simple de mots de passe, sans dépendre de services en ligne.

✨ Fonctionnalités principales
Personnalisation complète : Choisissez la longueur du mot de passe et sa complexité (majuscules, chiffres, caractères spéciaux).

Génération instantanée : Créez un nouveau mot de passe en un seul clic.

Copie facile : Un bouton "Copier" permet de transférer le mot de passe dans le presse-papiers pour une utilisation immédiate.

Sauvegarde intelligente :

Chaque mot de passe est sauvegardé dans un fichier mot_de_passe_sauvegardé.txt.

Avant chaque enregistrement, l'application demande une description (ex : "Gmail", "Facebook") pour savoir à quoi sert le mot de passe.

Chaque entrée est horodatée (date et heure précises) pour un suivi chronologique.

Les nouveaux mots de passe sont ajoutés à la fin du fichier, sans jamais écraser les anciens.

🚀 Comment l'utiliser ?
Assurez-vous d'avoir Python 3 installé sur votre machine.

Sauvegardez le code dans un fichier nommé Motsdepasse.py.

Ouvrez un terminal ou une invite de commandes, naviguez jusqu'au dossier contenant le fichier, et lancez le script avec la commande :

bash
python Motsdepasse.py
L'application se lance :

Ajustez la longueur et cochez les options de complexité.

Cliquez sur Générer.

Pour enregistrer, cliquez sur Sauvegarder, entrez une description, et validez.

📂 Organisation du fichier de sauvegarde
Le fichier mot_de_passe_sauvegardé.txt est créé automatiquement dans le même dossier que le script. Chaque ligne est formatée de la manière suivante pour une lisibilité maximale :

text
Description       Date et Heure                  Mot de Passe
-----------       -------------------            --------------------
Gmail             2025-09-26 13:18:05            Ex&mple-Passw0rd!
GitHub            2025-09-26 13:19:21            An0ther_S3cure-P@ss
⚠️ Remarques importantes
Sécurité : Ce script est destiné à un usage personnel. Le fichier mot_de_passe_sauvegardé.txt contient des informations sensibles en clair. Assurez-vous qu'il est stocké dans un emplacement sécurisé et que votre ordinateur est protégé.

Droits d'accès : Le script doit avoir les permissions d'écrire des fichiers dans le dossier où il est exécuté.
