from pydantic import BaseModel

class BlogModels(BaseModel):
    heading : str
    sub_heading : str
    content : str
    username : str
    tags : list

class EnduserModel(BaseModel):
    pass