from pydantic import BaseModel

#buy/sell -> [{indicator: value}, {indicator: value}]

class Strategy(BaseModel):
    creater: str
    buy: list
    sell: list
    is_private: bool 
    upvote: int 
    downvote: int 