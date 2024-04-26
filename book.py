from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

from db import load_book, save_book
from schema import BookInput, BookOutput

app = FastAPI()

books = load_book()


@app.get("/api/books")
def get_books(category: str|None = None, id_: int|None = None) -> list[BookOutput]:
  result = books
  if category:
    result = [book for book in books if book.category == category]
  if id_:
    return [book for book in result if book.id_ == id_]
  return result

@app.get("/api/books/{id_}")
def get_book_byid_(id_: int) -> BookOutput:
  result = [book for book in books if book.id_ == id_]
  if result:
    return result[0]
  raise HTTPException(status_code=404, detail=f"No book with id={id_}")

if __name__ == "__main__":
  uvicorn.run("book:app",reload=True)

@app.post("/api/books")
def add_book(book: BookInput) -> BookOutput:
    new_book = BookOutput(
        title=book.title,
        isbn=book.isbn,
        category=book.category,
        publication=book.publication,
        price=book.price,
        id_=len(books) + 1,
    )
    books.append(new_book)
    save_book(books)
    return new_book


@app.delete("/api/books/{id_}")
def delete_book(id_: int):
    matches = [book for book in books if book.id_ == id_]
    if matches:
        books.remove(matches[0])
        save_book(books)
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")

@app.put("/api/books/{id_}")
def update_book(id_: int, new_book: BookInput) -> BookOutput:
    matches = [book for book in books if book.id_ == id_]
    if matches:
        book = matches[0]
        book.title = new_book.title
        book.isbn = new_book.isbn
        book.category = new_book.category
        book.publication = new_book.publication
        book.price = new_book.price
        save_book(books)
        return book
    else:
        raise HTTPException(status_code=404, detail=f"No book with _id={id_}")

