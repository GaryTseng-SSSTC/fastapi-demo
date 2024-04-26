from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

from db import load_book

app = FastAPI()

books = load_book()


@app.get("/api/books")
def get_books(category: str|None = None, id_: int|None = None) -> list:
  result = books
  if category:
    result = [book for book in books if book['category'] == category]
  if id_:
    return [book for book in result if book['id_'] == id_]
  return result

@app.get("/api/books/{id_}")
def get_book_byid_(id_: int) -> dict:
  result = [book for book in books if book['id_'] == id_]
  if result:
    return result[0]
  raise HTTPException(status_code=404, detail=f"No book with id={id_}")

if __name__ == "__main__":
  uvicorn.run("book:app",reload=True)





