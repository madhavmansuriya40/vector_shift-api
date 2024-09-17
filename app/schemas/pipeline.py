from pydantic import BaseModel
from typing import List

from schemas.edges import Edge
from schemas.node import Node


class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]
