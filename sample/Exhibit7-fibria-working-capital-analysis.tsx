import React from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } from 'recharts';

// 피브리아 현금전환주기 데이터 (2005-2015)
const workingCapitalData = [
  { 
    year: '2005', 
    dso: 51.2, 
    dsi: 45.5, 
    dpo: 38.3,
    ccc: 58.4
  },
  { 
    year: '2006', 
    dso: 47.5, 
    dsi: 42.3, 
    dpo: 36.2,
    ccc: 53.6
  },
  { 
    year: '2007', 
    dso: 42.8, 
    dsi: 46.7, 
    dpo: 39.8,
    ccc: 49.7
  },
  { 
    year: '2008', 
    dso: 38.4, 
    dsi: 42.6, 
    dpo: 37.5,
    ccc: 43.5
  },
  { 
    year: '2009', 
    dso: 58.3, 
    dsi: 75.4, 
    dpo: 35.2,
    ccc: 98.5
  },
  { 
    year: '2010', 
    dso: 61.2, 
    dsi: 79.5, 
    dpo: 40.6,
    ccc: 100.1
  },
  { 
    year: '2011', 
    dso: 52.7, 
    dsi: 63.8, 
    dpo: 39.5,
    ccc: 77.0
  },
  { 
    year: '2012', 
    dso: 56.8, 
    dsi: 82.5, 
    dpo: 30.5,
    ccc: 108.8
  },
  { 
    year: '2013', 
    dso: 60.3, 
    dsi: 68.4, 
    dpo: 37.8,
    ccc: 90.9
  },
  { 
    year: '2014', 
    dso: 36.5, 
    dsi: 82.2, 
    dpo: 41.2,
    ccc: 77.5
  },
  { 
    year: '2015 (6월)', 
    dso: 38.4, 
    dsi: 92.3, 
    dpo: 42.8,
    ccc: 87.9
  }
];

// SCF 프로그램 영향 분석 (P&G 거래에 대한 가정)
const scfImpactData = [
  { 
    scenario: '일반 결제 조건', 
    receivableDays: 60, 
    inventoryDays: 80, 
    payableDays: 40,
    cashCycle: 100,
    cashNeeded: 300 * (60 + 80 - 40) / 365 // P&G 연간 매출 $300M 기준
  },
  { 
    scenario: 'P&G 결제 연장 (SCF 없음)', 
    receivableDays: 105, 
    inventoryDays: 80, 
    payableDays: 40,
    cashCycle: 145,
    cashNeeded: 300 * (105 + 80 - 40) / 365
  },
  { 
    scenario: 'P&G SCF 프로그램', 
    receivableDays: 15, 
    inventoryDays: 80, 
    payableDays: 40,
    cashCycle: 55,
    cashNeeded: 300 * (15 + 80 - 40) / 365
  }
];

// 운전자본 부담 변화 비교
const workingCapitalNeedData = [
  {
    year: '2012',
    withoutSCF: 108.8 / 365 * 3159, // CCC * 연간 매출 (단위: 백만 달러)
    withSCF: 108.8 / 365 * 3159 
  },
  {
    year: '2013',
    withoutSCF: 90.9 / 365 * 2924,
    withSCF: (90.9 - 10) / 365 * 2924 // SCF 도입 시작, 부분적 효과
  },
  {
    year: '2014',
    withoutSCF: 77.5 / 365 * 3009,
    withSCF: (77.5 - 20) / 365 * 3009 // SCF 완전 도입 효과
  },
  {
    year: '2015',
    withoutSCF: 87.9 / 365 * 3099,
    withSCF: (87.9 - 20) / 365 * 3099
  }
];

// 금융위기 영향 시각화
const financialCrisisPeriods = [
  { startYear: '2008', endYear: '2009', event: '금융위기' },
  { startYear: '2013', endYear: '2015', event: 'SCF 도입' }
];

const FibriaWorkingCapitalAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">피브리아 현금전환주기 분석 (Exhibit 7)</h2>
      
      {/* 현금전환주기 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 현금전환주기 추이 (2005-2015, 단위: 일)</h3>
        <ResponsiveContainer width="100%" height={450}>
          <AreaChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`${value.toFixed(1)} 일`, '']} />
            <Legend />
            <defs>
              <linearGradient id="colorCCC" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#8884d8" stopOpacity={0.8}/>
                <stop offset="95%" stopColor="#8884d8" stopOpacity={0.2}/>
              </linearGradient>
            </defs>
            <Area type="monotone" dataKey="ccc" name="현금전환주기(CCC)" stroke="#8884d8" fillOpacity={1} fill="url(#colorCCC)" />
            
            {/* 금융위기 및 SCF 도입 기간 표시 */}
            {financialCrisisPeriods.map((period, index) => {
              const startIndex = workingCapitalData.findIndex(d => d.year === period.startYear);
              const endIndex = workingCapitalData.findIndex(d => d.year === period.endYear);
              if (startIndex === -1 || endIndex === -1) return null;
              
              const x1 = (startIndex / (workingCapitalData.length - 1)) * 100 + "%";
              const x2 = (endIndex / (workingCapitalData.length - 1)) * 100 + "%";
              
              return (
                <linearGradient key={index} id={`period${index}`} x1={x1} y1="0" x2={x2} y2="0">
                  <stop offset="0%" stopColor={index === 0 ? "rgba(255,0,0,0.3)" : "rgba(0,255,0,0.3)"} />
                  <stop offset="100%" stopColor={index === 0 ? "rgba(255,0,0,0.3)" : "rgba(0,255,0,0.3)"} />
                </linearGradient>
              );
            })}
            
            {financialCrisisPeriods.map((period, index) => {
              const startIndex = workingCapitalData.findIndex(d => d.year === period.startYear);
              const endIndex = workingCapitalData.findIndex(d => d.year === period.endYear);
              if (startIndex === -1 || endIndex === -1) return null;
              
              return (
                <rect
                  key={index}
                  x={`${(startIndex / (workingCapitalData.length - 1)) * 100}%`}
                  y="0%"
                  width={`${((endIndex - startIndex) / (workingCapitalData.length - 1)) * 100}%`}
                  height="100%"
                  fill={`url(#period${index})`}
                />
              );
            })}
          </AreaChart>
        </ResponsiveContainer>
        
        {/* 이벤트 레전드 */}
        <div className="flex justify-center mt-4 space-x-8">
          <div className="flex items-center">
            <div className="w-4 h-4 bg-red-300 mr-2"></div>
            <span>금융위기 기간</span>
          </div>
          <div className="flex items-center">
            <div className="w-4 h-4 bg-green-300 mr-2"></div>
            <span>SCF 프로그램 도입</span>
          </div>
        </div>
      </div>

      {/* 구성 요소별 추이 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 현금전환주기 구성 요소별 추이 (단위: 일)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`${value.toFixed(1)} 일`, '']} />
            <Legend />
            <Line type="monotone" dataKey="dso" name="매출채권회수기간(DSO)" stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="dsi" name="재고자산회전기간(DSI)" stroke="#82ca9d" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="dpo" name="매입채무지급기간(DPO)" stroke="#ff8042" strokeWidth={2} activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* 2013-2015년 변화 분석 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">3. SCF 프로그램 도입 전후 비교 (2012 vs 2014)</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h4 className="font-semibold text-center mb-2">현금전환주기 구성 요소 변화</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={[
                  { category: 'DSO', before: 56.8, after: 36.5, change: -20.3 },
                  { category: 'DSI', before: 82.5, after: 82.2, change: -0.3 },
                  { category: 'DPO', before: 30.5, after: 41.2, change: 10.7 },
                  { category: 'CCC', before: 108.8, after: 77.5, change: -31.3 }
                ]}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip formatter={(value) => [`${value.toFixed(1)} 일`, '']} />
                <Legend />
                <Bar dataKey="before" name="SCF 도입 전 (2012)" fill="#8884d8" />
                <Bar dataKey="after" name="SCF 도입 후 (2014)" fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div>
            <h4 className="font-semibold text-center mb-2">각 요소별 개선 일수</h4>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart
                data={[
                  { category: 'DSO', change: -20.3 },
                  { category: 'DSI', change: -0.3 },
                  { category: 'DPO', change: 10.7 },
                  { category: 'CCC', change: -31.3 }
                ]}
                margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip formatter={(value) => [`${value.toFixed(1)} 일 ${value < 0 ? '감소' : '증가'}`, '']} />
                <Legend />
                <Bar dataKey="change" name="2012-2014 변화 (일)" fill={({ change }) => (change < 0 ? "#82ca9d" : "#ff8042")} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* SCF 프로그램의 영향 분석 */}
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
                <YAxis />
                <Tooltip formatter={(value) => [`${value} 일`, '']} />
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
                <YAxis />
                <Tooltip formatter={(value) => [`$${value.toFixed(2)} 백만`, '']} />
                <Legend />
                <Bar dataKey="cashNeeded" name="필요 운전자본 (백만 달러)" fill="#82ca9d" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* 운전자본 부담 변화 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">5. SCF 프로그램으로 인한 운전자본 부담 변화</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={workingCapitalNeedData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip formatter={(value) => [`$${value.toFixed(2)} 백만`, '']} />
            <Legend />
            <Bar dataKey="withoutSCF" name="SCF 없는 경우 필요 운전자본" fill="#ff8042" />
            <Bar dataKey="withSCF" name="SCF 활용 시 필요 운전자본" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 핵심 인사이트 요약 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">핵심 인사이트</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">금융위기의 영향</h4>
            <p>2009-2010년 현금전환주기 100일 이상으로 급증</p>
            <p className="text-sm text-gray-600 mt-2">→ 외부 환경에 대한 취약성 확인</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">SCF 도입 효과</h4>
            <p>2012년 대비 2014년 현금전환주기 31.3일 감소</p>
            <p className="text-sm text-gray-600 mt-2">→ 주로 매출채권 회수기간(DSO) 개선에 기인</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">재고 부담 지속</h4>
            <p>재고자산회전기간(DSI)은 여전히 80일 이상 유지</p>
            <p className="text-sm text-gray-600 mt-2">→ 장거리 운송 및 글로벌 공급망의 특성</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">P&G 거래의 긍정적 영향</h4>
            <p>SCF 통해 결제 기간 105일에도 15일 내 현금화 가능</p>
            <p className="text-sm text-gray-600 mt-2">→ 현금 흐름 및 유동성 크게 개선</p>
          </div>
        </div>
      </div>

      {/* 케이스와의 연결성 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">케이스와의 연결성 및 시사점</h3>
        <ul className="list-disc pl-6 space-y-3">
          <li><span className="font-semibold">부채 부담에 대한 대응</span>: 현금전환주기 개선을 통해 운전자본 필요성 감소 → 부채 의존도 완화</li>
          <li><span className="font-semibold">금융위기 교훈</span>: 2008-2009년 위기 이후 유동성 관리의 중요성 인식 → SCF 프로그램의 전략적 활용</li>
          <li><span className="font-semibold">P&G와의 협상력</span>: 결제 기간 연장(105일)에도 SCF로 현금흐름 개선 → 거래 조건에 유연하게 대응</li>
          <li><span className="font-semibold">고정된 운영 구조</span>: 재고자산회전기간(80일)은 큰 변화 없음 → 공급망 자체의 물리적 제약 존재</li>
          <li><span className="font-semibold">금융 혁신의 가치</span>: SCF를 통해 물리적 공급망은 유지하면서 금융 흐름은 최적화 → 혁신적 접근법의 사례</li>
        </ul>
      </div>

      {/* SCF 은행 선택에 관한 시사점 */}
      <div className="w-full bg-green-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-green-800">SCF 은행 선택에 관한 시사점</h3>
        <p className="mb-4">현금전환주기 데이터를 통해 본 SCF 은행 선택 시 고려사항:</p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-green-700">플랫폼 안정성</h4>
            <p>운전자본 관리를 위한 핵심 도구로서의 SCF</p>
            <p className="text-sm text-gray-600 mt-2">→ 시티그룹의 검증된 플랫폼 vs JPMorgan의 새로운 관계</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-green-700">유동성 중요성</h4>
            <p>역사적 데이터가 보여주는 유동성 확보의 중요성</p>
            <p className="text-sm text-gray-600 mt-2">→ 신속하고 안정적인 매출채권 결제 능력 중시</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-green-700">할인율 최적화</h4>
            <p>운전자본 금액에 비해 할인율의 경제적 영향</p>
            <p className="text-sm text-gray-600 mt-2">→ 0.1%p 할인율 차이가 연간 약 $30만 비용 영향</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-green-700">은행 관계 다변화</h4>
            <p>금융위기 시 다양한 금융 파트너의 중요성</p>
            <p className="text-sm text-gray-600 mt-2">→ 새로운 은행 관계 구축을 통한 위험 분산</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FibriaWorkingCapitalAnalysis;
