from pydantic import BaseModel

'''
name -> stock name
category -> what type of company is this
link -> detail about this company
data -> {
    time_stemp: {
        indicator_name: value
    }
}
'''
class Stock(BaseModel):
    name: str
    category: str
    link: str
    data: dict