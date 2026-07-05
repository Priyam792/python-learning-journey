import requests as r

print("Welcome to NewsAPI".center(50))

print("What kind of NEWS you want to read ?")


options = [
    "Enter : ",
    "1 for Apple",
    "2 for Tesla",
    "3 for Business headlinesin the US right now",
    "4 for Top headlines from TechCrunch right now",
    "All articles published by the Wall Street Journal in the last 6 months, sorted by recent first",
]


for i in options:
    print(i)
choice = int((input(": ")))

print("fetching ........")


match choice:
    case 1:
        response = r.get(
            "https://newsapi.org/v2/everything?q=apple&from=2026-05-27&to=2026-05-27&sortBy=popularity&apiKey=48dd2a9216a24147bc7d288b6fd65412"
        )
    case 2:
        response = r.get(
            "https://newsapi.org/v2/everything?q=tesla&from=2026-04-28&sortBy=publishedAt&apiKey=48dd2a9216a24147bc7d288b6fd65412"
        )
    case 3:
        response = r.get(
            "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=48dd2a9216a24147bc7d288b6fd65412"
        )
    case 4:
        response = r.get(
            "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=48dd2a9216a24147bc7d288b6fd65412"
        )
    case 5:
        response = r.get(
            "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=48dd2a9216a24147bc7d288b6fd65412"
        )
    case _:  # handles any invalid input
        print("Invalid choice!")
        exit()

if response.status_code != 200:
    print("Failed to fetch news!")
    exit()


data = response.json()


for article in data["articles"]:
    print(article["title"])
    print("")
    print(article["description"])
    print("")
    print(article["url"])
    print("")
    print("---")
    print("")
