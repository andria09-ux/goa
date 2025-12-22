import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    const URL = "http://localhost:5000/";
    const getUrl = async () => {
      const response = await fetch(URL, {
        method: "GET",
      });
      const result = await response.json();
      setData(result);
    };
    getUrl();
  }, []);

  console.log(data)

  return (
    <></>
  )
}

export default App
