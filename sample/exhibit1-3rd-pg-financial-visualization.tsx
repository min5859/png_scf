import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ComposedChart, Area } from 'recharts';

const PGFinancialViz = () => {
  // P&G 재무 데이터 (Exhibit 1 기반)
  const financialData = [
    {
      year: '2011',
      revenue: 81104,
      grossProfit: 41245,
      operatingIncome: 15495,
      netIncome: 11797,
      grossMargin: 50.9,
      operatingMargin: 19.1,
      netMargin: 14.5,
      employees: 129000,
      eps: 4.12,
      dividend: 1.97
    },
    {
      year: '2012',
      revenue: 82006,
      grossProfit: 40595,
      operatingIncome: 14611,
      netIncome: 10756,
      grossMargin: 49.5,
      operatingMargin: 17.8,
      netMargin: 13.1,
      employees: 126000,
      eps: 3.82,
      dividend: 2.14
    },
    {
      year: '2013',
      revenue: 80116,
      grossProfit: 40125,
      operatingIncome: 14125,
      netIncome: 11312,
      grossMargin: 50.1,
      operatingMargin: 17.6,
      netMargin: 14.1,
      employees: 121000,
      eps: 4.04,
      dividend: 2.29
    },
    {
      year: '2014',
      revenue: 80510,
      grossProfit: 39899,
      operatingIncome: 15497,
      netIncome: 11643,
      grossMargin: 49.6,
      operatingMargin: 19.2,
      netMargin: 14.5,
      employees: 118000,
      eps: 4.19,
      dividend: 2.45
    },
    {
      year: '2015',
      revenue: 76279,
      grossProfit: 38031,
      operatingIncome: 14873,
      netIncome: 7036,
      grossMargin: 49.9,
      operatingMargin: 19.5,
      netMargin: 9.2,
      employees: 110000,
      eps: 2.50,
      dividend: 2.59
    }
  ];
  
  const formatNumber = (num) => {
    if (num >= 1000) {
      return `${(num / 1000).toFixed(1)}천억`;
    }
    return num;
  };

  return (
    <div className="p-4 bg-white rounded-lg">
      <h2 className="text-2xl font-bold text-center mb-8 text-blue-800">P&G 재무 성과 시각화 (2011-2015)</h2>
      
      {/* 1. 매출 및 이익 추이 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">1. P&G 매출 및 이익 추이 (백만 달러)</h3>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={financialData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip formatter={(value) => `${value.toLocaleString()} 백만`} />
              <Legend />
              <Bar dataKey="revenue" name="매출" fill="#8884d8" />
              <Bar dataKey="grossProfit" name="매출총이익" fill="#82ca9d" />
              <Bar dataKey="operatingIncome" name="영업이익" fill="#ffc658" />
              <Line type="monotone" dataKey="netIncome" name="순이익" stroke="#ff8042" strokeWidth={3} dot={{ r: 6 }} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 2015년 순이익 급감은 베네수엘라 사업 회계방식 변경으로 인한 21억 달러 일회성 비용 때문
          </p>
        </div>
      </div>

      {/* 2. 수익성 지표 (마진) */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">2. P&G 수익성 지표 추이 (%)</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={financialData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis domain={[0, 60]} />
              <Tooltip formatter={(value) => `${value}%`} />
              <Legend />
              <Line type="monotone" dataKey="grossMargin" name="매출총이익률" stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
              <Line type="monotone" dataKey="operatingMargin" name="영업이익률" stroke="#82ca9d" strokeWidth={2} activeDot={{ r: 8 }} />
              <Line type="monotone" dataKey="netMargin" name="순이익률" stroke="#ff8042" strokeWidth={2} activeDot={{ r: 8 }} />
            </LineChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 2015년 순이익률 하락은 일회성 비용 때문이며, 매출총이익률과 영업이익률은 비교적 안정적으로 유지됨
          </p>
        </div>
      </div>

      {/* 3. 임직원 수 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">3. P&G 임직원 수 추이</h3>
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={financialData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis yAxisId="left" />
              <YAxis yAxisId="right" orientation="right" domain={[0, 150000]} />
              <Tooltip formatter={(value, name) => [name === '임직원 수' ? `${value.toLocaleString()} 명` : `${value.toLocaleString()} 백만`, name]} />
              <Legend />
              <Area yAxisId="left" type="monotone" dataKey="revenue" name="매출" fill="#bbdefb" stroke="#2196f3" />
              <Line yAxisId="right" type="monotone" dataKey="employees" name="임직원 수" stroke="#673ab7" strokeWidth={3} dot={{ r: 6 }} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 2011-2015년 사이 임직원 수 15% 감소 (129,000명 → 110,000명)
          </p>
        </div>
      </div>

      {/* 4. 주주 가치 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">4. P&G 주주 가치 지표</h3>
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={financialData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis yAxisId="left" domain={[0, 5]} />
              <YAxis yAxisId="right" orientation="right" domain={[0, 3]} />
              <Tooltip />
              <Legend />
              <Bar yAxisId="left" dataKey="eps" name="주당순이익(EPS, $)" fill="#ff9800" />
              <Line yAxisId="right" type="monotone" dataKey="dividend" name="주당배당금(DPS, $)" stroke="#e91e63" strokeWidth={3} dot={{ r: 6 }} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * 순이익 감소에도 불구하고 배당금은 꾸준히 증가 (주주 가치 유지 노력)
          </p>
        </div>
      </div>

      {/* 3. 주요 인사이트 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">5. 주요 인사이트</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">매출 정체 및 하락</h4>
            <p>2012년 이후 매출 성장이 정체되고 2015년에는 5.3% 감소</p>
            <p className="text-sm text-gray-600 mt-2">→ 비용 절감 및 운전자본 최적화 필요성 증가</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">안정적인 이익률</h4>
            <p>영업이익률은 17-19% 대를 안정적으로 유지</p>
            <p className="text-sm text-gray-600 mt-2">→ AA- 신용등급 유지에 기여</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">2015년 순이익 급감</h4>
            <p>순이익이 70억 달러로 감소 (전년 대비 -40%)</p>
            <p className="text-sm text-gray-600 mt-2">→ 운전자본 관리의 중요성 부각</p>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">현금흐름 관리 필요성</h4>
            <p>매출의 약 80%가 비용 관련 (COGS + SG&A)</p>
            <p className="text-sm text-gray-600 mt-2">→ 공급망 금융으로 현금흐름 개선 가능</p>
          </div>
        </div>
      </div>

      {/* SCF 프로그램의 전략적 중요성 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">6. SCF 프로그램의 전략적 중요성</h3>
        <ul className="list-disc pl-6 space-y-2">
          <li><span className="font-semibold">운전자본 최적화</span>: 매출 하락 시기에 현금흐름 확보 필수</li>
          <li><span className="font-semibold">신용등급 활용</span>: AA- 등급으로 SCF 프로그램 유리하게 구축</li>
          <li><span className="font-semibold">공급업체 관계 유지</span>: 결제기간 연장에도 조기지불 옵션 제공</li>
          <li><span className="font-semibold">자본 효율성</span>: 손익계산서에 영향 없이 현금흐름 개선</li>
          <li><span className="font-semibold">산업 리더십</span>: 경쟁사 대비 혁신적인 공급망 금융 접근법</li>
        </ul>
      </div>

      {/* SCF 프로그램 도입 시점 표시 */}
      <div className="p-4 bg-gray-100 rounded-lg">
        <h3 className="text-lg font-semibold mb-2 text-center">SCF 프로그램 도입 및 효과</h3>
        <div className="flex justify-center mb-4">
          <div className="bg-blue-100 p-3 rounded-lg inline-block">
            <span className="font-bold text-blue-800">2013년 4월</span>: P&G SCF 프로그램 도입 시점
          </div>
        </div>
        <p className="mt-2 font-bold text-center mb-2">
          주요 재무적 효과
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-3 rounded shadow">
            <p className="font-semibold text-gray-700">단기 효과</p>
            <ul className="list-disc ml-6 mt-1">
              <li>손익계산서에는 직접적인 영향이 즉시 나타나지 않음</li>
              <li>공급업체 지불 조건: 45일 → 75일 연장</li>
              <li>운전자본 개선 및 현금흐름 효율화</li>
            </ul>
          </div>
          <div className="bg-white p-3 rounded shadow">
            <p className="font-semibold text-gray-700">장기 효과</p>
            <ul className="list-disc ml-6 mt-1">
              <li>공급업체 관계 강화 (윈-윈-윈 솔루션)</li>
              <li>운영 효율성 개선 (인보이스 처리 등)</li>
              <li>공급망 안정성 및 지속가능성 개선</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default PGFinancialViz;
