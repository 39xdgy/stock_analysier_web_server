def strategyEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "creater": item["creater"],
        "buy": item["buy"],
        "sell": item["sell"],
        "is_private": item["is_private"],
        "upvote": item["upvote"],
        "downvote": item["downvote"]
    }


def strategiesEntity(entity) -> list:
    return [strategyEntity(item) for item in entity]