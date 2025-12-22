import mongoose from "mongoose";

const UserSchema = mongoose.Schema({
    name: String,
    age: Number,
})

export const Users = mongoose.model("user", UserSchema); 