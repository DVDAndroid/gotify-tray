import json
import time

import websocket
from PyQt6 import QtCore

from .models import GotifyMessageModel, GotifyErrorModel


class Listener(QtCore.QThread):
    new_message = QtCore.pyqtSignal(GotifyMessageModel)
    error = QtCore.pyqtSignal(Exception)
    opened = QtCore.pyqtSignal()
    closed = QtCore.pyqtSignal(int, str)

    def __init__(self, hostname: str, client_token: str):
        super(Listener, self).__init__()
        self.hostname = hostname
        self.client_token = client_token

        self.ws = websocket.WebSocketApp(
            f"wss://{self.hostname}/stream?token={self.client_token}",
            on_message=self._on_message,
            on_error=self._on_error,
            on_open=self._on_open,
            on_close=self._on_close,
        )

        self.wait_time = 0

        self.running = False

    def reset_wait_time(self):
        self.wait_time = 0

    def increase_wait_time(self):
        if self.wait_time == 0:
            self.wait_time = 1
        else:
            self.wait_time = min(self.wait_time * 2, 10 * 60)

    def _on_message(self, ws: websocket.WebSocketApp, message: str):
        self.new_message.emit(GotifyMessageModel(json.loads(message)))

    def _on_error(self, ws: websocket.WebSocketApp, error: Exception):
        self.error.emit(error)

    def _on_open(self, ws: websocket.WebSocketApp):
        self.opened.emit()

    def _on_close(
        self, ws: websocket.WebSocketApp, close_status_code: int, close_msg: str
    ):
        self.closed.emit(close_status_code, close_msg)

    def stop(self):
        self.ws.close()
        self.running = False

    def run(self):
        self.running = True

        try:
            time.sleep(self.wait_time)
            self.ws.run_forever()
        finally:
            self.running = False
