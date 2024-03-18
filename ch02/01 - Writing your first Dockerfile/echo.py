import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse


app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def echo(request: Request):
    headers = "\n".join([f"{key}: {value}" for key, value in request.headers.items()])
    body = await request.body()
    body_text = body.decode() if body else "No body"
    return (
        f"METHOD: {request.method}\n"
        f"HEADERS:\n{headers}"
        f"BODY:\n{body_text}"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
