import React from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } from 'recharts';

// 피브리아 현금전환주기 데이터 (2005-2015) - 원본 Exhibit 7 기반 정확히 교정
const workingCapitalData = [
  { 
    year: '2005', 
    dso: 68, 
    dsi: 85, 
    dpo: 48, 
    ccc: 105 
  },
  { 
    year: '2006', 
    dso: 65, 
    dsi: 88, 
    dpo: 45, 
    ccc: 108 
  },
  { 
    year: '2007', 
    dso: 58, 
    dsi: 75, 
    dpo: 43, 
    ccc: 90 
  },
  { 
    year: '2008', 
    dso: 70, 
    dsi: 95, 
    dpo: 50, 
    ccc: 115 
  },
  { 
    year: '2009', 
    dso: 115, 
    dsi: 68, 
    dpo: 32, 
    ccc: 151 
  },
  { 
    year: '2010', 
    dso: 80, 
    dsi: 83, 
    dpo: 33, 
    ccc: 130 
  },
  { 
    year: '2011', 
    dso: 80, 
    dsi: 85, 
    dpo: 28, 
    ccc: 137 
  },
  { 
    year: '2012', 
    dso: 57, 
    dsi: 85, 
    dpo: 38, 
    ccc: 104 
  },
  { 
    year: '2013', 
    dso: 77, 
    dsi: 85, 
    dpo: 40, 
    ccc: 122 
  },
  { 
    year: '2014', 
    dso: 40, 
    dsi: 85, 
    dpo: 38, 
    ccc: 87 
  },
  { 
    year: '2015 (6월)', 
    dso: 37, 
    dsi: 85, 
    dpo: 37, 
    ccc: 85 
  }
];

// SCF 프로그램 영향 분석 (P&G 거래에 대한 가정)
const scfImpactData = [
  { 
    scenario: '일반 결제 조건\n(60일)', 
    receivableDays: 60, 
    inventoryDays: 80, 
    payableDays: 40,
    cashCycle: 100,
    cashNeeded: 300 * (60 + 80 - 40) / 365,
    calc: "60일 + 80일 - 40일 = 100일"
  },
  { 
    scenario: 'P&G 결제 연장\n(SCF 없음, 105일)', 
    receivableDays: 105, 
    inventoryDays: 80, 
    payableDays: 40,
    cashCycle: 145,
    cashNeeded: 300 * (105 + 80 - 40) / 365,
    calc: "105일 + 80일 - 40일 = 145일"
  },
  { 
    scenario: 'P&G SCF 프로그램\n(5일)', 
    receivableDays: 5, 
    inventoryDays: 80, 
    payableDays: 40,
    cashCycle: 45,
    cashNeeded: 300 * (5 + 80 - 40) / 365,
    calc: "5일 + 80일 - 40일 = 45일"
  }
];

// SCF 도입 전후 비교 데이터 - 원본 그래프 기준으로 수정
const comparativeData = [
  { 
    category: 'DSO', 
    before: 57, 
    after: 40, 
    change: -17 
  },
  { 
    category: 'DSI', 
    before: 85, 
    after: 85, 
    change: 0 
  },
  { 
    category: 'DPO', 
    before: 38, 
    after: 38, 
    change: 0 
  },
  { 
    category: 'CCC', 
    before: 104, 
    after: 87, 
    change: -17 
  }
];

// 운전자본 부담 변화 비교 - 수정된 데이터 기반
const workingCapitalNeedData = [
  {
    year: '2012 (SCF 전)',
    withoutSCF: 104 / 365 * 3159,
    withSCF: 104 / 365 * 3159,
    calcDesc: "104일/365일 × $3,159M = $901M",
    effect: 0
  },
  {
    year: '2013 (SCF 부분도입)',
    withoutSCF: 122 / 365 * 2924,
    withSCF: (122 - 10) / 365 * 2924,
    calcDesc: "(122일-10일)/365일 × $2,924M = $900M",
    effect: 10
  },
  {
    year: '2014 (SCF 완전도입)',
    withoutSCF: 87 / 365 * 3009,
    withSCF: (87 - 17) / 365 * 3009,
    calcDesc: "(87일-17일)/365일 × $3,009M = $580M",
    effect: 17
  },
  {
    year: '2015',
    withoutSCF: 85 / 365 * 3099,
    withSCF: (85 - 17) / 365 * 3099,
    calcDesc: "(85일-17일)/365일 × $3,099M = $575M",
    effect: 17
  }
];

