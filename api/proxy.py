import json
import os
import requests
from http.server import BaseHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE_DIR, "channels.json")) as f:
    CHANNELS = json.load(f)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # path: /indihome/gtv.mpd  atau  /visionplus/antv.mpd
        path = self.path.lstrip("/")
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

        try:
            resp = requests.get(origin_url, stream=True, timeout=10, headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://www.visionplus.id/" if cdn_type == "visionplus" else ""
            })
            self.send_response(resp.status_code)
            for header in ["Content-Type", "Content-Length", "Cache-Control"]:
                if header in resp.headers:
                    self.send_header(header, resp.headers[header])
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            for chunk in resp.iter_content(chunk_size=8192):
                self.wfile.write(chunk)
        except Exception as e:
            self._error(502, str(e))

    def _error(self, code, msg):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(msg.encode())

    def log_message(self, format, *args):
        pass
