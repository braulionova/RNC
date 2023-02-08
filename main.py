from fastapi import FastAPI, BackgroundTasks, HTTPException, Response, Body
from pydantic import BaseModel
from extract import *
import os


SECRET = os.getenv("SECRET")

#
app = FastAPI()

class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    driver=createDriver()

    homepage = getGoogleHomepage(driver)
    driver.close()
    return homepage

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}

class Empresa(BaseModel):
    rnc: str
        
@app.post("/get_rnc")
async def get_rnc(empresa: Empresa = Body()):
    driver=createDriver()
    #nombre empresa
    nombre_empresa = getRNC(driver, empresa.rnc)
    driver.close()
    #return
    return {"nombre_empresa": str(nombre_empresa)}
    


