from app.schemas.book import BookCreate

book = BookCreate(
    title='Clean Code',
    author='Robert C. Martin',
)

print(book)
print(book.title)
print(book.year)