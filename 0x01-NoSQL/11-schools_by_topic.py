#!/usr/bin/env python3
"""
Python function that returns the list of schools with a specific topic.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools that have a specific topic.

    Args:
        mongo_collection: The PyMongo collection object.
        topic: The topic to search for.

    Returns:
        Cursor: A cursor pointing to the documents matching the specified topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
