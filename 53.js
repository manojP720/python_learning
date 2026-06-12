const http = require('http')

const server = http.createServer((req, res) => {

    console.log(`${req.method} ${req.url}`)

    res.setHeader('Content-Type', 'application/json')

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

    } else if (req.url === '/skills' && req.method === 'GET') {
        res.writeHead(200)
        res.end(JSON.stringify({
            skills: ["HTTP", "Node.js", "Express"]
        }))

    } else if (req.url === '/time' && req.method === 'GET') {
        res.writeHead(200)
        res.end(JSON.stringify({
            currentTime: new Date().toLocaleString()
        }))

    } else {
        res.writeHead(404)
        res.end(JSON.stringify({
            error: "Route not found",
            path: req.url
        }))
    }

})

server.listen(3000, () => {
    console.log("Server running at http://localhost:3000")
    console.log("Press Ctrl+C to stop")
})