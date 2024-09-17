from fastapi import HTTPException, status
from pydantic import ValidationError
import networkx as nx

from schemas.pipeline import Pipeline
from schemas.pipeline_response import ParsePipelineResponse


class Parser:
    def __init__(self) -> None:
        pass

    async def parse(pipeline: Pipeline) -> ParsePipelineResponse:

        # Extract nodes and edges
        nodes = pipeline.nodes
        edges = pipeline.edges

        print("\n\n\n coming here ")
        # Count nodes and edges
        num_nodes: int = len(nodes)
        num_edges: int = len(edges)
        if num_edges == 0 or num_nodes == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No graph can be with 0 edge or 0 node")

        try:
            # Create a directed graph
            G = nx.DiGraph()

            # Add nodes to the graph
            for node in nodes:
                G.add_node(node.id)

            # Add edges to the graph
            for edge in edges:
                G.add_edge(edge.source, edge.target)

            # Check if the graph is a DAG
            is_dag: bool = nx.is_directed_acyclic_graph(G)

            # Return the results
            return ParsePipelineResponse(
                num_nodes=num_nodes,
                num_edges=num_edges,
                is_dag=is_dag
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred.")
