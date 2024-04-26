from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

app = FastAPI()

books =


@app.get("/api/books")
def get_books(category: str|None = None, _id: int|None = None) -> list:
  result = books
  if category:
    result = [book for book in books if book['category'] == category]
  if _id:
    return [book for book in result if book['_id'] == _id]
  return result

@app.get("/api/books/{_id}")
def get_book_by_id(_id: int) -> dict:
  result = [book for book in books if book['_id'] == _id]
  if result:
    return result[0]
  raise HTTPException(status_code=404, detail=f"No book with id={_id}")

if __name__ == "__main__":
  uvicorn.run("book:app",reload=True)





