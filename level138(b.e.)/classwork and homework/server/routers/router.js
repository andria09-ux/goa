import express from "express"
import authRoute from "./auth.route.js"
import projectRoute from "./project.route.js"

const router = express.Router()

router.use("/auth", authRoute)
router.use("/projects", projectRoute)


export default router