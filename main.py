from io import BytesIO
from PIL import Image
from fastapi import APIRouter, FastAPI
from fastapi import UploadFile,File
from yolo_model import model
from logger import logger


app=FastAPI(root_path="/food-classification")


@app.get("/")
def health_check():
    return{"status":"success healthcheck"}


@app.post("/detect_category")
async def detect_image_category(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(BytesIO(contents)).convert("RGB")

        results = model(image)
        result = results[0]

        bboxes = result.boxes
        conf = bboxes.conf
        cls = bboxes.cls

        re_food_category_list = []

        for c, cl in zip(conf, cls):
            if c > 0.5:
                re_food_category_list.append(int(cl+1))

        status = len(re_food_category_list) > 0
        logger.info(f" {file.filename} | cls: {re_food_category_list}")
        return {
            "cls": re_food_category_list,
            "status": status
        }

    except Exception as e:
        logger.error(f"{file.filename} | {str(e)}")
        return {
            "error": str(e)
        }

