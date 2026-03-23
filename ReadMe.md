# API Blog Backend - Documentation Complète

Ce projet est une API construite avec **FastAPI**. Elle permet de gérer un système de blog simple (CRUD : Create, Read, Update, Delete) avec une base de données SQLite.

## Technologies & Architecture
- **Langage** : Python 3.12
- **Framework** : FastAPI (pour la rapidité et Swagger automatique)
- **ORM** : SQLAlchemy (pour la gestion de la base de données)
- **Validation** : Pydantic (pour garantir que les données envoyées sont correctes)
- **Base de données** : SQLite (stockage local dans `blog.db`)

## Installation et Démarrage local

1. **Prérequis** : Avoir Python installé.
2. **Installer les dépendances** :
   ```bash
   pip install fastapi uvicorn sqlalchemy

## Accès à la Documentation Technique

Pour faciliter le test et la maintenance de l'API, une documentation interactive a été mise en place. Elle est générée automatiquement par le framework FastAPI.

**Lien local** : http://127.0.0.1:8000/docs 

**Note** : Ce lien est accessible une fois le serveur local lancé via la commande **uvicorn**.

Cette interface (Swagger UI) permet de tester chaque "**endpoint**" (POST, GET, PUT, DELETE) directement depuis le navigateur sans avoir besoin d'un outil externe comme Postman.
