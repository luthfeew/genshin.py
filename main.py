import genshin
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

cookies = {"ltuid": 119480035, "ltoken": "cnF7TiZqHAAvYqgCBoSPx5EjwezOh1ZHoqSHf7dT"}
client = genshin.Client(cookies)


@app.get("/full/{uid}")
async def read_item(uid: int):
    try:
        data = await client.get_full_genshin_user(uid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"uid": uid, "data": data}


@app.get("/partial/{uid}")
async def read_item(uid: int):
    try:
        data = await client.get_partial_genshin_user(uid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"uid": uid, "data": data}


@app.get("/abyss/{uid}")
async def read_item(uid: int):
    try:
        data = await client.get_full_genshin_user(uid)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    abyss = data.abyss.current if data.abyss.current.floors else data.abyss.previous
    return {"uid": uid, "data": abyss}
