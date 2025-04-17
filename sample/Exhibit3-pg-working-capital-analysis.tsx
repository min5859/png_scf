import React from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const workingCapitalData = [
  { year: '2000', dso: 26.6, dio: 60.6, dpo: 38.4, ccc: 48.8, adjustedDpo: 32.5 },
  { year: '2002', dso: 27.3, dio: 58.9, dpo: 36.1, ccc: 50.1, adjustedDpo: 30.8 },
  { year: '2002', dso: 28.0, dio: 61.6, dpo: 39.3, ccc: 50.3, adjustedDpo: 33.2 },
  { year: '2003', dso: 25.6, dio: 60.0, dpo: 46.1, ccc: 39.5, adjustedDpo: 38.5 },
  { year: '2004', dso: 28.8, dio: 63.9, dpo: 52.5, ccc: 40.2, adjustedDpo: 43.1 },
  { year: '2005', dso: 26.9, dio: 65.6, dpo: 49.8, ccc: 42.7, adjustedDpo: 41.1 },
  { year: '2006', dso: 30.6, dio: 69.3, dpo: 54.1, ccc: 45.8, adjustedDpo: 44.5 },
  { year: '2007', dso: 32.3, dio: 69.8, dpo: 58.4, ccc: 43.7, adjustedDpo: 47.9 },
  { year: '2008', dso: 31.1, dio: 78.2, dpo: 63.0, ccc: 46.4, adjustedDpo: 51.8 },
  { year: '2009', dso: 27.8, dio: 64.9, dpo: 56.4, ccc: 36.3, adjustedDpo: 47.2 },
  { year: '2010', dso: 25.1, dio: 62.9, dpo: 71.4, ccc: 16.6, adjustedDpo: 58.1 },
  { year: '2011', dso: 28.2, dio: 67.6, dpo: 73.5, ccc: 22.4, adjustedDpo: 59.7 },
  { year: '2012', dso: 27.0, dio: 59.2, dpo: 69.8, ccc: 16.4, adjustedDpo: 57.1 },
  { year: '2013', dso: 29.6, dio: 63.1, dpo: 80.1, ccc: 12.6, adjustedDpo: 64.9 },
  { year: '2014', dso: 29.0, dio: 60.7, dpo: 76.0, ccc: 13.7, adjustedDpo: 62.3 },
  { year: '2015', dso: 23.3, dio: 52.0, dpo: 78.8, ccc: -3.5, adjustedDpo: 64.8 }
];

// 2010-2015년 중요 이벤트
const timeline = [
  { year: '2010', event: "비용 절감 필요성 대두" },
  { year: '2012', event: "100억 달러 비용 절감 프로그램 발표" },
  { year: '2013', event: "공급망 금융(SCF) 프로그램 도입, 지불 기간 45→75일 연장" },
  { year: '2015', event: "현금전환주기 마이너스(-3.5일) 달성" }
];

