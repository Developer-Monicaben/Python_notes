
import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()   #read form data
name = form.getvalue("username")

print(f"<h2>Hello, {name}!</h2>")

# http://localhost:8000/index.html

# CGI is not working in Python because browsers don’t run CGI directly — they require a CGI-enabled web server.it is a basic local server

# python -m http.server 8000 --cgi   --->to run cgi