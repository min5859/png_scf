import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

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

// 시각화에 사용할 색상
const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884d8', '#82ca9d', '#ffc658', '#ff7300'];

// 차트 툴팁 포맷팅 함수
const formatCurrency = (value) => `R$ ${value.toLocaleString()} 백만`;
const formatPercent = (value) => `${value.toFixed(1)}%`;
const formatRatio = (value) => `${value.toFixed(2)}배`;
const formatDays = (value) => `${value} 일`;

const FibriaBalanceSheetAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-12 p-6 bg-white">
      <h2 className="text-3xl font-bold text-center text-blue-800 mb-4">피브리아 셀룰로즈 대차대조표 분석 (2012-2015)</h2>
      <p className="text-lg text-center max-w-4xl">이 분석은 피브리아 셀룰로즈의 재무 상태와 P&G와의 SCF(Supply Chain Finance) 프로그램이 미친 영향을 시각화하여 보여줍니다. 데이터는 2012년부터 2015년 6월까지의 기간을 포함합니다.</p>
      
      {/* 1. 자산, 부채, 자본 추이 */}
      <div className="w-full bg-blue-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-3 text-center text-blue-800">1. 자산, 부채, 자본 추이 (단위: 백만 레알)</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-4 text-gray-700">
            <span className="font-semibold">차트 설명:</span> 이 차트는 피브리아의 총자산, 총부채, 자본의 연도별 변화를 보여줍니다. 
            2012년부터 2014년까지 총자산이 감소하다가 2015년에 소폭 증가했으며, 
            총부채는 지속적으로 감소 추세를 보였습니다. 이는 회사의 부채 관리 노력을 보여줍니다.
          </p>
          <div className="font-semibold text-sm text-gray-600 mb-2">주요 포인트:</div>
          <ul className="list-disc pl-5 mb-4 text-sm text-gray-600">
            <li>총자산: 2012년 R$28,145백만에서 2015년 6월 R$26,501백만으로 5.8% 감소</li>
            <li>총부채: 2012년 R$12,974백만에서 2015년 6월 R$11,937백만으로 8.0% 감소</li>
            <li>자본: 상대적으로 안정적인 수준 유지 (R$14,500백만 ~ R$15,200백만 범위)</li>
          </ul>
        </div>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[0, 30000]} />
            <Tooltip formatter={(value) => formatCurrency(value)} />
            <Legend />
            <Bar dataKey="totalAssets" name="총자산" fill={COLORS[0]} />
            <Bar dataKey="totalLiabilities" name="총부채" fill={COLORS[3]} />
            <Bar dataKey="totalEquity" name="자본" fill={COLORS[1]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 2. 유동자산 구성 */}
      <div className="w-full bg-green-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-3 text-center text-green-800">2. 유동자산 구성 변화 (단위: 백만 레알)</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-4 text-gray-700">
            <span className="font-semibold">차트 설명:</span> 이 차트는 피브리아의 유동자산 구성 요소(현금, 매출채권, 재고자산, 기타유동자산)의 
            연도별 변화를 보여줍니다. 특히 눈에 띄는 점은 2012년에서 2014년까지 현금의 대폭 감소와 
            2014년 매출채권의 큰 폭 감소입니다.
          </p>
          <div className="font-semibold text-sm text-gray-600 mb-2">주요 포인트:</div>
          <ul className="list-disc pl-5 mb-4 text-sm text-gray-600">
            <li>현금: 2012년 R$3,296백만에서 2014년 R$745백만으로 77.4% 감소 후 2015년 다시 증가</li>
            <li>매출채권: 2013년 R$1,477백만에서 2014년 R$695백만으로 53.0% 급감 (SCF 프로그램 영향)</li>
            <li>재고자산: 상대적으로 안정적인 수준을 유지 (R$1,183백만~R$1,455백만)</li>
          </ul>
        </div>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[0, 7000]} />
            <Tooltip formatter={(value) => formatCurrency(value)} />
            <Legend />
            <Bar dataKey="cash" name="현금 및 단기투자" stackId="a" fill={COLORS[0]} />
            <Bar dataKey="accountsReceivable" name="매출채권" stackId="a" fill={COLORS[1]} />
            <Bar dataKey="inventory" name="재고자산" stackId="a" fill={COLORS[2]} />
            <Bar dataKey="otherCurrentAssets" name="기타유동자산" stackId="a" fill={COLORS[3]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 3. 부채 구성 */}
      <div className="w-full bg-red-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-3 text-center text-red-800">3. 부채 구성 변화 (단위: 백만 레알)</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-4 text-gray-700">
            <span className="font-semibold">차트 설명:</span> 이 차트는 피브리아의 부채 구성(매입채무, 단기차입금, 기타유동부채, 장기차입금, 기타비유동부채)의 
            연도별 변화를 보여줍니다. 특히 2013년에 단기차입금이 크게 증가했다가 2014년에 감소한 것이 주목할 만합니다.
          </p>
          <div className="font-semibold text-sm text-gray-600 mb-2">주요 포인트:</div>
          <ul className="list-disc pl-5 mb-4 text-sm text-gray-600">
            <li>단기차입금: 2013년에 R$2,973백만으로 급증 후 2014년 R$966백만으로 67.5% 감소</li>
            <li>장기차입금: 2012년 R$9,630백만에서 2013년 R$6,801백만으로 감소 후 다시 증가 추세</li>
            <li>매입채무: 점진적으로 증가 (R$436백만에서 R$637백만으로 46.1% 증가)</li>
          </ul>
        </div>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={balanceSheetData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[0, 14000]} />
            <Tooltip formatter={(value) => formatCurrency(value)} />
            <Legend />
            <Bar dataKey="accountsPayable" name="매입채무" stackId="a" fill={COLORS[0]} />
            <Bar dataKey="shortTermDebt" name="단기차입금" stackId="a" fill={COLORS[1]} />
            <Bar dataKey="otherCurrentLiabilities" name="기타유동부채" stackId="a" fill={COLORS[2]} />
            <Bar dataKey="longTermDebt" name="장기차입금" stackId="a" fill={COLORS[3]} />
            <Bar dataKey="otherLTLiabilities" name="기타비유동부채" stackId="a" fill={COLORS[4]} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 4. 유동성 지표 */}
      <div className="w-full bg-purple-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-3 text-center text-purple-800">4. 유동성 및 부채 지표 추이</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-4 text-gray-700">
            <span className="font-semibold">차트 설명:</span> 이 차트들은 피브리아의 유동비율과 부채비율의 변화를 보여줍니다. 
            2013년에 유동비율이 크게 하락했다가 이후 지속적으로 개선되는 추세를 보이며, 
            부채비율은 꾸준히 감소하여 회사의 재무 안정성이 개선되고 있음을 나타냅니다.
          </p>
          <div className="font-semibold text-sm text-gray-600 mb-2">주요 포인트:</div>
          <ul className="list-disc pl-5 mb-4 text-sm text-gray-600">
            <li>유동비율: 2012년 2.52배에서 2013년 1.31배로 급감 후, 2015년 6월 1.85배로 회복</li>
            <li>부채비율: 2012년 41.5%에서 2014년 36.3%로 감소 후, 2015년 6월 38.2%로 소폭 증가</li>
            <li>이러한 지표 개선은 SCF 프로그램 도입과 회사의 재무 관리 노력이 결합된 결과</li>
          </ul>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white p-4 rounded-lg">
            <h4 className="font-semibold text-center mb-2 text-purple-700">유동비율 (Current Ratio)</h4>
            <p className="text-sm text-gray-600 mb-4 text-center">유동자산 ÷ 유동부채, 높을수록 단기 지급능력이 양호</p>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                data={balanceSheetData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis domain={[0, 3]} />
                <Tooltip formatter={(value) => formatRatio(value)} />
                <Legend />
                <Line type="monotone" dataKey="currentRatio" name="유동비율" stroke={COLORS[0]} strokeWidth={3} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div className="bg-white p-4 rounded-lg">
            <h4 className="font-semibold text-center mb-2 text-purple-700">부채비율 (Debt-to-Capital)</h4>
            <p className="text-sm text-gray-600 mb-4 text-center">총부채 ÷ (부채+자본), 낮을수록 재무 안정성이 양호</p>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                data={balanceSheetData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis domain={[30, 45]} />
                <Tooltip formatter={(value) => formatPercent(value)} />
                <Legend />
                <Line type="monotone" dataKey="debtToCapital" name="부채비율" stroke={COLORS[3]} strokeWidth={3} activeDot={{ r: 8 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* 5. 운전자본 항목 */}
      <div className="w-full bg-yellow-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-3 text-center text-yellow-800">5. 운전자본 항목 추이 (단위: 백만 레알)</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-4 text-gray-700">
            <span className="font-semibold">차트 설명:</span> 이 차트는 피브리아의 순운전자본과 그 구성요소(매출채권, 재고자산, 매입채무)의 
            변화를 보여줍니다. 순운전자본은 '매출채권 + 재고자산 - 매입채무'로 계산되며, 
            일상적인 운영 활동에 필요한 자금을 의미합니다.
          </p>
          <div className="font-semibold text-sm text-gray-600 mb-2">주요 포인트:</div>
          <ul className="list-disc pl-5 mb-4 text-sm text-gray-600">
            <li>순운전자본: 2013년 R$2,156백만으로 정점을 찍은 후 2014년 R$1,341백만으로 37.8% 감소</li>
            <li>매출채권: 2013년에 크게 증가했다가 2014년에 급감 (SCF 프로그램의 영향)</li>
            <li>재고자산: 전반적으로 안정적인 수준 유지 (R$1,183백만~R$1,455백만)</li>
            <li>운전자본 감소는 기업의 자금 효율성 증가를 의미</li>
          </ul>
        </div>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[0, 2500]} />
            <Tooltip formatter={(value) => formatCurrency(value)} />
            <Legend />
            <Bar dataKey="accountsReceivable" name="매출채권" fill={COLORS[1]} />
            <Bar dataKey="inventory" name="재고자산" fill={COLORS[2]} />
            <Bar dataKey="accountsPayable" name="매입채무" fill={COLORS[0]} />
            <Bar dataKey="netWorkingCapital" name="순운전자본" fill={COLORS[3]} />
          </BarChart>
        </ResponsiveContainer>
        <div className="bg-yellow-100 p-4 rounded-lg mt-4">
          <div className="font-semibold mb-2">순운전자본 계산 방식:</div>
          <p>순운전자본 = 매출채권 + 재고자산 - 매입채무</p>
          <ul className="list-disc pl-5 mt-2">
            <li>2012년: R$964백만 + R$1,183백만 - R$436백만 = R$1,711백만</li>
            <li>2013년: R$1,477백만 + R$1,266백만 - R$587백만 = R$2,156백만</li>
            <li>2014년: R$695백만 + R$1,239백만 - R$593백만 = R$1,341백만</li>
            <li>2015년(6월): R$875백만 + R$1,455백만 - R$637백만 = R$1,693백만</li>
          </ul>
        </div>
      </div>

      {/* 6. SCF 영향 분석 */}
      <div className="w-full bg-indigo-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-3 text-center text-indigo-800">6. SCF 프로그램 영향 분석 (P&G 거래 기준)</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-4 text-gray-700">
            <span className="font-semibold">차트 설명:</span> 이 차트들은 SCF 프로그램 도입 전후의 매출채권 회수 기간과 
            자금조달 비용 변화를 보여줍니다. P&G와의 연간 거래 규모 3억 달러를 기준으로 분석했습니다.
          </p>
          <div className="font-semibold text-sm text-gray-600 mb-2">계산 방식:</div>
          <ul className="list-disc pl-5 mb-4 text-sm text-gray-600">
            <li>매출채권 가치: 연간 매출액(3억 달러) × 회수 기간(일) ÷ 365일</li>
            <li>SCF 이전: 3억 달러 × 60일 ÷ 365일 ≈ 4,932만 달러</li>
            <li>SCF 이후: 3억 달러 × 15일 ÷ 365일 ≈ 1,233만 달러</li>
            <li>자금조달 비용: 매출채권 가치 × 연간 자금조달 비율(SCF 이전 2.5%, SCF 이후 0.35%)</li>
          </ul>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white p-4 rounded-lg">
            <h4 className="font-semibold text-center mb-2 text-indigo-700">매출채권 회수 기간</h4>
            <p className="text-sm text-gray-600 mb-4 text-center">P&G에 제품 판매 후 대금을 받기까지 걸리는 평균 일수</p>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis domain={[0, 70]} />
                <Tooltip formatter={(value) => formatDays(value)} />
                <Legend />
                <Bar dataKey="daysOutstanding" name="매출채권 회수 기간" fill={COLORS[0]} />
              </BarChart>
            </ResponsiveContainer>
            <div className="mt-4 text-sm text-gray-600">
              <p className="font-semibold">영향 분석:</p>
              <p>SCF 프로그램을 통해 매출채권 회수 기간이 60일에서 15일로 75% 단축</p>
              <p>이는 피브리아의 현금흐름 개선과 운전자본 감소에 크게 기여</p>
            </div>
          </div>
          <div className="bg-white p-4 rounded-lg">
            <h4 className="font-semibold text-center mb-2 text-indigo-700">자금조달 비용 (연간, 백만 달러)</h4>
            <p className="text-sm text-gray-600 mb-4 text-center">매출채권 할인에 따른 연간 금융 비용</p>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis domain={[0, 1.5]} />
                <Tooltip formatter={(value) => `$${value.toFixed(2)} 백만`} />
                <Legend />
                <Bar dataKey="financingCost" name="자금조달 비용" fill={COLORS[3]} />
              </BarChart>
            </ResponsiveContainer>
            <div className="mt-4 text-sm text-gray-600">
              <p className="font-semibold">영향 분석:</p>
              <p>SCF 이전: 4,932만 달러 × 2.5% ≈ 123만 달러/년</p>
              <p>SCF 이후: 1,233만 달러 × 0.35% ≈ 4.3만 달러/년</p>
              <p>연간 약 119만 달러의 자금조달 비용 절감 (96.5% 감소)</p>
            </div>
          </div>
        </div>
      </div>

      {/* SCF 프로그램의 전략적 의미 */}
      <div className="w-full bg-yellow-50 p-6 rounded-xl shadow-md">
        <h3 className="text-2xl font-semibold mb-4 text-center text-yellow-800">SCF 프로그램의 전략적 의미</h3>
        <div className="bg-white p-4 rounded-lg mb-4">
          <p className="mb-3 text-gray-700">
            피브리아에게 P&G의 SCF 프로그램은 단순한 금융 거래를 넘어 전략적 가치를 제공합니다. 
            아래는 SCF 프로그램이 피브리아에게 주는 주요 전략적 이점입니다.
          </p>
        </div>
        <ul className="list-none space-y-3">
          <li className="bg-white p-4 rounded-lg shadow flex items-start">
            <div className="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">1</div>
            <div>
              <span className="font-semibold text-lg">유동성 확보:</span> 
              <p>매출채권 60일→15일로 단축으로 약 $37백만 빠른 현금 확보</p>
              <p className="text-sm text-gray-600 mt-1">계산: $300백만 × (60-15)/365 = $36.99백만의 운전자본 감소</p>
            </div>
          </li>
          <li className="bg-white p-4 rounded-lg shadow flex items-start">
            <div className="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">2</div>
            <div>
              <span className="font-semibold text-lg">이자 비용 절감:</span> 
              <p>연간 약 $1.19백만의 자금조달 비용 절감</p>
              <p className="text-sm text-gray-600 mt-1">계산: ($49.32백만 × 2.5%) - ($12.33백만 × 0.35%) = $1.19백만</p>
            </div>
          </li>
          <li className="bg-white p-4 rounded-lg shadow flex items-start">
            <div className="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">3</div>
            <div>
              <span className="font-semibold text-lg">대차대조표 개선:</span> 
              <p>매출채권 감소로 유동비율 개선 및 부채의존도 감소</p>
              <p className="text-sm text-gray-600 mt-1">2013년 이후 유동비율 증가(1.31→1.85)와 부채비율 감소(40.3%→38.2%)</p>
            </div>
          </li>
          <li className="bg-white p-4 rounded-lg shadow flex items-start">
            <div className="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">4</div>
            <div>
              <span className="font-semibold text-lg">환율 위험 관리:</span> 
              <p>달러 매출의 빠른 현금화로 환율 변동 위험 완화</p>
              <p className="text-sm text-gray-600 mt-1">브라질 레알/달러 환율 상승(1.96→2.69)에 따른 달러 부채 리스크 일부 상쇄</p>
            </div>
          </li>
          <li className="bg-white p-4 rounded-lg shadow flex items-start">
            <div className="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">5</div>
            <div>
              <span className="font-semibold text-lg">신용 관계 확대:</span> 
              <p>시티그룹 외에 JPMorgan Chase와의 관계 구축 기회</p>
              <p className="text-sm text-gray-600 mt-1">다양한 글로벌 은행과의 관계는 금융 위기 상황에서 대안적 자금원 확보에 중요</p>
            </div>
          </li>
        </ul>
      </div>