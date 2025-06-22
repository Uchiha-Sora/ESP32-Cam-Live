from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil

app = FastAPI()
latest_image_path = "latest.jpg"

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    with open(latest_image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"status": "received"}

@app.get("/latest")
def get_latest():
    return FileResponse(latest_image_path)
