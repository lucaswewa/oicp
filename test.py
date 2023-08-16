from dataclasses import dataclass
from typing import Optional, List
from marshmallow import Schema, fields, validate, post_load
import json

@dataclass
class Book:
    title: str
    isbn: str

@dataclass
class User:
    email: str
    books: Optional[List[Book]]

def validate_isbn(isbn: str) -> None:
    """Validates the isbn with some code (omitted), raise marshmallow.ValidationError if validation did not pass."""

class BookSchema(Schema):
    title = fields.String(required=True, validate=validate.Length(max=120))
    isbn = fields.String(required=True, validate=validate_isbn)

class UserSchema(Schema):
    email = fields.Email(required=True)
    books = fields.Nested(BookSchema, many=True, required=False)

    @post_load
    def make_obj(self, data, **kwargs):
        return User(**data)

raw_data_str = """{
    "email": "foo@bar.com",
    "books": [
        {"title": "Hitchhikers Guide to the Galaxy", "isbn": "123456789"},
        {"title": "Clean Coder", "isbn": "987654321"}
    ]
}"""
json_data = json.loads(raw_data_str)
schema = UserSchema()
user = schema.load(json_data)
print(user)
