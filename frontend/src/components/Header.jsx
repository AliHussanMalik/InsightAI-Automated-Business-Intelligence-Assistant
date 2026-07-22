import React from 'react';
import { Sparkles, Database } from 'lucide-react';
import { ThemeSelector } from './ThemeSelector';

export const Header = ({ datasets, activeDataset, onSelectDataset, backendStatus }) => {
  return (
    <header className="glass-card header-bar">
      <div className="brand">
        <div className="brand-icon">
          <Sparkles size={22} color="#ffffff" />
        </div>
        <div>
          <h1 className="brand-title">InsightAI</h1>
          <span className="brand-subtitle">Automated BI Assistant</span>
        </div>
      </div>

      <div className="header-actions">
        {/* Theme Selector */}
        <ThemeSelector />

        {/* Dataset Selector */}
        {datasets && datasets.length > 0 && (
          <div className="dataset-selector" style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <Database size={16} color="var(--text-muted)" />
            <select
              className="custom-select"
              value={activeDataset?.id || ''}
              onChange={(e) => {
                const found = datasets.find((d) => d.id === e.target.value);
                if (found) onSelectDataset(found);
              }}
            >
              {datasets.map((d) => (
                <option key={d.id} value={d.id}>
                  {d.filename} ({d.rows} rows)
                </option>
              ))}
            </select>
          </div>
        )}

        <div className="status-badge">
          <span className="status-dot" style={{ background: backendStatus ? 'var(--accent-emerald)' : 'var(--accent-rose)' }}></span>
          <span>{backendStatus ? 'Backend Connected' : 'Connecting...'}</span>
        </div>
      </div>
    </header>
  );
};

