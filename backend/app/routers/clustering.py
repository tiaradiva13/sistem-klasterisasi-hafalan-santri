
from fastapi import APIRouter
from sklearn.cluster import KMeans

router=APIRouter(prefix="/clustering")

@router.post("/predict")
def predict(data:list):
    model=KMeans(n_clusters=3, random_state=42)
    return {"cluster":model.fit_predict(data).tolist()}
