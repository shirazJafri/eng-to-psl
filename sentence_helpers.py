def check_adverb(psl_dict, pos, psl_sentence):
    if 'ADV' in psl_dict.keys():
        for key in psl_dict['ADV'].keys():
            if key == pos:
                psl_sentence += psl_dict['ADV'][key] + " "
                pos += 1
    return (psl_sentence, pos)

'''To tackle the 2 subject problem'''
def sort_noun_dict(psl_dict):
    sorted_list = []
    
    # Possession modifiers go first
    for noun_pair in psl_dict['NOUN']:
        if noun_pair[0] in ('poss'):
            sorted_list.append(noun_pair)
    
    # Subjects come first
    for noun_pair in psl_dict['NOUN']:
        if noun_pair[0] in ('csubj', 'csubjpass', 'nsubjpass', 'nsubj'):
            sorted_list.append(noun_pair)
            
    # Objects second
    for noun_pair in psl_dict['NOUN']:
        if noun_pair[0] in ('dobj', 'pobj'):
            sorted_list.append(noun_pair)
            
    # Rest of the nouns
    for noun_pair in psl_dict['NOUN']:
        if noun_pair[0] not in ('dobj', 'pobj', 'poss') and noun_pair[0] not in ('csubj', 'csubjpass', 'nsubjpass', 'nsubj'):
            sorted_list.append(noun_pair)
            
    psl_dict['NOUN'] = sorted_list
    
    return psl_dict