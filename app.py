
import json
import os
from socket import gethostname
from flask import Flask, jsonify, render_template, redirect, url_for, request

app = Flask(__name__)

app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename))

@app.route('/hw')
def hw():
    return 'Hello World!'

@app.route('/')
def index():
    p522 = False
    if gethostname() == 'tulsap522':
        p522 = True
    return render_template('index.html', p522=p522)

@app.route('/epydocs')
def epydocs():
    if gethostname() == 'tulsap522':
        return redirect('/epydocs/index.html')
    else:
        return render_template('epydocs.html')

@app.route('/printall_setup')
def pasetup():
    if gethostname() == 'tulsap522':
        p522 = True
    return redirect('/PrintAll/printall_server_setup.html')

@app.route('/eicdocs')
def eicdocs():
    if gethostname() == 'tulsap522':
        p522 = True
    return redirect('/eicdocs/')


@app.route('/printall_proc')
def paproc():
    return redirect('/PrintAll/printall_process.html')

@app.route('/multiagent')
def multiagent():
    return redirect('/MultiAgent/multiagent.html')

@app.route('/ubsetup')
def ubsetup():
    return redirect('/UbuntuServer/setup_notes.html')

@app.route('/ubinstall')
def ubinstall():
    return redirect('/UbuntuServer/install_notes.html')

@app.route('/ubadmin')
def ubadmin():
    return redirect('/UbuntuServer/admin_notes.html')

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

@app.route('/jsenrpc')
def jsonrpc():
    return render_template('jsonrpc.html')

@app.route('/eic_rpcjson')
def eic_rpcjson():
    return render_template('eic_rpcjson.html')

@app.route('/rpc/vehicle/getveh', methods=['POST'])
def getveh():
    jsonbody = json.load(request.stream)
    return jsonify({'veh': {'year': '2012'
                           ,'make': 'FORD'
                           ,'model': 'MUSTANG FAKE RESULTS'
                           ,'status': 'FAKE'}}  )

@app.route('/rpc/vehicle/getmodels', methods=['POST'])
def getmodels():
    jsonbody = json.load(request.stream)
    return jsonify({'models': ['ACCORD','CIVIC','CR-V','FAKED']})

@app.route('/rpc/vehicle/getmakes', methods=['POST'])
def getmakes():
    jsonbody = json.load(request.stream)
    return jsonify({'makes': ['ACUR','HOND','TYTA','FAKED']})

@app.route('/rpc/location', methods=['POST'])
def getlocation():
    jsonbody = json.load(request.stream)
    return jsonify({'locations': [['734330000', '734330001'], {'734330000': 'Elmore City, OK', '734330001': 'Pernell, OK'}] })

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
