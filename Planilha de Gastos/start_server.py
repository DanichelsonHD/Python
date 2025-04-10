import http.server
import socketserver
import webbrowser
import os

# Configurações do servidor
PORT = 5555
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Inicia o servidor
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Servidor iniciado em http://localhost:{PORT}")
    
    # Abre o navegador automaticamente
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    
    # Mantém o servidor ativo
    httpd.serve_forever()