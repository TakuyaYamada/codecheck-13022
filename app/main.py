#!/usr/bin/env python3
import re
from websocket import create_connection


def main(argv):
    pattern = r"Hello, I'm "

    ws = create_connection(
            "ws://challenge-server.code-check.io/api/websocket/hello")
    result = ws.recv()

    name = re.sub(pattern, '', result)
    ws.send("Hello, {0}".format(name))
    result = ws.recv()
    print("{0} said: {1}".format(name, result))
