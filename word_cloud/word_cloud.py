import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

try:
    topic = str(input("Enter the word you want to make word cloud: "))
    title = wikipedia.search(topic)[0]
    page = wikipedia.page(title)
    text = page.content

    background = np.array(Image.open("w_cloud.jpg"))
    unwanted_words = set(STOPWORDS)
    wrd_cloud = WordCloud(background_color = "black", max_words = 400, mask=background, stopwords = unwanted_words)
    wrd_cloud.generate(text)
    wrd_cloud.to_file('w_cloud.jpg')
except Exception as err:
    print(f"An error occured: {err}")