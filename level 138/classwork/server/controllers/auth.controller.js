export const loginPost = async (req, res) => {
    try {
        res.json({message: "smth smth"})
    }catch (error) {
        res.json({error: error})
    }
}