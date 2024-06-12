from fastapi import APIRouter

template_router = APIRouter(prefix="/template", tags=["Template"])

@template_router.get('', status_code=200, description="This is a basic get request")
def example_get():
	pass

@template_router.put('', status_code=200, description="This is a basic put request")
def example_put():
	pass

@template_router.post('', status_code=200, description="This is a basic post request")
def example_post():
	pass

@template_router.delete('', status_code=200, description="This is a basic delete request")
def example_delete():
	pass