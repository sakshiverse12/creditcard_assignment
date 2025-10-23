import { useState, useRef } from 'react';
import Header from './components/Header';
import UploadZone from './components/UploadZone';
import ResultsDisplay from './components/ResultsDisplay';
import StatsCards from './components/StatsCards';
import IssuerBadges from './components/IssuerBadges';
import Footer from './components/Footer';

const API_BASE_URL = 'http://localhost:5000';

function App() {
  const [files, setFiles] = useState([]);
  const [uploading, setUploading] = useState(false);
  const [results, setResults] = useState([]);
  const [error, setError] = useState(null);
  const [stats, setStats] = useState({
    totalParsed: 0,
    successRate: 100,
    avgConfidence: 0
  });

  const handleFilesSelected = async (selectedFiles) => {
    setError(null);
    setFiles(selectedFiles);
    
    if (selectedFiles.length > 0) {
      await uploadFiles(selectedFiles);
    }
  };

  const uploadFiles = async (filesToUpload) => {
    setUploading(true);
    setError(null);

    try {
      if (filesToUpload.length === 1) {
        // Single file upload
        const formData = new FormData();
        formData.append('file', filesToUpload[0]);

        const response = await fetch(`${API_BASE_URL}/api/parse`, {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Failed to parse statement');
        }

        const data = await response.json();
        const newResult = {
          id: Date.now(),
          filename: filesToUpload[0].name,
          data: data.data,
          status: 'success',
          parsedAt: data.parsed_at
        };

        setResults(prev => [newResult, ...prev]);
        updateStats([newResult, ...results]);
      } else {
        // Batch upload
        const formData = new FormData();
        filesToUpload.forEach(file => {
          formData.append('files', file);
        });

        const response = await fetch(`${API_BASE_URL}/api/batch-parse`, {
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Failed to parse statements');
        }

        const data = await response.json();
        const newResults = data.results.map(result => ({
          id: Date.now() + Math.random(),
          filename: result.filename,
          data: result.data,
          status: result.status,
          parsedAt: data.parsed_at
        }));

        setResults(prev => [...newResults, ...prev]);
        updateStats([...newResults, ...results]);
      }

      setFiles([]);
    } catch (err) {
      setError(err.message);
      console.error('Upload error:', err);
    } finally {
      setUploading(false);
    }
  };

  const updateStats = (allResults) => {
    const successful = allResults.filter(r => r.status === 'success').length;
    const total = allResults.length;
    const avgConf = allResults.reduce((acc, r) => {
      const conf = r.data?.extraction_confidence;
      if (conf === 'high') return acc + 100;
      if (conf === 'medium') return acc + 65;
      if (conf === 'low') return acc + 30;
      return acc;
    }, 0) / total;

    setStats({
      totalParsed: total,
      successRate: total > 0 ? Math.round((successful / total) * 100) : 100,
      avgConfidence: Math.round(avgConf) || 0
    });
  };

  const handleClearResults = () => {
    setResults([]);
    setStats({
      totalParsed: 0,
      successRate: 100,
      avgConfidence: 0
    });
  };

  const handleRemoveResult = (id) => {
    const newResults = results.filter(r => r.id !== id);
    setResults(newResults);
    updateStats(newResults);
  };

  return (
    <div className="min-h-screen bg-linear-to-br from-slate-50 via-blue-50 to-indigo-50">
      <Header />
      
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
        {/* Hero Section */}
        <div className="text-center space-y-4 py-8">
          <h1 className="text-5xl font-bold bg-linear-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
            Credit Card Statement Parser
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Extract key financial data from your credit card statements instantly. 
            Supports 5 major issuers with AI-powered accuracy.
          </p>
        </div>

        {/* Issuer Badges */}
        <IssuerBadges />

        {/* Stats Cards */}
        {results.length > 0 && <StatsCards stats={stats} />}

        {/* Upload Zone */}
        <UploadZone 
          onFilesSelected={handleFilesSelected}
          uploading={uploading}
          error={error}
        />

        {/* Results Display */}
        {results.length > 0 && (
          <ResultsDisplay 
            results={results}
            onClear={handleClearResults}
            onRemove={handleRemoveResult}
          />
        )}

        {/* Empty State */}
        {results.length === 0 && !uploading && (
          <div className="text-center py-16 space-y-4">
            <div className="w-24 h-24 mx-auto bg-linear-to-br from-blue-100 to-indigo-100 rounded-full flex items-center justify-center">
              <svg className="w-12 h-12 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 className="text-xl font-semibold text-slate-700">No statements parsed yet</h3>
            <p className="text-slate-500">Upload your first credit card statement to get started</p>
          </div>
        )}
      </main>

      <Footer />
    </div>
  );
}

export default App;