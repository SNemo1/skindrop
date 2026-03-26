import random
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"  # Так таблиця буде називатися в базі
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    balance = Column(Integer, default=1000)
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

skins = [
    {'name' : 'Awp Asimov', 'sum' : 15000 , 'procent' : 5.4},
    {'name' : 'AK47 Neon-Rider', 'sum' : 1000 , 'procent' : 24.6},
    {'name' : 'Awp Neo-Nuar', 'sum' : 5000 , 'procent' : 30},
    {'name' : 'glock Shinobu' ,'sum' : 500 , 'procent' : 40}
]

@app.get("/spin")
def spin_roulette():
    chances = [5.4, 24.6, 30, 40]
    winner = random.choices(skins, k = 1, weights = chances)
    return {"massage": f"Оце так пощастило! Тобі випав {winner[0]['name']} {winner[0]['sum']}"}

@app.post("/register/{username}")
def register_user(username: str, db: Session = Depends(get_db)):
    user = User(username=username)
    db.add(user)
    db.commit()

    return {"message": f"Гравець {username} успішно створений! Твій баланс 1000$"}


