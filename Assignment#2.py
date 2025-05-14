ali = {
    "name": "Ali",
    "age": "15",
    "grade": "10",
    "hobby": "cricket",
    "city": "Lahore",
    "friend": "Zain",
    "goal": "doctor",
    "pet": "cat",
    "food": "biryani",
    "mood": "happy"
}

# 1. Access a value
print(ali["hobby"])

# 2. Add a new key-value pair
ali["school"] = "GHS"
print(ali)

# 3. Update an existing value
ali["goal"] = "engineer"
print(ali)

# 4. Delete a key-value pair
del ali["pet"]
print(ali)

# 5. Get all keys
print(ali.keys())

# 6. Get all values
print(ali.values())

# 7. Get all items
print(ali.items())

# 8. Check if a key exists
print("city" in ali)

# 9. Get value using get()
print(ali.get("food"))

# 10. Clear all items
ali.clear()
print(ali)
