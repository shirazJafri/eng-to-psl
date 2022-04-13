# from joblib import load
from rpunct import RestorePuncts

rpunct = RestorePuncts()

# tokenizer = load('GrammarFixerTokenizer.joblib')
# model = load('GrammarFixerModel.joblib')

def fixSentence(sentence):
    # input_text = "fix: { " + str(sentence) + "} </s>"

    # input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=256, truncation=True, add_special_tokens=True)

    # outputs = model.generate(
    #     input_ids=input_ids,
    #     max_length=256,
    #     num_beams=4,
    #     repetition_penalty=1.0,
    #     length_penalty=1.0,
    #     early_stopping=True
    # )

    # sentence_v1 = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
        
    return str(rpunct.punctuate(sentence, lang= 'en'))