from secrets import randbelow
import string


# Create dictionary of all words that appear in the book
def word_dict(filename, skip_header):
    """this function returns a dictionary of all words in the given book file"""

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

# Skip the Header of each Book


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break

# Returns Total number of Words


def total_words(book):
    """Returns number of total words in Histogramm"""

    return sum(book.values())

# Returns Number of different words of each Book


def different_words(book):
    """Returns the number of different words in a histogram."""

    return len(book)

# Returns top ten Most Common Words in Descending order


def most_common(book, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency, hist is a dict

    returns: list of (frequency, word) pairs
    """
    stopwords = word_dict("txt-file/stopwords.txt", False)
    # print(stopwords.keys())
    lst = []

    for word, frequency in book.items():
        if excluding_stopwords:
            if word in stopwords:
                continue
        lst.append((frequency, word))
    lst.sort(reverse=True)

    return lst

# This function returns a random text generated from the given book
# Markov tutorial found here : `1. Article: https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
#                   2. Article:  https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6


def rand_text(txt_file):
    """This function returns a random text generated from the given book. 
    txt-file = name and place of the text file downloaded from Gutenberg Projects 
    """
    import numpy as np
    f = open(txt_file, encoding="utf-8")
    # f = open("txt-file/GreatGatsby.txt", encoding="utf8")
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

# Spacy tutorial: https://spacy.io/
def rand_text_analysis(random_text):
    """This function analyses random generated text and prints out found NOUNS, VERBS and classifies 
    Persons, Date, Time and Geopolitical Entity (GPE) found in the random generated text. 
    random_text = rand_text(filename)
    """

    import spacy
    from spacy import displacy

    # Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("en_core_web_sm")
    # f = rand_text(txt_file)

    # f = open("txt-file/GreatGatsby.txt", encoding="utf8")

    f = random_text

    print(f)
    print(" ")
    doc = nlp(f)

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


def one_sentece(txt_file):
    """This function returns just one sentence of the random text generated in the rand_text funtion
    txt-file = name and place of the text file downloaded from Gutenberg Projects 
    """
    li = []
    for i in rand_text(txt_file):
        li.append(i)
        if i == ".":
            break
        text = ''.join([str(item) for item in li])

    return text

## Source: project introduction slides 
def sentence_sentiment_analysis(txt_file):
    """ This function prints a sentiment analysis of the generated random sentece.
    txt-file = name and place of the text file downloaded from Gutenberg Projects """

    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    sentence = one_sentece(txt_file)

    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    print("")
    print("Here is the random sentence:")
    print(sentence, ".")
    print("")
    print("Here is the Sentiment Score")
    return score 

## Section where I analyzed the sentiments of the whole book
def book_text(filename, skip_header):
    """This function returns a plain and cleaned version of the book text, which is needed for the sentiment analysis."""

    li = []
    fp = open(filename, encoding="UTF-8")

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
            # word = word.lower()
            # word = word.strip(strippables)
            li.append(word)
        
    text = ' '.join([str(item) for item in li])

    return text 

def book_sentiment_analysis(file):
    """This function returns the sentiment score of an entire book. 
    file = txt-file of the book. """
    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    # text = word_dict("txt-file/GreatGatsby.txt", skip_header=True)
    text = file 

    score = SentimentIntensityAnalyzer().polarity_scores(text)
    
    return(score)





def main():
# get dictionary of every word in book
    gatsby_dict = word_dict("txt-file/GreatGatsby.txt", skip_header=True)
    alice_dict = word_dict("txt-file/Alice.txt", skip_header=True)
    peter_dict = word_dict("txt-file/PeterPan.txt", skip_header=True)


# open text file
    gatsby_txt = "txt-file/GreatGatsby.txt"
    alice_txt = "txt-file/Alice.txt"
    peter_txt = "txt-file/PeterPan.txt"



# plain text
    text_sample_gatsby = rand_text(gatsby_txt)
    text_sample_alice = rand_text(alice_txt)
    text_sample_peter = rand_text(peter_txt)



# Sentiment analysis book 
    great_gatsby = book_text("txt-file/GreatGatsby.txt", skip_header=True)
    sentiment_gatsby = book_sentiment_analysis(great_gatsby)

    alice_wonderland = book_text("txt-file/Alice.txt", skip_header=True)
    sentiment_alice = book_sentiment_analysis(alice_wonderland)

    peter_pan = book_text("txt-file/PeterPan.txt", skip_header=True)
    sentiment_peter = book_sentiment_analysis(peter_pan)

    
   
    print("----------------------")
    print("Start of the Analysis:")
    print("Book: The Great Gatsby")
    print("Author: F. Scott Fitzgerald")
    print("Published: 10th of April, 1925 ")
    print("----------------------")
    print("")
    print("Total number of words: ", total_words(gatsby_dict))
    print("----------------------")
    print("")
    print("Total number of different words: ", different_words(gatsby_dict))
    print("----------------------")
    print("")
    t = most_common(gatsby_dict, excluding_stopwords=True)
    print('The 10 most common words are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)
    print("----------------------")
    print("")
    print('The 10 least common words are:')
    t = most_common(gatsby_dict, excluding_stopwords=True)
    for freq, word in t[-10:-1]:
        print(word, '\t', freq)
    print("----------------------")
    print("")
    print("Here is a random generated text")
    print("")
    print(rand_text(gatsby_txt))
    print("----------------------")
    print("")
    print("Here is another random generated text, this time analized with spacy:")
    print("")
    print(rand_text_analysis(text_sample_gatsby))
    print("----------------------")
    print("")
    print("Here is one randomly generated sentence:")
    print("")
    print(one_sentece(gatsby_txt))
    print("----------------------")
    print("")
    print("Here is a sentiment analysis of this random sentece:")
    print("")
    print(sentence_sentiment_analysis(gatsby_txt))
    print("----------------------")
    print("")
    print("This is a sentiment analysis for the book:")
    print("The Great Gatsby")
    print(sentiment_gatsby)
    print("----------------------")
    print("")
    print("Analysis for 'The Great Gatsby' is finished." )
    print("")
    print("")
    ## Analysis of the book "Alice’s Adventures in Wonderland"
    print("----------------------")
    print("Start of the Analysis:")
    print("Book: Alice’s Adventures in Wonderland")
    print("Author: Lewis Carroll")
    print("Published: January, 1991 ")
    print("----------------------")
    print("")
    print("Total number of words: ", total_words(alice_dict))
    print("----------------------")
    print("")
    print("Total number of different words: ", different_words(alice_dict))
    print("----------------------")
    print("")
    t = most_common(alice_dict, excluding_stopwords=True)
    print('The 10 most common words are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)
    print("----------------------")
    print("")
    print('The 10 least common words are:')
    t = most_common(alice_dict, excluding_stopwords=True)
    for freq, word in t[-10:-1]:
        print(word, '\t', freq)
    print("----------------------")
    print("")
    print("Here is a random generated text")
    print("")
    print(rand_text(alice_txt))
    print("----------------------")
    print("")
    print("Here is another random generated text, this time analized with spacy:")
    print("")
    print(rand_text_analysis(text_sample_alice))
    print("----------------------")
    print("")
    print("Here is one randomly generated sentence:")
    print("")
    print(one_sentece(alice_txt))
    print("----------------------")
    print("")
    print("Here is a sentiment analysis of this random sentece:")
    print("")
    print(sentence_sentiment_analysis(alice_txt))
    print("----------------------")
    print("")
    print("This is a sentiment analysis for the entire book:")
    print("Alice’s Adventures in Wonderland")
    print("")
    print(sentiment_alice)
    print("----------------------")
    print("")
    print("Analysis for 'Alice’s Adventures in Wonderland' is finished." )
    print("")
    ## Analysis of the book "Peter Pan"
    print("----------------------")
    print("Start of the Analysis:")
    print("Book: Peter Pan")
    print("Author: James M. Barrie")
    print("Published: July, 1991 ")
    print("----------------------")
    print("")
    print("Total number of words: ", total_words(peter_dict))
    print("----------------------")
    print("")
    print("Total number of different words: ", different_words(peter_dict))
    print("----------------------")
    print("")
    t = most_common(peter_dict, excluding_stopwords=True)
    print('The 10 most common words are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)
    print("----------------------")
    print("")
    print('The 10 least common words are:')
    t = most_common(peter_dict, excluding_stopwords=True)
    for freq, word in t[-10:-1]:
        print(word, '\t', freq)
    print("----------------------")
    print("")
    print("Here is a random generated text")
    print("")
    print(rand_text(peter_txt))
    print("----------------------")
    print("")
    print("Here is another random generated text, this time analized with spacy:")
    print("")
    print(rand_text_analysis(text_sample_peter))
    print("----------------------")
    print("")
    print("Here is one randomly generated sentence:")
    print("")
    print(one_sentece(peter_txt))
    print("----------------------")
    print("")
    print("Here is a sentiment analysis of this random sentece:")
    print("")
    print(sentence_sentiment_analysis(peter_txt))
    print("----------------------")
    print("")
    print("This is a sentiment analysis for the entire book:")
    print("Peter Pan")
    print("")
    print(sentiment_peter)
    print("----------------------")
    print("")
    print("Analysis for 'Peter Pan' is finished." )
    print("")
    print("This is the end of Assignment 2: Text Analysis and Text Mining." )
    print("You can find my Writeup and Reflection in the README.md file." )
    print("")
    print("----------------------")







if __name__ == '__main__':
    main()


# sources used:
# Spacy tutorial: https://spacy.io/
# Markov tutorial: `1. Article: https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
#                   2. Article:  https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6
