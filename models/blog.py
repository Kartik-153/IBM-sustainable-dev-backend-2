from pydantic import BaseModel

class BlogModels(BaseModel):
    heading : str
    sub_heading : str
    content : str
    username : str
    tags : list
    image_url: str

class EnduserModel(BaseModel):
    pass