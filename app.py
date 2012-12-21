import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

app.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename=filename))


@app.route('/hw')
def hw():
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')

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
