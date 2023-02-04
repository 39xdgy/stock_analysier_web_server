from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    nick_name: str
    email:str 
    phone:str
    cookie_number: int
    result_list: list
    fav_stock: list
    strategy: list
    