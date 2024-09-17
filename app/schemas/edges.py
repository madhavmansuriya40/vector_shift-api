from pydantic import BaseModel
from typing import Dict, Any


class Edge(BaseModel):
    source: str
    sourceHandle: str
    target: str
    targetHandle: str
    type: str
    animated: bool
    markerEnd: Dict[str, Any]
    id: str
