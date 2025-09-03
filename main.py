from fastapi import FastAPI
from starlette.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health():
    return JSONResponse(content="Ok", status_code=200, media_type="text/plain")

