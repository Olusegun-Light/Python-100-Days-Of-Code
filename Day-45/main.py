from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# Find the first article link
article_tag = soup.find(name="a", class_="storylink")

# Check if the article_tag is not None before accessing its attributes
if article_tag:
    article_text = article_tag.getText()
    article_link = article_tag.get("href")
    article_upvote = soup.find(name="span", class_="score").getText()
    print(article_upvote)
else:
    print("No article found on the page.")
