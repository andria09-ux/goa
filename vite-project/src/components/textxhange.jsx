import React, { useState } from 'react'

function textxhange() {
    const [text, setText] = useState('henlo')
    return (
        <div>
            <h1>{text}</h1>
            <button onClick={() => setText('bai bai')}>baitton</button>
        </div>
    )
}

export default textxhange
