// const currentData = new Date()
// console.log(currentData)

class Human{
    constructor(name, surname, age){
        this.name = name;
        this.surname = surname;
        this.age = age;
    }

    greeter(){
        console.log(`greetings ${this.name} ${this.surname}`)
    }

    greeter(gamesCount){
        console.log(`greetings ${this.name} ${this.surname} games count:${gamesCount}`)
    }

    get talk(){
        console.log(`H E L L O`)
    }

    set someWords(name){
        console.log(name)
    }
}
const newHuman = new Human("davit", "grdzelo", 19);


newHuman.talk
newHuman.someWords = "winner takes it all"
console.log(newHuman.someWords)
// newHuman.greeter()
// newHuman.greeter(44)
// console.log(newHuman)
