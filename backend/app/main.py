from fastapi import FastAPI
import json

app = FastAPI()
@app.get("/monitor")
def monitor():
    return json.load(...)
@app.get("/city")
def city():
    with open("config/city.json") as f:
        return json.load(f)

@app.get("/layers")
def layers():
    with open("config/layers.json") as f:
        return json.load(f)

@app.get("/scenario")
def scenario():
    with open("config/scenario.json") as f:
        return json.load(f)