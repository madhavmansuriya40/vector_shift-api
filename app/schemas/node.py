from pydantic import BaseModel
from typing import Dict


class Node(BaseModel):
    id: str
    type: str
    position: Dict[str, float]
    data: Dict[str, str]
    width: float
    height: float
    selected: bool
    positionAbsolute: Dict[str, float]
    dragging: bool
