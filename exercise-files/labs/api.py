from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route("/encode", methods=['GET'])
def encode_data():
    user_input = request.args.get('input')
    command = 'echo '+user_input+' | base64'
    output = subprocess.check_output([command], shell=True)
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True) 
