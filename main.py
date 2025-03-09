from fastapi import FastAPI

app = FastAPI()

@app.get("/test_api")
def read_root():
    return {"id": 101,
            "name": "Buddy",
            "breed": "Golden Retriever",
            "age": 3,
            "isVaccinated": True}


