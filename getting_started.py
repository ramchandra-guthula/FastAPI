from fastapi import FastAPI

# Uvicorn is a lightning-fast ASGI server implementation
import uvicorn

# Creating a instance of FastAPI
app = FastAPI(debug=True)


# app is the variable what we have declared above, you can use any of rest method along with 'app' post,get,put,delete, head, options and patch
# Its not mandatory we have to call only get, we can call put also its just a guideline not a mandatory
@app.get('/')
# async stands for asynchronous, Handle the requests until it respond back and do execute others in the mean time
async def start():
    return "Hello FastAPI"


# running your app application
if __name__ == "__main__":
    # pass 'app' is the instance of fastapi
    uvicorn.run(app, host="127.0.0.1", port=8000)
