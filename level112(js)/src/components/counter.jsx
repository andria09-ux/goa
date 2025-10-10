import React from 'react'
import { useState } from 'react'
export default function Counter() {
  const [count, setCount] = useState(0)
  const handleincrease = () =>{
    setCount(count + 1)
    // count = count + 1
    console.log("increase", count)
  }
  return (
    <div className='flex flex-col *:[button]:bg-red-500'>
      <button>{count}</button>
      <button onClick={handleincrease}>+1</button>
    </div>
  )
}
