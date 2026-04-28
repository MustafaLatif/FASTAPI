from fastapi import FastAPI,HTTPException,status
from schemas import PostCreate , PostResponse
app= FastAPI()

#fake database
posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

#Create Post
@app.post("/posts",response_model= PostResponse, status_code= status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_post = {
        "id": len(posts)+1,
        **post.model_dump()
    }
    posts.append(new_post)
    return new_post

#Get all posts
@app.get("/posts", response_model=PostResponse)
def  get_post(post_id: int):
    for post in posts:
        if post["id"]``==post_id:
            return post
        raise HTTPException(status_code=404, detail="post not found")
    
#Delete all posts
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            deleted =posts.pop(index)
            return { "message": "Deleted", "data": "Deleted"}
    raise HTTPException(status_code=404, detail="post not  found")  