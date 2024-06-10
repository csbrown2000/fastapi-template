import os
from fastapi import FastAPI

app = FastAPI(
	title="Boat Catalog",
	description="API for keeping track of boats and scoring them based on client interests/needs"
)

app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:5173", "http://main.d26iid5rbhmv9u.amplifyapp.com"],
	allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"]
)
