def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "first_name": item["first_name"],
        "last_name": item["last_name"],
        "nick_name": item["nick_name"],
        "email": item["email"],
        "phone_number": item["phone_number"],
        "cookie_number": item["cookie_number"],
        "result_list": item["result_list"],
        "fav_stock": item["fav_stock"],
        "strategy": item["strategy"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]