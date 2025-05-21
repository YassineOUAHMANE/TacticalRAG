import React, { useState } from 'react';
import { askQuestion } from '../api/api';

const ChatInterface = () => {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await askQuestion(question);
    setResponse(res.answer);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Posez votre question..."
        />
        <button type="submit">Envoyer</button>
      </form>
      <div>{response}</div>
    </div>
  );
};

export default ChatInterface;
