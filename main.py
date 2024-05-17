from fastapi import FastAPI, UploadFile, File, HTTPException, Response #import class FastAPI() từ thư viện fastapi
import subprocess
import os
import uuid
from random import randint
import sys
sys.path.append('./AI')
from image_test import run_model


IMAGE_FOLDER='./storage'
FUNCTION_FILE_PATH = "./AI/image_test.py"
FUNCTION_NAME="run"

app = FastAPI() # gọi constructor và gán vào biến app


@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}

@app.post("/model/image",status_code=200) # giống flask, khai báo phương thức get và url
async def image_test(image: UploadFile = File(...)): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    try:
        filename = image.filename
        content = await image.read()

        # Save the image in the uploads folder
        image_path = os.path.join(IMAGE_FOLDER, filename)
        with open(image_path, "wb") as buffer:
            buffer.write(content)

        output=run_model(filename)
        output=float(output)
        os.remove(image_path)
        return {"value":output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# db = []


# @app.post("/images")
# async def create_upload_file(file: UploadFile=File(...)):

#     file.filename = f"{uuid.uuid4()}.jpg"
#     contents = await file.read()  # <-- Important!

#     db.append(contents)

#     return {"filename": file.filename}


# @app.get("/images")
# async def read_random_file():

#     # get a random file from the image db
#     random_index = randint(0, len(db) - 1)

#     # return a response object directly as FileResponse expects a file-like object
#     # and StreamingResponse expects an iterator/generator
#     response = Response(content=db[random_index])

#     return response        