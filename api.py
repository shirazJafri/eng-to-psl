import flask
import requests
from flask import request, jsonify
from psl_dictionary import break_sentence_refix
from word_mapping import words_mapping
from video_formation import video_formation

path = 'http://192.168.0.108:5000/static/'

app = flask.Flask(__name__, static_url_path= '/static')
app.config['DEBUG'] = True

@app.route('/api/fixSentence', methods= ['POST'])
def psl_sentence_generation():
    try:
        if request.method == 'POST':
            json_data = request.json
            sentence = json_data['sentence']
            print(sentence)
            
            if sentence:
                if len(sentence.split()) > 1:
                    sentence = break_sentence_refix(sentence)

                sentences, paths = words_mapping(sentence)

                file_name = video_formation(sentences, paths)

                if file_name:
                    response = {
                        "status": "success",
                        "data": {
                            "file_path": path + file_name
                        }
                    }
                    return jsonify(response)

            response = {
                    "status": "fail",
                    "data": {
                        "file_path": ""
                    }
            }

        return jsonify(response)

    except requests.exceptions.RequestException as error:
        response = {
                    "status": "error",
                    "data": {
                        "error": error
                    }
            }
        
        return jsonify(response)

@app.route('/api/', methods= ['GET', 'POST'])
def defaultRoute():
    response = {
                "status": "success",
                "data": {
                    "server_status": "Fine"
                }
            }
    return jsonify(response)

if __name__=='__main__':
    app.run(host= '0.0.0.0')




