import { useState } from 'react';
import ResultCard from './ResultCard';

const ResultsDisplay = ({ results, onClear, onRemove }) => {
  const [expandedId, setExpandedId] = useState(null);

  return (
    <div className="space-y-4">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-slate-800">Parsed Statements</h2>
          <p className="text-slate-500 mt-1">{results.length} statement{results.length !== 1 ? 's' : ''} processed</p>
        </div>
        <button
          onClick={onClear}
          className="px-4 py-2 text-red-600 hover:bg-red-50 rounded-lg transition-colors font-medium flex items-center space-x-2"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
          </svg>
          <span>Clear All</span>
        </button>
      </div>

      {/* Results Grid */}
      <div className="grid gap-4">
        {results.map((result) => (
          <ResultCard
            key={result.id}
            result={result}
            isExpanded={expandedId === result.id}
            onToggle={() => setExpandedId(expandedId === result.id ? null : result.id)}
            onRemove={() => onRemove(result.id)}
          />
        ))}
      </div>
    </div>
  );
};

export default ResultsDisplay;
