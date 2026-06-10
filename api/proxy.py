import json
import os
from http.server import BaseHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE_DIR, "channels.json")) as f:
    CHANNELS = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.lstrip("/").split("?")[0]
        parts = path.split("/")

        if len(parts) != 2:
            self._error(400, "Bad request")
            return

        cdn_type = parts[0]
        slug = parts[1].replace(".mpd", "")

        if cdn_type not in CHANNELS or slug not in CHANNELS[cdn_type]:
            self._error(404, f"Channel not found: {cdn_type}/{slug}")
            return

        origin_url = CHANNELS[cdn_type][slug]

        self.send_response(301)
        self.send_header("Location", origin_url)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def _error(self, code, msg):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(msg.encode())

    def log_message(self, format, *args):
        pass
