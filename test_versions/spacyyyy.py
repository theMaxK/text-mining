# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import string 


with open("txt-file/GreatGatsby.txt", encoding="utf8") as myfile: 
    head = [next(myfile) for x in range(100)]
print(head)


f = open("txt-file/GreatGatsby.txt", encoding="utf8")
text = f.read()

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


def word_dict(filename, skip_header):

    
    fp = open(filename, encoding="UTF8")

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):  # iteration ends at this point
            break
        
        return line 




def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF THE PROJECT'):
            break

hist = word_dict("txt-file/GreatGatsby.txt", skip_header=True)
print(hist[:10])

# Process whole documents
# text = ("When Sebastian Thrun started working on self-driving cars at "
#         "Google in 2007, few people outside of the company took him "
#         "seriously. “I can tell you very senior CEOs of major American "
#         "car companies would shake my hand and turn away because I wasn’t "
#         "worth talking to,” said Thrun, in an interview with Recode earlier "
#         "this week.")

# text = 
doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)