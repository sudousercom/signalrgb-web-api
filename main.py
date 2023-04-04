import os
from urllib.parse import unquote
from urllib.parse import urlparse
from flask import Flask, request

# IP and PORT definitions
IPADDR = "127.0.0.1"
PORT = "8080"

# App urls list
ALLOWED_VIEW_URLS = ['dashboard', 'monitoring', 'cooling', 'customize', 'devices', 'layouts', 'debuginfo', 'logs', 'dumps']

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the SignalRGB web API Server!</br> Source - <a href="https://github.com/sudousercom/signalrgb-web-api">https://github.com/sudousercom/signalrgb-web-api</a>'

@app.route('/view/<path:path>')
def view(path):
    if path not in ALLOWED_VIEW_URLS:
        return '404 Not Found', 404
    url = f'signalrgb://view/{path}'
    os.system(f'start {url}')
    return f'Launched URL: {url}'
    
@app.route('/effect/apply/<path:path>')
def apply_effect(path):
    effect_name, args = parse_effect_args(path)
    if "?-silentlaunch-" not in args:
        args = "?-silentlaunch-&" + args.lstrip("?")
    args = args.replace('&', '^&')
    url = f'signalrgb://effect/apply/{effect_name}{args}'
    os.system(f'start {url} {args}')
    return f'Launched URL: {url}'

def parse_effect_args(path):
    path = unquote(path).replace("'", "%27").replace(" ", "%20").replace(":","%3A")
    parts = path.split("-silentlaunch-")
    effect_name = parts[0]
    args = ""
    if len(parts) > 1:
        args = "-silentlaunch-" + parts[1]
    if request.query_string:
        args += "?" + request.query_string.decode()
    return effect_name, args

if __name__ == '__main__':
    app.run(host=IPADDR, port=PORT)
