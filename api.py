import flask
from flask import request, jsonify
from psl_dictionary import break_sentence_refix
from word_mapping import words_mapping
from video_formation import video_formation

path = 'http://ecc5-182-255-48-81.ngrok.io/static/'

app = flask.Flask(__name__, static_url_path= '/static')
app.config['DEBUG'] = True

@app.route('/api/fixSentence', methods= ['GET', 'POST'])
def psl_sentence_generation():
    if request.method == 'POST':
        json_data = request.json
        sentence = json_data['sentence']
        
        if sentence:
            psl_sentences = break_sentence_refix(sentence)

            print(psl_sentences)
            
            sentences, paths = words_mapping(psl_sentences)

            file_name = video_formation(sentences, paths)

            return jsonify({'static_file': path + file_name})

    return jsonify({'static_file': ""})

@app.route('/', methods= ['GET', 'POST'])
def defaultRoute():
    return jsonify({'sentence': "Server is running"})

if __name__=='__main__':
    app.run()




