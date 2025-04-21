import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ComposedChart } from 'recharts';

const PGFinancialDashboard = () => {
  // Exhibit 1의 데이터
  const financialData = [
    { 
      year: 2011, 
      revenue: 81104, 
      cogs: 39859, 
      grossProfit: 41245, 
      sga: 25750, 
      operatingIncome: 15495, 
      netIncome: 11797,
      grossMargin: 50.9,
      operatingMargin: 19.1,
      netMargin: 14.5,
      cogsRatio: 49.1,
      sgaRatio: 31.7
    },
    { 
      year: 2012, 
      revenue: 82006, 
      cogs: 41411, 
      grossProfit: 40595, 
      sga: 25984, 
      operatingIncome: 14611, 
      netIncome: 10756,
      grossMargin: 49.5,
      operatingMargin: 17.8,
      netMargin: 13.1,
      cogsRatio: 50.5,
      sgaRatio: 31.7
    },
    { 
      year: 2013, 
      revenue: 80116, 
      cogs: 39991, 
      grossProfit: 40125, 
      sga: 26000, 
      operatingIncome: 14125, 
      netIncome: 11612,
      grossMargin: 50.1,
      operatingMargin: 17.6,
      netMargin: 14.5,
      cogsRatio: 49.9,
      sgaRatio: 32.5
    },
    { 
      year: 2014, 
      revenue: 80510, 
      cogs: 40611, 
      grossProfit: 39899, 
      sga: 24402, 
      operatingIncome: 15497, 
      netIncome: 11643,
      grossMargin: 49.6,
      operatingMargin: 19.2,
      netMargin: 14.5,
      cogsRatio: 50.4,
      sgaRatio: 30.3
    },
    { 
      year: 2015, 
      revenue: 76279, 
      cogs: 38248, 
      grossProfit: 38031, 
      sga: 23158, 
      operatingIncome: 14873, 
      netIncome: 7036,
      grossMargin: 49.9,
      operatingMargin: 19.5,
      netMargin: 9.2,
      cogsRatio: 50.1,
      sgaRatio: 30.4
    }
  ];

  // 현금흐름 관련 데이터
  const cashFlowData = [
    { year: 2011, depreciation: 2838, capex: 3306, advertising: 9210 },
    { year: 2012, depreciation: 3204, capex: 3964, advertising: 9222 },
    { year: 2013, depreciation: 2982, capex: 4008, advertising: 9364 },
    { year: 2014, depreciation: 3141, capex: 3848, advertising: 8979 },
    { year: 2015, depreciation: 3134, capex: 3736, advertising: 8290 }
  ];

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-6 text-center">P&G 재무 데이터 시각화 (2011-2015)</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        {/* 1. 매출 및 주요 비용 추이 */}
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">매출 및 주요 비용 추이 ($백만)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <ComposedChart data={financialData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip formatter={(value) => `$${value.toLocaleString()}`} />
              <Legend />
              <Bar dataKey="revenue" name="매출" fill="#8884d8" />
              <Bar dataKey="cogs" name="COGS" fill="#82ca9d" />
              <Bar dataKey="sga" name="SG&A" fill="#ffc658" />
            </ComposedChart>
          </ResponsiveContainer>
        </div>

        {/* 2. 이익 추이 */}
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">이익 추이 ($백만)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={financialData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip formatter={(value) => `$${value.toLocaleString()}`} />
              <Legend />
              <Line type="monotone" dataKey="grossProfit" name="매출총이익" stroke="#8884d8" activeDot={{ r: 8 }} />
              <Line type="monotone" dataKey="operatingIncome" name="영업이익" stroke="#82ca9d" />
              <Line type="monotone" dataKey="netIncome" name="순이익" stroke="#ff7300" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* 3. 이익률 추이 */}
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">이익률 추이 (%)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={financialData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis domain={[0, 60]} />
              <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
              <Legend />
              <Line type="monotone" dataKey="grossMargin" name="매출총이익률" stroke="#8884d8" />
              <Line type="monotone" dataKey="operatingMargin" name="영업이익률" stroke="#82ca9d" />
              <Line type="monotone" dataKey="netMargin" name="순이익률" stroke="#ff7300" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* 4. 비용 구조 */}
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">비용 구조 (매출 대비 %)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={financialData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis domain={[0, 100]} />
              <Tooltip formatter={(value) => `${value.toFixed(1)}%`} />
              <Legend />
              <Bar dataKey="cogsRatio" name="COGS/매출" stackId="a" fill="#82ca9d" />
              <Bar dataKey="sgaRatio" name="SG&A/매출" stackId="a" fill="#ffc658" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* 5. 자본지출 및 관련 비용 */}
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">자본지출 및 주요 비용 ($백만)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={cashFlowData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip formatter={(value) => `$${value.toLocaleString()}`} />
              <Legend />
              <Line type="monotone" dataKey="depreciation" name="감가상각비" stroke="#8884d8" />
              <Line type="monotone" dataKey="capex" name="자본지출" stroke="#82ca9d" />
              <Line type="monotone" dataKey="advertising" name="광고비" stroke="#ff7300" />
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* 6. 매출 성장률 vs 이익 성장률 */}
        <div className="bg-white p-4 rounded shadow">
          <h2 className="text-lg font-semibold mb-4">연도별 증감률 ($백만)</h2>
          <ResponsiveContainer width="100%" height={300}>
            <ComposedChart data={financialData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip formatter={(value) => `$${value.toLocaleString()}`} />
              <Legend />
              <Bar dataKey="revenue" name="매출" fill="#8884d8" />
              <Line type="monotone" dataKey="netIncome" name="순이익" stroke="#ff7300" strokeWidth={2} />
            </ComposedChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="bg-blue-50 p-4 rounded shadow">
        <h2 className="text-lg font-semibold mb-2">SCF 프로그램 관점의 주요 발견점</h2>
        <ul className="list-disc pl-5 space-y-2">
          <li>2012년 비용 절감 프로그램 도입 이후 SG&A는 10.9% 감소하여 매출 감소율(7.0%)보다 더 효과적으로 관리됨</li>
          <li>영업이익률은 2011년 19.1%에서 소폭 상승하여 2015년 19.5%로 개선</li>
          <li>2015년 순이익 급감은 베네수엘라 사업 관련 특별손실 때문이며, 기본 영업 구조는 안정적</li>
          <li>SCF 프로그램은 운전자본 관리를 통한 현금흐름 개선 전략으로서, 영업이익률 유지 및 개선에 기여</li>
        </ul>
      </div>
    </div>
  );
};

export default PGFinancialDashboard;
