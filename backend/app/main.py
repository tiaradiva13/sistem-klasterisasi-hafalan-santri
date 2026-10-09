
from fastapi import FastAPI
from app.routers import auth, santri, hafalan, clustering

app = FastAPI(title="Sistem Klasterisasi Hafalan Santri")

app.include_router(auth.router)
app.include_router(santri.router)
app.include_router(hafalan.router)
app.include_router(clustering.router)

@app.get("/")
def root():
    return {"status":"running"}
