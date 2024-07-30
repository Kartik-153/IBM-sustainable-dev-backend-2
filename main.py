from fastapi import FastAPI
from routes.entry import entry_root
from routes.blog import blog_root

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# origins = ['https://127.0.0.1.8000']  
          
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(entry_root)
app.include_router(blog_root)
