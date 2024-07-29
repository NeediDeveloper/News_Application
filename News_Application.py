import requests

choice = input("Enter 1 for News and 0 for Headlines: ")
def News():
    type = input("Which type of news you want: ")
    ApiKey = "" # Enter the API key
    url = f"https://newsapi.org/v2/everything?q={type}&from=2024-06-29&sortBy=publishedAt&apiKey={ApiKey}"
    Main_Page = requests.get(url).json()
    articles = Main_Page["articles"]
    head = []
    counter = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
    for article in articles:
        head.append(article["title"])
    for i in range(len(counter)):
        print(f"Today's {counter[i]} news about {type} is : {head[i]}")
    
def New_Headlines():
    country = input("Enter Country: ")
    ApiKey = "" # Enter the API key
    url = f"https://gnews.io/api/v4/top-headlines?country={country}&category=general&apikey={ApiKey}"
    Main_Page = requests.get(url).json()
    articles = Main_Page["articles"]
    head = []
    counter = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"]
    for article in articles:
        head.append(article["title"])
    for i in range(len(counter)):
        print(f"Today's {counter[i]} headlines is: {head[i]}")

if "1" in choice:
    News()
else:
    New_Headlines()