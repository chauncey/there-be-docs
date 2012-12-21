
import json
import os
from flask import Flask, jsonify, render_template, url_for, request

app = Flask(__name__)

app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename))


@app.route('/hw')
def hw():
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/yuiasync')
def yuiasync():
    return render_template('yuiasync.html')

@app.route('/cgi-bin/<script>', methods=['GET', 'POST'])
def pymessage(script):
    if script.startswith('bbw.sh'):
        return "The agent is {0}.".format(request.args.get('agent'))
    elif script == 'pymessage.py':
        return "The agent is {0}".format(request.form['agent'])
    else:
        return jsonify({'msg': "The agent is {0}".format(request.form['agent'])})

@app.route('/jsonrpc')
def jsonrpc():
    return render_template('jsonrpc.html')

@app.route('/rpc/echo', methods=['GET', 'POST'])
def echo():
    '''Testing echo route'''
    if request.method == 'POST':
        jsonbody = json.load(request.stream)
        return jsonify({'result': repr(jsonbody)})
    return jsonify({'result': request.args.get('params', 'Nada')})

def templated(template=None):
    '''Allowing /pagename to automatically use pagename.html
    @param template: Optional template file name'''
    def decorator(f):
        '''Decorate the function by finding a *.html file'''
        @wraps(f)
        def decorated_function(*args, **kwargs):
            '''Finding the *.html file'''
            template_name = template
            if template_name is None:
                template_name = request.endpoint.replace('.', '/')+'.html'
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        debug = True
    else:
        debug = False
    app.run(host='0.0.0.0', port=port, debug=debug)
