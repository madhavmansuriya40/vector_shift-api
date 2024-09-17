from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from schemas.pipeline_response import ParsePipelineResponse
from schemas.pipeline import Pipeline
from pipeline.parser import Parser

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def ready():
    return """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Service Status</title>
    </head>
    <body style="width: 100%; text-align: center;">

        <h2>Service Up and Running! 😈</h2>

        <p>
            <a href="https://vector-shift-api.onrender.com/docs" style="text-decoration: none; color: blue;">Click here open docs</a>
        </p>

    </body>
    </html>
    """


@app.post('/pipelines/parse', response_model=ParsePipelineResponse)
async def parse_pipeline(request: Request) -> ParsePipelineResponse:

    # Read and validate JSON data from request
    pipeline_data = await request.json()
    print("\n\n\n pipeline_data --> ", pipeline_data)
    pipeline = Pipeline(**pipeline_data)

    print("\n\n\n moulded pipeline_data --> ", pipeline_data)

    # parser pipeline
    print("\n\n\n calling parse")
    return await Parser.parse(pipeline=pipeline)
