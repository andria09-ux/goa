import './App.css'
import audio123 from "./assets/audio/audio.mp3"

function App() {

  return (
    <div>
      <p>audio</p>
      <audio controls src={audio123}/>
    </div>
  )
}

export default App
