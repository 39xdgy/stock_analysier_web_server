from pydantic import BaseModel

class Strategy(BaseModel):
    creater: str
    buy: list
    sell: list
    is_private: bool 
    upvote: int 
    downvote: int 