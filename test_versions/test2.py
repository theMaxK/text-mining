import string
# f = open("txt-file/GreatGatsby.txt", encoding="utf8")
# text = f.read()

# print(text)


def word_dict(filename, skip_header):

    hist = {}
    fp = open(filename, encoding="UTF8")

    if skip_header:
        skip_gutenberg_header(fp)

    strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):  # iteration ends at this point
            break

        # replace the "---...---" sections of the book
        line = line.replace("-", " ")

        for word in line.split():  # without the .split() we would get every character...why?
            # print(word)
            word = word.lower()
            word = word.strip(strippables)

            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break


def total_words(hist):
    """Returns number of total words in Histogramm"""

    return sum(hist.values())


def different_words(hist):
    """Returns the number of different words in a histogram."""

    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency, hist is a dict

    returns: list of (frequency, word) pairs
    """
    stopwords = word_dict("txt-file/stopwords.txt", False)
    # print(stopwords.keys())
    lst = []

    for word, frequency in hist.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        lst.append((frequency, word))
    lst.sort(reverse=True)

    return lst


def rand_text():
    import numpy as np
    # f = filename
    f = open("txt-file/GreatGatsby.txt", encoding="utf8")
    text = f.read()

    corpus = text.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])

    pairs = make_pairs(corpus)

    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)
    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = 100

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    text = ' '.join(chain)

    return text


def one_sentece():
     li = []
     for i in rand_text():
        li.append(i)
        if i == ".": 
            break
        text = ''.join([str(item) for item in li])

     return text

def sentiment_analysis():
    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    sentence = one_sentece()

    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print(sentence,".")
    print(score)


def rand_text_analysis():

    import spacy
    from spacy import displacy

    # Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("en_core_web_sm")

    text = rand_text()
    print(text)
    print(" ")
    doc = nlp(text)


    # Analyze syntax
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print(" ")
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    print(" ")

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        # rand_text_analized = entity.text, entity.label_
        print(entity.text, entity.label_)
        # return rand_text_analized


def main():
    gatsby = open("txt-file/GreatGatsby.txt", encoding="UTF-8")

    hist = word_dict("txt-file/GreatGatsby.txt", skip_header=True)

    # print(hist)
    print("----------------------")
    print("Start of the Analysis:")
    print("Book: The Great Gatsby")
    print("Author: F. Scott Fitzgerald")
    print("Published: 10th of April, 1925 ")
    print("----------------------")
    print("Total number of words: ", total_words(hist))
    print("----------------------")
    print("Total number of different words: ", different_words(hist))
    print("----------------------")

    t = most_common(hist, excluding_stopwords=True)
    print('The 10 most common words are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)

    print("----------------------")
    print('The 10 least common words are:')
    t = most_common(hist, excluding_stopwords=True)
    for freq, word in t[-10:-1]:
        print(word, '\t', freq)

    print("----------------------")
    print("Here is another random generated text")
    print("")
    print(rand_text())
    print("----------------------")
    print("Here is another random generated text, this time analized with spacy:")
    print("")
    print(rand_text_analysis())
    print("----------------------")
    print(one_sentece())
    print("----------------------")
    print(sentiment_analysis())





if __name__ == '__main__':
    main()



## sources used: 
# Spacy tutorial: https://spacy.io/
# Markov tutorial: `1. Article: https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
#                   2. Article:  https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
