import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

// 손익계산서 데이터 (단위: 백만 레알)
const incomeData = [
  { 
    year: '2012', 
    revenue: 6174, 
    cogs: 5237, 
    grossProfit: 937, 
    sgaExpense: 579, 
    operatingIncome: 345, 
    netIncome: -705,
    grossMargin: 15.2,
    operatingMargin: 5.6,
    netMargin: -11.4,
    exchangeRate: 1.955,
    revenueUSD: 3159,
    pulpSales: 5357,
    pulpPrice: 780
  },
  { 
    year: '2013', 
    revenue: 6317, 
    cogs: 5302, 
    grossProfit: 1535, 
    sgaExpense: 642, 
    operatingIncome: 914, 
    netIncome: -706,
    grossMargin: 22.2,
    operatingMargin: 13.2,
    netMargin: -10.2,
    exchangeRate: 2.1605,
    revenueUSD: 2924,
    pulpSales: 5198,
    pulpPrice: 770
  },
  { 
    year: '2014', 
    revenue: 7084, 
    cogs: 5546, 
    grossProfit: 1538, 
    sgaExpense: 644, 
    operatingIncome: 1660, 
    netIncome: 156,
    grossMargin: 21.7,
    operatingMargin: 23.4,
    netMargin: 2.2,
    exchangeRate: 2.3547,
    revenueUSD: 3009,
    pulpSales: 5305,
    pulpPrice: 741
  },
  { 
    year: '2015 (6월까지)', 
    revenue: 8054, 
    cogs: 5560, 
    grossProfit: 2494, 
    sgaExpense: 703, 
    operatingIncome: 1698, 
    netIncome: -449,
    grossMargin: 31.0,
    operatingMargin: 21.1,
    netMargin: -5.6,
    exchangeRate: 2.5989,
    revenueUSD: 3099,
    pulpSales: 5370,
    pulpPrice: 793
  }
];

// 환율 및 펄프 가격 추이
const marketData = [
  { year: '2012', exchangeRate: 1.955, pulpPrice: 780 },
  { year: '2013', exchangeRate: 2.1605, pulpPrice: 770 },
  { year: '2014', exchangeRate: 2.3547, pulpPrice: 741 },
  { year: '2015', exchangeRate: 2.5989, pulpPrice: 793 }
];

// SCF 프로그램 영향 분석 (2013년 SCF 도입)
const scfImpactData = [
  { 
    year: '2012', 
    withoutSCF: {
      financingCost: 154.35, // 가정: 60일 매출채권, 2.5% 금리
      cashFlow: 3159 - 154.35
    },
    withSCF: {
      financingCost: 154.35,
      cashFlow: 3159 - 154.35
    }
  },
  { 
    year: '2013', 
    withoutSCF: {
      financingCost: 146.20, // 60일, 2.5% 금리
      cashFlow: 2924 - 146.20
    },
    withSCF: {
      financingCost: 34.02, // 15일, 0.35% 할인율 (도입 중)
      cashFlow: 2924 - 34.02
    }
  },
  { 
    year: '2014', 
    withoutSCF: {
      financingCost: 150.45, // 60일, 2.5% 금리
      cashFlow: 3009 - 150.45
    },
    withSCF: {
      financingCost: 31.59, // 15일, 0.35% 할인율
      cashFlow: 3009 - 31.59
    }
  },
  { 
    year: '2015', 
    withoutSCF: {
      financingCost: 154.95, // 60일, 2.5% 금리
      cashFlow: 3099 - 154.95
    },
    withSCF: {
      financingCost: 32.54, // 15일, 0.35% 할인율
      cashFlow: 3099 - 32.54
    }
  }
];

const FibriaFinancialAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">피브리아 셀룰로즈 재무 분석 (2012-2015)</h2>
      
      {/* 매출 및 이익 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 매출 및 이익 추이 (단위: 백만 레알)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={incomeData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[-1000, 9000]} />
            <Tooltip formatter={(value) => [`R$ ${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="revenue" name="매출" fill="#8884d8" />
            <Bar dataKey="grossProfit" name="매출총이익" fill="#82ca9d" />
            <Bar dataKey="operatingIncome" name="영업이익" fill="#ffc658" />
            <Bar dataKey="netIncome" name="당기순이익" fill="#ff8042" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 수익성 비율 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 수익성 비율 추이 (%)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={incomeData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[-15, 35]} />
            <Tooltip formatter={(value) => [`${value}%`, '']} />
            <Legend />
            <Line type="monotone" dataKey="grossMargin" name="매출총이익률" stroke="#82ca9d" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="operatingMargin" name="영업이익률" stroke="#ffc658" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="netMargin" name="순이익률" stroke="#ff8042" strokeWidth={2} activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* 환율 및 펄프 가격 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">3. 환율 및 펄프 가격 추이</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={marketData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis yAxisId="left" />
            <YAxis yAxisId="right" orientation="right" domain={[700, 850]} />
            <Tooltip />
            <Legend />
            <Line yAxisId="left" type="monotone" dataKey="exchangeRate" name="환율(레알/달러)" stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line yAxisId="right" type="monotone" dataKey="pulpPrice" name="펄프 가격(USD/톤)" stroke="#82ca9d" strokeWidth={2} activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* SCF 프로그램 영향 분석 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">4. SCF 프로그램 영향 분석 (단위: 백만 달러)</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">자금조달 비용 비교</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip formatter={(value) => [`$${value.toFixed(2)} 백만`, '']} />
                <Legend />
                <Bar dataKey="withoutSCF.financingCost" name="SCF 없음 (2.5% 금리)" fill="#ff8042" />
                <Bar dataKey="withSCF.financingCost" name="SCF 이용 (0.35% 할인율)" fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">연간 절감액</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={[
                  { year: '2013', savings: 146.20 - 34.02 },
                  { year: '2014', savings: 150.45 - 31.59 },
                  { year: '2015', savings: 154.95 - 32.54 }
                ]}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis />
                <Tooltip formatter={(value) => [`$${value.toFixed(2)} 백만`, '']} />
                <Legend />
                <Bar dataKey="savings" name="SCF 통한 연간 절감액" fill="#8884d8" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* 핵심 인사이트 요약 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">핵심 인사이트</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">사업 성과의 양면성</h4>
            <p>2012-2015년 영업이익 크게 개선 (345 → 1698백만 레알)</p>
            <p className="text-sm text-gray-600 mt-2">→ 하지만 환율 손실로 당기순이익은 변동성 큼</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">환율 영향</h4>
            <p>레알/달러 환율 상승 (1.96 → 2.60)</p>
            <p className="text-sm text-gray-600 mt-2">→ 달러 매출에 유리하나 달러 부채에 불리</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">수익성 개선</h4>
            <p>매출총이익률 15.2% → 31.0%로 크게 상승</p>
            <p className="text-sm text-gray-600 mt-2">→ 운영 효율성 향상 및 펄프 가격 상승 효과</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">SCF 프로그램 효과</h4>
            <p>연간 약 120백만 달러 자금조달 비용 절감</p>
            <p className="text-sm text-gray-600 mt-2">→ 현금흐름 개선 및 유동성 강화</p>
          </div>
        </div>
      </div>

      {/* SCF 프로그램의 전략적 의미 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">피브리아에 대한 SCF 프로그램의 전략적 의미</h3>
        <ul className="list-disc pl-6 space-y-3">
          <li><span className="font-semibold">높은 부채 비용 절감</span>: 일반 기업 대출(2-3%) 대비 훨씬 낮은 0.35% 할인율로 자금조달 가능</li>
          <li><span className="font-semibold">환율 변동성 대응</span>: 달러 표시 매출채권의 빠른 현금화로 환율 리스크 감소</li>
          <li><span className="font-semibold">신용등급 상승 지원</span>: 유동성 개선이 신용등급 향상에 기여 (BB → BBB-)</li>
          <li><span className="font-semibold">현금전환주기 단축</span>: 매출채권 회수 기간 60일→15일로 단축</li>
          <li><span className="font-semibold">글로벌 은행과의 관계 강화</span>: 시티그룹과의 거래 관계 심화</li>
        </ul>
      </div>

      {/* 주요 도전 과제 */}
      <div className="w-full bg-red-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-red-800">피브리아의 주요 도전 과제</h3>
        <ul className="list-disc pl-6 space-y-3">
          <li><span className="font-semibold">환율 리스크</span>: 레알화 약세로 달러 표시 부채 부담 증가</li>
          <li><span className="font-semibold">변동성 높은 순이익</span>: 견고한 영업이익에도 불구하고 환율 손실로 인한 순이익 변동성</li>
          <li><span className="font-semibold">유동성 관리</span>: 2008년 금융위기 이후 자금 조달의 어려움 경험</li>
          <li><span className="font-semibold">장기적 신용 관계</span>: 다양한 은행과의 관계 구축 필요성</li>
        </ul>
      </div>
    </div>
  );
};

export default FibriaFinancialAnalysis;
