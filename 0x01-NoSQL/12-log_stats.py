#!/usr/bin/env python3
"""
Log Stats
"""

from pymongo import MongoClient


def count_logs(collection):
    """Counts the number of documents in a collection"""
    return collection.count_documents({})

def count_methods(collection):
    """Counts the number of documents for each HTTP method"""
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {}
    for method in methods:
        counts[method] = collection.count_documents({"method": method})
    return counts

def count_status_check(collection):
    """Counts the number of status check requests"""
    return collection.count_documents({"method": "GET", "path": "/status"})

def print_stats(log_count, method_counts, status_check_count):
    """Prints the statistics"""
    print(f"{log_count} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx
    log_count = count_logs(logs_collection)
    method_counts = count_methods(logs_collection)
    status_check_count = count_status_check(logs_collection)
    print_stats(log_count, method_counts, status_check_count)
