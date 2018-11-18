import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt

pages = requests.get("https://www.imdb.com/title/tt7715202/reviews")

soup = BeautifulSoup(pages.content, 'html.parser')

review = soup.find_all(class_="text show-more__control")

positive, negative, neutral = 0, 0, 0
x = 0
for i in review:
    text = i.get_text()
    x += 1
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        positive = positive + 1
        a = positive
    elif sentiment == 0:
        neutral = neutral + 1
        b = negative
    elif sentiment < 0:
        negative = negative + 1
        c = neutral

print("Positive reviews = ", positive)
print("Neutral reviews = ", neutral)
print("Negative reviews = ", negative)
print("total reviews = ", x)


yy = [19, 3, 3]
labels = ["positive","negative", "neutral"]
plt.pie(yy, labels = labels, autopct = "%2f")
# plot title
plt.title('Movie Analysis')
# showing legend
plt.axes().set_aspect("equal")
# function to show the plot
plt.show()