from pydantic import BaseModel


class ParsePipelineResponse(BaseModel):
    num_nodes: int
    num_edges: int
    is_dag: bool
