import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / "src"))

import uvicorn
from fastapi import FastAPI
from config.router import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
