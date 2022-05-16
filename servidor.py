import smtplib
import email.message
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def envia_email():
    msg = email.message.Message()
    msg['Subject'] = request.form['id_assunto']
    msg['From'] = request.form['id_email_remetente']
    msg['To'] = request.form['id_email_destinatario']
    password = request.form['id_senha']
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(request.form['id_mensagem'])

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    return ('<h1>Email enviado com sucesso!</h1><br>')


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5000, debug=True)