import json
import socket
import re

def setup_listener(data_queue):
    with open("config.json") as credentials_file:
        file_contents = credentials_file.read()

    config_json = json.loads(file_contents)

    server = config_json["server"]
    port = int(config_json["port"])
    token = config_json["token"]
    nickname = config_json["nickname"]
    channel = config_json["channel"]

    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    resp = sock.recv(2048).decode('utf-8') # need to do it once first

    while True:
        resp = sock.recv(2048).decode('utf-8')

        if resp.startswith('PING'):
            sock.send("PONG\n".encode('utf-8'))
        
        elif len(resp) > 0:
            print(resp)

            result = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', resp)

            if result:
                username, channel, message = result.groups()
                message = message[:-1]
                data_queue.put(message)