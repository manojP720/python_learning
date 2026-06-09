const fs = require('fs')

// WRITE a file
fs.writeFileSync('notes.txt', 'This is my first Node.js file!')
console.log("File created!")

// READ a file
const content = fs.readFileSync('notes.txt', 'utf8')
console.log("File content:", content)

// APPEND to a file
fs.appendFileSync('notes.txt', '\nSecond line added.')

// READ again
const updated = fs.readFileSync('notes.txt', 'utf8')
console.log("Updated content:", updated)

// CHECK if file exists
const exists = fs.existsSync('notes.txt')
console.log("File exists?", exists)

// DELETE the file
fs.unlinkSync('notes.txt')
console.log("File deleted!")