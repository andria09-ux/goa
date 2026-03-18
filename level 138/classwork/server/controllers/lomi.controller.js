export const gatMainFunc = async (req, res) => {
    try{
        res.json({message: "request has been sent"})
    }catch (error){
        res.json({message: error})
    }
}

export const getAuth = async (req, res) => {
    try{
        res.json({message: "user has been idk"})
    }catch (error){
        res.json({message: error})
    }
}