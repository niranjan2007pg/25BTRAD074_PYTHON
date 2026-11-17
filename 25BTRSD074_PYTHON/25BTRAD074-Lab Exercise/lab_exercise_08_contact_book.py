# Lab Exercise 8: Contact Book Using Lists and Dictionaries
# Student: Niranjan P G | USN: 25BTRAD074

contacts = [
    {"name": "Alice Johnson", "phone": "9876543210"},
    {"name": "Bob Smith", "phone": "9123456780"}
]

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})
    print(f"Added: {name}")

def search_contact(name):
    for c in contacts:
        if c["name"].lower() == name.lower():
            return c
    return None

def update_contact(name, new_phone):
    c = search_contact(name)
    if c:
        c["phone"] = new_phone
        print(f"Updated: {name} -> {new_phone}")

def delete_contact(name):
    c = search_contact(name)
    if c:
        contacts.remove(c)
        print(f"Deleted: {name}")

def display_all():
    print(f"\n{'Name':<18} {'Phone':<14}")
    print("-" * 32)
    for c in contacts:
        print(f"{c['name']:<18} {c['phone']:<14}")

if __name__ == "__main__":
    print("=== Contact Book Management ===")
    add_contact("Charlie Brown", "9988776655")
    display_all()
    print(f"\nSearch 'Alice': {search_contact('Alice Johnson')}")
    update_contact("Bob Smith", "9000011111")
    delete_contact("Charlie Brown")
    display_all()
