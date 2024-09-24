favorite_books = {
    "title": "rich dad poor dad",
    "author": "robert kiyosaki",
    "genre": "personal finances"
}

#displaying all the items in a given dictionary

print(favorite_books.items())

#returning dictionary keys
print(favorite_books.keys())

#returning dictionary values
print(favorite_books.values())

#retrieving only genre
print(favorite_books.get("genre"))

