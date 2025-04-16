import React from 'react';
import { BarChart, Bar, LineChart, Line, PieChart, Pie, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const balanceSheetData = [
  { 
    year: '2011', 
    currentAssets: 21970, 
    totalAssets: 138354,
    currentLiabilities: 27293, 
    totalLiabilities: 70353,
    totalEquity: 68001,
    cash: 2768,
    accountsReceivable: 6275,
    inventory: 7379,
    accountsPayable: 8022,
    currentRatio: 0.80,
    totalDebt: 32014,
    debtToCapital: 32.0
  },
  { 
    year: '2012', 
    currentAssets: 21910, 
    totalAssets: 132244,
    currentLiabilities: 24907, 
    totalLiabilities: 68209,
    totalEquity: 64035,
    cash: 4436,
    accountsReceivable: 6068,
    inventory: 6721,
    accountsPayable: 7920,
    currentRatio: 0.88,
    totalDebt: 29778,
    debtToCapital: 31.7
  },
  { 
    year: '2013', 
    currentAssets: 23990, 
    totalAssets: 139263,
    currentLiabilities: 30037, 
    totalLiabilities: 70554,
    totalEquity: 68709,
    cash: 5947,
    accountsReceivable: 6508,
    inventory: 6909,
    accountsPayable: 8777,
    currentRatio: 0.80,
    totalDebt: 31543,
    debtToCapital: 31.5
  },
  { 
    year: '2014', 
    currentAssets: 31617, 
    totalAssets: 144266,
    currentLiabilities: 33726, 
    totalLiabilities: 74290,
    totalEquity: 69976,
    cash: 10686,
    accountsReceivable: 6386,
    inventory: 6759,
    accountsPayable: 8461,
    currentRatio: 0.94,
    totalDebt: 35417,
    debtToCapital: 33.6
  },
  { 
    year: '2015', 
    currentAssets: 29646, 
    totalAssets: 129495,
    currentLiabilities: 29790, 
    totalLiabilities: 66445,
    totalEquity: 63050,
    cash: 11612,
    accountsReceivable: 4861,
    inventory: 5454,
    accountsPayable: 8257,
    currentRatio: 1.00,
    totalDebt: 30298,
    debtToCapital: 32.5
  }
];

const workingCapitalData = [
  { 
    year: '2011', 
    accountsReceivable: 6275,
    inventory: 7379,
    accountsPayable: 8022,
    workingCapital: 5632, // AR + Inv - AP
    cashConversionCycle: 22.4, // From exhibit 3
  },
  { 
    year: '2012', 
    accountsReceivable: 6068,
    inventory: 6721,
    accountsPayable: 7920,
    workingCapital: 4869,
    cashConversionCycle: 16.4,
  },
  { 
    year: '2013', 
    accountsReceivable: 6508,
    inventory: 6909,
    accountsPayable: 8777,
    workingCapital: 4640,
    cashConversionCycle: 12.6,
  },
  { 
    year: '2014', 
    accountsReceivable: 6386,
    inventory: 6759,
    accountsPayable: 8461,
    workingCapital: 4684,
    cashConversionCycle: 13.7,
  },
  { 
    year: '2015', 
    accountsReceivable: 4861,
    inventory: 5454,
    accountsPayable: 8257,
    workingCapital: 2058,
    cashConversionCycle: -3.5,
  }
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

const formatNumber = (num) => {
  return `$${(num / 1000).toFixed(1)}B`;
};

const PGBalanceSheetAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">P&G 대차대조표 분석 (2011-2015)</h2>
      
      {/* 자산, 부채, 자본 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 자산, 부채, 자본 추이 (단위: 백만 달러)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis tickFormatter={(value) => `$${value/1000}B`} />
            <Tooltip formatter={(value) => [`$${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="totalAssets" name="총자산" fill="#8884d8" />
            <Bar dataKey="totalLiabilities" name="총부채" fill="#ff8042" />
            <Bar dataKey="totalEquity" name="자본" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 유동자산 vs 유동부채 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 유동자산 vs 유동부채 (단위: 백만 달러)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis tickFormatter={(value) => `$${value/1000}B`} />
            <Tooltip formatter={(value) => [`$${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="currentAssets" name="유동자산" fill="#8884d8" />
            <Bar dataKey="currentLiabilities" name="유동부채" fill="#ff8042" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 운전자본 관련 항목 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">3. 운전자본 관련 항목 추이 (단위: 백만 달러)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis tickFormatter={(value) => `$${value/1000}B`} />
            <Tooltip formatter={(value) => [`$${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="accountsReceivable" name="매출채권" fill="#8884d8" />
            <Bar dataKey="inventory" name="재고자산" fill="#82ca9d" />
            <Bar dataKey="accountsPayable" name="매입채무" fill="#ff8042" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 현금전환주기 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">4. 현금전환주기(CCC) 추이 (단위: 일)</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[-5, 25]} />
            <Tooltip formatter={(value) => [`${value} 일`, '']} />
            <Legend />
            <Line type="monotone" dataKey="cashConversionCycle" name="현금전환주기" stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* 현금 보유량과 부채 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">5. 현금 보유량과 부채 (단위: 백만 달러)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis tickFormatter={(value) => `$${value/1000}B`} />
            <Tooltip formatter={(value) => [`$${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Line type="monotone" dataKey="cash" name="현금 및 단기투자" stroke="#82ca9d" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="totalDebt" name="총부채" stroke="#ff8042" strokeWidth={2} activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>
      
      {/* 인사이트 요약 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">핵심 인사이트</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">현금 보유량 증가</h4>
            <p>2011년 27억 달러에서 2015년 116억 달러로 4배 이상 증가</p>
            <p className="text-sm text-gray-600 mt-2">→ 유동성 관리 강화 및 불확실성 대비</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">현금전환주기 개선</h4>
            <p>2011년 22.4일에서 2015년 -3.5일로 대폭 개선</p>
            <p className="text-sm text-gray-600 mt-2">→ 공급망 금융의 효과 입증</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">매출채권 감소</h4>
            <p>2014년 대비 2015년 매출채권 15억 달러 감소</p>
            <p className="text-sm text-gray-600 mt-2">→ 매출채권 회수 효율성 향상</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">유동비율 개선</h4>
            <p>2011년 0.80에서 2015년 1.00으로 개선</p>
            <p className="text-sm text-gray-600 mt-2">→ 단기 재무 건전성 강화</p>
          </div>
        </div>
      </div>

      {/* SCF 프로그램과의 연결성 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">공급망 금융(SCF) 프로그램과의 연관성</h3>
        <ul className="list-disc pl-6 space-y-2">
          <li><span className="font-semibold">매입채무 유지</span>: 결제 기간 연장에도 매입채무 금액 유지 (약 82-83억 달러)</li>
          <li><span className="font-semibold">현금 증가</span>: 운전자본 최적화로 2014-2015년 현금 보유량 증가</li>
          <li><span className="font-semibold">재고자산 관리</span>: 2015년 재고자산 감소로 운전자본 추가 개선</li>
          <li><span className="font-semibold">부채비율 안정성</span>: 부채비율(32.5%)을 유지하며 신용등급(AA-) 보호</li>
          <li><span className="font-semibold">가시적 효과</span>: 현금전환주기 마이너스로 전환 - 공급업체 자금으로 운영 가능</li>
        </ul>
      </div>
    </div>
  );
};

export default PGBalanceSheetAnalysis;
