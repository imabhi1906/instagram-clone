from fastapi import FastAPI

app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

textPosts = {
    1: {
        "title": "Amazing Post",
        "content": "What an amazing platform to upload and share content!"
    },
    2: {
        "title": "Python Tips",
        "content": "Always use virtual environments to keep your projects clean and isolated."
    },
    3: {
        "title": "FastAPI is Awesome",
        "content": "FastAPI makes building APIs super fast with automatic docs and validation."
    },
    4: {
        "title": "Daily Motivation",
        "content": "Consistency is more important than intensity. Keep building every day."
    },
    5: {
        "title": "Tech Update",
        "content": "AI tools are evolving rapidly and changing how developers work."
    },
    6: {
        "title": "Learning Journey",
        "content": "Every expert was once a beginner. Keep practicing and improving."
    },
    7: {
        "title": "Debugging Tip",
        "content": "Read error messages carefully—they usually tell you exactly what's wrong."
    },
    8: {
        "title": "Backend Basics",
        "content": "APIs connect frontend and backend systems to exchange data efficiently."
    }
}

@app.get('/')
async def root():
    return {"message": "server is running"}

@app.get('/posts')
async def get_all_posts(limit: int=None):
    if limit:
        return dict(list(textPosts.items())[:limit])
    return textPosts

@app.get("/posts/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    