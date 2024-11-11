# Import necessary libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# Sample text (you can replace this with your own text)
text = """
Python is an amazing programming language. It is widely used in data science, 
machine learning, and web development. It is also very easy to learn!
"""

# Create a WordCloud object
wordcloud = WordCloud(width=400, height=200, background_color='white').generate(random())

# Display the generated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Hide the axes
plt.show()
