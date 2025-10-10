import React from 'react'
import { useEffect, useState } from 'react'

export default function App() {
  const [post, setPosts] = useState([])

  useEffect(() => {
    const apiFetch = async () => {
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(json => setPosts(json))
      .then(err => console.log(err))
    }
    apiFetch()
  },[])
  console.log(posts)
  return (
    <div>
      {posts.map(posts => <div>{posts.title}</div>)}
      {/* <ul>{posts.map((posts, index)<li></li>}</ul> */}
    </div>
  )
}
