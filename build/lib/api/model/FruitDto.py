from pydantic import BaseModel


class FruitDto(BaseModel):
    file: str
