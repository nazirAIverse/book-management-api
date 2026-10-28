from app.db.base import Base
from app.db.session import engine

from app.models.book import Book
from app.models.user import User


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")