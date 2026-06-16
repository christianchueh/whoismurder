import asyncio
from fastapi import FastAPI
import uvicorn

# ─── 1. 建立 FastAPI 網頁伺服器 ───
app = FastAPI()

# 瀏覽器用的 GET 請求
@app.get("/")
async def home_get():
    return {"status": "🤖 誰是臥底機器人 24 暢通運作中！"}

# 專門給 UptimeRobot 用的 HEAD 請求（完全不帶 request 參數，避免底層解析出錯）
@app.head("/")
async def home_head():
    return None  # HEAD 請求依照 HTTP 規範本來就不需要回傳內容，給個空值即可


# ─── 3. 用同一個事件循環啟動 ───
async def main():

    config = uvicorn.Config(app, host="0.0.0.0", port=10000, log_level="info")
    server = uvicorn.Server(config)

    await asyncio.gather(
        server.serve(),
    )

if __name__ == "__main__":
    asyncio.run(main())
