import express from "express"
import { config } from "dotenv"
import { connectDB } from "./DB/connectDB.js"
//import { Users } from "./models/model.user.js"

config();
const app = express()
const port = 5000 || process.env.PORT;

app.get("/", async (req, res) => {
    // const user = await Users.find()
    // res.send(user);
})

app.listen(port, () => {
    connectDB();
    console.log("App is connected", port)
})