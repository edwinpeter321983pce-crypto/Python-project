friends = {
    "lin lin": "autism",
    "kap twan khai": "naughty kap",
    "myat min khant": "bo kyat aung san",
    "hein htet zan": "silent sigma",
    "khant mion paing": "kind boy",
    "thein htike": "mapilla",
    "brother kyaw phyo zan": "father",
    "brotherr umesh": "mother",
    "brother lin latt": "uncle",
    "brother tnh": "spider man"
}

# Start a continuous loop
while True:
    name = input("\nEnter the person's name that you wanna know about (or type 'no' to exit): ").lower()
    
    # Allow the user to break out of the loop
    if name == 'no':
        print("Goodbye!")
        break

    if name in friends:
        print(f"{name.title()} is a {friends[name]}!")
    else:
        print("friend not found! SORRY!")