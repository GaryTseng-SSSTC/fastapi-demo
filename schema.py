from sqlmodel import SQLModel, Field, Relationship

class BookInput(SQLModel):
    title: str
    isbn: str
    category: str
    publication: str
    price: float

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Book Name",
                "isbn": "abcd-1234",
                "category": "Fiction",
                "publication": "2023-10-20",
                "price": 120,
            }
        }

class Book(BookInput, table=True):
    id_: int | None = Field(primary_key=True, default=None)
    #auth_id: int = Field(foreign_key="author.id_")
    #author: "Author" = Relationship(back_populates="books")

    
class BookOutput(BookInput):
    id_: int

    class Config:
        json_schema_extra = {
            "example": {
                "id_": 1,
                "title": "The Book Name",
                "isbn": "abcd-1234",
                "category": "Fiction",
                "publication": "2023-10-20",
                "price": 120,
            }
        }


if __name__ == "__main__":
    book = BookOutput(
        id_=10, title="test", isbn="1234", category="test", publication="2023", price="30"
    )
    print(book)
    print(book.model_dump())
    print(book.model_dump_json())
    print(book.isbn)
    print(book.id_)
