from fastapi import FastAPI, UploadFile, File, HTTPException, Response #import class FastAPI() từ thư viện fastapi
import subprocess
import os

IMAGE_FOLDER='./storage'
FUNCTION_FILE_PATH = "./AI/image_test.py"

app = FastAPI() # gọi constructor và gán vào biến app


@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}

@app.post("/model/image") # giống flask, khai báo phương thức get và url
async def image_test(image: UploadFile = File(...)): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    try:
        filename = image.filename
        content = await image.read()

        # Save the image in the uploads folder
        image_path = os.path.join(IMAGE_FOLDER, filename)
        with open(image_path, "wb") as buffer:
            buffer.write(content)


        # Call image_test.py with the image name as an argument
        process = subprocess.run(
        [FUNCTION_FILE_PATH, filename], capture_output=True, text=True, check=True
        )
        result_float = float(process.stdout.strip())  # Convert output to 
        return Response(content=result_float, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))