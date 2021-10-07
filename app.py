import os
import signal
from gi.repository import Notify
from flask import Flask

Notify.init("Flask server")

app = Flask(__name__)

Notify.Notification.new("Servidor Iniciado").show()

"""
Abaixo estão os webhooks. Você deve modificar este arquivo conforme sua
preferência. Basta seguir o modelo do decorator e, em "send_command()", você
coloca o comando desejado quando a URL designada for acessada.
"""

@app.route('/unlock', methods=['GET'])
def unlock():
    send_command('loginctl unlock-session')
    return 'Desbloqueando PC...'

@app.route('/lock', methods=['GET'])
def lock():
    send_command('loginctl lock-session')
    return 'Bloqueando PC...'

@app.route('/discord', methods=['GET'])
def open_discord():
    send_command('discord')
    return 'Abrindo discord...'

@app.route('/spotify', methods=['GET'])
def open_spotify():
    send_command('spotify')
    return 'Abrindo spotify...'

@app.route('/isalive', methods=['GET'])
def check_status():
    Notify.Notification.new("Servidor está online!").show()
    return 'Servidor está no ar!'

@app.route('/ps4wake', methods=['GET'])
def wake_ps4():
    send_command('ps4-waker')

    return 'Ligando PS4...'

@app.route('/ps4sleep', methods=['GET'])
def sleep_ps4():
    send_command('ps4-waker standby')
    return 'Colocando ps4 em modo de repouso...'

@app.route('/shutdown', methods=['GET'])
def shutdown():
    
    Notify.Notification.new("Servidor desligado").show()

    os.kill(os.getpid(), signal.SIGTERM)

def send_command(command):
    """
    Cria um shell script separado que, simplesmente, armazena o comando.
    Posteriormente, executa este comando via outro shell script.

    Recebe: Comando a ser executado.
    Devolve: nada.
    """
    with open('command.sh', 'w') as action:
        action.write(command)
    os.system('./run_command.sh')
