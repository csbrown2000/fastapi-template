from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

# Router imports
from routers.routerTemplate import template_router

app = FastAPI(
	title="FastAPI Template",
	description="Template that contains all necessary dependencies and basic folder/file structure to get your app up and running in minutes"
)

app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:5173"], # Change this if you are using something other than vite + react for frontend
	allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"]
)

# Include other routers - easily separate routers in the routers folder
app.include_router(template_router)