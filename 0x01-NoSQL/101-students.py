#!/usr/bin/env python3
"""
A function to retrieve top-performing students sorted by average score.
"""


def top_students(mongo_collection):
    """Retrieves students sorted by average score.

    Args:
        mongo_collection: A pymongo collection object representing the
        students' data.

    Returns:
        A cursor object containing documents of students sorted by average
        score in descending order.
    """
    return mongo_collection.aggregate([
        {
            "$project":
                {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
                }
        },
        {
            "$sort":
                {
                    "averageScore": -1
                }
        }
    ])
