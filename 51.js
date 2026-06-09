// Node.js gives you built-in modules called "core modules"
// You don't install these — they come with Node

// 1. OS module — read info about your computer
const os = require('os')

console.log("Your OS:", os.platform())        // 'win32', 'linux', 'darwin'
console.log("CPU cores:", os.cpus().length)   // how many CPU cores you have
console.log("Free memory:", os.freemem())     // bytes of free RAM
console.log("Home directory:", os.homedir())  // your home folder path

// 2. PATH module — work with file paths safely
const path = require('path')

const filePath = path.join('users', 'manoj', 'documents', 'file.txt')
console.log("Joined path:", filePath)
// Windows: users\manoj\documents\file.txt
// Linux/Mac: users/manoj/documents/file.txt
// path.join handles the slash difference automatically!

console.log("Extension:", path.extname('photo.jpg'))   // .jpg
console.log("Filename:", path.basename('/users/manoj/photo.jpg'))  // photo.jpg