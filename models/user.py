from pydantic import BaseModel

class User(BaseModel):
    first_name: str
    last_name: str
    nick_name: str
    email:str 
    phone_number:str
    cookie_number: int
    result_list: list
    fav_stock: list
    strategy: list
    