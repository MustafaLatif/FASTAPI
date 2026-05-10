from typing import Annotated
from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy import select
from sqlalchemy.orm import session

import models from database import Base, engine, get_db
from schemas import(
    UserCreate,
    UserResponse,
    PostUpdate,
    PostCreate,
    PostResponse,
)

app = FastAPI()
Base.metadata.create_all(bind=engine)

#-------USERS-------

@app.post(
    "/users",
    response_model= UserResponse,
    status_code=status.HTTP_201_CREATED,
          )

def create_user(
    user: UserCreate,
    db: Annotated[session, Depends(get_db)],
):
    new_user = models.User(
        username=user.username,
        email= user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
@app.get("/users", response_model=list[UserResponse])
def get_users(db: Annotated[session, Depends(get_db)]):
    result = db.execute(select(models.User))
    users = result.scalars().all()

    return users

@app.get("/users/{user_id}", response_model=list[UserResponse])
def get_users( user_id: int, db:Annotated[session, Depends(get_db)]):
    result = db.execute(
        select(models.User).where(models.User.id == user_id)
    )

    user = result.scalers().first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    
    return user

# ---------------- POSTS ----------------

@app.post(
    "/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(
    post: PostCreate,
    db: Annotated[session, Depends(get_db)],
):
    result = db.execute(
        select(models.User).where(
            models.User.id == post.user_id
        )
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    new_post = models.Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id,
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@app.get("/posts", response_model=list[PostResponse])
def get_posts(db: Annotated[session, Depends(get_db)]):
    result = db.execute(select(models.Post))

    posts = result.scalars().all()

    return posts


@app.get("/posts/{post_id}", response_model=PostResponse)
def get_post(
    post_id: int,
    db: Annotated[session, Depends(get_db)],
):
    result = db.execute(
        select(models.Post).where(
            models.Post.id == post_id
        )
    )

    post = result.scalars().first()

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    return post


@app.put("/posts/{post_id}", response_model=PostResponse)
def update_post(
    post_id: int,
    post: PostUpdate,
    db: Annotated[session, Depends(get_db)],
):
    result = db.execute(
        select(models.Post).where(
            models.Post.id == post_id
        )
    )

    found_post = result.scalars().first()

    if not found_post:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    found_post.title = post.title
    found_post.content = post.content

    db.commit()
    db.refresh(found_post)

    return found_post


@app.delete("/posts/{post_id}")
def delete_post(
    post_id: int,
    db: Annotated[session, Depends(get_db)],
):
    result = db.execute(
        select(models.Post).where(
            models.Post.id == post_id
        )
    )

    post = result.scalars().first()

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found",
        )

    db.delete(post)
    db.commit()

    return {
        "message": "Post deleted successfully"
    }

#------ USER POSTS RELATIONSHIP ------

@app.get(
"/users/(user_id)/posts",
response_model=list[PostResponse],
)
def get_user_posts(
    user_id: int,
    db: Annotated[session, Depends(get_db)],
):
    result = db.execute(
        select(models.User).where(
            models.User.id == user_id
        )
    )
    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail=" User not found",
        )
    
    return user.posts
