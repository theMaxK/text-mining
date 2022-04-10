import string
# f = open("txt-file/GreatGatsby.txt", encoding="utf8")
# text = f.read()

# print(text)


def book_text(filename, skip_header):

    
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

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break

def book_sentiment_analysis(file):
    import nltk
    nltk.download('vader_lexicon')
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    # text = word_dict("txt-file/GreatGatsby.txt", skip_header=True)
    text = file 

    score = SentimentIntensityAnalyzer().polarity_scores(text)
    
    return(score)


def main():
    # gatsby = open("txt-file/GreatGatsby.txt", encoding="UTF-8")

    great_gatsby = book_text("txt-file/GreatGatsby.txt", skip_header=True)
    alice = book_text("txt-file/Alice.txt", skip_header=True)
    moby_dick = book_text("txt-file/Moby.txt", skip_header=True)
    peter_pan = book_text("txt-file/PeterPan.txt", skip_header=True)







    sentiment_gatsby = book_sentiment_analysis(great_gatsby)
    sentiment_moby = book_sentiment_analysis(moby_dick)
    sentiment_alice = book_sentiment_analysis(alice)
    sentiment_peter = book_sentiment_analysis(peter_pan)




    # print(hist)
    # print(alice)
    # print(great_gatsby)
    print("----------------------")
    print("This is a sentiment analysis for the book:")
    print("The Great Gatsby")
    print(sentiment_gatsby)
    print("----------------------")
    print("This is a sentiment analysis for the book:")
    print("Moby Dick")
    print(sentiment_moby)
    print("----------------------")
    print("This is a sentiment analysis for the book:")
    print("Alice in Wonderland")  
    print(sentiment_alice)
    print("----------------------")
    print("This is a sentiment analysis for the book:")
    print("Peter Pan")  
    print(sentiment_peter)
    print("----------------------")
  


if __name__ == '__main__':
    main()




