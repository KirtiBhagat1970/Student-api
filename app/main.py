from fastapi import FastAPI
app=FastAPI(title="Student API")

@app.get("/")
def Home():
    return{
        "message":"Welcome to Student API"}

@app.get("/health")
def health_check():
    return{
        "status":"ok",
        "service":"student-api"}