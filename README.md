# text-mining

Please read the [instructions](instructions.md).

----------------------------------------------------------

My Project can be found under: 'final_version.py' 

Project Writeup and Reflection: 

# 1. Project Overview

For my project I used three books from the Project Gutenberg Source, "The Great Gatsby", "Alice’s Adventures in Wonderland" and "Peter Pan". I decided to go with those books because I have read them all and I loved Peter Pan as a kid. As analyzing techniques I used Word Frequencies to find out total number of words, total number of different words, most/least common words in the book. After that I used the Markov Text Synthesis 
(tutorial found here:
1. Article: https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
2. Article:  https://towardsdatascience.com/simulating-text-with-markov-chains-in-python-1a27e6d13fc6)
to generate some random sentences and  paragraph samples from each one of the books. I then used the generated sentences and paragraph samples to analyze them with the Natural Language Toolkit and create a sentiment analysis out of the text samples. Through the "basic" analysis of number of words etc. I wanted to get used to analyzing and cleaning a text and wanted to get a better understanding of my text sources. With my more advanced analyses I wanted to create something fun and interesting. I found it extremely interesting to create random sentences and paragraphs and I sounded like a good and fun idea to use them in order to come up with a sentiment score. 

# 2. Implementation

The major components of my Analysis were Numpy, Spacy and NLTK. Through libraries I was able to build most of my funtion in order to come up with random paragraphs/sentences (Numpy), analyse those texts for Nouns, Verbs or other entities like Persons, Times, Geographical Entities or Places (Spacy) and finally create a sentiment score (NLTK) for my generated text samples. I found that those libraries work very well together for my purposes and I can use them , one after another to create a fun project. 

As for the Markov Analysis and generation of random text samples, I really wanted to implement that into my analysis. Therefore I researched a lot and found almost exclusivly very difficult code for me to understand. Here I made the decision to not go with code examples, using nltk, spacy and markovify altogether, but with a simpler version just using numpy. I decided to go with that solution because I was able to get most parts of the code and understood what the function is doing. I prefered that solution over copying a code I did not understand, even tough the result would have probably been better. 

# 3. Results: 
Unfortunately I was not able to implement any graphs of my findings, but what I found intersting to see is that the word "said" is on 1st place in terms of most common words, followed by almost immediatly the names of the main characters of each book. another interesting fact I found out about is that the ratio of total words to total number of different words is for the Great Gatsby 15,2%, for Alice's Adventure in Wonderland 13,8% and for Peter Pan 12,56%. This is interesting because The Great Gatsby is the oldest book with the highest ratio. 

Another interesting result were all the random sentences I read throughout the time, here are my favorites: 
From Gatsby: 
I lay down and she saw him get married," continued Tom savagely
Sentiment Score: neg: 24.2% and neutral 75.8%

He was interrupted breathlessly. 
Sentiment Score: Negative: 42.3% and Neutral 57.7%

From Peter Pan: 
Hook's cabin impressed them as just thought children were asleep, same time?" "Certainly," said John. 
Sentiment Score: Neutral to 81.9% and Positive to 18.1% 

What I always found fascinating were how the random text got analysed from spacy. Here is one interesting example: 

From Great Gatsby: 

Project Gutenberg trademark. It was startled, naturally, but she laughed, an abortive sorrows and I’d corroborate this. You must have lasted indefinitely except a romantic women preceded us to her, Daisy and to exact a brilliant smile. Mr. McKee was still vibrant emotions. “Sit right away at dawn wasn’t always a moment. “Put her hard up with pride that you’ll never had passed so I had just come? I knew why I was coming. Something in France. Evidently he deserved. However, as things that burns all night with Dan Cody’s yacht dropped from the poor. ------------------------------------------------------------------------ He stayed so when she

Noun phrases: ['Project Gutenberg trademark', 'It', 'she', 'an abortive sorrows', 'I', 'this', 'You', 'a romantic women', 'us', 'her', 'a brilliant smile', 'Mr. McKee', 'vibrant emotions', 'dawn', 'a moment', 'her', 'pride', 'you', 'I', 'I', 'I', 'Something', 'France', 'he', 'things', 'that', 'Dan Cody’s yacht', 'He']

Verbs: ['laugh', '’d', 'corroborate', 'last', 'precede', 'exact', 'sit', 'put', 'pass', 'come', 'know', 'come', 'deserve', 'burn', 'drop', 
'stay']

Project Gutenberg PERSON
Daisy PERSON
McKee PERSON
France GPE
all night TIME
Dan Cody’s PERSON


# 4. Reflection

What I really liked about this assignment is that one could be creative in terms of how to combine all those different analysing techniques. I combine random text generation with sentinment analysis and spacy's text analysis and found my results almost every time very amusing. 
Next time I'd love to clean my text better, as I found out to late to change was that I have included the header and footer in my random text generation and that leads to some unpleasing results from time to time. My plan was to compare my results with one another but I ran out of time. My learning therefore is that I have to concentrate on less books and more comparison next time. Other than that I am happy with my results and hope to strenghten my abilities to mine text and analyse it in the futture. I had a lot of fun and hope to use my learned abilities to better understand code and better code myself. I wish I'd knew that it sometimes can take a lot of time to find the right text source to use and that one can use sample files to test code instead of using the master file. It happaned to me several times that I rewrote code in a file that worked and afterwards it was broke and I had to fix it again. That cost me alot of precious time. 



