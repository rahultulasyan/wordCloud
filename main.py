import wordcloud
from matplotlib import pyplot as plt


def calculate_frequencies(file_contents):

    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them",
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being",
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how",
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    finalWords = {}
    words = file_contents.split()
    for word in words:

        # Only add a word to finalWord if
        # 1. it is made up of alphabets and
        # 2. it not in uninteresting list.

        if word.isalpha() and word.lower() not in uninteresting_words:
            finalWords[word] = finalWords.get(word, 0) + 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(finalWords)
    return cloud.to_array()


# file_contents holds the entire file as a string
file_contents = open("python-handbook.txt").read()
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()
