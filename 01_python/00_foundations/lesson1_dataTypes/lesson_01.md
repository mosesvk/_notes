Practice Assignment (Do This Locally)

Create a file: lesson1_types.py

Task A — Records Pipeline

Create a list of user records (dicts)

Each record must have:

id (int)

email (str)

roles (list of strings)

Task B — Deduplication

Use a set to detect duplicate emails

Raise an exception if a duplicate is found

Task C — Immutable Keys

Create a tuple key (id, email)

Store processed users in a dict keyed by that tuple

Example shape (not full solution):

processed = {
    (1, "a@test.com"): {...}
}