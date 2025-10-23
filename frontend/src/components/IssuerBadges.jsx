const issuers = [
  { name: 'Chase', icon: '🏦', color: 'from-blue-600 to-blue-700' },
  { name: 'American Express', icon: '💳', color: 'from-indigo-600 to-indigo-700' },
  { name: 'Citibank', icon: '🏛️', color: 'from-red-600 to-red-700' },
  { name: 'Capital One', icon: '💰', color: 'from-purple-600 to-purple-700' },
  { name: 'Discover', icon: '🔍', color: 'from-orange-600 to-orange-700' },
];

const IssuerBadges = () => {
  return (
    <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-200">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-slate-800">Supported Issuers</h3>
        <span className="px-3 py-1 bg-green-100 text-green-700 text-xs font-medium rounded-full">
          5 Banks
        </span>
      </div>
      <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
        {issuers.map((issuer) => (
          <div
            key={issuer.name}
            className="group relative bg-linear-to-br from-slate-50 to-slate-100 rounded-xl p-4 hover:shadow-md transition-all duration-200 cursor-pointer border border-slate-200 hover:border-slate-300"
          >
            <div className="flex flex-col items-center space-y-2">
              <div className={`w-12 h-12 bg-linear-to-br ${issuer.color} rounded-lg flex items-center justify-center text-2xl shadow-md group-hover:scale-110 transition-transform`}>
                {issuer.icon}
              </div>
              <span className="text-xs font-medium text-slate-700 text-center">
                {issuer.name}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default IssuerBadges;
