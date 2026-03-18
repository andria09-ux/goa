import dotenv from "dotenv"
import express from "express"
import mongoose from "mongoose"
dotenv.config()

const app = express()
const port = process.env.PORT || 3000

const connectDB = async () => {
    try {
        const conn = await mongoose.connect(process.env.MONGODB_URI)
        console.log(`MongoDB connected: ${conn.connect.host}`)
    } catch(err){
        console.log(err.message)
    }
}
app.listen(port, () =>{
    connectDB()
    console.log("server is running on port", port)
})

app.get("/user", async (req, res) => {
    try{
        const UserSchema = mongoose.Schema(
            {
                name: String,
                surname: String,
            },
            {
                timestamps: true,
            },
        )
        const USER = mongoose.model("user", UserSchema)
        const user = await USER.find()
        res.json(user)
        console.log(user)
    }
    
    catch{}
})