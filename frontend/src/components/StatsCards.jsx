const StatsCards = ({ stats }) => {
  return (
    <div className="grid md:grid-cols-3 gap-6">
      {/* Total Parsed */}
      <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-md transition-shadow">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm font-medium text-slate-600">Total Parsed</p>
            <p className="text-3xl font-bold text-slate-800 mt-2">{stats.totalParsed}</p>
            <p className="text-xs text-slate-500 mt-1">Statements processed</p>
          </div>
          <div className="w-14 h-14 bg-linear-to-br from-blue-100 to-blue-200 rounded-2xl flex items-center justify-center">
            <svg className="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
            </svg>
          </div>
        </div>
      </div>

      {/* Success Rate */}
      <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-md transition-shadow">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm font-medium text-slate-600">Success Rate</p>
            <p className="text-3xl font-bold text-green-600 mt-2">{stats.successRate}%</p>
            <p className="text-xs text-slate-500 mt-1">Successful extractions</p>
          </div>
          <div className="w-14 h-14 bg-linear-to-br from-green-100 to-green-200 rounded-2xl flex items-center justify-center">
            <svg className="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>
        <div className="mt-4 w-full bg-slate-100 rounded-full h-2 overflow-hidden">
          <div 
            className="h-full bg-linear-to-r from-green-500 to-green-600 rounded-full transition-all duration-500"
            style={{ width: `${stats.successRate}%` }}
          ></div>
        </div>
      </div>

      {/* Avg Confidence */}
      <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-md transition-shadow">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm font-medium text-slate-600">Avg Confidence</p>
            <p className="text-3xl font-bold text-purple-600 mt-2">{stats.avgConfidence}%</p>
            <p className="text-xs text-slate-500 mt-1">Extraction quality</p>
          </div>
          <div className="w-14 h-14 bg-linear-to-br from-purple-100 to-purple-200 rounded-2xl flex items-center justify-center">
            <svg className="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
        </div>
        <div className="mt-4 w-full bg-slate-100 rounded-full h-2 overflow-hidden">
          <div 
            className="h-full bg-linear-to-r from-purple-500 to-purple-600 rounded-full transition-all duration-500"
            style={{ width: `${stats.avgConfidence}%` }}
          ></div>
        </div>
      </div>
    </div>
  );
};

export default StatsCards;
