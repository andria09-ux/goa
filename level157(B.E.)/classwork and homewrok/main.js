import dotenv from "dotenv";
import express from "express";
import mongoose from "mongoose";
dotenv.config();

const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());
const connectDB = async () => {
  try {
    const conn = await mongoose.connect(process.env.MONGODB_URI);
    console.log(`MongoDB connected: ${conn.connection.host}`);
  } catch (err) {
    console.log(err.message);
  }
};

const UserSchema = mongoose.Schema(
  {
    name: String,
    email: String,
  },
  {
    timestamps: true,
  },
);
const USER = mongoose.model("user", UserSchema);
app.post("/user", async (req, res) => {
  try {
    const user = await USER.create(req.body);
    res.status(201).json({ message: "user created successfully", user });
    console.log(user);
  } catch (err) {
    console.log(err.message);
  }
});
app.get("/user", async (req, res) => {
  try {
    const user = await USER.find();
    res.status(200).json(user);
    console.log(user);
  } catch (err) {
    console.log(err.message);
  }
});

app.listen(port, () => {
  connectDB();
  console.log("server is running on port", port);
});