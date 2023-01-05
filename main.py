from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# import matplotlib.pyplot as plt
# from talib import abstract
# import talib as tb
# import MetaTrader5 as mt5
from datetime import datetime
# import pandas as pd
import time
import os
import json

app = FastAPI()

origins = [
   "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ativo/{teste}")
async def root(teste):
    lista = os.listdir(os.getcwd()+'/datas')
    teste = teste.upper()
    ativo = "df_"+teste
    
    x = list(map(str,lista))
    y = "-".join(x)

    if y.find(ativo) !=-1:
        with open(os.getcwd()+'/datas'+'/'+ativo, 'r') as f:
            data = json.load(f)

        return {
            'result':f"Yes, {ativo} exists in list",
            'data':data
        }
    


    else:
        return {'result':f"No, {ativo}  does not exists in list"}

    # for item in lista:
    #     with open(os.getcwd()+'/datas'+'/'+item, 'r') as f:
    #         data = json.load(f)
    #         # df = pd.DataFrame(data)
    #         return {'json_obj':data}
   