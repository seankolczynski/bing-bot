import os


def setup():
    if not os.path.exists("lists"):
        os.mkdir("lists")
        print("Generating reference files...")
        open("lists/ThawList.txt", "w").close()
        open("lists/TodaysSearches.txt", "w").close()
    if not os.path.exists("password"):
        os.mkdir("password")
    if not os.path.exists("password/pword.txt"):
        password = input("Enter your bing password: ")
        open("password/pword.txt", "w").write(password)