const PGWorkingCapitalAnalysis = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">P&G 운전자본 관리 분석 (2000-2015)</h2>
      
      {/* 운전자본 관리 핵심 지표 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 운전자본 관리 핵심 지표 추이 (단위: 일)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[-10, 90]} />
            <Tooltip formatter={(value) => [`${value} 일`, '']} />
            <Legend />
            <Line type="monotone" dataKey="dso" name="매출채권회수기간(DSO)" stroke="#8884d8" strokeWidth={2} />
            <Line type="monotone" dataKey="dio" name="재고자산회전기간(DIO)" stroke="#82ca9d" strokeWidth={2} />
            <Line type="monotone" dataKey="dpo" name="매입채무지급기간(DPO)" stroke="#ff8042" strokeWidth={2} />
            <Line type="monotone" dataKey="ccc" name="현금전환주기(CCC)" stroke="#ff0000" strokeWidth={3} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* 현금전환주기 변화 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 현금전환주기 변화 (2000-2015)</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[-10, 60]} />
            <Tooltip formatter={(value) => [`${value} 일`, '']} />
            <Legend />
            <Bar dataKey="ccc" name="현금전환주기(CCC)" fill="#ff0000" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      {/* 매입채무지급기간(DPO) 변화 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">3. 매입채무지급기간(DPO) 변화 (2000-2015)</h3>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart
            data={workingCapitalData}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[30, 90]} />
            <Tooltip formatter={(value) => [`${value} 일`, '']} />
            <Legend />
            <Line type="monotone" dataKey="dpo" name="매입채무지급기간(DPO)" stroke="#ff8042" strokeWidth={3} />
            <Line type="monotone" dataKey="adjustedDpo" name="조정된 DPO" stroke="#8884d8" strokeWidth={2} dot={{ r: 5 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* 2015년 구성 요소 분석 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">4. 2015년 운전자본 구성 요소 비교</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-blue-50 p-4 rounded-lg shadow text-center">
            <h4 className="font-bold text-blue-700 text-lg">매출채권회수기간</h4>
            <p className="text-3xl font-bold mt-2">23.3일</p>
            <p className="text-sm text-gray-600 mt-2">2000년 대비 -3.3일</p>
            <p className="text-sm text-gray-600">2010년 대비 -1.8일</p>
          </div>
          <div className="bg-green-50 p-4 rounded-lg shadow text-center">
            <h4 className="font-bold text-green-700 text-lg">재고자산회전기간</h4>
            <p className="text-3xl font-bold mt-2">52.0일</p>
            <p className="text-sm text-gray-600 mt-2">2000년 대비 -8.6일</p>
            <p className="text-sm text-gray-600">2010년 대비 -10.9일</p>
          </div>
          <div className="bg-orange-50 p-4 rounded-lg shadow text-center">
            <h4 className="font-bold text-orange-700 text-lg">매입채무지급기간</h4>
            <p className="text-3xl font-bold mt-2">78.8일</p>
            <p className="text-sm text-gray-600 mt-2">2000년 대비 +40.4일</p>
            <p className="text-sm text-gray-600">2010년 대비 +7.4일</p>
          </div>
        </div>
        <div className="mt-4 bg-red-50 p-4 rounded-lg shadow text-center">
          <h4 className="font-bold text-red-700 text-lg">현금전환주기(CCC)</h4>
          <p className="text-3xl font-bold mt-2">-3.5일</p>
          <p className="text-sm text-gray-600 mt-2">2000년 대비 -52.3일</p>
          <p className="text-sm text-gray-600">2010년 대비 -20.1일</p>
        </div>
      </div>

      {/* 주요 이벤트 타임라인 */}
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">5. 주요 이벤트 타임라인 (2010-2015)</h3>
        <div className="relative">
          <div className="border-l-2 border-blue-500 ml-6 md:ml-12 pl-8 md:pl-16 py-4 space-y-10">
            {timeline.map((item, index) => (
              <div key={index} className="relative">
                <div className="absolute -left-10 md:-left-20 top-1 w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center">
                  <span className="text-white font-bold">{index + 1}</span>
                </div>
                <div className="bg-blue-50 p-4 rounded-lg shadow">
                  <h4 className="font-bold text-blue-700">{item.year}</h4>
                  <p>{item.event}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* 인사이트 요약 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">핵심 인사이트</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">매입채무지급기간(DPO) 지속적 증가</h4>
            <p>2000년 38.4일 → 2010년 71.4일 → 2015년 78.8일</p>
            <p className="text-sm text-gray-600 mt-2">→ 공급업체 결제 기간 연장 전략의 성공적 실행</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">현금전환주기(CCC) 혁신적 개선</h4>
            <p>2000년 48.8일 → 2010년 16.6일 → 2015년 -3.5일</p>
            <p className="text-sm text-gray-600 mt-2">→ 마이너스 CCC 달성으로 운전자본에서 현금 창출</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">SCF 프로그램 효과 (2013년 이후)</h4>
            <p>DPO 증가 + 재고/매출채권 감소 → CCC 대폭 개선</p>
            <p className="text-sm text-gray-600 mt-2">→ 공급업체 관계 유지하면서 현금흐름 최적화</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">2015년 운전자본 혁신</h4>
            <p>DSO/DIO 최저치 + DPO 최고치 = 마이너스 CCC</p>
            <p className="text-sm text-gray-600 mt-2">→ 매출 감소에도 현금흐름 개선 효과 입증</p>
          </div>
        </div>
      </div>

      {/* SCF 프로그램 영향 분석 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">공급망 금융(SCF) 프로그램의 영향</h3>
        <ul className="list-disc pl-6 space-y-3">
          <li><span className="font-semibold">벤치마킹 결과 반영</span>: 경쟁사 대비 낮은 DPO(45일)를 75일로 연장</li>
          <li><span className="font-semibold">주주수익률(TSR) 개선</span>: 현금흐름 증가로 배당금 지급 능력 강화</li>
          <li><span className="font-semibold">운전자본 효율화</span>: 15년간 CCC 52일 개선 (48.8일 → -3.5일)</li>
          <li><span className="font-semibold">공급업체 부담 경감</span>: 결제 연장과 동시에 조기 결제 옵션 제공</li>
          <li><span className="font-semibold">산업 리더십</span>: 운전자본 관리에서 업계 최고 수준 달성</li>
        </ul>
      </div>
    </div>
  );
};

export default PGWorkingCapitalAnalysis;
