type TweetProps = { text: string; }

const Tweet = (props: TweetProps) => {
  return (
    <p>{props.text}</p>
  )
}

export default Tweet