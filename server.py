from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()
latest_image_path = "latest.jpg"

@app.post("/upload")
async def upload_image(request: Request):
    data = await request.body()
    with open(latest_image_path, "wb") as f:
        f.write(data)
    return {"status": "received"}

@app.get("/latest")
def get_latest():
    return FileResponse(latest_image_path)