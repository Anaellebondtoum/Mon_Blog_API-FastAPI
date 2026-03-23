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
