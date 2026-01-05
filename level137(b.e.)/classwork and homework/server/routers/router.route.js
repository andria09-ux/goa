import express from "express"
import { getAuth, getMainFunk } from "../controllers/lomi.controllers"


const router = express.Router()

router.get("/", getMainFunk)

router.get("/auth", getAuth)


export default router