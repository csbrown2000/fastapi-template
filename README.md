# FastAPI template

This template includes a basic example of how FastAPI works and a template layout for a starter project. I have included all the necessary dependencies managed in a poetry virtual environment to make project setup even easier.

## Folder / File Structure

This templates includes folders for routers, models, and controllers.

#### Routers

The routers folder contains a template router with some basic request samples. The routers folder should be used for additional routers that you add to your project as you see fit. This helps keep routes organized in one place and can increase the readability of your code if used properly.

#### Models

The models folder contains a template model file with two, very basic, model definitions. Using pydantics' BaseModel, defining models is super easy. Creating these models can help with request and response models that you need throughout your API.

#### Controllers

The conrollers folder is meant for any extra logic or database connections you may need. I have left this blank as needs may vary depending on the application and the type of database you are using.

## Dependencies

```
python = "^3.12"
uvicorn = "^0.30.1"
fastapi = "^0.111.0"
python-dotenv = "^1.0.1"
```
