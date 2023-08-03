import { useState } from 'react';
import './App.css';

export default function Home() {
  const [chat, setChat] = useState([]);
  const [inputText, setInputText] = useState('');
  const [submittedInput, setSubmittedInput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setInputText(''); // Clear the input text after submitting
  
    const responseStream = await fetch('http://localhost:5000/question_answering', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ question: [inputText] }),
    });
  
    const reader = responseStream.body.getReader();
    const decoder = new TextDecoder();
  
    const processStream = async () => {
      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          break;
        }
  
        const decodedValue = decoder.decode(value);
        setChat((prevChat) => [...prevChat, decodedValue]);
      }
    };
  
    processStream();
    
    setSubmittedInput(inputText); // Set the submitted input
  };
  

  const handleInputChange = (e) => {
    setInputText(e.target.value);
    
  };

  const handleQuestionDisplay = (e) => {
    setSubmittedInput(e.target.value);
  }

  const renderChatMessages = () => {
    let expandedString = '';
    for (const message of chat) {
      expandedString += message;
    }
    return expandedString.trim();
  };

  return (
    <div className="container">
      <h1>
        ITDZ Prototyp
      </h1>
      <div className="chat-container">
        {
          submittedInput && (
            <p className="submitted-input chat-text">{submittedInput}</p>
          )
        }
        
        {submittedInput && (<div className="chat chat-text">
          
          <span className="message">{renderChatMessages()}</span>
        </div>)}
      </div>
      <div className='question-container'>
        <form className='question' onSubmit={handleSubmit}>
          <input
            type="text"
            value={inputText}
            onChange={handleInputChange}
            placeholder="Enter your message"
          />
          <button type="submit" className='submit-button'>Send</button>
        </form>
      </div>

      <style jsx>{`
        
      `}</style>
    </div>
  );
}