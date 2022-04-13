from sentence_helpers import sort_noun_dict, check_adverb

def psl_sentence_formation(psl_dict):
    psl_dict = sort_noun_dict(psl_dict)
    psl_sentence = ''
    pos = 0
    is_past = False
    is_cont = False
    is_perfect = False

    (psl_sentence, pos) = check_adverb(psl_dict, pos, psl_sentence)

    # Simple Past - Was goes at the start of the sentence
    if psl_dict['VERB'] != []:
        for verb_pair in psl_dict['VERB']:
            if verb_pair[0] == 'VBD':
                psl_sentence += verb_pair[1] + " "
                is_past = True
                psl_dict['VERB'].remove(verb_pair)

    # NOUN arrangement (still needs work)
    if psl_dict['NOUN'] != []:
        if len(psl_dict['NOUN']) > 1:
            for noun_pair in psl_dict['NOUN']:
                psl_sentence += noun_pair[1] + " "
                pos += 1

                ### ADVERBIAL CHECK GOES OVER HERE
                (psl_sentence, pos) = check_adverb(psl_dict, pos, psl_sentence)

        else:
            psl_sentence += psl_dict['NOUN'][0][1] + " "
            pos += 1
            (psl_sentence, pos) = check_adverb(psl_dict, pos, psl_sentence)

    # ADJECTIVE arrangement (always after Noun in PSL)
    if 'ADJ' in psl_dict.keys():
        psl_sentence += psl_dict['ADJ'] + " "
        pos += 1
        ### ADVERBIAL CHECK GOES OVER HERE
        (psl_sentence, pos) = check_adverb(psl_dict, pos, psl_sentence)


    # VERB arrangement    
    if psl_dict['VERB'] != []:
        for verb_pair in psl_dict['VERB']:
            if verb_pair[0] == 'VBG':
                is_cont = True
                psl_sentence += verb_pair[1] + " "
            elif verb_pair[0] == 'VBN':
                is_perfect = True
                psl_sentence += verb_pair[1] + " "
            elif is_past and verb_pair[1] != 'VBD':
                psl_sentence += verb_pair[1] + " "
            elif not is_past:
                psl_sentence += verb_pair[1] + " "

    ### ADVERBIAL CHECK GOES OVER HERE

    if is_perfect:
        psl_sentence += " full "

    if 'FUT_INDEF' in psl_dict.keys():
        psl_sentence += psl_dict['FUT_INDEF'] + " "

    if is_cont:
        psl_sentence += " now "

    if 'NEG' in psl_dict.keys():
        psl_sentence += psl_dict['NEG'] + " "

    if 'WH_QUES' in psl_dict.keys():
        psl_sentence += psl_dict['WH_QUES'] + " "

    elif 'AUX_QUES' in psl_dict.keys():
        psl_sentence += psl_dict['AUX_QUES'] + " "

    psl_sentence = " ".join(psl_sentence.split())

    if 'WH_QUES' in psl_dict.keys() or 'AUX_QUES' in psl_dict.keys():
        psl_sentence += "?"
    else:
        psl_sentence += "."
        
    return psl_sentence.capitalize()