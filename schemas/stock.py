def stockEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "category": item["category"],
        "link": item["link"],
        "data": item["data"]
    }

def stocksEntity(entity) -> list:
    return [stockEntity(item) for item in entity]