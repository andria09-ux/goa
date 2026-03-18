import React, { useState } from 'react'

export default function App() {

  const [count, setCount] = useState(0)

  const increase = () => {
    setCount(count + 1)
  }

  const decrease = () => {
    setCount(count - 1)
  }

  return (
    <div>
      <div>clicks: {count}</div>
      <button onClick={increase}>click +</button>
      <button onClick={decrease}>click -</button>
    </div>
  )
}

