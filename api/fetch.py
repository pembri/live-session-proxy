import os
import requests
from http.server import BaseHTTPRequestHandler

PROXY_KEY = os.environ.get("PROXY_KEY", "")

BLOCKED_HOSTS = []  # opsional: block host tertentu

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
        from urllib.parse import urlparse, parse_qs, unquote
        parsed  = urlparse(self.path)
        params  = parse_qs(parsed.query)
        url_list = params.get("url", [])

        if not url_list:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing ?url=")
            return

        target_url = unquote(url_list[0])

        # Validasi scheme
        if not target_url.startswith("http://") and not target_url.startswith("https://"):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid URL")
            return

        # ── Fetch upstream ──────────────────────────────────────────────────────
        try:
            resp = requests.get(
                target_url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
                    "Accept":     "*/*",
                },
                timeout=15,
                stream=True,
                allow_redirects=True,
            )
        except Exception as e:
            self.send_response(502)
            self.end_headers()
            self.wfile.write(f"Fetch error: {e}".encode())
            return

        # ── Return response ─────────────────────────────────────────────────────
        self.send_response(resp.status_code)
        ct = resp.headers.get("Content-Type", "application/octet-stream")
        self.send_header("Content-Type", ct)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store")
        self.end_headers()

        for chunk in resp.iter_content(chunk_size=8192):
            self.wfile.write(chunk)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "X-Proxy-Key, Content-Type")
        self.end_headers()
