from flask import Flask, render_template, request, redirect, url_for
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
chat_history = []


@app.route('/', methods=['GET', 'POST'])
def index():
    global chat_history
    if request.method == 'POST':
        msg = request.form.get('message')
        if msg:
            # Connect to the TCP server
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    client_socket.connect(("localhost", 10000))
                    client_socket.send(msg.encode('utf-8'))
                    response = client_socket.recv(1024).decode('utf-8')
                    chat_history.append(('Server', response))
            except Exception as e:
                chat_history.append(('Error', str(e)))

            chat_history.append(('Client', msg))
            return redirect(url_for('index'))

    return render_template('chat.html', chat_history=chat_history)


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
