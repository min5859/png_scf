import React from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, LineChart, Line, PieChart, Pie, Cell } from 'recharts';
import { ArrowUpCircle, ArrowDownCircle, DollarSign, Clock, BarChart2, AlertTriangle } from 'lucide-react';

const FibriaSCFAnalysis = () => {
  // 환율 데이터
  const exchangeRateData = [
    { year: '2012', rate: 1.96 },
    { year: '2013', rate: 2.16 },
    { year: '2014', rate: 2.35 },
    { year: '2015', rate: 2.69 },
  ];

  // 환율 손실 데이터 (단위: 백만 헤알)
  const currencyLossData = [
    { year: '2012', loss: 735 },
    { year: '2013', loss: 933 },
    { year: '2014', loss: 722 },
    { year: '2015', loss: 1926 },
  ];

  // 신용등급별 이자율 데이터
  const creditRateData = [
    { rating: 'AAA', rate: 0.48 },
    { rating: 'AA', rate: 0.63 },
    { rating: 'A', rate: 0.74 },
    { rating: 'BBB', rate: 1.13 },
    { rating: 'BB', rate: 2.80 },
  ];

  return (
    <div className="flex flex-col space-y-8 p-6 bg-gray-50">
      {/* 제목 섹션 */}
      <div className="bg-white rounded-lg shadow-lg p-6 border-l-4 border-blue-500">
        <h1 className="text-2xl font-bold text-blue-800 mb-2">Fibria는 SCF 프로그램을 계속 사용해야 할까요?</h1>
        <p className="text-gray-600">Supply Chain Finance (SCF) 프로그램 분석</p>
      </div>

      {/* 핵심 분석 카드 */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-lg shadow p-4 border-t-4 border-green-500">
          <div className="flex items-center mb-3">
            <DollarSign className="h-8 w-8 text-green-500 mr-2" />
            <h3 className="text-lg font-semibold">자금 조달 비용 절감</h3>
          </div>
          <p className="text-sm text-gray-600">P&G의 AA- 신용등급을 활용하여 Fibria의 BBB- 등급보다 유리한 조건으로 자금 조달 가능</p>
          <div className="mt-3 p-2 bg-green-50 rounded text-sm">
            <span className="font-bold">SCF 금융 비율:</span> 1.27% (3개월 LIBOR 0.27% + 스프레드 1.00%)
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-4 border-t-4 border-amber-500">
          <div className="flex items-center mb-3">
            <Clock className="h-8 w-8 text-amber-500 mr-2" />
            <h3 className="text-lg font-semibold">운전자본 기간 단축</h3>
          </div>
          <p className="text-sm text-gray-600">현금 전환 주기(CCC)를 약 100일에서 대폭 단축시켜 운전자본 부담 감소</p>
          <div className="mt-3 p-2 bg-amber-50 rounded text-sm">
            <span className="font-bold">단축 효과:</span> 105일 → 5일 (100일 개선)
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-4 border-t-4 border-red-500">
          <div className="flex items-center mb-3">
            <ArrowDownCircle className="h-8 w-8 text-red-500 mr-2" />
            <h3 className="text-lg font-semibold">환차손 문제 해결</h3>
          </div>
          <p className="text-sm text-gray-600">달러 표시 부채(90% 이상)로 인한 환차손 위험을 빠른 달러 유입으로 완화</p>
          <div className="mt-3 p-2 bg-red-50 rounded text-sm">
            <span className="font-bold">2015년 환차손:</span> 19억 헤알 ($741M)
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-4 border-t-4 border-blue-500">
          <div className="flex items-center mb-3">
            <BarChart2 className="h-8 w-8 text-blue-500 mr-2" />
            <h3 className="text-lg font-semibold">금융위기 대응력</h3>
          </div>
          <p className="text-sm text-gray-600">2008년 금융위기 시 자금 조달의 "극도의 어려움" 경험을 바탕으로 유동성 확보 강화</p>
          <div className="mt-3 p-2 bg-blue-50 rounded text-sm">
            <span className="font-bold">효과:</span> 다양한 유동성 확보 채널 구축
          </div>
        </div>
      </div>

      {/* 환율 변동과 금융위기 경험 섹션 */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4 text-gray-800">헤알/달러 환율 변동 추이</h3>
          <ResponsiveContainer width="100%" height={200}>
            <LineChart data={exchangeRateData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="year" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="rate" stroke="#3b82f6" name="헤알/달러 환율" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
          <div className="mt-3 p-3 bg-blue-50 rounded-md">
            <div className="flex items-center">
              <ArrowUpCircle className="h-5 w-5 text-red-500 mr-2" />
              <p className="text-sm">
                <span className="font-bold">환율 상승 의미:</span> 헤알화 가치 하락, 달러 표시 부채 부담 증가
              </p>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4 text-gray-800">금융위기와 자금 조달 어려움</h3>
          <div className="flex items-center justify-center mb-3">
            <AlertTriangle className="h-16 w-16 text-amber-500" />
          </div>
          <div className="bg-amber-50 rounded-lg p-4 mb-4">
            <p className="text-center font-bold text-amber-700 mb-2">2008년 금융위기 경험</p>
            <p className="text-sm text-center">"자금 조달이 극도로 어렵거나 불가능했던" 기간</p>
          </div>
          <div className="bg-red-50 rounded-lg p-4">
            <p className="text-center font-bold text-red-700 mb-2">환율 변동으로 인한 손실</p>
            <div className="grid grid-cols-2 gap-2 text-center">
              <div>
                <p className="text-xs">2015년</p>
                <p className="font-bold text-red-600">R$ 1,926M</p>
              </div>
              <div>
                <p className="text-xs">2014년</p>
                <p className="font-bold text-red-600">R$ 722M</p>
              </div>
              <div>
                <p className="text-xs">2013년</p>
                <p className="font-bold text-red-600">R$ 933M</p>
              </div>
              <div>
                <p className="text-xs">2012년</p>
                <p className="font-bold text-red-600">R$ 735M</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* 금리 비교와 운전자본 관리 섹션 */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4 text-gray-800">신용등급별 이자율 비교 (1년 만기)</h3>
          <ResponsiveContainer width="100%" height={200}>
            <BarChart data={creditRateData} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="rating" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="rate" fill="#10b981" name="이자율 (%)" />
            </BarChart>
          </ResponsiveContainer>
          <div className="mt-4 grid grid-cols-2 gap-2">
            <div className="p-3 bg-green-50 rounded-md">
              <p className="text-sm text-center">
                <span className="font-bold text-green-700">P&G 신용등급:</span><br />AA- (0.63% 수준)
              </p>
            </div>
            <div className="p-3 bg-amber-50 rounded-md">
              <p className="text-sm text-center">
                <span className="font-bold text-amber-700">Fibria 신용등급:</span><br />BBB- (1.13% 수준)
              </p>
            </div>
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold mb-4 text-gray-800">Fibria의 운전자본 관리 개선</h3>
          <div className="grid grid-cols-1 gap-4">
            <div className="bg-blue-50 rounded-lg p-4">
              <p className="font-semibold text-center mb-2">현금 전환 주기 (Cash Conversion Cycle)</p>
              <div className="flex items-center justify-center space-x-6">
                <div className="text-center">
                  <p className="text-xs text-gray-600">기존</p>
                  <p className="font-bold text-3xl text-red-600">100일</p>
                  <p className="text-xs">(80일 재고 + 60일 미수금 - 40일 미지급금)</p>
                </div>
                <div className="font-bold text-xl">→</div>
                <div className="text-center">
                  <p className="text-xs text-gray-600">SCF 활용</p>
                  <p className="font-bold text-3xl text-green-600">45일</p>
                  <p className="text-xs">(80일 재고 + 5일 미수금 - 40일 미지급금)</p>
                </div>
              </div>
            </div>
            
            <div className="bg-green-50 rounded-lg p-4">
              <p className="font-semibold text-center mb-2">빠른 현금화의 장점</p>
              <ul className="text-sm">
                <li className="flex items-center mb-1">
                  <span className="h-2 w-2 bg-green-500 rounded-full mr-2"></span>
                  <span>달러 부채 직접 상환으로 환위험 관리</span>
                </li>
                <li className="flex items-center mb-1">
                  <span className="h-2 w-2 bg-green-500 rounded-full mr-2"></span>
                  <span>자본 지출 및 전략적 투자 자금 확보</span>
                </li>
                <li className="flex items-center mb-1">
                  <span className="h-2 w-2 bg-green-500 rounded-full mr-2"></span>
                  <span>배당금 지급 등 주주가치 증대</span>
                </li>
                <li className="flex items-center">
                  <span className="h-2 w-2 bg-green-500 rounded-full mr-2"></span>
                  <span>금융위기 시 유동성 버퍼 확보</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      {/* SCF 작동 방식 설명 */}
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h3 className="text-lg font-semibold mb-4 text-gray-800">SCF 프로그램 작동 방식</h3>
        <div className="flex flex-col md:flex-row bg-blue-50 rounded-lg p-4 space-y-4 md:space-y-0 md:space-x-4">
          <div className="flex-1 p-3 bg-white rounded shadow">
            <p className="font-semibold text-blue-800 mb-2">1. 송장 발행</p>
            <p className="text-sm">Fibria가 P&G에 상품 배송 후 송장 발행</p>
          </div>
          <div className="flex-1 p-3 bg-white rounded shadow">
            <p className="font-semibold text-blue-800 mb-2">2. 송장 승인</p>
            <p className="text-sm">P&G가 송장 승인 및 지불 약속 확인</p>
          </div>
          <div className="flex-1 p-3 bg-white rounded shadow">
            <p className="font-semibold text-blue-800 mb-2">3. 조기 지불</p>
            <p className="text-sm">SCF 은행이 승인 후 5일 내 Fibria에 할인된 금액 지불</p>
          </div>
          <div className="flex-1 p-3 bg-white rounded shadow">
            <p className="font-semibold text-blue-800 mb-2">4. 만기 지불</p>
            <p className="text-sm">P&G가 105일 후 SCF 은행에 전체 금액 지불</p>
          </div>
        </div>
      </div>

      {/* 결론 섹션 */}
      <div className="bg-gradient-to-r from-blue-500 to-purple-500 rounded-lg shadow-lg p-6 text-white">
        <h2 className="text-xl font-bold mb-4">결론: Fibria는 SCF 프로그램을 계속 사용해야 합니다</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="bg-white bg-opacity-20 p-4 rounded-lg">
            <h4 className="font-semibold mb-2">주요 이점</h4>
            <ul className="list-disc pl-5 text-sm space-y-1">
              <li>더 낮은 자금 조달 비용 (P&G의 AA- 신용등급 활용)</li>
              <li>운전자본 주기 100일 단축으로 자금 효율성 극대화</li>
              <li>달러 부채 90%로 인한 환차손 위험 완화</li>
              <li>2008년 금융위기와 같은 상황에서의 유동성 확보</li>
              <li>전략적 투자, 배당금 지급에 활용 가능한 안정적 현금흐름</li>
            </ul>
          </div>
          <div className="bg-white bg-opacity-20 p-4 rounded-lg">
            <h4 className="font-semibold mb-2">추천 전략</h4>
            <ul className="list-disc pl-5 text-sm space-y-1">
              <li>Citigroup과 JPMorgan Chase 간 경쟁 입찰 진행</li>
              <li>SCF 은행 스프레드 협상 (현재 1.00%)</li>
              <li>두 은행과의 관계 유지하면서 유리한 조건 확보</li>
              <li>금융위기 대비 다양한 자금 조달 경로 확보</li>
              <li>SCF로 확보한 달러를 달러 부채 상환에 활용하여 환위험 관리</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FibriaSCFAnalysis;