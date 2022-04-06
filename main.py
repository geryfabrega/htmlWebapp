import re
from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)

@app.route('/test', methods=['GET','POST'])
def test():
    print(request.method)
    if request.method == 'GET':
        @after_this_request
        def add_header(response):
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

        jsonResp = {'jack': 4098, 'sape': 4139}
        return jsonify(jsonResp)
    if request.method == 'POST':
        print("GOAT IN THE WATER!")
        @after_this_request
        def add_header(response):
            print(request.get_data())
            parse(request.data)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        jsonResp = {'jack': 4098, 'sape': 4139}
        return jsonify(jsonResp)


def parse(data):
    data = str(data)
    oneLine = ''.join(data)
    res = [i for i in range(len(oneLine)) if oneLine.startswith("Profilepictureof", i)]
    for i in range(len(res)):
        name = oneLine[res[i]+ 19:res[i]+55]
        name = name.split("upn")[0]
        print(name)

if __name__ == '__main__':
    app.run(host='localhost', port=8989)
