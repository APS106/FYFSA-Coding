from collections import Counter
from matplotlib import pyplot as plt
from wordcloud import WordCloud

# List of words from the CSV file
words = [
    "good", "struggling", "cautious", "loaded", "average", "interested", "confident",
    "good", "good", "excited", "good", "harder", "interesting", "anxious", "confident",
    "enlightened", "great", "opportunity", "relaxed", "curious"
]

# Convert all words to lower case
words = [word.lower() for word in words]

# Count frequency of each word
word_counts = Counter(words)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white', max_font_size=150).generate_from_frequencies(word_counts)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

'''
Sentiment Analysis Option
'''

import nltk
from nltk.corpus import opinion_lexicon

# Ensure the necessary NLTK data is downloaded
nltk.download('opinion_lexicon')
nltk.download('punkt')

# Define a function to classify words
def classify_words(word_list):
    positive_words = set(opinion_lexicon.positive())
    negative_words = set(opinion_lexicon.negative())

    positive_list = []
    negative_list = []

    for word in word_list:
        if word in positive_words:
            positive_list.append(word)
        elif word in negative_words:
            negative_list.append(word)

    return positive_list, negative_list

positive_words, negative_words = classify_words(words)

# Create a color function
def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    if word in positive_words:
        return "green"
    elif word in negative_words:
        return "red"
    else:
        return "black"

# Generate word cloud with color function
wordcloud = WordCloud(width=800, height=400, background_color='white', max_font_size=150, color_func=color_func).generate_from_frequencies(word_counts)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()