import React from 'react';
import { CheckCircle2, AlertOctagon, HelpCircle } from 'lucide-react';

export const QualityPanel = ({ quality }) => {
  if (!quality) return null;

  const missingValues = quality.missing_values || {};
  const missingPercents = quality.missing_percentage || {};
  const constantCols = quality.constant_columns || [];
  const highCardinality = quality.high_cardinality_columns || [];
  const emptyCols = quality.empty_columns || [];

  return (
    <div className="glass-card">
      <h3 style={{ fontSize: 18, fontWeight: 700, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 10 }}>
        <CheckCircle2 color="var(--accent-emerald)" size={20} />
        Data Quality & Health Audit
      </h3>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16, marginBottom: 20 }}>
        <div style={{ padding: 16, background: 'rgba(255,255,255,0.02)', borderRadius: 12, border: '1px solid var(--border-glass)' }}>
          <div style={{ fontSize: 13, color: 'var(--text-muted)' }}>Constant Columns (Zero Variance)</div>
          <div style={{ fontSize: 18, fontWeight: 700, marginTop: 4, color: constantCols.length > 0 ? 'var(--accent-amber)' : 'var(--accent-emerald)' }}>
            {constantCols.length > 0 ? constantCols.join(', ') : 'None detected'}
          </div>
        </div>

        <div style={{ padding: 16, background: 'rgba(255,255,255,0.02)', borderRadius: 12, border: '1px solid var(--border-glass)' }}>
          <div style={{ fontSize: 13, color: 'var(--text-muted)' }}>High-Cardinality Columns (&gt;90% Unique)</div>
          <div style={{ fontSize: 18, fontWeight: 700, marginTop: 4, color: highCardinality.length > 0 ? 'var(--accent-cyan)' : 'var(--text-main)' }}>
            {highCardinality.length > 0 ? highCardinality.join(', ') : 'None detected'}
          </div>
        </div>

        <div style={{ padding: 16, background: 'rgba(255,255,255,0.02)', borderRadius: 12, border: '1px solid var(--border-glass)' }}>
          <div style={{ fontSize: 13, color: 'var(--text-muted)' }}>Empty Columns (100% Missing)</div>
          <div style={{ fontSize: 18, fontWeight: 700, marginTop: 4, color: emptyCols.length > 0 ? 'var(--accent-rose)' : 'var(--accent-emerald)' }}>
            {emptyCols.length > 0 ? emptyCols.join(', ') : 'None detected'}
          </div>
        </div>
      </div>

      <h4 style={{ fontSize: 15, fontWeight: 600, color: 'var(--text-muted)', marginBottom: 12 }}>Missing Values Breakdown by Column</h4>
      
      <table className="data-table">
        <thead>
          <tr>
            <th>Column Name</th>
            <th>Missing Count</th>
            <th>Missing Percentage</th>
            <th>Health Status</th>
          </tr>
        </thead>
        <tbody>
          {Object.keys(missingValues).map((col) => {
            const count = missingValues[col];
            const pct = missingPercents[col] || 0;
            return (
              <tr key={col}>
                <td style={{ fontWeight: 600 }}>{col}</td>
                <td>{count}</td>
                <td>{pct}%</td>
                <td>
                  {count === 0 ? (
                    <span style={{ color: 'var(--accent-emerald)', fontSize: 13, fontWeight: 600 }}>Clean</span>
                  ) : pct > 20 ? (
                    <span style={{ color: 'var(--accent-rose)', fontSize: 13, fontWeight: 600 }}>High Missing</span>
                  ) : (
                    <span style={{ color: 'var(--accent-amber)', fontSize: 13, fontWeight: 600 }}>Minor Missing</span>
                  )}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
};
