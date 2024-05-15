#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on kwargs
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a collection based on keyword arguments.

    Args:
        mongo_collection: The PyMongo collection object.
        **kwargs: Keyword arguments representing the document to be inserted.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
