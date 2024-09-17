from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from schemas.pipeline_response import ParsePipelineResponse
from schemas.pipeline import Pipeline
from pipeline.parser import Parser

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    try:
        pipeline = Pipeline(**pipeline_data)
    except Exception as ex:
        if 'validation errors for Pipeline' in str(ex):

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incomplete pipeline")
        else:

            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred.")

    print('4')
    # parser pipeline
    return await Parser.parse(pipeline=pipeline)
