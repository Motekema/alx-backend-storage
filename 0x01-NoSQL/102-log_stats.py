#!/usr/bin/env python3
"""
Module documentation
"""
def log_stats(mongo_collection):
    """
    Prints some stats about Nginx logs stored in MongoDB
    """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = mongo_collection.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])

    print("Methods:")
    for method in methods:
        print(f"    method {method['_id']}: {method['count']}")

    status = mongo_collection.aggregate([
        {"$group": {"_id": "$status", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ])

    print("Status check:")
    for stat in status:
        print(f"    {stat['_id']}: {stat['count']}")

    ips = mongo_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print("IPs:")
    for ip in ips:
        print(f"    {ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    pass
