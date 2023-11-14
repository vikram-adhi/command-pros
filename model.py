from pydantic import BaseModel
from enum import Enum

class ProductEnum(str, Enum):
    aos10 = "aos10"
    aos8 = "aos8"
    cppm = "cppm"

class CommandRetriever(BaseModel):
    input_text: str
    product: ProductEnum