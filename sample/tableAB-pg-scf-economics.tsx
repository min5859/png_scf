import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line, ComposedChart, Sankey, PieChart, Pie, Cell } from 'recharts';

const PGSCFEconomicsViz = () => {
  // Table A: P&G Supply Chain Finance 예시 데이터
  const tableAData = [
    {
      scenario: '기존 상태',
      days: 45,
      receivable: 45,
      payable: 45,
      financingCost: 2.92,
      netAmount: 997.08,
      description: 'SCF 도입 전 기본 결제 조건'
    },
    {
      scenario: '지불조건 연장(SCF 없음)',
      days: 75,
      receivable: 75,
      payable: 45,
      financingCost: 5.83,
      netAmount: 994.17,
      description: 'SCF 없이 지불 기간만 연장 (공급업체 부담 증가)'
    },
    {
      scenario: 'SCF 프로그램 적용',
      days: 75,
      receivable: 15,
      payable: 45,
      financingCost: 2.17,
      netAmount: 997.83,
      description: 'SCF 적용 시 (P&G는 75일 후 지불, 공급업체는 15일 후 은행에서 수령)'
    }
  ];

  // SCF 프로그램에 따른 지불 일정 시각화용 데이터
  const paymentTimelineData = [
    { name: 'D+0', scf: 0, traditional: 0, label: '인보이스 발행' },
    { name: 'D+15', scf: 997.83, traditional: 0, label: 'SCF 조기지불' },
    { name: 'D+45', scf: 997.83, traditional: 997.08, label: '기존 지불기한' },
    { name: 'D+75', scf: 997.83, traditional: 994.17, label: '연장된 지불기한' }
  ];

  // Table B: SCF 인보이스 할인율 계산 데이터
  const tableBData = {
    daysFinanced: 60,
    libor60Day: 0.30,
    bankSpread: 1.00,
    financingRate: 1.30,
    discountPercentage: 0.22
  };

  // 할인율 구성 파이 차트용 데이터
  const discountRateData = [
    { name: 'LIBOR 60일', value: tableBData.libor60Day },
    { name: '은행 스프레드', value: tableBData.bankSpread }
  ];

  // 공급업체 관점에서 3가지 시나리오 비교 데이터
  const supplierPerspectiveData = [
    {
      name: '기존 지불조건',
      invoiceAmount: 1000,
      daysToReceive: 45,
      financingCost: 2.92,
      netAmount: 997.08,
      annualRate: 3.50
    },
    {
      name: 'SCF 없는 지불연장',
      invoiceAmount: 1000,
      daysToReceive: 75,
      financingCost: 5.83,
      netAmount: 994.17,
      annualRate: 3.50
    },
    {
      name: 'SCF 프로그램',
      invoiceAmount: 1000,
      daysToReceive: 15,
      financingCost: 2.17,
      netAmount: 997.83,
      annualRate: 1.30
    }
  ];

  // P&G 관점에서의 운전자본 영향 데이터
  const pgPerspectiveData = [
    {
      name: '기존 지불조건',
      DPO: 45,
      workingCapitalImpact: 0,
      cashOutflow: 1000,
      cashOutflowDay: 45
    },
    {
      name: 'SCF 프로그램',
      DPO: 75,
      workingCapitalImpact: 30,
      cashOutflow: 1000,
      cashOutflowDay: 75
    }
  ];
  
  // 색상 설정
  const colors = {
    blue: '#2196f3',
    lightBlue: '#90caf9',
    green: '#4caf50',
    lightGreen: '#c8e6c9',
    red: '#f44336',
    orange: '#ff9800',
    purple: '#9c27b0',
    grey: '#9e9e9e'
  };
  
  // 파이 차트 색상
  const COLORS = ['#0088FE', '#00C49F'];

  return (
    <div className="p-4 bg-white rounded-lg">
      <h2 className="text-2xl font-bold text-center mb-8 text-blue-800">P&G SCF 프로그램의 경제적 효과 분석</h2>
      
      {/* 1. 3가지 시나리오 비교 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">1. 3가지 시나리오 비교 (인보이스 금액: $1,000)</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={tableAData}
              margin={{ top: 20, right: 30, left: 20, bottom: 30 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="scenario" angle={-15} textAnchor="end" height={60} />
              <YAxis yAxisId="left" />
              <YAxis yAxisId="right" orientation="right" domain={[992, 1000]} />
              <Tooltip formatter={(value, name) => [
                name === '공급업체 수령액' ? `$${value.toFixed(2)}` : `${value}일`, 
                name
              ]} />
              <Legend />
              <Bar yAxisId="left" dataKey="days" name="P&G 지불기한" fill={colors.blue} />
              <Bar yAxisId="left" dataKey="receivable" name="공급업체 수금기한" fill={colors.green} />
              <Line yAxisId="right" type="monotone" dataKey="netAmount" name="공급업체 수령액" stroke={colors.red} strokeWidth={2} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * SCF 프로그램을 통해 P&G는 지불기한을 연장하고, 공급업체는 더 빨리 현금 수령 가능
          </p>
        </div>
      </div>

      {/* 2. 지불 타임라인 비교 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">2. 공급업체 현금 수령 타임라인</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart
              data={paymentTimelineData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis domain={[0, 1100]} />
              <Tooltip formatter={(value) => value > 0 ? `$${value.toFixed(2)}` : '$0'} />
              <Legend />
              <Line type="stepAfter" dataKey="scf" name="SCF 프로그램" stroke={colors.green} strokeWidth={3} dot={{ r: 6 }} />
              <Line type="stepAfter" dataKey="traditional" name="기존 지불조건" stroke={colors.blue} strokeWidth={3} dot={{ r: 6 }} />
            </LineChart>
          </ResponsiveContainer>
          <div className="flex justify-center mt-2 space-x-8">
            <div className="flex items-center">
              <div className="w-4 h-4 bg-green-500 mr-2"></div>
              <span>SCF: 15일 후 $997.83 수령</span>
            </div>
            <div className="flex items-center">
              <div className="w-4 h-4 bg-blue-500 mr-2"></div>
              <span>기존: 45일 후 $997.08 수령</span>
            </div>
          </div>
        </div>
      </div>

      {/* 3. SCF 할인율 구성 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">3. SCF 인보이스 할인율 구성 요소</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="h-72">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={discountRateData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  outerRadius={80}
                  label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                  dataKey="value"
                >
                  {discountRateData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip formatter={(value) => `${value}%`} />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div className="bg-gray-50 p-4 rounded-lg flex flex-col justify-center">
            <h4 className="font-bold text-center mb-4">SCF 할인율 계산</h4>
            <table className="w-full text-left">
              <tbody>
                <tr className="border-b border-gray-200">
                  <td className="py-2 font-semibold">SCF 은행 금융 기간</td>
                  <td className="py-2 text-right">{tableBData.daysFinanced}일</td>
                </tr>
                <tr className="border-b border-gray-200">
                  <td className="py-2 font-semibold">LIBOR (60일)</td>
                  <td className="py-2 text-right">{tableBData.libor60Day}%</td>
                </tr>
                <tr className="border-b border-gray-200">
                  <td className="py-2 font-semibold">은행 스프레드</td>
                  <td className="py-2 text-right">{tableBData.bankSpread}%</td>
                </tr>
                <tr className="border-b border-gray-200">
                  <td className="py-2 font-semibold">SCF 파이낸싱 연이율</td>
                  <td className="py-2 text-right">{tableBData.financingRate}%</td>
                </tr>
                <tr className="bg-blue-50">
                  <td className="py-2 font-bold">SCF 인보이스 할인율</td>
                  <td className="py-2 text-right font-bold">{tableBData.discountPercentage}%</td>
                </tr>
                <tr>
                  <td className="py-2 text-sm text-gray-600" colSpan="2">
                    계산식: 할인율 = (연이율 × 금융기간) ÷ 360
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* 4. 공급업체 관점 비교 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">4. 공급업체 관점에서의 비교</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <ComposedChart
              data={supplierPerspectiveData}
              margin={{ top: 20, right: 30, left: 20, bottom: 30 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" angle={-15} textAnchor="end" height={60} />
              <YAxis yAxisId="left" domain={[0, 80]} />
              <YAxis yAxisId="right" orientation="right" />
              <Tooltip formatter={(value, name) => [
                name === '수령액' ? `$${value.toFixed(2)}` : 
                name === '연이율' ? `${value}%` : 
                name === '대기 일수' ? `${value}일` : 
                `$${value.toFixed(2)}`, 
                name
              ]} />
              <Legend />
              <Bar yAxisId="left" dataKey="daysToReceive" name="대기 일수" fill={colors.blue} />
              <Bar yAxisId="right" dataKey="financingCost" name="금융 비용" fill={colors.red} />
              <Line yAxisId="right" type="monotone" dataKey="netAmount" name="수령액" stroke={colors.green} strokeWidth={2} />
              <Line yAxisId="left" type="monotone" dataKey="annualRate" name="연이율" stroke={colors.purple} strokeWidth={2} />
            </ComposedChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * SCF 프로그램은 더 낮은 연이율(3.5% → 1.3%)과 더 빠른 수금(45일 → 15일)을 제공
          </p>
        </div>
      </div>

      {/* 5. P&G 관점에서의 효과 */}
      <div className="mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center">5. P&G 관점에서의 효과</h3>
        <div className="h-72">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart
              data={pgPerspectiveData}
              margin={{ top: 20, right: 30, left: 20, bottom: 10 }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip formatter={(value) => value === 1000 ? `$${value}` : `${value}일`} />
              <Legend />
              <Bar dataKey="DPO" name="지불 기간(DPO)" fill={colors.blue} />
              <Bar dataKey="workingCapitalImpact" name="운전자본 개선 효과(일)" fill={colors.green} />
              <Bar dataKey="cashOutflowDay" name="실제 지불일" fill={colors.orange} />
            </BarChart>
          </ResponsiveContainer>
          <p className="text-center text-sm mt-2 text-gray-600">
            * P&G는 SCF를 통해 지불 기간(DPO)을 30일 연장하고 그만큼 운전자본을 개선
          </p>
        </div>
      </div>

      {/* 6. SCF 프로그램의 경제적 효과 요약 */}
      <div className="w-full bg-blue-50 p-6 rounded-lg mb-10">
        <h3 className="text-xl font-semibold mb-4 text-center text-blue-800">6. SCF 프로그램의 경제적 효과 요약</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">P&G의 이점</h4>
            <ul className="list-disc ml-5 mt-2">
              <li>지불 기간 연장: 45일 → 75일 (+30일)</li>
              <li>운전자본 개선 (30일 추가 현금 보유)</li>
              <li>공급업체 관계 유지 및 강화</li>
              <li>어음 할인료 부담 없음 (공급업체 비용)</li>
            </ul>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">공급업체의 이점</h4>
            <ul className="list-disc ml-5 mt-2">
              <li>더 빠른 현금화: 45일 → 15일 (-30일)</li>
              <li>더 낮은 금융 비용: 3.5% → 1.3% (P&G 신용등급 활용)</li>
              <li>예측 가능한 현금흐름 확보</li>
              <li>재무제표 개선 (매출채권 감소)</li>
            </ul>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">SCF 은행의 이점</h4>
            <ul className="list-disc ml-5 mt-2">
              <li>안정적 수익: 1.0% 스프레드</li>
              <li>P&G 신용등급(AA-)에 기반한 낮은 위험</li>
              <li>공급업체와 새로운 관계 형성 기회</li>
              <li>거래 규모 확대 가능성 (P&G 외 공급망)</li>
            </ul>
          </div>
          <div className="bg-white p-4 rounded shadow">
            <h4 className="font-bold text-blue-700">핵심 성공 요인</h4>
            <ul className="list-disc ml-5 mt-2">
              <li>P&G의 높은 신용등급(AA-)</li>
              <li>경쟁적인 SCF 은행 구조 (시티그룹 vs JP모건)</li>
              <li>공급업체의 선택 자유도 보장</li>
              <li>"윈-윈-윈" 구조 설계</li>
            </ul>
          </div>
        </div>
      </div>

      {/* 7. Table A & B 요약 */}
      <div className="w-full bg-yellow-50 p-6 rounded-lg">
        <h3 className="text-xl font-semibold mb-4 text-center text-yellow-800">7. $300M 연간 거래 기준 SCF 효과 시뮬레이션</h3>
        <div className="overflow-x-auto">
          <table className="w-full bg-white border-collapse border border-gray-300 rounded">
            <thead className="bg-gray-100">
              <tr>
                <th className="border border-gray-300 p-2">시나리오</th>
                <th className="border border-gray-300 p-2">결제 조건</th>
                <th className="border border-gray-300 p-2">공급업체 수령 시점</th>
                <th className="border border-gray-300 p-2">금융 비용(연간)</th>
                <th className="border border-gray-300 p-2">P&G 운전자본 효과</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="border border-gray-300 p-2">기존 조건</td>
                <td className="border border-gray-300 p-2">45일</td>
                <td className="border border-gray-300 p-2">45일</td>
                <td className="border border-gray-300 p-2">$2.1M (3.5%)</td>
                <td className="border border-gray-300 p-2">-</td>
              </tr>
              <tr>
                <td className="border border-gray-300 p-2">SCF 없는 연장</td>
                <td className="border border-gray-300 p-2">75일</td>
                <td className="border border-gray-300 p-2">75일</td>
                <td className="border border-gray-300 p-2">$4.2M (3.5%)</td>
                <td className="border border-gray-300 p-2">+$25M (30일)</td>
              </tr>
              <tr className="bg-green-50">
                <td className="border border-gray-300 p-2 font-bold">SCF 프로그램</td>
                <td className="border border-gray-300 p-2 font-bold">75일</td>
                <td className="border border-gray-300 p-2 font-bold">15일</td>
                <td className="border border-gray-300 p-2 font-bold">$1.6M (1.3%)</td>
                <td className="border border-gray-300 p-2 font-bold">+$25M (30일)</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p className="text-center text-sm mt-4 text-gray-600">
          * SCF 프로그램은 P&G에게 $25M의 운전자본 개선 효과를 제공하면서, 동시에 공급업체의 금융 비용을 기존 조건 대비 $0.5M 절감
        </p>
      </div>
    </div>
  );
};

export default PGSCFEconomicsViz;
