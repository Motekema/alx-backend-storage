#!/usr/bin/env python3
"""
Module documentation
"""
def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$topics.score"}, "name": {"$first": "$name"}}},
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))

if __name__ == "__main__":
    pass
