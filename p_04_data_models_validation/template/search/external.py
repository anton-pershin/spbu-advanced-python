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
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError


class QueryIn(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    text: str
    top_k: int = 5

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError

    @field_validator("top_k")
    @classmethod
    def validate_top_k(cls, value: int) -> int:
        ##########################
        ### PUT YOUR CODE HERE ###
        ##########################
        raise NotImplementedError
