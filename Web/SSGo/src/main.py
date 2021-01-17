from flask import Flask, request, send_file, abort, redirect
from subprocess import check_output, CalledProcessError
from glob import glob
app = Flask(__name__)

@app.route("/")
def index():
    return send_file('index.html')

@app.route("/source")
def source():
    return send_file(__file__)

@app.route("/visit")
def visit():
    url = request.args.get('url')
    if not url:
        return redirect(index)
    try:
        result = check_output(['curl', '--max-time', '1', '-s', url])
    except CalledProcessError as e:
        result = e.output
    return result

@app.route("/backdoor", methods=['GET_FLAG'])
def magic_path_to_get_flag():
    if request.remote_addr != '127.0.0.1':
        abort(403)
    return send_file(glob('/flag*')[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=10003)
