from fastapi import FastAPI
from app.databases import Base, engine
from app.routes import transactions, analytics, users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Tracker API",
    description="Advanced Finance Backend with JWT, Analytics, and Role-Based Access",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(transactions.router)
app.include_router(analytics.router)
@app.get("/")
def home():
    return {"message": "Finance Tracker API Running 🚀"}