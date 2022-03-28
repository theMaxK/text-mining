# # 1. Option 
# encoding= utf8 needed because other wise error message saying the following: UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1362: character maps to <undefined>
# f = open("txt-file/GreatGatsby.txt", encoding="utf8")
# print(f.read())

# 2. Option
import urllib.request

url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode("utf-8")
print(text)


## word appearences in dict 
## tf - idf 

def word_count(text): 
    counts = dict()
    words = text.split()

    for word in words: 
        if word in words: 
            counts[word] += 1
        else: 
            counts[word] = 1 

    return counts 


    



def main():

    url = "https://www.gutenberg.org/cache/epub/64317/pg64317.txt"
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")

    # print(text)

    print(word_count(text))

if __name__ == '__main__':
    main()




