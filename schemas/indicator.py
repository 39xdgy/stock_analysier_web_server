def indicatorEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "discription": item["discription"]
    }

def indicatorsEntity(entity) -> list:
    return [indicatorEntity(item) for item in entity]