const ResultCard = ({ result, isExpanded, onToggle, onRemove }) => {
  const getConfidenceColor = (confidence) => {
    if (confidence === 'high') return 'bg-green-100 text-green-800 border-green-200';
    if (confidence === 'medium') return 'bg-yellow-100 text-yellow-800 border-yellow-200';
    return 'bg-orange-100 text-orange-800 border-orange-200';
  };

  const getIssuerIcon = (issuer) => {
    const icons = {
      'Chase': '🏦',
      'American Express': '💳',
      'Citibank': '🏛️',
      'Capital One': '💰',
      'Discover': '🔍'
    };
    return icons[issuer] || '💳';
  };

  const getIssuerColor = (issuer) => {
    const colors = {
      'Chase': 'from-blue-600 to-blue-700',
      'American Express': 'from-indigo-600 to-indigo-700',
      'Citibank': 'from-red-600 to-red-700',
      'Capital One': 'from-purple-600 to-purple-700',
      'Discover': 'from-orange-600 to-orange-700'
    };
    return colors[issuer] || 'from-slate-600 to-slate-700';
  };

  const formatCurrency = (amount) => {
    if (!amount) return 'N/A';
    return amount;
  };

  const formatDate = (date) => {
    if (!date) return 'N/A';
    return date;
  };

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden hover:shadow-md transition-shadow">
      {/* Card Header */}
      <div className="p-6 border-b border-slate-100">
        <div className="flex items-start justify-between">
          <div className="flex items-start space-x-4 flex-1">
            {/* Issuer Badge */}
            <div className={`w-14 h-14 rounded-xl bg-linear-to-br ${getIssuerColor(result.data.card_issuer)} flex items-center justify-center text-2xl shadow-lg`}>
              {getIssuerIcon(result.data.card_issuer)}
            </div>

            {/* Info */}
            <div className="flex-1 min-w-0">
              <div className="flex items-center space-x-3">
                <h3 className="text-lg font-semibold text-slate-800 truncate">
                  {result.data.card_issuer || 'Unknown Issuer'}
                </h3>
                <span className={`px-3 py-1 text-xs font-medium rounded-full border ${getConfidenceColor(result.data.extraction_confidence)}`}>
                  {result.data.extraction_confidence} confidence
                </span>
              </div>
              <p className="text-sm text-slate-500 mt-1 truncate">{result.filename}</p>
              <div className="flex items-center space-x-4 mt-2 text-sm text-slate-600">
                <span className="flex items-center space-x-1">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
                  </svg>
                  <span>•••• {result.data.card_last_4_digits || 'N/A'}</span>
                </span>
                <span className="flex items-center space-x-1">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                  <span>{formatDate(result.data.statement_date)}</span>
                </span>
              </div>
            </div>
          </div>

          {/* Actions */}
          <div className="flex items-center space-x-2 ml-4">
            <button
              onClick={onToggle}
              className="p-2 hover:bg-slate-100 rounded-lg transition-colors"
              title={isExpanded ? 'Collapse' : 'Expand'}
            >
              <svg 
                className={`w-5 h-5 text-slate-600 transition-transform ${isExpanded ? 'rotate-180' : ''}`} 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            <button
              onClick={onRemove}
              className="p-2 hover:bg-red-50 text-red-600 rounded-lg transition-colors"
              title="Remove"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        {/* Quick Stats */}
        <div className="grid grid-cols-3 gap-4 mt-4 pt-4 border-t border-slate-100">
          <div className="text-center">
            <p className="text-sm text-slate-500">Balance</p>
            <p className="text-lg font-bold text-slate-800">{formatCurrency(result.data.total_balance)}</p>
          </div>
          <div className="text-center border-x border-slate-100">
            <p className="text-sm text-slate-500">Due</p>
            <p className="text-lg font-bold text-slate-800">{formatCurrency(result.data.minimum_payment)}</p>
          </div>
          <div className="text-center">
            <p className="text-sm text-slate-500">Due Date</p>
            <p className="text-lg font-bold text-slate-800">{formatDate(result.data.payment_due_date)}</p>
          </div>
        </div>
      </div>

      {/* Expanded Details */}
      {isExpanded && (
        <div className="p-6 bg-slate-50 space-y-6 animate-fadeIn">
          {/* Account Information */}
          <div>
            <h4 className="text-sm font-semibold text-slate-700 mb-3 flex items-center space-x-2">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
              <span>Account Information</span>
            </h4>
            <div className="grid md:grid-cols-2 gap-4">
              <DataField label="Account Holder" value={result.data.account_holder} />
              <DataField label="Card Number" value={`•••• ${result.data.card_last_4_digits}`} />
              <DataField label="Credit Limit" value={formatCurrency(result.data.credit_limit)} />
              <DataField label="Available Credit" value={formatCurrency(result.data.available_credit)} />
            </div>
          </div>

          {/* Billing Information */}
          <div>
            <h4 className="text-sm font-semibold text-slate-700 mb-3 flex items-center space-x-2">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
              <span>Billing Information</span>
            </h4>
            <div className="grid md:grid-cols-2 gap-4">
              <DataField label="Billing Cycle" value={result.data.billing_cycle} />
              <DataField label="Statement Date" value={formatDate(result.data.statement_date)} />
              <DataField label="Payment Due Date" value={formatDate(result.data.payment_due_date)} />
              <DataField label="Total Balance" value={formatCurrency(result.data.total_balance)} />
            </div>
          </div>

          {/* Export Options */}
          <div className="flex items-center justify-between pt-4 border-t border-slate-200">
            <div className="text-xs text-slate-500">
              Parsed at: {new Date(result.parsedAt).toLocaleString()}
            </div>
            <button className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors text-sm font-medium flex items-center space-x-2">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              <span>Export JSON</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

const DataField = ({ label, value }) => (
  <div className="bg-white rounded-lg p-3 border border-slate-200">
    <p className="text-xs text-slate-500 mb-1">{label}</p>
    <p className="text-sm font-semibold text-slate-800">{value || 'N/A'}</p>
  </div>
);

export default ResultCard;
