import genshin
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# dummy token
cookies = {"ltuid": 119480035, "ltoken": "cnF7TiZqHAAvYqgCBoSPx5EjwezOh1ZHoqSHf7dT"}
client = genshin.Client(cookies)


@app.get("/")
def read_root():
    return Response("HoYoLAB API by TahuBulat")


# @app.get("/full/{uid}")
# async def read_item(uid: int):
#     try:
#         data = await client.get_full_genshin_user(uid)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     return {"uid": uid, "data": data}


# @app.get("/partial/{uid}")
# async def read_item(uid: int):
#     try:
#         data = await client.get_partial_genshin_user(uid)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     return {"uid": uid, "data": data}


# @app.get("/abyss/{uid}")
# async def read_item(uid: int):
#     try:
#         data = await client.get_full_genshin_user(uid)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     abyss = data.abyss.current if data.abyss.current.floors else data.abyss.previous
#     return {"uid": uid, "data": abyss}


@app.get("/checkin/{ltuid_v2}/{ltmid_v2}/{ltoken_v2}")
async def read_item(ltuid_v2: int, ltmid_v2: str, ltoken_v2: str):
    try:
        cookies = {"ltuid_v2": ltuid_v2, "ltmid_v2": ltmid_v2, "ltoken_v2": ltoken_v2}
        client = genshin.Client(cookies, game=genshin.Game.GENSHIN)
        reward = await client.claim_daily_reward()
    except genshin.AlreadyClaimed:
        return Response("Daily reward already claimed")
    else:
        return Response(f"Claimed {reward.amount}x {reward.name}")
