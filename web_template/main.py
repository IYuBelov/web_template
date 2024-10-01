from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"data": "Hello World"}



if __name__ == '__main__':
    import subprocess
    subprocess.run("uvicorn main:app --reload")