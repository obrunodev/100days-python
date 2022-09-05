import { useState } from 'react'
import Tweet from './components/Tweet'

function App() {
  // Inicializando um estado com strings dentro do array
  const [tweets, setTweets] = useState<string[]>([
    'Tweet 1',
    'Tweet 2',
    'Tweet 3',
  ]);

  function createTweet() {
    setTweets([...tweets, 'Tweet 5']);
  }

  return (
    <>
      <h1>Hello world</h1>

      <button onClick={createTweet}>Adicionar tweet</button>
      
      {tweets.map(tweet => {
        return <Tweet text={tweet} />
      })}
    </>
  )
}

export default App
