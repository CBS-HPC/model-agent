import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
import pytest
@pytest.fixture
def api():
    class Handler(BaseHTTPRequestHandler):
        public_access = False
        incomplete_stream = False
        accept_any_key = False
        response_model = "test-model"
        chat_content = "OK"
        stream_finish_reason = True
        stream_error = False
        listed_model = "test-model"

        def log_message(self, *args):
            pass

        def respond(self, data, content_type="application/json", status=200):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def permitted(self):
            authorization = self.headers.get("Authorization")
            if self.public_access or authorization == "Bearer testing-key" or (self.accept_any_key and authorization):
                return True
            self.respond(b"{}", status=401)
            return False

        def do_GET(self):
            if self.permitted():
                self.respond(json.dumps({"data": [{"id": self.listed_model}]}).encode())

        def do_POST(self):
            body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
            if not self.permitted():
                return
            if body.get("stream"):
                event = {"model": self.response_model, "choices": [{"delta": {"content": "OK"}}]}
                content = b"data: " + json.dumps(event).encode() + b"\n\n"
                if self.stream_error:
                    content += b'data: {"error":{"message":"private backend details"}}\n\n'
                if self.stream_finish_reason:
                    event["choices"] = [{"delta": {}, "finish_reason": "stop"}]
                    content += b"data: " + json.dumps(event).encode() + b"\n\n"
                if not self.incomplete_stream:
                    content += b"data: [DONE]\n\n"
                self.respond(content, "text/event-stream")
            else:
                self.respond(json.dumps({"model": self.response_model, "choices": [
                    {"message": {"content": self.chat_content}, "finish_reason": "stop"}]}).encode())

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_port}/v1", Handler
    server.shutdown()
    server.server_close()
    thread.join(timeout=2)

