import React, { useState } from 'react'
import Tweet from '../../components/Tweet';

const Feed = () => {
  // Inicializando um estado para os tweets
  const [tweets, setTweets] = useState([
    'Tweet 1',
    'Tweet 2',
    'Tweet 3',
  ]);

  function createTweet() {
    setTweets([...tweets, `Tweet ${tweets.length+1}`])
  }

  return (
    <>
      <h1>Feed de tweets</h1>

      {tweets.map((tweet, index) => {
        return <Tweet text={tweet} key={index} />
      })}

      <button
        onClick={createTweet}
        style={{
          border: 0,
          background: '#333',
          color: '#eee',
          fontSize: '20px',
          padding: '5px 10px'
        }}
      >
        Adicionar tweet
      </button>
    </>
  )
}

export default Feed