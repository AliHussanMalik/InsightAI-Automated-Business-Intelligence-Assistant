import React, { useState } from 'react';
import { MessageSquare, X, Send, Bot, User, Sparkles, Loader2 } from 'lucide-react';
import { queryDataset } from '../services/api';

export const NLQChatDrawer = ({ activeDataset }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    {
      sender: 'bot',
      text: 'Hello! I am your InsightAI Assistant. Ask me anything about your active dataset in natural language!',
    },
  ]);
  const [inputQuestion, setInputQuestion] = useState('');
  const [isQuerying, setIsQuerying] = useState(false);

  const sampleChips = [
    'How many rows?',
    'What are the column names?',
    'What is the maximum value?',
    'How many missing values?',
    'What is the dataset size?',
  ];

  const handleSend = async (questionText) => {
    const question = questionText || inputQuestion;
    if (!question.trim()) return;

    if (!activeDataset?.id) {
      setMessages((prev) => [
        ...prev,
        { sender: 'user', text: question },
        { sender: 'bot', text: 'Please upload or select a dataset first before querying.' },
      ]);
      setInputQuestion('');
      return;
    }

    const userMsg = { sender: 'user', text: question };
    setMessages((prev) => [...prev, userMsg]);
    setInputQuestion('');
    setIsQuerying(true);

    try {
      const res = await queryDataset(activeDataset.id, question);
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: res.answer || 'Query processed.' },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { sender: 'bot', text: `Error: ${err.message}` },
      ]);
    } finally {
      setIsQuerying(false);
    }
  };

  return (
    <>
      {/* Floating Toggle Button */}
      <button
        className="floating-chat-btn"
        onClick={() => setIsOpen(!isOpen)}
        title="Open Natural Language Query Assistant"
      >
        {isOpen ? <X size={26} /> : <MessageSquare size={26} />}
      </button>

      {/* Drawer */}
      {isOpen && (
        <div className="chat-drawer">
          <div className="chat-header">
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <Sparkles size={18} color="var(--accent-cyan)" />
              <span style={{ fontWeight: 700, fontSize: 15 }}>NLQ AI Assistant</span>
            </div>
            <button
              onClick={() => setIsOpen(false)}
              style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer' }}
            >
              <X size={18} />
            </button>
          </div>

          <div className="chat-body">
            {messages.map((msg, idx) => (
              <div key={idx} className={`chat-bubble ${msg.sender}`}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4, fontSize: 11, opacity: 0.8 }}>
                  {msg.sender === 'bot' ? <Bot size={12} /> : <User size={12} />}
                  <span>{msg.sender === 'bot' ? 'InsightAI' : 'You'}</span>
                </div>
                <div>{msg.text}</div>
              </div>
            ))}

            {isQuerying && (
              <div className="chat-bubble bot" style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <Loader2 className="animate-spin" size={14} />
                <span>Searching dataset...</span>
              </div>
            )}
          </div>

          {/* Quick Suggestion Chips */}
          <div style={{ padding: '0 16px 8px' }}>
            <div style={{ fontSize: 11, color: 'var(--text-dim)', marginBottom: 4 }}>Quick prompts:</div>
            <div className="chip-group">
              {sampleChips.map((chip, idx) => (
                <button key={idx} className="chip" onClick={() => handleSend(chip)}>
                  {chip}
                </button>
              ))}
            </div>
          </div>

          <div className="chat-footer">
            <input
              type="text"
              className="chat-input"
              placeholder="Ask a question about your data..."
              value={inputQuestion}
              onChange={(e) => setInputQuestion(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSend()}
            />
            <button className="chat-send-btn" onClick={() => handleSend()}>
              <Send size={16} />
            </button>
          </div>
        </div>
      )}
    </>
  );
};
