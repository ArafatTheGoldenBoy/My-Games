function randrange(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
class Player {
    name = " player"; age = 13; gender = "none"; good_deeds = 0; bad_deeds = 0; is_alive = true; time_line = 60; good_action = ["zero"
        , "charity", "prayer for others", "haz", "zakat", "salat", "repent", "tawhid"];
    bad_action = ["zero", "greed", "envy", "lust", "wrath", "sloth", "murder", "shirk"]; good_life_history = [];
    bad_life_history = []; all_life_history = [];
    special_case = ["Becouse you did the shirk but you didn't repent. According to islam Allah not forgive for your behavier.Final destination is Hell."];
    constructor(name, age, gender) { this.gender = gender; this.name = name; this.age = age }
    aging() {
        if
            (this.is_alive == true) { this.age += 1 } else {
            console.log("He died at the age of ", this.age);

        }
    }
    random_death() {
        const random_age = randrange(this.age + 1, 63)
        this.time_line = random_age
        console.log(" He will die at ", random_age)
        //document.getElementById("death").innerHTML = "He died at the age of " + random_age;
    }
    daily_action() {
        const rd = randrange(-7, 7)
        if (rd > 0) {
            this.good_deeds += rd
            if (rd == 6) {
                this.good_deeds += -this.bad_deeds
                this.bad_deeds = 0
            }
            this.good_life_history.push(this.good_action[rd])
            this.good_life_history.push(rd)
            this.all_life_history.push(this.good_action[rd])
        }
        else if (rd == 0) {
        }
        else {
            this.bad_deeds += rd
            this.bad_life_history.push(this.bad_action[-rd])
            this.bad_life_history.push(-rd)
            this.all_life_history.push(this.bad_action[-rd])
        }
        return rd > 0 ? this.good_action[rd] : this.bad_action[-rd]
    }
    calculate_deeds() {
        const total_deeds = this.good_deeds + this.bad_deeds
        console.log(" amol nama : ", total_deeds)
        document.getElementById("score").innerHTML = " Amol nama : " + total_deeds;
        let position_of_shirk = -1
        let position_of_repent = -1
        for (let i = 0; this.all_life_history.length > i; i++) {
            console.log("histoy: " + this.all_life_history[i]);
            if (this.all_life_history[i] == "shirk") {
                position_of_shirk = i
            }
            if (this.all_life_history[i] == "repent") {
                position_of_repent = i
            }
        }
        console.log("last position of shirk" + position_of_shirk);
        console.log("last position of repent" + position_of_repent);
        if (position_of_shirk > -1 && position_of_shirk > position_of_repent) {
            console.log(this.special_case[0]);
            document.getElementById("result").innerHTML = this.special_case[0];
        }
        else {
            if (total_deeds >= 0) {
                console.log("Final destination: Paradise")
                document.getElementById("result").innerHTML = "Final destination: Paradise";
            }
            else {
                console.log("Final destination: Hell")
                document.getElementById("result").innerHTML = "Final destination: Hell";
            }
        }
    }
}
const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay * 1000))

player1 = new Player("Yasin", 28, "Male")
player1.random_death()
console.log("Player's total lifetime is ", player1.time_line)
const stop = async () => {
    for (let i = player1.age; player1.time_line > i; i++) {
        daily_result = player1.daily_action()
        await sleep(1);
        document.getElementById("daily_result").innerHTML = `Age: ${player1.age} | committing: ${daily_result}`;
        console.log("Good deeds are: " + player1.good_life_history);
        document.getElementById("good_deeds").innerHTML = player1.good_life_history;
        console.log("Bad deeds are:" + player1.bad_life_history);
        document.getElementById("bad_deeds").innerHTML = player1.bad_life_history;
        document.getElementById("history2").innerHTML = player1.all_life_history;
        player1.aging()
        if (player1.age == player1.time_line) {
            document.getElementById("dr").innerHTML = "---";
            document.getElementById("daily_result").innerHTML = "---";
            player1.is_alive = false
            break
        }
    }
}
stop()
// Create a Neural Network
const network = new brain.NeuralNetwork();
const network2 = new brain.NeuralNetwork();
async function stop2() {
    time = (player1.time_line + 2) - player1.age
    await sleep(time)
    player1.calculate_deeds()
    document.getElementById("death").innerHTML = "He died at the age of " + player1.time_line;
    console.log("good deeds score: " + player1.good_deeds)
    console.log("Evil deeds score: " + player1.bad_deeds)
    // Train the Network
    network.train([
        { input: { g: 1, b: 0 }, output: { peradise: 1 } },
        { input: { g: 0.6, b: 0.4 }, output: { peradise: 1 } },
        { input: { g: 0, b: 1 }, output: { hell: 1 } },
        { input: { g: 0.3, b: 0.8 }, output: { hell: 1 } },

    ]);
    // Train the Network
    network2.train([
        { input: { g: 1, b: 0 }, output: { peradise: 1 } },
        { input: { g: 0.7, b: 0.4 }, output: { peradise: 1 } },
        { input: { g: 0, b: 1 }, output: { hell: 1 } },
        { input: { g: 0.1, b: 0.6 }, output: { hell: 1 } },

    ]);
    /*
    max = player1.good_deeds > -player1.bad_deeds ? player1.good_deeds : -player1.bad_deeds; // 10>2 -> 10 or 2>10 -> 10
    min = player1.good_deeds < -player1.bad_deeds ? player1.good_deeds : -player1.bad_deeds; // 10<2 -> 2 or 2<10 -> 2
    normalized_good_deeds = ((player1.good_deeds - 0.1) - player1.bad_deeds) / (player1.good_deeds - player1.bad_deeds)
    normalized_bad_deeds = ((-player1.bad_deeds + 0.1) + player1.bad_deeds) / (player1.good_deeds - player1.bad_deeds) */
    let result = network.run({ g: player1.good_deeds, b: -player1.bad_deeds });
    let result2 = network2.run({ g: player1.good_deeds, b: -player1.bad_deeds });
    console.log(`normalized_good_deeds = ${player1.good_deeds}`);
    console.log(`normalized_bad_deeds = ${-player1.bad_deeds}`);
    console.log(`ai thinks: peradise = ${result["peradise"]} | hell = ${result["hell"]}`);
    console.log(`ai 2 thinks: peradise = ${result2["peradise"]} | hell = ${result2["hell"]}`);
    document.getElementById("ai1").innerHTML = "ai thinks: peradise = " + result["peradise"] + " | hell = " + result["hell"];
    document.getElementById("ai2").innerHTML = "ai thinks: peradise = " + result2["peradise"] + " | hell = " + result2["hell"];
}
stop2()
console.log("Player is alive: " + player1.is_alive)
console.log("History of doing deeds" + player1.all_life_history)
console.log("Thank you for playing")