import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
from dnslib import DNSRecord

HTTP_PORT = 8000
DNS_PORT = 5353


class HTTPHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[HTTP] {self.client_address[0]}:{self.client_address[1]} - {format % args}")

    def do_GET(self):
        print(f"[HTTP] GET {self.path}")
        print(f"[HTTP] Headers: {dict(self.headers)}")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


class DNSServer(socketserver.UDPServer):
    allow_reuse_address = True


class DNSHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, sock = self.request

        try:
            request = DNSRecord.parse(data)

            for question in request.questions:
                print(
                    f"[DNS] {self.client_address[0]} "
                    f"asked for {question.qname} "
                    f"(type={question.qtype})"
                )

            # Return an empty but valid DNS response.
            reply = request.reply()
            sock.sendto(reply.pack(), self.client_address)

        except Exception as e:
            print(f"[DNS] Error: {e}")


if __name__ == "__main__":
    http_server = HTTPServer(("0.0.0.0", HTTP_PORT), HTTPHandler)
    dns_server = DNSServer(("0.0.0.0", DNS_PORT), DNSHandler)

    print(f"HTTP listener: 0.0.0.0:{HTTP_PORT}")
    print(f"DNS listener:  0.0.0.0:{DNS_PORT}")

    import threading

    threading.Thread(target=http_server.serve_forever, daemon=True).start()
    dns_server.serve_forever()
