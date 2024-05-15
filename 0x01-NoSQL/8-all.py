#!/usr/bin/env python3
""" List all documents in a MongoDB collection """
import pymongo


def list_all(mongo_collection):
    """List all documents in a MongoDB collection.

    Args:
        mongo_collection: The PyMongo collection object.

    Returns:
        list: A list of documents in the collection. Returns an empty list if
        no documents exist.
    """
    documents_list = []

    for doc in mongo_collection.find():
        documents_list.append(doc)

    return documents_list
