import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ComposedChart, Area } from 'recharts';

const PGBalanceSheetViz = () => {
  // P&G 대차대조표 데이터 (Exhibit 2 기반)
  const balanceSheetData = [
    {
      year: '2011',
      cashAndInvestments: 2768,
      accountsReceivable: 6275,
      inventory: 7379,
      currentAssets: 21970,
      totalAssets: 138354,
      accountsPayable: 8022,
      currentLiabilities: 27293,
      longTermDebt: 22033,
      totalLiabilities: 70353,
      totalEquity: 68001,
      currentRatio: 0.80,
      totalDebt: 32014,
      netDebt: 29246,
      debtToTotalCapital: 32.0,
      financialLeverage: 2.03
    },
    {
      year: '2012',
      cashAndInvestments: 4436,
      accountsReceivable: 6068,
      inventory: 6721,
      currentAssets: 21910,
      totalAssets: 132244,
      accountsPayable: 7920,
      currentLiabilities: 24907,
      longTermDebt: 21080,
      totalLiabilities: 68209,
      totalEquity: 64035,
      currentRatio: 0.88,
      totalDebt: 29778,
      netDebt: 25342,
      debtToTotalCapital: 31.7,
      financialLeverage: 2.07
    },
    {
      year: '2013',
      cashAndInvestments: 5947,
      accountsReceivable: 6508,
      inventory: 6909,
      currentAssets: 23990,
      totalAssets: 139263,
      accountsPayable: 8777,
      currentLiabilities: 30037,
      longTermDebt: 19111,
      totalLiabilities: 70554,
      totalEquity: 68709,
      currentRatio: 0.80,
      totalDebt: 31543,
      netDebt: 25596,
      debtToTotalCapital: 31.5,
      financialLeverage: 2.03
    },
    {
      year: '2014',
      cashAndInvestments: 10686,
      accountsReceivable: 6386,
      inventory: 6759,
      currentAssets: 31617,
      totalAssets: 144266,
      accountsPayable: 8461,
      currentLiabilities: 33726,
      longTermDebt: 19811,
      totalLiabilities: 74290,
      totalEquity: 69976,
      currentRatio: 0.94,
      totalDebt: 35417,
      netDebt: 24731,
      debtToTotalCapital: 33.6,
      financialLeverage: 2.06
    },
    {
      year: '2015',
      cashAndInvestments: 11612,
      accountsReceivable: 4861,
      inventory: 5454,
      currentAssets: 29646,
      totalAssets: 129495,
      accountsPayable: 8257,
      currentLiabilities: 29790,
      longTermDebt: 18297,
      totalLiabilities: 66445,
      totalEquity: 63050,
      currentRatio: 1.00,
      totalDebt: 30298,
      netDebt: 18686,
      debtToTotalCapital: 32.5,
      financialLeverage: 2.05
    }
  ];
  
  // 자산 구조 데이터 계산
  const assetStructureData = balanceSheetData.map(year => ({
    year: year.year,
    currentAssets: year.currentAssets,
    nonCurrentAssets: year.totalAssets - year.currentAssets,
    totalAssets: year.totalAssets,
    currentAssetsPercent: Math.round(year.currentAssets / year.totalAssets * 100)
  }));
  
  // 부채 및 자본 구조 데이터 계산
  const liabEquityStructureData = balanceSheetData.map(year => ({
    year: year.year,
    currentLiabilities: year.currentLiabilities,
    longTermLiabilities: year.totalLiabilities - year.currentLiabilities,
    equity: year.totalEquity,
    total: year.totalLiabilities + year.totalEquity
  }));

  // 운전자본 항목 데이터
  const workingCapitalData = balanceSheetData.map(year => ({
    year: year.year,
    accountsReceivable: year.accountsReceivable,
    inventory: year.inventory,
    accountsPayable: year.accountsPayable,
    workingCapital: year.currentAssets - year.currentLiabilities,
    currentRatio: year.currentRatio
  }));
  
  // 현금 및 부채 데이터
  const cashDebtData = balanceSheetData.map(year => ({
    year: year.year,
    cashAndInvestments: year.cashAndInvestments,
    totalDebt: year.totalDebt,
    netDebt: year.netDebt,
    debtToTotalCapital: year.debtToTotalCapital,
    cashToTotalAssets: Math.round(year.cashAndInvestments / year.totalAssets * 100)
  }));
  
  // SCF 도입 전후 비교 데이터
  const scfComparisonData = [
    { name: '매출채권', before: 6068, after: 6386, change: 318 },
    { name: '재고', before: 6721, after: 6759, change: 38 },
    { name: '매입채무', before: 7920, after: 8461, change: 541 },
    { name: '운전자본', before: -2997, after: -2109, change: 888 },
  ];

  // 색상 설정
  const colors = {
    blue: '#2196f3',
    lightBlue: '#90caf9',
    green: '#4caf50',
    lightGreen: '#c8e6c9',
    red: '#f44336',
    orange: '#ff9800',
    purple: '#9c27b0',
    grey: '#9e9e9e'
  };

  return (
    <div className="p-4 bg-white rounded-lg">
      <h2 className="text-2xl font-bold text-center mb-8 text-blue-800">P&G 대차대조표 분석 (2011-2015)</h2>
      
      {/* 1. 자산 구조 변화 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">1. P&G 자산 구조 변화 (백만 달러)</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={assetStructureData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <YAxis yAxisId="right" orientation="right" domain={[0, 30]} />
              <Tooltip formatter={(value, name) => [
                name === '유동자산 비율' ? `${value}%` : `$${value.toLocaleString()} 백만`, 
                name
              ]} />
              <Legend />
              <Bar dataKey="currentAssets" name="유동자산" stackId="a" fill={colors.lightBlue} />
              <Bar dataKey="nonCurrentAssets" name="비유동자산" stackId="a" fill={colors.blue} />
              <Line yAxisId="right" type="monotone" dataKey="currentAssetsPercent" name="유동자산 비율" stroke={colors.orange} strokeWidth={3} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 유동자산 비율이 2011년 15.9%에서 2015년 22.9%로 증가
          </p>
        </div>
      </div>
      
      {/* 2. 부채 및 자본 구조 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">2. P&G 부채 및 자본 구조 (백만 달러)</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={liabEquityStructureData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip formatter={(value) => `$${value.toLocaleString()} 백만`} />
              <Legend />
              <Bar dataKey="currentLiabilities" name="유동부채" stackId="a" fill={colors.red} />
              <Bar dataKey="longTermLiabilities" name="비유동부채" stackId="a" fill={colors.orange} />
              <Bar dataKey="equity" name="자본" stackId="a" fill={colors.green} />
            </BarChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 자본 구조는 2011-2015년 기간 동안 비교적 안정적으로 유지 (자기자본비율: 약 48-49%)
          </p>
        </div>
      </div>

      {/* 3. 운전자본 관련 항목 변화 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">3. P&G 운전자본 관련 항목 변화</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={workingCapitalData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis domain={[-8000, 10000]} />
              <YAxis yAxisId="right" orientation="right" domain={[0, 1.2]} />
              <Tooltip formatter={(value, name) => [
                name === '유동비율' ? value.toFixed(2) : `$${value.toLocaleString()} 백만`, 
                name
              ]} />
              <Legend />
              <Bar dataKey="accountsReceivable" name="매출채권" fill={colors.lightBlue} />
              <Bar dataKey="inventory" name="재고자산" fill={colors.lightGreen} />
              <Bar dataKey="accountsPayable" name="매입채무" fill={colors.red} />
              <Line type="monotone" dataKey="workingCapital" name="순운전자본" stroke={colors.purple} strokeWidth={2} />
              <Line yAxisId="right" type="monotone" dataKey="currentRatio" name="유동비율" stroke={colors.orange} strokeWidth={3} dot={{ r: 5 }} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 유동비율이 2011년 0.80에서 2015년 1.00으로 개선됨
            <span className="ml-4 font-semibold text-blue-700">SCF 도입(2013년 4월)</span>
          </p>
        </div>
      </div>

      {/* 4. 현금 및 부채 추이 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">4. P&G 현금 및 부채 추이</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={cashDebtData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <YAxis yAxisId="right" orientation="right" domain={[0, 12]} />
              <Tooltip formatter={(value, name) => [
                name === '현금자산 비율' || name === '부채자본비율' ? `${value}%` : `$${value.toLocaleString()} 백만`, 
                name
              ]} />
              <Legend />
              <Bar dataKey="cashAndInvestments" name="현금 및 투자자산" fill={colors.green} />
              <Bar dataKey="totalDebt" name="총부채" fill={colors.red} />
              <Line type="monotone" dataKey="netDebt" name="순부채" stroke={colors.purple} strokeWidth={2} />
              <Line yAxisId="right" type="monotone" dataKey="cashToTotalAssets" name="현금자산 비율" stroke={colors.blue} strokeWidth={2} />
              <Line yAxisId="right" type="monotone" dataKey="debtToTotalCapital" name="부채자본비율" stroke={colors.orange} strokeWidth={2} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 현금자산이 2011년 $2,768백만에서 2015년 $11,612백만으로 크게 증가 (비율: 2.0% → 9.0%)
          </p>
        </div>
      </div>

      {/* 5. SCF 도입 전후 비교 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">5. SCF 도입 전후 비교 (2012 vs 2014, 백만 달러)</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={scfComparisonData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip formatter={(value) => `$${value.toLocaleString()} 백만`} />
              <Legend />
              <Bar dataKey="before" name="SCF 도입 전 (2012)" fill={colors.lightBlue} />
              <Bar dataKey="after" name="SCF 도입 후 (2014)" fill={colors.blue} />
              <Bar dataKey="change" name="변화" fill={colors.green} />
            </BarChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * SCF 도입 후 매입채무 $541백만 증가, 순운전자본 $888백만 개선
          </p>
        </div>
      </div>

      {/* 6. 핵심 인사이트 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">6. 대차대조표 분석 주요 인사이트</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">운전자본 개선</h4>
            <p>유동비율 0.80(2011) → 1.00(2015)으로 개선</p>
            <p className="text-sm text-gray-600 mt-2">→ SCF 프로그램이 운전자본 개선에 기여</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">현금보유 증가</h4>
            <p>현금 및 투자자산이 4배 이상 증가 ($2.8B → $11.6B)</p>
            <p className="text-sm text-gray-600 mt-2">→ 금융 유연성 및 위기 대응력 강화</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">매출채권 관리 개선</h4>
            <p>2015년 매출채권 $4,861백만, 2014년 대비 24% 감소</p>
            <p className="text-sm text-gray-600 mt-2">→ 효율적인 현금회수 체계 구축</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">순부채 감소</h4>
            <p>순부채가 $29.2B(2011) → $18.7B(2015)로 크게 감소</p>
            <p className="text-sm text-gray-600 mt-2">→ 재무 건전성 강화 및 이자비용 절감</p>
          </div>
        </div>
      </div>

      {/* 7. SCF와 대차대조표의 연관성 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">7. SCF와 대차대조표의 연관성</h3>
        <ul className="list-disc pl-6 space-y-2">
          <li><span className="font-semibold">매입채무 관리</span>: SCF를 통해 매입채무 지급 기간 연장(45일→75일)하면서도 공급업체와의 관계 유지</li>
          <li><span className="font-semibold">현금 관리 최적화</span>: 향상된 현금 보유력이 더 큰 재무적 유연성 제공</li>
          <li><span className="font-semibold">AA- 신용등급 유지</span>: 안정적인 부채구조 및 레버리지(~2.0)가 높은 신용등급 유지에 기여</li>
          <li><span className="font-semibold">운전자본 효율성</span>: 유동자산 대비 유동부채 비율 개선으로 자금 운용 효율성 향상</li>
          <li><span className="font-semibold">장기적 재무 구조 강화</span>: SCF는 단기적 현금흐름을 넘어 장기적 재무 건전성에 기여</li>
        </ul>
      </div>
    </div>
  );
};

export default PGBalanceSheetViz;
