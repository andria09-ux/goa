import express from "express";
import { config } from "dotnev";
import { connectDB } from "./db/connectdb.js";
import { Users } from "./models/user.model.js"

config();
const app = express()
const port = 5000 || process.env.PORT

app.get("/", async (req, res) => {
    const user = await Users.find
    res.send(user)

})

app.listen(port, () => {
   connectDB();
   console.log("app is connected", port)
 })