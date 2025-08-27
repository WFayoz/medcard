from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


"""
ctrl + t
command + t (mac)
pull
merge


ctrl + k
command + k (mac)
commit

ctrl + shift + k
command + shift + k (mac)
push


git
github, gitlab, bitbucket
github cicd, gitlab cicd

branch 

features


"""