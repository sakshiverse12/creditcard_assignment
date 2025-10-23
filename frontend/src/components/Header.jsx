import { useState } from 'react';

const Header = () => {
  const [showInfo, setShowInfo] = useState(false);

  return (
    <header className="bg-white/80 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-linear-to-br from-blue-600 to-indigo-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" />
              </svg>
            </div>
            <div>
              <h1 className="text-xl font-bold text-slate-800">StatementParse</h1>
              <p className="text-xs text-slate-500">by Sure Finance</p>
            </div>
          </div>

          {/* Nav */}
          <nav className="hidden md:flex items-center space-x-6">
            <button
              onClick={() => setShowInfo(!showInfo)}
              className="text-slate-600 hover:text-blue-600 transition-colors font-medium"
            >
              How it works
            </button>
            <a href="#features" className="text-slate-600 hover:text-blue-600 transition-colors font-medium">
              Features
            </a>
            <a 
              href="https://creditcard-assignment.onrender.com/health" 
              target="_blank" 
              rel="noopener noreferrer"
              className="px-4 py-2 bg-linear-to-r from-blue-600 to-indigo-600 text-white rounded-lg hover:shadow-lg transition-all duration-200 font-medium"
            >
              API Status
            </a>
          </nav>

          {/* Mobile menu button */}
          <button className="md:hidden p-2 rounded-lg hover:bg-slate-100 transition-colors">
            <svg className="w-6 h-6 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>

      {/* Info Panel */}
      {showInfo && (
        <div className="border-t border-slate-200 bg-white">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
            <div className="grid md:grid-cols-3 gap-6">
              <div className="space-y-2">
                <div className="w-8 h-8 bg-blue-100 rounded-lg flex items-center justify-center">
                  <span className="text-blue-600 font-bold">1</span>
                </div>
                <h3 className="font-semibold text-slate-800">Upload Statement</h3>
                <p className="text-sm text-slate-600">Drag and drop or click to upload your credit card statement PDF</p>
              </div>
              <div className="space-y-2">
                <div className="w-8 h-8 bg-indigo-100 rounded-lg flex items-center justify-center">
                  <span className="text-indigo-600 font-bold">2</span>
                </div>
                <h3 className="font-semibold text-slate-800">Auto Processing</h3>
                <p className="text-sm text-slate-600">Our AI identifies the issuer and extracts 10+ key data points</p>
              </div>
              <div className="space-y-2">
                <div className="w-8 h-8 bg-purple-100 rounded-lg flex items-center justify-center">
                  <span className="text-purple-600 font-bold">3</span>
                </div>
                <h3 className="font-semibold text-slate-800">View Results</h3>
                <p className="text-sm text-slate-600">Get structured data instantly with confidence scores</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </header>
  );
};

export default Header;
