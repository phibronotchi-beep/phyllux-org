from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
ROOT = r"D:\WS\programs\Phyllux-repos\phyllux-org"
Handler = partial(SimpleHTTPRequestHandler, directory=ROOT)
print("SERVING", ROOT, "on 8787", flush=True)
ThreadingHTTPServer(("127.0.0.1", 8787), Handler).serve_forever()
