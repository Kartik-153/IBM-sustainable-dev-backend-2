#one doc

def DecodeBlog(doc) -> dict:
    return {
        "_id": str(doc["_id"]),
        "title": doc["heading"],
        "sub_heading": doc["sub_heading"],
        "author": doc["username"],
        "content": doc["content"],
        "date": doc["date"]
    }

# all blogs
def DecodeBlogs(docs) -> list:
    return [DecodeBlog(doc) for doc in docs]