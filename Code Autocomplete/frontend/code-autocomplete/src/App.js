import { useState } from 'react';
import Header from './components/Header';
import Editor from './components/Editor';
import Suggestion from './components/Suggestion';
import './App.css';

import Grid from '@mui/material/Grid';

function App() {
  const [enteredCode, setEnteredCode] = useState('');
  const [codeSuggestions, setCodeSuggestions] = useState([]);

  const codeChangeHandler = event => {
    setEnteredCode(event.target.value);
  }

  const clearSuggestions = () => {
    setCodeSuggestions([]);
  }

  const suggestCode = () => {
    console.log("Request Sent!!!");
    fetch('/codeSuggestions', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        prompt: enteredCode
      })
    }).then(
      res => res.json()
    ).then(
      res => {
        setCodeSuggestions(res.suggestions);
        console.log("Recived Responses!!!");
      }
    );
  }

  return (
    <div className='app'>
      <Header />
      <Grid container spacing={2}>
        <Grid item xs={7}>
          <Editor
            value={enteredCode}
            changeHandler={codeChangeHandler}
            onRequest={suggestCode}
          />
        </Grid>
        <Grid item xs={5}>
          <Suggestion
            codeSuggestions={codeSuggestions}
            onClearSuggestions={clearSuggestions}
          />
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
