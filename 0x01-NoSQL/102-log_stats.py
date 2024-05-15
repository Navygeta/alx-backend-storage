#!/usr/bin/env python3
"""Log Stats

This script retrieves statistics from an Nginx log collection stored in a
MongoDB database.

Functions:
    log_stats: Connects to the MongoDB database, retrieves the Nginx
    log collection,and prints statistics regarding the log entries.
"""

from pymongo import MongoClient


def log_stats():
    """Retrieve statistics from the Nginx log collection.

    This function connects to the MongoDB database where the Nginx logs are
    stored, retrieves the log collection, and prints statistics regarding the
    log entries. The statistics include the total number of log entries, the
    count for each HTTP method, the count of requests with the method 'GET' and
    path '/status', and the top 10 most present IP addresses.

    Args:
        None

    Returns:
        None
    """
    # Connect to MongoDB and retrieve the log collection
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    # Count total log entries
    total = logs_collection.count_documents({})

    # Count log entries for each HTTP method
    get = logs_collection.count_documents({"method": "GET"})
    post = logs_collection.count_documents({"method": "POST"})
    put = logs_collection.count_documents({"method": "PUT"})
    patch = logs_collection.count_documents({"method": "PATCH"})
    delete = logs_collection.count_documents({"method": "DELETE"})

    # Count log entries with method 'GET' and path '/status'
    path = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    # Count the occurrence of each IP address and sort them
    top_ips = logs_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    # Print statistics
    print(f"{total} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")
    print("IPs:")
    for ip_data in top_ips:
        print(f"\t{ip_data['_id']}: {ip_data['count']}")


if __name__ == "__main__":
    log_stats()
