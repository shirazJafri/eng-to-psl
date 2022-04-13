from joblib import load
import string

words_dict = load('words_dict.joblib')

def bare_form(sentence):
    # Punctuation removal
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Lower-case transformation
    sentence = sentence.lower()
    
    return " ".join(sentence.split())

def mapping(sentence):
    sentence_split = sentence.split()

    paths = []

    for word in sentence_split:
        if word in words_dict.keys():
            paths.append(words_dict[word])
        else:
            letters = list(word)
            
            for letter in letters:
                paths.append(words_dict[letter])
        
    return paths

def flatten(t):
    return [item for sublist in t for item in sublist]

def words_mapping(sentences):
    all_paths = []
    for sentence in sentences:
        sentence = bare_form(sentence)

        all_paths.append(mapping(sentence))

    return (sentences, flatten(all_paths))




