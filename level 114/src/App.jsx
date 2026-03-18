import { useEffect, useState } from "react"

export default function App() {
  const [posts, setPost] = useState([])
  
  useEffect(() => {

    const apiPost = async () => {
      const URL = "https://jsonplaceholder.typicode.com"
      const URL_POSTS = `${URL}/posts`
      const URL_COMMENT = `${URL}/comments`

      try {
        const request = await fetch(URL_POSTS, {
          method: "GET",
          // param: {},
          // signal
          // header
        })
        if (!request.ok) {
          throw new Error(`Response status: ${respond.status}`)
        }
        const respond = await request.json()
        console.log(respond)
        setPost(respond)
      } catch (error) {

        console.error(error.message)


      }
    }
    apiPost()


  }, [])
  return (
    <div className="bg-gray-500 space-y-2">
      {posts.map(post => <p>{post.title}</p>)}
    </div>
  )
}