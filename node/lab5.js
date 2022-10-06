const http = require("http");

const server = http.createServer((req, res) => {
  res.writeHead(200, {"Content-Type": "text/html"});

  res.end(`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <h1>Hello! Welcome to my site!</h1>
	<p><a> href='/sysinfo'>Get info about this system</a></p>
        <p>${req.url}</p>
        <p>${req.method}</p>
      </body>
    </html>
  `)

}).listen(3000)

console.log("Server listening on port 3000")