// 금융 조건 비교
const financingRatesData = [
  {
    scenario: 'SCF 프로그램',
    rate: 1.3,
    ratingBase: 'P&G AA- 등급',
    calcBase: 'LIBOR + 1% 스프레드',
    annualSavings: '약 $30만 (연간)'
  },
  {
    scenario: 'Fibria 일반 자금조달',
    rate: 2.5,
    ratingBase: 'Fibria BBB- 등급',
    calcBase: '미 달러화 3% 내외',
    annualSavings: '-'
  },
  {
    scenario: '일반 팩토링',
    rate: 3.5,
    ratingBase: '-',
    calcBase: '투자등급 고객 기준',
    annualSavings: '-'
  }
];

const FibriaWorkingCapitalAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">피브리아 현금전환주기 분석 (Exhibit 7)</h2>
      
      {/* 1. 현금전환주기 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 현금전환주기 추이 (2005-2015)</h3>
        <ResponsiveContainer width="100%" height={450}>
          <LineChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis label={{ value: '일수', angle: -90, position: 'insideLeft' }} 
                   domain={[0, 160]} />
            <Tooltip formatter={(value) => [`${value} 일`, '']} />
            <Legend verticalAlign="bottom" />
            <Line type="monotone" dataKey="ccc" name="현금전환주기(CCC)" stroke="#000000" strokeWidth={3} dot={{ r: 5 }} />
            <Line type="monotone" dataKey="dso" name="매출채권회수기간(DSO)" stroke="#999999" strokeWidth={2} />
            <Line type="monotone" dataKey="dsi" name="재고자산회전기간(DSI)" stroke="#CCCCCC" strokeWidth={2} strokeDasharray="5 5" />
            <Line type="monotone" dataKey="dpo" name="매입채무지급기간(DPO)" stroke="#000000" strokeWidth={1} strokeDasharray="2 2" />
            
            {/* 이벤트 영역 표시 */}
            <rect x="34%" y="0%" width="9%" height="100%" fill="rgba(255,0,0,0.1)" />
            <rect x="73%" y="0%" width="18%" height="100%" fill="rgba(0,128,0,0.1)" />
          </LineChart>
        </ResponsiveContainer>
        
        <div className="flex justify-center mt-4 space-x-8">
          <div className="flex items-center">
            <div className="w-4 h-4 bg-red-100 mr-2"></div>
            <span>금융위기 (2008-2009)</span>
          </div>
          <div className="flex items-center">
            <div className="w-4 h-4 bg-green-100 mr-2"></div>
            <span>SCF 도입 (2013-2015)</span>
          </div>
        </div>
      </div>

      {/* 2. 현금전환주기 구성 요소별 추이 - 개별 차트 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 현금전환주기 구성 요소별 추이</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">DSO & DSI 추이</h4>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                data={workingCapitalData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis label={{ value: '일수', angle: -90, position: 'insideLeft' }} 
                       domain={[0, 160]} />
                <Tooltip formatter={(value) => [`${value} 일`, '']} />
                <Legend />
                <Line type="monotone" dataKey="dso" name="매출채권회수기간(DSO)" stroke="#999999" strokeWidth={2} />
                <Line type="monotone" dataKey="dsi" name="재고자산회전기간(DSI)" stroke="#CCCCCC" strokeWidth={2} strokeDasharray="5 5" />
              </LineChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">DPO & CCC 추이</h4>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                data={workingCapitalData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="year" />
                <YAxis label={{ value: '일수', angle: -90, position: 'insideLeft' }} 
                       domain={[0, 160]} />
                <Tooltip formatter={(value) => [`${value} 일`, '']} />
                <Legend />
                <Line type="monotone" dataKey="dpo" name="매입채무지급기간(DPO)" stroke="#000000" strokeWidth={1} strokeDasharray="2 2" />
                <Line type="monotone" dataKey="ccc" name="현금전환주기(CCC)" stroke="#000000" strokeWidth={3} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div className="mt-4 p-4 bg-blue-50 rounded-lg">
          <p className="text-center text-sm text-blue-800">
            <strong>계산식:</strong> 현금전환주기(CCC) = DSO + DSI - DPO<br/>
            <strong>2012년:</strong> 57일 + 85일 - 38일 = 104일<br/>
            <strong>2014년:</strong> 40일 + 85일 - 38일 = 87일 (17일 감소)
          </p>
        </div>
      </div>

      {/* 3. SCF 프로그램 도입 전후 비교 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">3. SCF 프로그램 도입 전후 비교 (2012 vs 2014)</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">구성 요소별 변화</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={comparativeData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis label={{ value: '일수', angle: -90, position: 'insideLeft' }} />
                <Tooltip formatter={(value) => [`${value} 일`, '']} />
                <Legend />
                <Bar dataKey="before" name="SCF 도입 전 (2012)" fill="#8884d8" />
                <Bar dataKey="after" name="SCF 도입 후 (2014)" fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">개선 효과 분석</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={comparativeData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis label={{ value: '일수 변화', angle: -90, position: 'insideLeft' }} />
                <Tooltip formatter={(value, name, props) => {
                  const desc = props.payload.category === 'DSO' ? 'SCF 직접 효과' : 
                              props.payload.category === 'CCC' ? '총 개선 효과' : 'SCF와 직접 관련 없음';
                  return [`${value} 일 ${value < 0 ? '감소' : value > 0 ? '증가' : '변화 없음'}`, desc];
                }} />
                <Legend />
                <Bar dataKey="change" name="2012-2014 변화 (일)" fill={({ change }) => (change < 0 ? "#82ca9d" : change > 0 ? "#ff8042" : "#cccccc")} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div className="mt-4 p-4 bg-blue-50 rounded-lg">
          <p className="text-center text-sm text-blue-800">
            <strong>핵심 변화:</strong> DSO가 57일에서 40일로 17일 감소 (SCF의 직접적 효과)<br/>
            <strong>DSI와 DPO:</strong> SCF와 직접적인 관련이 없으며 큰 변화 없음<br/>
            <strong>총 효과:</strong> CCC가 104일에서 87일로 17일 감소
          </p>
        </div>
      </div>

      {/* 4. SCF 프로그램이 P&G 거래에 미치는 영향 분석 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">4. SCF 프로그램이 P&G 거래에 미치는 영향 분석</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">현금전환주기 비교</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="scenario" />
                <YAxis label={{ value: '일수', angle: -90, position: 'insideLeft' }} />
                <Tooltip formatter={(value, name, props) => {
                  if (name === 'cashCycle') return [`${value} 일`, props.payload.calc];
                  return [value, name];
                }} />
                <Legend />
                <Bar dataKey="cashCycle" name="현금전환주기 (일)" fill="#8884d8" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">필요 운전자본 금액</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={scfImpactData}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="scenario" />
                <YAxis label={{ value: '백만 달러', angle: -90, position: 'insideLeft' }} />
                <Tooltip formatter={(value, name) => {
                  if (name === 'cashNeeded') return [`$${value.toFixed(1)}M`, '계산식: CCC/365 × $300M'];
                  return [value, name];
                }} />
                <Legend />
                <Bar dataKey="cashNeeded" name="필요 운전자본 (백만 달러)" fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
        <div className="mt-4 p-4 bg-blue-50 rounded-lg">
          <p className="text-center text-sm text-blue-800">
            <strong>효과:</strong> P&G SCF 사용 시 필요 운전자본 $82.2M → $37.0M으로 $45.2M 감소<br/>
            <strong>계산:</strong> $300M × (CCC ÷ 365일) = 필요 운전자본<br/>
            <strong>비교:</strong> 일반 결제(100일) → SCF 사용(45일) = 55일 감소
          </p>
        </div>
      </div>

      {/* 5. SCF 프로그램으로 인한 운전자본 부담 변화 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">5. SCF 프로그램으로 인한 운전자본 부담 변화</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={workingCapitalNeedData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis label={{ value: '백만 달러', angle: -90, position: 'insideLeft' }} />
            <Tooltip formatter={(value, name, props) => {
              if (name === 'withoutSCF') return [`$${value.toFixed(1)}M`, 'SCF 없음'];
              if (name === 'withSCF') return [`$${value.toFixed(1)}M`, props.payload.calcDesc];
              return [value, name];
            }} />
            <Legend />
            <Bar dataKey="withoutSCF" name="SCF 없는 경우 필요 운전자본" fill="#ff8042" />
            <Bar dataKey="withSCF" name="SCF 활용 시 필요 운전자본" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
        <div className="mt-4 p-4 bg-yellow-50 rounded-lg">
          <p className="text-center text-sm text-yellow-800">
            <strong>SCF 효과 가정:</strong> 2013년(10일 감소), 2014-2015년(17일 감소)<br/>
            <strong>운전자본 계산식:</strong> 현금전환주기 × (연간 매출 ÷ 365일)<br/>
            <strong>환율 영향:</strong><br/>
            - 유리한 점: 달러 기반 매출의 레알화 가치 증가 → 레알화 기준 수익 증가<br/>
            - 불리한 점: 달러 기반 부채의 레알화 가치 증가 → 부채 부담 증가 (Fibria 부채의 90% 이상이 달러 표시)
          </p>
        </div>
      </div>

      {/* 6. 자금조달 옵션 비교 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">6. 자금조달 옵션 비교</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart
            data={financingRatesData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="scenario" />
            <YAxis label={{ value: '이자율 (%)', angle: -90, position: 'insideLeft' }} />
            <Tooltip formatter={(value, name, props) => {
              if (name === 'rate') return [`${value.toFixed(1)}%`, `${props.payload.calcBase}`];
              return [value, name];
            }} />
            <Legend />
            <Bar dataKey="rate" name="자금조달 이자율 (%)" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
        <div className="mt-4 p-4 bg-green-50 rounded-lg">
          <p className="text-center text-sm text-green-800">
            <strong>할인율 0.1%p 차이의 영향 계산:</strong><br/>
            $300M × 0.001 × (100일 ÷ 365일) ≈ $82,192<br/>
            자금 회전 효과 고려 시 약 $30만/연간 비용 영향 추정
          </p>
        </div>
      </div>

      {/* 핵심 인사이트 요약 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">핵심 인사이트</h3>
        <ul className="list-disc pl-6 space-y-3">
          <li><span className="font-semibold">SCF의 직접적인 효과는 DSO(매출채권회수기간) 감소</span>: 57일 → 40일 (17일 감소)</li>
          <li><span className="font-semibold">P&G 거래의 효과</span>: 결제 기간 105일에도 SCF로 5일 내 현금화 → 현금흐름 크게 개선</li>
          <li><span className="font-semibold">금융 혁신의 가치</span>: 물리적 공급망은 유지(DSI 변화 없음)하면서 금융 흐름만 최적화</li>
          <li><span className="font-semibold">운전자본 감소</span>: 2014년 기준 약 $146M의 운전자본 감소 효과 (부채 상환, 투자 등에 활용 가능)</li>
        </ul>
      </div>
    </div>
  );
};

export default FibriaWorkingCapitalAnalysis;