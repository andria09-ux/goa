import express from "express"
import { config } from "dotenv"
import { connectDB } from "./DB/connectDB.js"
import { Users } from "./models/model.user.js"
import cors from "cors"
import router from "./routers/router.js"

config();
const app = express()


app.use(cors());
app.use(express.json())
const port = 5000 || process.env.PORT;

app.use("/api", router)

app.listen(port, () => {
    connectDB();
    console.log("App is connected", port)
})

