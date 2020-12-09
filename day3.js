const input = require('fs').readFileSync('day2_input.txt', 'utf-8');
let treeMap = input
    .split('\n')
    .map(x => x.split(''));

console.log(treeMap[0])
// console.log(input.slice(Math.max(input.length - 2, 1)))
