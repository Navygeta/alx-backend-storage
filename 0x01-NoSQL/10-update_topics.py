#!/usr/bin/env python3
"""
Python function that updates the topics of a school document.
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document in the collection.

    Args:
        mongo_collection: The PyMongo collection object.
        name: The name of the school document to be updated.
        topics: The list of topics to be set in the updated document.

    Returns:
        The result of the update operation.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
