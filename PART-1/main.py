from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
posts: list[dict]=[
  {
    "id": 1,
    "name": "Betty Clark",
    "email": "betty.clark@outlook.com"
  },
  {
    "id": 2,
    "name": "Charlotte Harris",
    "email": "charlotte.harris25@hotmail.com"
  },
  {
    "id": 3,
    "name": "Charles Garcia",
    "email": "charlesgarcia@company.com"
  },
  {
    "id": 4,
    "name": "Amelia Thomas",
    "email": "ameliathomas10@proton.me"
  },
  {
    "id": 5,
    "name": "Susan Brown",
    "email": "susan.brown@email.com"
  }
]
@app.get("/", response_class=HTMLResponse)
@app.get("/posts", response_class=HTMLResponse)

def home():
    return f"<h1>{posts[0]}</h1>"

@app.get("/api/posts")
def get_posts():
    return posts