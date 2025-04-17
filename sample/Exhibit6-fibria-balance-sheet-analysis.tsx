import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

// 대차대조표 데이터 (단위: 백만 레알)
const balanceSheetData = [
  { 
    year: '2012', 
    currentAssets: 6246,
    cash: 3296,
    accountsReceivable: 964,
    inventory: 1183,
    otherCurrentAssets: 803,
    totalAssets: 28145,
    currentLiabilities: 2475,
    accountsPayable: 436,
    shortTermDebt: 1138,
    otherCurrentLiabilities: 901,
    longTermDebt: 9630,
    otherLTLiabilities: 869,
    totalLiabilities: 12974,
    totalEquity: 15171,
    currentRatio: 2.52,
    totalDebt: 10768,
    debtToCapital: 41.5,
    exchangeRate: 1.955
  },
  { 
    year: '2013', 
    currentAssets: 5807,
    cash: 2099,
    accountsReceivable: 1477,
    inventory: 1266,
    otherCurrentAssets: 965,
    totalAssets: 26750,
    currentLiabilities: 4448,
    accountsPayable: 587,
    shortTermDebt: 2973,
    otherCurrentLiabilities: 888,
    longTermDebt: 6801,
    otherLTLiabilities: 1010,
    totalLiabilities: 12259,
    totalEquity: 14491,
    currentRatio: 1.31,
    totalDebt: 9773,
    debtToCapital: 40.3,
    exchangeRate: 2.1605
  },
  { 
    year: '2014', 
    currentAssets: 3261,
    cash: 745,
    accountsReceivable: 695,
    inventory: 1239,
    otherCurrentAssets: 582,
    totalAssets: 25594,
    currentLiabilities: 2099,
    accountsPayable: 593,
    shortTermDebt: 966,
    otherCurrentLiabilities: 540,
    longTermDebt: 7361,
    otherLTLiabilities: 1518,
    totalLiabilities: 10978,
    totalEquity: 14616,
    currentRatio: 1.55,
    totalDebt: 8327,
    debtToCapital: 36.3,
    exchangeRate: 2.3547
  },
  { 
    year: '2015 (6월)', 
    currentAssets: 3862,
    cash: 1386,
    accountsReceivable: 875,
    inventory: 1455,
    otherCurrentAssets: 146,
    totalAssets: 26501,
    currentLiabilities: 2086,
    accountsPayable: 637,
    shortTermDebt: 894,
    otherCurrentLiabilities: 555,
    longTermDebt: 8121,
    otherLTLiabilities: 1730,
    totalLiabilities: 11937,
    totalEquity: 14563,
    currentRatio: 1.85,
    totalDebt: 9015,
    debtToCapital: 38.2,
    exchangeRate: 2.6913
  }
];

// 운전자본 항목 데이터
const workingCapitalData = [
  {
    year: '2012',
    accountsReceivable: 964,
    inventory: 1183,
    accountsPayable: 436,
    netWorkingCapital: 1711
  },
  {
    year: '2013',
    accountsReceivable: 1477,
    inventory: 1266,
    accountsPayable: 587,
    netWorkingCapital: 2156
  },
  {
    year: '2014',
    accountsReceivable: 695,
    inventory: 1239,
    accountsPayable: 593,
    netWorkingCapital: 1341
  },
  {
    year: '2015 (6월)',
    accountsReceivable: 875,
    inventory: 1455,
    accountsPayable: 637,
    netWorkingCapital: 1693
  }
];

// SCF 영향 분석 데이터
const scfImpactData = [
  {
    category: 'SCF 이전',
    daysOutstanding: 60,
    arValue: 300 * 60/365, // P&G 매출 3억 달러, 60일 회수
    financingCost: 300 * 60/365 * 0.025, // 2.5% 자금조달 비용
    liquidityImpact: 'Low'
  },
  {
    category: 'SCF 이후',
    daysOutstanding: 15,
    arValue: 300 * 15/365, // P&G 매출 3억 달러, 15일 회수
    financingCost: 300 * 15/365 * 0.0035, // 0.35% SCF 할인율
    liquidityImpact: 'High'
  }
];

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8'];

const FibriaBalanceSheetAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">피브리아 셀룰로즈 대차대조표 분석 (2012-2015)</h2>
      
      {/* 자산, 부채, 자본 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 자산, 부채, 자본 추이 (단위: 백만 레알)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`R$ ${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="totalAssets" name="총자산" fill="#8884d8" />
            <Bar dataKey="totalLiabilities" name="총부채" fill="#ff8042" />
            <Bar dataKey="totalEquity" name="자본" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 유동자산 구성 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 유동자산 구성 변화 (단위: 백만 레알)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`R$ ${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="cash" name="현금 및 단기투자" stackId="a" fill="#8884d8" />
            <Bar dataKey="accountsReceivable" name="매출채권" stackId="a" fill="#82ca9d" />
            <Bar dataKey="inventory" name="재고자산" stackId="a" fill="#ffc658" />
            <Bar dataKey="otherCurrentAssets" name="기타유동자산" stackId="a" fill="#ff8042" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 부채 구성 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">3. 부채 구성 변화 (단위: 백만 레알)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`R$ ${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="accountsPayable" name="매입채무" stackId="a" fill="#8884d8" />
            <Bar dataKey="shortTermDebt" name="단기차입금" stackId="a" fill="#82ca9d" />
            <Bar dataKey="otherCurrentLiabilities" name="기타유동부채" stackId="a" fill="#ffc658" />
            <Bar dataKey="longTermDebt" name="장기차입금" stackId="a" fill="#ff8042" />
            <Bar dataKey="otherLTLiabilities" name="기타비유동부채" stackId="a" fill="#0088FE" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 유동성 지표 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">4. 유동성 및 부채 지표 추이</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">유동비율</h4>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                data={balanceSheetData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis domain={[0, 3]} />
                <Tooltip formatter={(value) => [`${value.toFixed(2)}배`, '']} />
                <Legend />
                <Line type="monotone" dataKey="currentRatio" name="유동비율" stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">부채비율</h4>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                data={balanceSheetData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis domain={[30, 45]} />
                <Tooltip formatter={(value) => [`${value.toFixed(1)}%`, '']} />
                <Legend />
                <Line type="monotone" dataKey="debtToCapital" name="부채비율" stroke="#ff8042" strokeWidth={2} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* 운전자본 항목 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">5. 운전자본 항목 추이 (단위: 백만 레알)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`R$ ${value.toLocaleString()} 백만`, '']} />
            <Legend />
            <Bar dataKey="accountsReceivable" name="매출채권" fill="#82ca9d" />
            <Bar dataKey="inventory" name="재고자산" fill="#ffc658" />
            <Bar dataKey="accountsPayable" name="매입채무" fill="#8884d8" />
            <Bar dataKey="netWorkingCapital" name="순운전자본" fill="#ff8042" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* SCF 영향 분석 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">6. SCF 프로그램 영향 분석 (P&G 거래 기준)</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">매출채권 회수 기간</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip formatter={(value) => [`${value} 일`, '']} />
                <Legend />
                <Bar dataKey="daysOutstanding" name="매출채권 회수 기간" fill="#8884d8" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">자금조달 비용 (연간, 백만 달러)</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip formatter={(value) => [`$${value.toFixed(2)} 백만`, '']} />
                <Legend />
                <Bar dataKey="financingCost" name="자금조달 비용" fill="#ff8042" />
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
            <h4 className="font-bold text-blue-700">유동성 개선</h4>
            <p>2013년 유동비율 1.31에서 2015년 1.85로 개선</p>
            <p className="text-sm text-gray-600 mt-2">→ SCF 프로그램의 긍정적 영향 확인</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">자본 구조 개선</h4>
            <p>부채비율 41.5%에서 38.2%로 감소</p>
            <p className="text-sm text-gray-600 mt-2">→ 신용등급 개선(BBB-)에 기여</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">현금 흐름 변동</h4>
            <p>2014년 현금 급감 후 2015년 다시 증가</p>
            <p className="text-sm text-gray-600 mt-2">→ 유동성 관리의 중요성 부각</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">달러 부채 부담</h4>
            <p>전체 부채의 90% 이상이 달러 표시 부채</p>
            <p className="text-sm text-gray-600 mt-2">→ 환율 상승시 부채 부담 증가</p>
          </div>
        </div>
      </div>

      {/* SCF 프로그램의 전략적 의미 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">SCF 프로그램의 전략적 의미</h3>
        <ul className="list-disc pl-6 space-y-3">
          <li><span className="font-semibold">유동성 확보</span>: 매출채권 60일→15일로 단축으로 약 $37백만 빠른 현금 확보</li>
          <li><span className="font-semibold">이자 비용 절감</span>: 연간 약 $1.5백만의 자금조달 비용 절감</li>
          <li><span className="font-semibold">대차대조표 개선</span>: 매출채권 감소로 유동비율 개선 및 부채의존도 감소</li>
          <li><span className="font-semibold">환율 위험 관리</span>: 달러 매출의 빠른 현금화로 환율 변동 위험 완화</li>
          <li><span className="font-semibold">신용 관계 확대</span>: 시티그룹 외에 JPMorgan Chase와의 관계 구축 기회</li>
        </ul>
      </div>

      {/* 의사결정 포인트 */}
      <div className="w-full bg-green-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-green-800">케이스의 의사결정 포인트</h3>
        <p className="mb-4">피브리아는 현재 SCF 프로그램을 재검토하고 다음 결정을 내려야 합니다:</p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-green-700">1. 은행 유지 vs. 변경</h4>
            <p className="mb-2">현재: 시티그룹 (0.35% 할인율)</p>
            <p className="mb-2">대안: JPMorgan Chase (할인율 미정)</p>
            <p className="text-sm text-gray-600">고려사항: 할인율, 관계 유지, 다양한 은행 관계의 가치</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-green-700">2. 계약 조건 재협상</h4>
            <p className="mb-2">현재 시장 환경: LIBOR 하락 (Exhibit 8)</p>
            <p className="mb-2">가능성: 더 낮은 할인율 협상</p>
            <p className="text-sm text-gray-600">고려사항: 시장 금리, P&G와의 관계, 장기적 파트너십</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FibriaBalanceSheetAnalysis;
