import React, { useState, useRef } from 'react';
import { UploadCloud, FileSpreadsheet, AlertCircle, Loader2 } from 'lucide-react';

export const UploadZone = ({ onUploadSuccess, isLoading }) => {
  const [isDragActive, setIsDragActive] = useState(false);
  const [errorMsg, setErrorMsg] = useState(null);
  const fileInputRef = useRef(null);

  const handleFileSelect = (file) => {
    if (!file) return;

    const ext = file.name.split('.').pop().toLowerCase();
    if (!['csv', 'xlsx', 'xls'].includes(ext)) {
      setErrorMsg('Unsupported file type. Please upload a .csv, .xlsx, or .xls file.');
      return;
    }

    if (file.size > 20 * 1024 * 1024) {
      setErrorMsg('File size exceeds the 20 MB limit.');
      return;
    }

    setErrorMsg(null);
    onUploadSuccess(file);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setIsDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileSelect(e.dataTransfer.files[0]);
    }
  };

  return (
    <div
      className={`upload-zone ${isDragActive ? 'drag-active' : ''}`}
      onDragOver={(e) => { e.preventDefault(); setIsDragActive(true); }}
      onDragLeave={() => setIsDragActive(false)}
      onDrop={handleDrop}
      onClick={() => fileInputRef.current?.click()}
    >
      <input
        type="file"
        ref={fileInputRef}
        onChange={(e) => handleFileSelect(e.target.files[0])}
        accept=".csv,.xlsx,.xls"
        style={{ display: 'none' }}
      />

      {isLoading ? (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
          <Loader2 className="animate-spin" size={48} color="var(--accent-cyan)" />
          <h3 className="upload-title" style={{ color: 'var(--accent-cyan)' }}>
            Profiling & Analyzing Dataset...
          </h3>
          <p className="upload-desc">Computing stats, correlations, quality metrics & generating visual graphs.</p>
        </div>
      ) : (
        <>
          <div className="upload-icon-wrapper">
            <UploadCloud size={32} />
          </div>

          <h3 className="upload-title">Drag & Drop Dataset or Click to Browse</h3>
          <p className="upload-desc">Upload your business data to automatically trigger full AI profiling and natural language query processing.</p>

          <div className="file-badges">
            <span className="badge">.CSV</span>
            <span className="badge">.XLSX</span>
            <span className="badge">.XLS</span>
            <span className="badge">Max 20 MB</span>
          </div>

          {errorMsg && (
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 8, marginTop: 16, color: 'var(--accent-rose)', fontSize: 14 }}>
              <AlertCircle size={16} />
              <span>{errorMsg}</span>
            </div>
          )}
        </>
      )}
    </div>
  );
};
