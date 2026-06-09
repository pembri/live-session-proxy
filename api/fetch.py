import os
from urllib.request import urlopen, Request
from urllib.parse import urlparse, parse_qs, unquote
from http.server import BaseHTTPRequestHandler

PROXY_KEY = os.environ.get("PROXY_KEY", "")

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # ── Auth ────────────────────────────────────────────────────────────────
        key = self.headers.get("X-Proxy-Key", "")
        if not PROXY_KEY or key != PROXY_KEY:
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Forbidden")
            return

        # ── Ambil target URL ────────────────────────────────────────────────────
        parsed   = urlparse(self.path)
        params   = parse_qs(parsed.query)
        url_list = params.get("url", [])

        if not url_list:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing ?url=")
            return

        target_url = unquote(url_list[0])

        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid URL")
            return

        # ── Fetch upstream ──────────────────────────────────────────────────────
        try:
            req = Request(target_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                "Accept":     "*/*",
            })
            resp = urlopen(req, timeout=15)
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(f"Fetch error: {e}".encode())
            return

        # ── Return response ─────────────────────────────────────────────────────
        self.send_response(resp.status)
        ct = resp.headers.get("Content-Type", "application/octet-stream")
        self.send_header("Content-Type", ct)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store")
        self.end_headers()

        while True:
            chunk = resp.read(8192)
            if not chunk:
                break
            self.wfile.write(chunk)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Proxy-Key, Content-Type")
        self.end_headers()
