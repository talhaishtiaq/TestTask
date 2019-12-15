import http.server
import socketserver
from db import conn

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    HtmlContent = ""
    db = conn
    cursor = db.cursor(buffered=True)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.parse_data()
        self.log()
        self.wfile.write(bytes(self.HtmlContent, "utf8"))
        return

    def parse_data(self):
        self.HtmlContent = ("<html><head><style type='text/css'>table {border-collapse: separate;border-spacing: 50px 0;}td {padding: 10px 0;}</style>"+
        "<body><table><thead><td>id</td><td>timestamp</td><td>temperature</td><td>duration</td></thead><tbody>")
        sql = "select * from data;"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        while row is not None:
            self.HtmlContent += "<tr><td>%s</td>"%row[0]
            self.HtmlContent += "<td>"+row[1]+"</td>"
            self.HtmlContent += "<td>"+row[2]+"</td>"
            self.HtmlContent += "<td>"+row[3]+"</td></tr>"
            row = self.cursor.fetchone()

    def log(self):
        sql = "INSERT INTO logs (message) VALUES ('Get: Data requested from "+self.client_address[0]+"')"
        self.cursor.execute(sql)
        self.db.commit()



if __name__ == '__main__':
    print('Server listening on port 8080...')
    httpd = socketserver.TCPServer(('', 8080), RequestHandler)
    httpd.serve_forever()
