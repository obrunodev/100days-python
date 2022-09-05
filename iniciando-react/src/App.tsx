import { useState } from 'react';
import Tweet from './components/Tweet';

import './App.css';
import AppRoutes from './routes';

function App() {
  return (
    <AppRoutes />
    // <>
    //   <h1>Hello world</h1>

    //   <button
    //     onClick={createTweet}
    //     style={{
    //       border: 0,
    //       background: '#333',
    //       color: '#eee',
    //       fontSize: '20px',
    //       padding: '5px 10px'
    //     }}
    //   >
    //     Adicionar tweet
    //   </button>
      
    //   {tweets.map(tweet => {
    //     return <Tweet text={tweet} />
    //   })}
    // </>
  )
}

export default App
