from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import modele, schemas, database

# Création des tables dans la base de données
modele.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Mon premier Blog API")

# 1. Creer un article
@app.post("/api/articles", response_model=schemas.ArticleResponse, status_code=201)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(database.get_db)):
    db_article = modele.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

# 2. Lire tous les articles
@app.get("/api/articles")
def read_articles(db: Session = Depends(database.get_db)):
    return db.query(modele.Article).all()

# 3. Lire un article par son ID
@app.get("/api/articles/{id}")
def read_article(id: int, db: Session = Depends(database.get_db)):
    article = db.query(modele.Article).filter(modele.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé !")
    return article

# 4. Supprimer un article
@app.delete("/api/articles/{id}")
def delete_article(id: int, db: Session = Depends(database.get_db)):
    article = db.query(modele.Article).filter(modele.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Impossible de supprimer : ID inexistant")
    db.delete(article)
    db.commit()
    return {"message": "L'article a été supprimé avec succès"}

# 5. Modifier un article
@app.put("/api/articles/{id}", response_model=schemas.ArticleResponse)
def update_article(id: int, updated_data: schemas.ArticleCreate, db: Session = Depends(database.get_db)):
    article_query = db.query(modele.Article).filter(modele.Article.id == id)
    article = article_query.first()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article non trouvé")
    
    # On met à jour les champs
    article_query.update(updated_data.dict(), synchronize_session=False)
    db.commit()
    return article_query.first()

# 6. Rechercher un article (par titre ou contenu)
@app.get("/api/articles/search")
def search_articles(query: str, db: Session = Depends(database.get_db)):
    articles = db.query(modele.Article).filter(
        modele.Article.title.contains(query) | modele.Article.content.contains(query)
    ).all()
    return articles
