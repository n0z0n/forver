from flask import Flask, request, jsonify
from yapf.yapflib.yapf_api import FormatCode
import json
app = Flask(__name__)


@app.route("/", methods=['POST'])
def webhook():
    option = json.loads(request.form.get('option'))
    f = request.files.get('source')
    source = f.read().decode('utf-8')
    formatedObj = FormatCode(source, style_config=option['style'])
    response = dict(formated=formatedObj[0], status=formatedObj[1])
    return jsonify(response)


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
