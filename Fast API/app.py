from fastapi import FastAPI
app=FastAPI(title="my first api")

@app.get("/")
def read_root():
    return {"message":"Hello from fast-api!"}
