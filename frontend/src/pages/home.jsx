import React from 'react';
import ChatInterface from '../components/ChatInterface';
import UploadForm from '../components/UploadForm';

const Home = () => (
  <div>
    <h1>Football RAG</h1>
    <UploadForm />
    <ChatInterface />
  </div>
);

export default Home;
