import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

export default function App(){
  async function fetchData(){
    fetch('https://jsonplaceholder.typicode.com/todos/1')
      .then(response => response.json())
      .then(json => console.log(json))
  }
  return(
    <div>
      <button onClick={fetchData}>fetch data</button>
    </div>
  )
}
