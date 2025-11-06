print("Welcome to the library!")
library = []
book1 = input("Enter the name of the book you own \n")
library.append(book1)
book2 = input(
    "Enter the name of another book you own (or press Enter to skip): \n")
if book2:
    library.append(book2)
    print(f"Your Library: {library}")
else:
    print(f"Your Library: {library}")
wish_list = []
wish1 = input("Enter the name of a book you wish to have in the future: \n")
wish_list.append(wish1)
wish2 = input(
    "Enter the name of another book you wish to have (or press Enter to skip): \n")
if wish2:
    wish_list.append(wish2)
    print(f"Your wish list: {wish_list}")
else:
    print(f"Your wish list: {wish_list}")
choose = input(
    "Enter the name of book from your wishlist that you've acquired (or enter to skip): \n")
if choose:
    library.append(choose)
    wish_list.remove(choose)
    print(f"Updated Library: {library}")
    print(f"Updated wishlist: {wish_list}")
else:
    print(f"Your Library: {library}")
    print(f"Your wishlist: {wish_list}")
donate = input(
    "Name a book from library to donate if you want: or Enter to skip \n")
if donate:
    library.remove(donate)
    print(f"Your final library after donation is: {library}")
else:
    print(f"Your library is: {library}")
