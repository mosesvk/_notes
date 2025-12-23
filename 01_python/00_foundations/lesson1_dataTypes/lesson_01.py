# Task A — Records pipeline
users = [
    {
        "id": 1,
        "email": "alice@test.com",
        "roles": ["admin", "user"]
    },
    {
        "id": 2,
        "email": "bob@test.com",
        "roles": ["user"]
    },
    {
        "id": 3,
        "email": "charlie@test.com",
        "roles": ["user"]
    }
]

# Task B — Deduplication
seen_emails = set()
processed_users = {}

for user in users:
    email = user["email"]

    if email in seen_emails:
        raise ValueError(f"Duplicate email detected: {email}")

    seen_emails.add(email)

    # Task C — Immutable key
    key = (user["id"], user["email"])
    processed_users[key] = user

print("Processed users:")
for k, v in processed_users.items():
    print(k, v)
