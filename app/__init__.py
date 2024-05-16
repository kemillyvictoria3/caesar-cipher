from flask import Flask, render_template, request, flash

def create_app():
    #Create and configure the app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asbvvjhbsjhghsgbkhjckhgckjhgskk'

    @app.route("/")
    def home(name='Home'):
        return render_template('index.html', name=name)

    @app.route("/encode" ,methods=('get', 'POST'))
    def encode(name='Encode'):
        if request.method == 'POST':
            cipher_key = request.form['cipher_key']
            message = request.form['message']

            if not cipher_key:
                flash('A chave é obrigatória...')
            elif not message:
                flash('a mensagem é necessária...')
            else:
                flash('ENCODE')
  
        return render_template('encode.html', name=name)
    
    return app
