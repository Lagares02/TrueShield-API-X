from fastapi import FastAPI
from routes import x

app = FastAPI()

# Incluir rutas
app.include_router(x.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)