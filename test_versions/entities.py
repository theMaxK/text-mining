from random import sample


def sample_txt(sentence): 
    return sentence 


def rand_text_analysis(txt_file):

    import spacy
    from spacy import displacy

    # Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("en_core_web_sm")
    # f = rand_text(txt_file)

    # f = open("txt-file/GreatGatsby.txt", encoding="utf8")

    f = txt_file
    

    text = sample_txt(f)
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


x = "Hallo Welt, wie geht es heute denn der Lotte, ich hoffe doch gut!"

print(sample_txt(x))
print(rand_text_analysis(x))