from pydantic import BaseModel

# Example model definitions
class User(BaseModel):
	name: str
	age: int

class UserCollection(BaseModel):
	users: list[User]