from fastapi import FastAPI, security
import uvicorn
import route

TITLE = "FatAPI sample AWS API's app"
VERSION = "v0.0.1"
DESCRIPTION = """

Site under construction, get back after sometime

```[
{
    "App_name": "AWS API",
    "region": "us-east-1", 
    "status": "Ram"
}
``
"""
app = FastAPI(title=TITLE, version=VERSION, description=DESCRIPTION, debug=True)
# app.include_router(
#     route,
#     prefix="/s3",
#     tags=["aws", "s3"]
# )
app.include_router(route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)