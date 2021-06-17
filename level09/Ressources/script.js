const token = process.argv[2]
let result = token[0]
for (let index = 1; index < token.length; index++) {
  result += String.fromCharCode(token[index].charCodeAt() - index)
}
console.log(result)