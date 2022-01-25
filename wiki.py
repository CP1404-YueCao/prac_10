import wikipedia

search_content = input("What are you searching for? ")
while search_content != "":
    print(wikipedia.search(search_content, results=3))
    choose_content = input("Please choose one: ")
    print(wikipedia.summary(choose_content))
    ny = wikipedia.page(choose_content)
    print(ny.title)
    print(ny.url)
