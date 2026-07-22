import React from 'react';
import { Layers, Columns, Copy, AlertTriangle, HardDrive, Hash } from 'lucide-react';

export const KPICards = ({ profile, dataset }) => {
  if (!profile && !dataset) return null;

  const totalRows = profile?.rows ?? dataset?.rows ?? 0;
  const totalCols = profile?.columns ?? dataset?.columns ?? 0;
  const duplicates = profile?.duplicate_rows ?? 0;
  const missingValues = profile?.missing_values ? Object.values(profile.missing_values).reduce((a, b) => a + b, 0) : 0;
  const memoryMb = profile?.memory_usage_mb ?? 0;

  const kpis = [
    {
      label: 'Total Rows',
      value: totalRows.toLocaleString(),
      icon: <Layers size={22} color="var(--accent-indigo)" />,
      bg: 'rgba(99, 102, 241, 0.15)',
    },
    {
      label: 'Columns Count',
      value: totalCols,
      icon: <Columns size={22} color="var(--accent-cyan)" />,
      bg: 'rgba(6, 182, 212, 0.15)',
    },
    {
      label: 'Duplicate Rows',
      value: duplicates,
      icon: <Copy size={22} color={duplicates > 0 ? 'var(--accent-amber)' : 'var(--accent-emerald)'} />,
      bg: duplicates > 0 ? 'rgba(245, 158, 11, 0.15)' : 'rgba(16, 185, 129, 0.15)',
    },
    {
      label: 'Missing Values',
      value: missingValues,
      icon: <AlertTriangle size={22} color={missingValues > 0 ? 'var(--accent-rose)' : 'var(--accent-emerald)'} />,
      bg: missingValues > 0 ? 'rgba(244, 63, 94, 0.15)' : 'rgba(16, 185, 129, 0.15)',
    },
    {
      label: 'Memory Usage',
      value: `${memoryMb} MB`,
      icon: <HardDrive size={22} color="var(--accent-violet)" />,
      bg: 'rgba(139, 92, 246, 0.15)',
    },
  ];

  return (
    <div className="kpi-grid">
      {kpis.map((kpi, idx) => (
        <div key={idx} className="glass-card kpi-card">
          <div className="kpi-icon" style={{ background: kpi.bg }}>
            {kpi.icon}
          </div>
          <div>
            <div className="kpi-val">{kpi.value}</div>
            <div className="kpi-lbl">{kpi.label}</div>
          </div>
        </div>
      ))}
    </div>
  );
};
