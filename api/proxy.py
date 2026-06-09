from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, unquote
import urllib.request

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)

        if 'url' not in params:
            self.send_response(400)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(b'Missing url param')
            return

        target_url = unquote(params['url'][0])

        try:
            referer = urlparse(target_url).scheme + '://' + urlparse(target_url).netloc + '/'
        except:
            referer = ''

        try:
            req = urllib.request.Request(target_url, headers={
                'User-Agent':    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Referer':       referer,
                'Origin':        referer,
                'Accept':        '*/*',
                'Cache-Control': 'no-cache',
            })
            with urllib.request.urlopen(req) as resp:
                ct = resp.headers.get('Content-Type', 'application/octet-stream')
                body = resp.read()
                self.send_response(200)
                self.send_header('Content-Type', ct)
                self.send_header('Cache-Control', 'no-cache, no-store')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(body)

        except urllib.error.HTTPError as e:
            self.send_response(e.code)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(f'Upstream error: {e.code}'.encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(f'Relay error: {str(e)}'.encode())
