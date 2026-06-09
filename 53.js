// server.js  ← create a NEW file with this name
const http = require('http')

const server = http.createServer((req, res) => {
    // req = the incoming request (what the client sent)
    // res = the response (what we send back)

    console.log(`${req.method} ${req.url}`)  // log every request

    // Set response headers
    res.setHeader('Content-Type', 'application/json')

    // Route based on URL
    if (req.url === '/' && req.method === 'GET') {
        res.writeHead(200)
        res.end(JSON.stringify({
            message: "Welcome to my first Node.js server!",
            author: "Manoj"
        }))

    } else if (req.url === '/about' && req.method === 'GET') {
        res.writeHead(200)
        res.end(JSON.stringify({
            name: "Manoj",
            role: "Backend Engineer (in training)",
            day: 2
        }))

    } else {
        // Any other URL → 404
        res.writeHead(404)
        res.end(JSON.stringify({
            error: "Route not found",
            path: req.url
        }))
    }
})

// Start listening on port 3000
server.listen(3000, () => {
    console.log("Server running at http://localhost:3000")
    console.log("Press Ctrl+C to stop")
})