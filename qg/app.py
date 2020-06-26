import os, subprocess
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

def generate():
    myenv = os.environ.copy()
    myenv['PYTORCH_PRETRAINED_BERT_CACHE'] = '/bert-cased-pretrained-cache'
    subprocess.call(['python', '/unilm/unilm-v1/src/biunilm/decode_seq2seq.py',
                    '--bert_model', 'bert-large-cased',
                    '--new_segment_ids', '--mode', 's2s',
                    '--input_file', '/data/answers_flask.txt',
                    '--model_recover_path', '/data/qg_model.bin',
                    '--max_seq_length', '512', '--max_tgt_length', '48',
                    '--batch_size', '16', '--beam_size', '1', '--length_penalty', '0',
                    '--output_file', '/data/questions_flask.txt'], env=myenv)

@app.route('/', methods=['POST'])
def hello_world():
    data = request.get_json(force=True)
    contexts = data['context']
    answers = data['answers']
    with open('/data/answers_flask.txt', 'w') as f:
        for c, a in zip(contexts, answers):
            f.write(c + ' [SEP] ' + a + '\n')
    
    generate()
    questions = None
    with open('/data/questions_flask.txt', 'r') as f:
        questions = f.readlines()
    
    return jsonify({'questions': questions})


