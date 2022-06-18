from fastapi import FastAPI
import uvicorn
import requests
import json

app = FastAPI()


@app.get("/requires/all_data")
async def get_all_users_data():
    connection = requests.get('https://reqres.in/api/users?page=2').text
    all_data = json.loads(connection)
    return {"all_data": all_data}


@app.get("/requires/get_users")
async def get_users():
    for i in range(2):
        connection = requests.get(f'https://reqres.in/api/users?page={i}').text
        all_data = json.loads(connection)
        return {"all_data": all_data}


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8001)
