import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { UploadZone } from './components/UploadZone';
import { KPICards } from './components/KPICards';
import { QualityPanel } from './components/QualityPanel';
import { VisualizationsGallery } from './components/VisualizationsGallery';
import { InsightsPanel } from './components/InsightsPanel';
import { NLQChatDrawer } from './components/NLQChatDrawer';
import { uploadDataset, fetchAllDatasets } from './services/api';
import { LayoutDashboard, ShieldCheck, BarChart3, Lightbulb } from 'lucide-react';

export default function App() {
  const [datasets, setDatasets] = useState([]);
  const [activeDataset, setActiveDataset] = useState(null);
  const [analysisData, setAnalysisData] = useState(null);
  const [activeTab, setActiveTab] = useState('overview');
  const [isLoading, setIsLoading] = useState(false);
  const [backendStatus, setBackendStatus] = useState(true);

  useEffect(() => {
    loadExistingDatasets();
  }, []);

  const loadExistingDatasets = async () => {
    try {
      const data = await fetchAllDatasets();
      setDatasets(data || []);
      setBackendStatus(true);
      if (data && data.length > 0) {
        setActiveDataset(data[0]);
      }
    } catch (err) {
      console.warn("Backend unavailable or starting up:", err);
      setBackendStatus(false);
    }
  };

  const handleUpload = async (file) => {
    setIsLoading(true);
    try {
      const result = await uploadDataset(file);
      setAnalysisData(result);
      if (result.dataset) {
        setActiveDataset(result.dataset);
        setDatasets((prev) => [result.dataset, ...prev]);
      }
      setActiveTab('overview');
    } catch (err) {
      alert(`Upload failed: ${err.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      {/* Top Header */}
      <Header
        datasets={datasets}
        activeDataset={activeDataset}
        onSelectDataset={setActiveDataset}
        backendStatus={backendStatus}
      />

      {/* Drag and Drop Upload Zone */}
      <UploadZone onUploadSuccess={handleUpload} isLoading={isLoading} />

      {/* Dashboard Section */}
      {activeDataset && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          {/* Executive KPI Summary */}
          <KPICards profile={analysisData?.profile} dataset={activeDataset} />

          {/* Navigation Tabs */}
          <div className="tabs-container">
            <button
              className={`tab-btn ${activeTab === 'overview' ? 'active' : ''}`}
              onClick={() => setActiveTab('overview')}
            >
              <LayoutDashboard size={18} />
              Overview &amp; Profile
            </button>

            <button
              className={`tab-btn ${activeTab === 'quality' ? 'active' : ''}`}
              onClick={() => setActiveTab('quality')}
            >
              <ShieldCheck size={18} />
              Data Health &amp; Quality Audit
            </button>

            <button
              className={`tab-btn ${activeTab === 'visualizations' ? 'active' : ''}`}
              onClick={() => setActiveTab('visualizations')}
            >
              <BarChart3 size={18} />
              Visual Analytics Gallery
            </button>

            <button
              className={`tab-btn ${activeTab === 'insights' ? 'active' : ''}`}
              onClick={() => setActiveTab('insights')}
            >
              <Lightbulb size={18} />
              AI Insights &amp; Recommendations
            </button>
          </div>

          {/* Tab Content Panels */}
          {activeTab === 'overview' && (
            <div className="glass-card">
              <h3 style={{ fontSize: 18, fontWeight: 700, marginBottom: 16 }}>
                Active Dataset: <span style={{ color: 'var(--accent-cyan)' }}>{activeDataset.filename}</span>
              </h3>
              <p style={{ color: 'var(--text-muted)', fontSize: 14, lineHeight: 1.6 }}>
                This dataset contains <strong>{activeDataset.rows}</strong> rows and <strong>{activeDataset.columns}</strong> columns.
                Use the tabs above to explore quality metrics, visual distributions, and automated AI insights, or click the bottom-right chat button to ask natural language questions.
              </p>
            </div>
          )}

          {activeTab === 'quality' && (
            <QualityPanel quality={analysisData?.quality} />
          )}

          {activeTab === 'visualizations' && (
            <VisualizationsGallery
              visualizations={analysisData?.visualizations}
              correlation={analysisData?.correlation}
            />
          )}

          {activeTab === 'insights' && (
            <InsightsPanel
              insights={analysisData?.ai_insight}
              recommendations={analysisData?.recommendations}
            />
          )}
        </div>
      )}

      {/* Natural Language Query Chat Assistant Drawer */}
      <NLQChatDrawer activeDataset={activeDataset} />
    </div>
  );
}
