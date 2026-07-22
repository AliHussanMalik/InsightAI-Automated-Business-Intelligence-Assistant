import React from 'react';
import { BarChart3, LineChart } from 'lucide-react';

export const VisualizationsGallery = ({ visualizations, correlation }) => {
  if (!visualizations || visualizations.length === 0) {
    return (
      <div className="glass-card" style={{ textAlign: 'center', padding: 40, color: 'var(--text-muted)' }}>
        No numeric visualizations available for this dataset.
      </div>
    );
  }

  const strongCorrelations = correlation?.strong_correlations || [];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
      {/* Strong Correlations Summary */}
      {strongCorrelations.length > 0 && (
        <div className="glass-card">
          <h3 style={{ fontSize: 18, fontWeight: 700, marginBottom: 12, display: 'flex', alignItems: 'center', gap: 8 }}>
            <LineChart color="var(--accent-cyan)" size={20} />
            Strong Column Correlations (&ge; 0.70)
          </h3>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10 }}>
            {strongCorrelations.map((item, idx) => (
              <div key={idx} className="badge" style={{ background: 'rgba(6, 182, 212, 0.15)', color: '#fff', padding: '8px 14px', fontSize: 13 }}>
                <strong>{item.column_1}</strong> &amp; <strong>{item.column_2}</strong>: {item.correlation}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Visual Graphs Cards */}
      <div className="glass-card">
        <h3 style={{ fontSize: 18, fontWeight: 700, marginBottom: 20, display: 'flex', alignItems: 'center', gap: 8 }}>
          <BarChart3 color="var(--accent-indigo)" size={20} />
          Automated Visual Distributions
        </h3>

        <div className="charts-grid">
          {visualizations.map((vis, idx) => (
            <div key={idx} className="chart-card glass-card" style={{ background: 'rgba(30, 41, 59, 0.4)' }}>
              <h4 style={{ fontSize: 16, fontWeight: 700, color: 'var(--accent-cyan)' }}>
                {vis.column} Analysis
              </h4>
              <div style={{ fontSize: 13, color: 'var(--text-muted)' }}>
                Generated Distribution Histogram &amp; Outlier Boxplot
              </div>
              <div style={{ display: 'flex', gap: 8, marginTop: 8 }}>
                <span className="badge">Histogram</span>
                <span className="badge">Boxplot</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
