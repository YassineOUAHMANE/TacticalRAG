import React, { useState } from 'react';
import './App.css';

// Import de la fonction API
import { askQuestion } from './api/api.js';

function App() {
  const [question, setQuestion] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!question.trim()) return;

    const userMessage = { sender: 'user', text: question };
    setMessages((prev) => [...prev, userMessage]);
    setQuestion('');

    try {
      // Utilisation de la fonction d'API centralisée
      const data = await askQuestion(question);
      const botMessage = { sender: 'bot', text: data.answer };
      setMessages((prev) => [...prev, botMessage]);
    } catch (err) {
      console.error(err);
      const errorMessage = { sender: 'bot', text: "Erreur de connexion avec le backend." };
      setMessages((prev) => [...prev, errorMessage]);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <h1>TacticalRAG</h1>
        <p>Réalisé par AIT MOUSSA Amine & OUAHMANE Yassine</p>
      </div>
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              handleSend();
            }
          }}
          placeholder="Posez votre question..."
        />

        <button onClick={handleSend}>Envoyer</button>
      </div>
    </div>
  );
}

export default App;
