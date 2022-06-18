from fastapi import FastAPI
import uvicorn
from enum import Enum

run = FastAPI()


class car_brands(str, Enum):
    benz = "Benz"
    ford = "Ford"
    hundai = "Hundai"
    honda = "Honda"


user_data = []


@run.post('/me/user_name')
async def user_reg(user_name: str):
    user_data.append(user_name)
    return {'user_name': user_name}


@run.get('/me/info/{info}')
async def info(info):
    for i in user_data:
        if i == info:
            return f"User {info} is registered already"
        else:
            return f"User {info} not available"


@run.get('/me/get_all_users')
async def get_all_users():
    return {"status_code": 200, "result": user_data}


@run.get('/car/{brand}')
async def cars(brand: car_brands):
    return {"Car brand": brand}


if __name__ == "__main__":
    uvicorn.run(run, host='127.0.0.1', port=8000)
