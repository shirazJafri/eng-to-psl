import spacy
nlp = spacy.load('en_core_web_sm')
from fixSentence import fixSentence
from psl_sentence_form import psl_sentence_formation

def break_sentence_refix(sentences):
    psl_sentences = []
    print('Fixed sentence: ', sentences)
    fixed_sentence = fixSentence(sentences)
    tokens = nlp(fixed_sentence)

    for sent in tokens.sents:
        fixed_sent = fixSentence(str(sent))
        psl_dict = psl_dict_generation(str(fixed_sent).capitalize())
        psl_sentence = psl_sentence_formation(psl_dict)
        psl_sentences.append(psl_sentence)

    return psl_sentences

def psl_dict_generation(sentence):
    doc = nlp(sentence)
    
    psl_dict = {}
    nouns = []
    verbs = []
    adverbs = {}

    for token in doc:
        # NOUN in PSL
        if token.tag_ in ['NN', 'NNS', 'NNP', 'NNPS', 'PRP', 'PRP$'] or token.dep_ in ('csubj', 'csubjpass', 'nsubjpass', 'nsubj'):
            temp_list= [token.dep_, token.text]
            nouns.append(temp_list)

        # VERB/AUX in PSL
        elif token.tag_ in ['VB', 'VBG', 'VBN', 'VBP', 'VBZ'] and token.pos_ != 'AUX':
            temp_list = [token.tag_, token.lemma_]
            verbs.append(temp_list)

        elif token.tag_ in ['VBN'] and token.pos_ == 'AUX':
            temp_list = [token.tag_, '']
            verbs.append(temp_list)

        # Simple Past
        elif token.tag_ in ['VBD'] and (token.pos_ == 'AUX' or token.dep_ == 'ROOT'):
            # Checking for auxilary question
            for token_2 in doc:
                if token_2.text == '?':
                    psl_dict['AUX_QUES'] = 'Yes - No'

            temp_list = [token.tag_, 'was']
            verbs.append(temp_list)

            if token.dep_ == 'ROOT' and str(token.text).lower() != 'was':
                verbs.append(['VBD_2', token.lemma_])

        # Future Indefinite Tense
        elif token.tag_ in ['MD']:
            psl_dict['FUT_INDEF'] = 'after'
            for token_4 in doc:
                if token_4.text == '?':
                    psl_dict['AUX_QUES'] = 'Yes - No'

        # ADJ in PSL
        elif token.tag_ in ['JJ', 'JJS']:
            psl_dict['ADJ'] = token.text

        # Negations in PSL
        elif token.dep_ == 'neg':
            psl_dict['NEG'] = 'not'

        # Adverbs in PSL
        elif token.tag_ in ['RB', 'RBR', 'RBS']:
            adverbs[token.i] = token.text

        # Wh-questions in PSL
        elif token.tag_ in ['WP', 'WP$', 'WRB']:
            if token.lemma_ == 'when':
                psl_dict['WH_QUES'] = 'time'
            else:
                psl_dict['WH_QUES'] = token.lemma_

        # Auxiliary questions in PSL
        elif (token.pos_ == 'AUX' and token.dep_ == 'ROOT') or token.dep_ == 'aux':
            is_question = False
            for token_3 in doc:
                if token_3.text == '?':
                    is_question = True

            if token.tag_ not in ['VBD'] and is_question:
                psl_dict['AUX_QUES'] = 'Yes - No'

    psl_dict['NOUN'] = nouns
    psl_dict['VERB'] = verbs
    psl_dict['ADV'] = adverbs
    
    return psl_dict