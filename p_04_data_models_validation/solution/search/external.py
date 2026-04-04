from __future__ import annotations

from typing import TypedDict

from pydantic import BaseModel, ConfigDict, field_validator


class DocumentPayload(TypedDict):
    id: str
    text: str


class QueryPayload(TypedDict, total=False):
    text: str
    top_k: int


class DocumentIn(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    id: str
    text: str

    @field_validator("id", "text")
    @classmethod
    def validate_non_empty(cls, value: str) -> str:
        if not value:
            raise ValueError("must be non-empty")
        return value


class QueryIn(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    text: str
    top_k: int = 5

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        if not value:
            raise ValueError("text must be non-empty")
        return value

    @field_validator("top_k")
    @classmethod
    def validate_top_k(cls, value: int) -> int:
        if value <= 0:
            raise ValueError("top_k must be positive")
        return value
