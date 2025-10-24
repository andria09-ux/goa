// 1
let i = 5
i = 20
console.log(i)

const o = "o"
console.log(o)

//2
let a = 2
if (a = 5){
    console.log("true")
}else{
    console.log("false")
}

if (a < 5 && a > 0){
    console.log("True")
}

//3
let x = 10
let y = 5
console.log(x + y)
console.log(x - y)
console.log(x * y)
console.log(x / y)
console.log(x % y)

if (x > y){
    y++
}

//4
let k = 1 
let s = 2
let r = "abs"

if (k < s && r == "abs"){
    console.log("yaas")
}else if (k < s || k > s){
    console.log("false")
}else if (! r == "abs"){
    console.log("false again")
}

//5
let n = 694206741

if (n > 10){
    console.log("big num")
}else if (n < 10){
    console.log("smol num")
}else if (n == 10){
    console.log("10")
}

let color = ""

//6
let whileloop = 0
while (whileloop < 11){
    console.log(whileloop)
    whileloop++
} 

while (whileloop < 6){
    console.log(whileloop)
    whileloop++
} 

do{
    console.log(whileloop)
    whileloop++
}while (whileloop < 5);

//7
function addNums(num1, num2){
    console.log(num1 + num2)
}
addNums(2, 2)

function greet(name){
    console.log(`hello ${name}`)
}
greet(john)