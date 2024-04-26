from fastapi import FastAPI
from fastapi import HTTPException
import uvicorn

app = FastAPI()

books = [
    {
        "_id": 1,
        "title": "Alien Explorations",
        "isbn": "978-3-16-148410-0",
        "category": "Science Fiction",
        "publication": "2020-07-15",
        "price": 350
    },
    {
        "_id": 2,
        "title": "Midnight Diner",
        "isbn": "978-4-16-148411-7",
        "category": "Fiction",
        "publication": "2018-12-20",
        "price": 280
    },
    {
        "_id": 3,
        "title": "Spiritual Guide",
        "isbn": "978-2-16-148412-4",
        "category": "Self-Help",
        "publication": "2019-03-10",
        "price": 220
    },
    {
        "_id": 4,
        "title": "City Stroll",
        "isbn": "978-1-16-148413-1",
        "category": "Travel",
        "publication": "2021-01-25",
        "price": 300
    },
    {
        "_id": 5,
        "title": "Mathematical Puzzles",
        "isbn": "978-9-16-148414-8",
        "category": "Academic",
        "publication": "2017-08-30",
        "price": 450
    },
    {
        "_id": 6,
        "title": "The Impact of Time",
        "isbn": "978-8-16-148415-5",
        "category": "Philosophy",
        "publication": "2016-04-15",
        "price": 380
    },
    {
        "_id": 7,
        "title": "Art of Baking",
        "isbn": "978-7-16-148416-2",
        "category": "Cooking",
        "publication": "2019-11-05",
        "price": 320
    },
    {
        "_id": 8,
        "title": "The Little Prince",
        "isbn": "978-6-16-148417-9",
        "category": "Children's Literature",
        "publication": "2015-06-25",
        "price": 180
    },
    {
        "_id": 9,
        "title": "World History",
        "isbn": "978-5-16-148418-6",
        "category": "History",
        "publication": "2018-10-30",
        "price": 280
    },
    {
        "_id": 10,
        "title": "Ecology of Earth",
        "isbn": "978-4-16-148419-3",
        "category": "Natural Science",
        "publication": "2021-06-15",
        "price": 360
    },
    {
        "_id": 11,
        "title": "Economic Theory",
        "isbn": "978-3-16-148420-9",
        "category": "Economics",
        "publication": "2017-01-20",
        "price": 400
    },
    {
        "_id": 12,
        "title": "Fitness Guide",
        "isbn": "978-2-16-148421-6",
        "category": "Health",
        "publication": "2020-03-10",
        "price": 300
    },
    {
        "_id": 13,
        "title": "The Path of Music",
        "isbn": "978-1-16-148422-3",
        "category": "Music",
        "publication": "2016-09-25",
        "price": 250
    },
    {
        "_id": 14,
        "title": "Introduction to Psychology",
        "isbn": "978-9-16-148423-0",
        "category": "Psychology",
        "publication": "2018-02-15",
        "price": 420
    },
    {
        "_id": 15,
        "title": "Photography Basics",
        "isbn": "978-8-16-148424-7",
        "category": "Photography",
        "publication": "2019-07-20",
        "price": 320
    },
    {
        "_id": 16,
        "title": "Animation Production",
        "isbn": "978-7-16-148425-4",
        "category": "Design",
        "publication": "2015-11-10",
        "price": 350
    },
    {
        "_id": 17,
        "title": "Programming Concepts",
        "isbn": "978-6-16-148426-1",
        "category": "Technology",
        "publication": "2017-03-05",
        "price": 500
    },
    {
        "_id": 18,
        "title": "Travel Photography",
        "isbn": "978-5-16-148427-8",
        "category": "Travel",
        "publication": "2016-08-15",
        "price": 290
    },
    {
        "_id": 19,
        "title": "Watercolor Techniques",
        "isbn": "978-4-16-148428-5",
        "category": "Art",
        "publication": "2018-12-10",
        "price": 380
    },
    {
        "_id": 20,
        "title": "Crafts and Design",
        "isbn": "978-3-16-148429-2",
        "category": "Design",
        "publication": "2020-01-25",
        "price": 270
    }
]


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





