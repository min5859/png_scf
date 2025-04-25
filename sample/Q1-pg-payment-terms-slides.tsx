import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const PGPresentation = () => {
  // 파이 차트 데이터
  const costCuttingData = [
    { name: '간접비 절감', value: 30, color: '#0088FE' },
    { name: '상품 제조원가 절감', value: 60, color: '#00C49F' },
    { name: '마케팅 효율성 절감', value: 10, color: '#FFBB28' }
  ];

  // 지급 기간 비교 데이터
  const paymentTermsData = [
    { name: 'P&G(기존)', days: 45, fill: '#8884d8' },
    { name: 'P&G(변경)', days: 75, fill: '#82ca9d' },
    { name: '업계 평균', days: 85, fill: '#ffc658' },
    { name: '업계 최대', days: 100, fill: '#ff8042' }
  ];

  // 운전자본 지표 데이터
  const workingCapitalData = [
    { year: '2010', dso: 25.1, dpo: 71.4, ccc: 16.6 },
    { year: '2011', dso: 28.2, dpo: 73.5, ccc: 22.4 },
    { year: '2012', dso: 27.0, dpo: 69.8, ccc: 16.4 },
    { year: '2013', dso: 29.6, dpo: 80.1, ccc: 12.6 },
    { year: '2014', dso: 29.0, dpo: 76.0, ccc: 13.7 },
    { year: '2015', dso: 23.3, dpo: 78.8, ccc: -3.5 }
  ];

  return (
    <div className="bg-gray-50 p-4 rounded-lg shadow-lg">
      {/* 타이틀 슬라이드 */}
      <div className="bg-blue-700 text-white p-8 rounded-lg shadow-lg mb-8 text-center">
        <h1 className="text-4xl font-bold mb-2">P&G 공급업체 지급 조건 연장 분석</h1>
        <p className="text-xl">KAIST EMBA 발표자료</p>
        <p className="mt-4 text-lg">2025년 4월</p>
      </div>

      {/* P&G 소개 */}
      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">P&G 기업 소개</h2>
        <div className="flex justify-between items-center">
          <div className="w-1/2 pr-4">
            <p className="mb-3">• 1837년 설립, 세계적으로 인정받는 소비재 기업</p>
            <p className="mb-3">• 20개 이상의 브랜드가 연간 10억 달러 이상 매출 달성</p>
            <p className="mb-3">• 2015년 기준 805억 달러 매출, 116억 달러 순이익</p>
            <p className="mb-3">• 1932년부터 다우존스 산업평균지수 구성종목</p>
            <p className="mb-3">• S&P 신용등급 AA-</p>
          </div>
          <div className="w-1/2 bg-gray-100 p-4 rounded-lg">
            <h3 className="text-lg font-bold mb-2 text-blue-700">주요 10억 달러 이상 브랜드</h3>
            <ul className="grid grid-cols-2 gap-2">
              <li className="bg-blue-100 p-2 rounded-lg text-center">Always</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">Bounty</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">Charmin</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">Gillette</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">Olay</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">Oral-B</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">Pampers</li>
              <li className="bg-blue-100 p-2 rounded-lg text-center">기타</li>
            </ul>
          </div>
        </div>
      </div>

      {/* 주요 배경 */}
      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">P&G 지급 조건 연장 배경</h2>
        <div className="grid grid-cols-2 gap-6">
          <div className="bg-yellow-50 p-4 rounded-lg border-l-4 border-yellow-400">
            <h3 className="text-lg font-bold mb-2">글로벌 경기 침체 영향</h3>
            <p>2008년 금융위기 이후 성장과 수익 정체</p>
            <p className="mt-2">투자자들의 비용 절감 압박 증가</p>
          </div>
          <div className="bg-green-50 p-4 rounded-lg border-l-4 border-green-400">
            <h3 className="text-lg font-bold mb-2">운전자본 관리 개선 필요성</h3>
            <p>벤치마킹 결과, 경쟁사 대비 지급 기간이 짧음</p>
            <p className="mt-2">현금흐름 개선을 통한 경쟁력 강화 필요</p>
          </div>
          <div className="bg-blue-50 p-4 rounded-lg border-l-4 border-blue-400">
            <h3 className="text-lg font-bold mb-2">경영 전략 변화</h3>
            <p>총주주수익률(TSR) 중심의 전략으로 변화</p>
            <p className="mt-2">현금흐름 중요성 부각</p>
          </div>
          <div className="bg-purple-50 p-4 rounded-lg border-l-4 border-purple-400">
            <h3 className="text-lg font-bold mb-2">비용 절감 프로그램 실행</h3>
            <p>5년간 100억 달러 규모 비용 절감 프로그램</p>
            <p className="mt-2">사무직 11,000개 포지션 감축</p>
          </div>
        </div>
      </div>

      {/* 100억 달러 비용 절감 내역 */}
      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">100억 달러 비용 절감 프로그램 내역</h2>
        <div className="flex items-center justify-between">
          <div className="w-1/2">
            <ResponsiveContainer width="100%" height={300}>
              <PieChart>
                <Pie
                  data={costCuttingData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  outerRadius={100}
                  fill="#8884d8"
                  dataKey="value"
                  label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                >
                  {costCuttingData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.color} />
                  ))}
                </Pie>
                <Tooltip formatter={(value) => `${value}억 달러`} />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="w-1/2 pl-6">
            <div className="bg-blue-50 p-4 rounded-lg mb-4">
              <h3 className="text-lg font-bold text-blue-700">간접비 절감</h3>
              <p className="text-3xl font-bold">30억 달러</p>
            </div>
            <div className="bg-green-50 p-4 rounded-lg mb-4">
              <h3 className="text-lg font-bold text-green-700">상품 제조원가 절감</h3>
              <p className="text-3xl font-bold">60억 달러</p>
            </div>
            <div className="bg-yellow-50 p-4 rounded-lg">
              <h3 className="text-lg font-bold text-yellow-700">마케팅 효율성 절감</h3>
              <p className="text-3xl font-bold">10억 달러</p>
            </div>
          </div>
        </div>
      </div>

      {/* 지급 기간 비교 */}
      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">업계 지급 기간 비교</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={paymentTermsData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis label={{ value: '지급 기간 (일)', angle: -90, position: 'insideLeft' }} />
            <Tooltip formatter={(value) => `${value}일`} />
            <Legend />
            <Bar dataKey="days" name="지급 기간 (일)" />
          </BarChart>
        </ResponsiveContainer>
        <div className="mt-4 p-4 bg-gray-100 rounded-lg">
          <p className="font-semibold">핵심 인사이트:</p>
          <p>P&G는 경쟁사 대비 평균 30-55일 더 빠르게 대금을 지불하고 있었습니다. 이는 현금 유동성 및 운전자본 측면에서 경쟁 열위로 작용했습니다.</p>
        </div>
      </div>

      {/* 주요 운전자본 지표 변화 */}
      <div className="bg-white p-6 rounded-lg shadow mb-8">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">P&G 운전자본 지표 변화 (2010-2015)</h2>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={workingCapitalData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="dso" name="매출채권 회전일수 (DSO)" fill="#8884d8" />
            <Bar dataKey="dpo" name="매입채무 회전일수 (DPO)" fill="#82ca9d" />
            <Bar dataKey="ccc" name="현금전환주기 (CCC)" fill="#ffc658" />
          </BarChart>
        </ResponsiveContainer>
        <div className="mt-4 grid grid-cols-2 gap-4">
          <div className="p-3 bg-green-50 rounded-lg">
            <p className="font-semibold text-green-700">지급 조건 연장 효과 (2013):</p>
            <p>• DPO 증가: 69.8일 → 80.1일</p>
            <p>• CCC 감소: 16.4일 → 12.6일</p>
          </div>
          <div className="p-3 bg-blue-50 rounded-lg">
            <p className="font-semibold text-blue-700">지속적인 개선 (2015):</p>
            <p>• 현금전환주기(CCC) -3.5일 달성</p>
            <p>• 부정적 CCC는 공급업체 자금으로 운영 가능함을 의미</p>
          </div>
        </div>
      </div>

      {/* 결론 */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h2 className="text-2xl font-bold mb-4 text-blue-700">지급 조건 연장의 핵심 이유</h2>
        <div className="grid grid-cols-2 gap-6 mb-6">
          <div className="bg-blue-100 p-4 rounded-lg flex items-center">
            <div className="bg-blue-700 text-white rounded-full w-10 h-10 flex items-center justify-center mr-3 flex-shrink-0">1</div>
            <p className="font-semibold">비용 절감 프로그램의 일환</p>
          </div>
          <div className="bg-blue-100 p-4 rounded-lg flex items-center">
            <div className="bg-blue-700 text-white rounded-full w-10 h-10 flex items-center justify-center mr-3 flex-shrink-0">2</div>
            <p className="font-semibold">총주주수익률(TSR) 중심 경영 전략</p>
          </div>
          <div className="bg-blue-100 p-4 rounded-lg flex items-center">
            <div className="bg-blue-700 text-white rounded-full w-10 h-10 flex items-center justify-center mr-3 flex-shrink-0">3</div>
            <p className="font-semibold">업계 벤치마킹 결과 반영</p>
          </div>
          <div className="bg-blue-100 p-4 rounded-lg flex items-center">
            <div className="bg-blue-700 text-white rounded-full w-10 h-10 flex items-center justify-center mr-3 flex-shrink-0">4</div>
            <p className="font-semibold">운전자본 관리 효율성 개선</p>
          </div>
        </div>
        
        <div className="bg-yellow-50 p-4 rounded-lg border-l-4 border-yellow-500">
          <h3 className="text-lg font-bold mb-2">핵심 결론:</h3>
          <p>P&G는 지급 조건 연장을 통해 현금흐름을 개선하고 경쟁력을 강화했으나, 동시에 공급망 금융(SCF) 프로그램을 도입함으로써 공급업체와의 관계도 고려한 전략적 결정을 내렸습니다.</p>
        </div>
      </div>
    </div>
  );
};

export default PGPresentation;
