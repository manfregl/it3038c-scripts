const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    var Days = Math.floor (os.uptime() / 86400);
    var totalmem = Math.floor (os.totalmem / 1000);
    var freemem = Math.floor (os.freemem / 1000);
    var CPU = os.cpus().length
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
	<h1>Hello! Welcome to my site!</h1>
	<p><a href='/sysinfo'> Get info about the system</a></p>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${Days} days</p>
        <p>Total Memory: ${totalmem} mb</p>
        <p>Free Memory: ${freemem} mb</p>
        <p>Number of CPUs: ${CPU} </p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");
