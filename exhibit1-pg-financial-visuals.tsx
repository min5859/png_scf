import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const data = [
  { year: '2011', revenue: 81104, grossProfit: 41245, operatingIncome: 15495, netIncome: 11797, grossMargin: 50.9, operatingMargin: 19.1, netMargin: 14.5 },
  { year: '2012', revenue: 82006, grossProfit: 40595, operatingIncome: 14611, netIncome: 10756, grossMargin: 49.5, operatingMargin: 17.8, netMargin: 13.1 },
  { year: '2013', revenue: 80116, grossProfit: 40125, operatingIncome: 14125, netIncome: 11412, grossMargin: 50.1, operatingMargin: 17.6, netMargin: 14.1 },
  { year: '2014', revenue: 80510, grossProfit: 39899, operatingIncome: 15497, netIncome: 11643, grossMargin: 49.6, operatingMargin: 19.2, netMargin: 14.5 },
  { year: '2015', revenue: 76279, grossProfit: 38031, operatingIncome: 14873, netIncome: 7036, grossMargin: 49.9, operatingMargin: 19.5, netMargin: 9.2 },
];

const formatNumber = (num) => {
  if (num >= 1000) {
    return `${(num / 1000).toFixed(1)}천억`;
  }
  return num;
};

const PGFinancialVisuals = () => {
  return (
    <div className="flex flex-col items-center space-y-10 p-6 bg-white">
      <h2 className="text-2xl font-bold text-center text-blue-800">P&G 재무 지표 시각화 (2011-2015)</h2>
      
      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">1. 주요 재무 지표 추이 (단위: 백만 달러)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart
            data={data}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis tickFormatter={formatNumber} />
            <Tooltip formatter={(value) => [`$${value} 백만`, '']} />
            <Legend />
            <Bar dataKey="revenue" name="매출" fill="#8884d8" />
            <Bar dataKey="grossProfit" name="매출총이익" fill="#82ca9d" />
            <Bar dataKey="operatingIncome" name="영업이익" fill="#ffc658" />
            <Bar dataKey="netIncome" name="당기순이익" fill="#ff8042" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="w-full">
        <h3 className="text-xl font-semibold mb-3 text-center">2. 수익성 비율 추이 (%)</h3>
        <ResponsiveContainer width="100%" height={400}>
          <LineChart
            data={data}
            margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis domain={[0, 60]} />
            <Tooltip formatter={(value) => [`${value}%`, '']} />
            <Legend />
            <Line type="monotone" dataKey="grossMargin" name="매출총이익률" stroke="#8884d8" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="operatingMargin" name="영업이익률" stroke="#82ca9d" strokeWidth={2} activeDot={{ r: 8 }} />
            <Line type="monotone" dataKey="netMargin" name="순이익률" stroke="#ff8042" strokeWidth={2} activeDot={{ r: 8 }} />
          </LineChart>
        </ResponsiveContainer>
      </div>

      <div className="w-full bg-blue-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">3. 주요 인사이트</h3>
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

      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">4. SCF 프로그램의 전략적 중요성</h3>
        <ul className="list-disc pl-6 space-y-2">
          <li><span className="font-semibold">운전자본 최적화</span>: 매출 하락 시기에 현금흐름 확보 필수</li>
          <li><span className="font-semibold">신용등급 활용</span>: AA- 등급으로 SCF 프로그램 유리하게 구축</li>
          <li><span className="font-semibold">공급업체 관계 유지</span>: 결제기간 연장에도 조기지불 옵션 제공</li>
          <li><span className="font-semibold">자본 효율성</span>: 손익계산서에 영향 없이 현금흐름 개선</li>
          <li><span className="font-semibold">산업 리더십</span>: 경쟁사 대비 혁신적인 공급망 금융 접근법</li>
        </ul>
      </div>
    </div>
  );
};

export default PGFinancialVisuals;
