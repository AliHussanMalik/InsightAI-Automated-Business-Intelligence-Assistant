import React from 'react';
import { Lightbulb, Wrench } from 'lucide-react';

export const InsightsPanel = ({ insights, recommendations }) => {
  const aiInsights = insights || [];
  const aiRecs = recommendations || [];

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(340px, 1fr))', gap: 24 }}>
      {/* Insights */}
      <div className="glass-card">
        <h3 style={{ fontSize: 18, fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 10, color: 'var(--accent-cyan)' }}>
          <Lightbulb size={22} />
          Automated AI Insights
        </h3>

        {aiInsights.length === 0 ? (
          <p style={{ color: 'var(--text-muted)' }}>No insights generated yet.</p>
        ) : (
          aiInsights.map((insight, idx) => (
            <div key={idx} className="insight-item">
              <span className="insight-bullet"></span>
              <span style={{ fontSize: 14, lineHeight: 1.5 }}>{insight}</span>
            </div>
          ))
        )}
      </div>

      {/* Recommendations */}
      <div className="glass-card">
        <h3 style={{ fontSize: 18, fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 10, color: 'var(--accent-amber)' }}>
          <Wrench size={22} />
          Actionable Cleaning Recommendations
        </h3>

        {aiRecs.length === 0 ? (
          <p style={{ color: 'var(--text-muted)' }}>No recommendations needed.</p>
        ) : (
          aiRecs.map((rec, idx) => (
            <div key={idx} className="insight-item" style={{ borderColor: 'rgba(245, 158, 11, 0.2)' }}>
              <span className="insight-bullet" style={{ background: 'var(--accent-amber)' }}></span>
              <span style={{ fontSize: 14, lineHeight: 1.5 }}>{rec}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
};
