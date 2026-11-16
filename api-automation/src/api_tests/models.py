"""Response models. `extra="forbid"` turns any unexpected field into a test failure (contract drift)."""
from pydantic import BaseModel, ConfigDict


class Post(BaseModel):
    model_config = ConfigDict(extra="forbid")

    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    model_config = ConfigDict(extra="forbid")

    postId: int
    id: int
    name: str
    email: str
    body: str


class User(BaseModel):
    """Only the fields the tests rely on. Nested objects (address, company) are allowed but not checked."""

    model_config = ConfigDict(extra="allow")

    id: int
    name: str
    username: str
    email: str
