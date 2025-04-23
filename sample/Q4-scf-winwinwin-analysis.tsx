import React from 'react';
import { ArrowUpCircle, TrendingUp, Clock, PieChart, DollarSign, CheckCircle, XCircle, Star, Award, Settings } from 'lucide-react';

const WinWinWinAnalysis = () => {
  return (
    <div className="flex flex-col w-full bg-gradient-to-br from-blue-50 to-indigo-50 p-6 rounded-xl shadow-lg">
      {/* Header */}
      <div className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-indigo-800 mb-2">P&G 공급망 금융(SCF) 프로그램</h1>
        <h2 className="text-2xl font-semibold text-indigo-600">"Win-Win-Win" 분석</h2>
        <div className="mt-4 flex justify-center">
          <div className="bg-white px-6 py-2 rounded-full shadow-md">
            <p className="text-gray-700 font-medium">2012년 발표된 5년간 <span className="text-green-600 font-bold">$100억</span> 비용 절감 프로그램의 일환</p>
          </div>
        </div>
      </div>

      {/* Triple Win Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {/* P&G Win */}
        <div className="bg-white rounded-xl shadow-md overflow-hidden border-t-4 border-blue-500 hover:shadow-xl transition-shadow">
          <div className="p-5">
            <div className="flex items-center mb-4">
              <div className="bg-blue-100 p-3 rounded-full mr-4">
                <TrendingUp className="h-6 w-6 text-blue-600" />
              </div>
              <h3 className="text-xl font-bold text-blue-800">P&G의 이점</h3>
            </div>
            <ul className="space-y-3">
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-blue-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">운전자본 개선 (DPO 45일→75일)</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-blue-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">업계 평균(75~100일)에 맞춰 경쟁력 강화</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-blue-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">공급업체 관계 유지 및 강화</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-blue-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">현금 흐름 개선 및 비용 절감</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Suppliers Win */}
        <div className="bg-white rounded-xl shadow-md overflow-hidden border-t-4 border-green-500 hover:shadow-xl transition-shadow">
          <div className="p-5">
            <div className="flex items-center mb-4">
              <div className="bg-green-100 p-3 rounded-full mr-4">
                <DollarSign className="h-6 w-6 text-green-600" />
              </div>
              <h3 className="text-xl font-bold text-green-800">공급업체의 이점</h3>
            </div>
            <ul className="space-y-3">
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">P&G의 AA- 신용등급 활용한 낮은 자금 조달 비용</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">15일 또는 75일 중 선택적 지급 유연성</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">신속한 현금화 가능 (Fibria: 5일 내 현금화)</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-green-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">미수금 감소로 대차대조표 개선</span>
              </li>
            </ul>
          </div>
        </div>

        {/* Banks Win */}
        <div className="bg-white rounded-xl shadow-md overflow-hidden border-t-4 border-purple-500 hover:shadow-xl transition-shadow">
          <div className="p-5">
            <div className="flex items-center mb-4">
              <div className="bg-purple-100 p-3 rounded-full mr-4">
                <PieChart className="h-6 w-6 text-purple-600" />
              </div>
              <h3 className="text-xl font-bold text-purple-800">SCF 은행의 이점</h3>
            </div>
            <ul className="space-y-3">
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">P&G의 낮은 위험 프로필 활용한 새로운 비즈니스</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">1% 스프레드를 통한 안정적인 수익</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">P&G의 수천 개 공급업체와 새로운 관계 구축</span>
              </li>
              <li className="flex items-start">
                <CheckCircle className="h-5 w-5 text-purple-500 mr-2 mt-0.5 flex-shrink-0" />
                <span className="text-gray-700">P&G의 높은 신용등급으로 금융 위험 최소화</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      {/* Key Success Factors */}
      <div className="bg-white rounded-xl p-6 shadow-md mb-8">
        <h3 className="text-xl font-bold text-amber-800 mb-6 text-center">SCF 프로그램 핵심 성공 요인</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
            <div className="bg-amber-100 p-3 rounded-full mb-3">
              <Star className="h-6 w-6 text-amber-600" />
            </div>
            <h4 className="font-semibold text-amber-700 text-center mb-2">P&G의 높은 신용등급 (AA-)</h4>
            <p className="text-gray-700 text-sm text-center">공급업체에게 낮은 할인율을 제공하고 은행에게는 안정적인 신용 위험 제공</p>
          </div>
          <div className="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
            <div className="bg-amber-100 p-3 rounded-full mb-3">
              <Settings className="h-6 w-6 text-amber-600" />
            </div>
            <h4 className="font-semibold text-amber-700 text-center mb-2">경쟁적인 SCF 은행 구조</h4>
            <p className="text-gray-700 text-sm text-center">시티그룹과 JP모건/도이치뱅크의 경쟁으로 공급업체에게 유리한 조건 제공</p>
          </div>
          <div className="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
            <div className="bg-amber-100 p-3 rounded-full mb-3">
              <Award className="h-6 w-6 text-amber-600" />
            </div>
            <h4 className="font-semibold text-amber-700 text-center mb-2">공급업체 선택 자유도 보장</h4>
            <p className="text-gray-700 text-sm text-center">SCF 참여 여부, 은행 선택, 할인 시점 등에 대한 자율성 부여</p>
          </div>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          <div className="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
            <div className="bg-amber-100 p-3 rounded-full mb-3">
              <Clock className="h-6 w-6 text-amber-600" />
            </div>
            <h4 className="font-semibold text-amber-700 text-center mb-2">글로벌 확장 및 단계적 접근</h4>
            <p className="text-gray-700 text-sm text-center">3,500개 주요 공급업체부터 시작하여 점진적으로 확대, 지역별 특성 고려한 접근</p>
          </div>
          <div className="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
            <div className="bg-amber-100 p-3 rounded-full mb-3">
              <TrendingUp className="h-6 w-6 text-amber-600" />
            </div>
            <h4 className="font-semibold text-amber-700 text-center mb-2">업체별 맞춤형 금융 솔루션</h4>
            <p className="text-gray-700 text-sm text-center">공급업체의 재무 상황과 지역에 따른 맞춤형 SCF 조건 협상 가능</p>
          </div>
        </div>
      </div>

      {/* Infographics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        {/* P&G Financial Impact */}
        <div className="bg-white rounded-xl p-5 shadow-md hover:shadow-xl transition-shadow flex flex-col items-center">
          <h3 className="text-lg font-semibold text-blue-800 mb-4">P&G 연간 구매 금액</h3>
          <div className="text-4xl font-bold text-blue-600 mb-2">$60억</div>
          <div className="flex items-center justify-center bg-blue-50 w-full p-3 rounded-lg">
            <ArrowUpCircle className="h-5 w-5 text-blue-500 mr-2" />
            <span className="text-gray-700 font-medium">지급 기간 30일 연장 시 약 <span className="text-blue-600 font-bold">$4.9억</span> 운전자본 개선</span>
          </div>
        </div>

        {/* SCF Program Adoption */}
        <div className="bg-white rounded-xl p-5 shadow-md hover:shadow-xl transition-shadow flex flex-col items-center">
          <h3 className="text-lg font-semibold text-green-800 mb-4">SCF 프로그램 도입 현황</h3>
          <div className="relative h-32 w-32 mb-3">
            <div className="absolute inset-0 rounded-full bg-gray-200"></div>
            <div className="absolute inset-0 rounded-full bg-green-500" style={{ clipPath: 'polygon(0 0, 100% 0, 100% 20%, 0 20%)' }}></div>
            <div className="absolute inset-0 flex items-center justify-center">
              <span className="text-3xl font-bold text-green-700">20%</span>
            </div>
          </div>
          <div className="text-center text-gray-700">
            <p>전체 공급업체 중 약 <b>700개 업체</b> 참여</p>
            <p>연간 <b>$13억</b> 구매액(전체의 약 20%)</p>
          </div>
        </div>

        {/* Timeline */}
        <div className="bg-white rounded-xl p-5 shadow-md hover:shadow-xl transition-shadow">
          <h3 className="text-lg font-semibold text-purple-800 mb-4 text-center">SCF 프로그램 타임라인</h3>
          <div className="relative">
            <div className="absolute left-4 top-0 bottom-0 w-0.5 bg-purple-200"></div>
            <div className="space-y-4 ml-10">
              <div className="relative">
                <div className="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                  <Clock className="h-3 w-3 text-white" />
                </div>
                <p className="text-sm text-gray-500">2012</p>
                <p className="text-gray-700">$100억 비용 절감 프로그램 발표</p>
              </div>
              <div className="relative">
                <div className="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                  <Clock className="h-3 w-3 text-white" />
                </div>
                <p className="text-sm text-gray-500">2013년 4월</p>
                <p className="text-gray-700">SCF 프로그램 론칭 및 지급 기간 연장 발표</p>
              </div>
              <div className="relative">
                <div className="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                  <Clock className="h-3 w-3 text-white" />
                </div>
                <p className="text-sm text-gray-500">2013년 중반</p>
                <p className="text-gray-700">Fibria SCF 프로그램 참여</p>
              </div>
              <div className="relative">
                <div className="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                  <Clock className="h-3 w-3 text-white" />
                </div>
                <p className="text-sm text-gray-500">2015년 중반</p>
                <p className="text-gray-700">약 700개 업체 참여, 2단계 확장 계획</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Potential Losers */}
      <div className="bg-white rounded-xl p-6 shadow-md mb-8">
        <h3 className="text-xl font-bold text-red-800 mb-4">손해를 볼 수 있는 당사자</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-red-50 p-4 rounded-lg">
            <div className="flex items-start">
              <XCircle className="h-5 w-5 text-red-500 mr-2 mt-0.5 flex-shrink-0" />
              <div>
                <h4 className="font-semibold text-red-700">지역 은행들</h4>
                <p className="text-gray-700 text-sm">기존에 공급업체에 대출 사업 기회 감소, 특히 개발도상국 은행들이 타격</p>
              </div>
            </div>
          </div>
          <div className="bg-red-50 p-4 rounded-lg">
            <div className="flex items-start">
              <XCircle className="h-5 w-5 text-red-500 mr-2 mt-0.5 flex-shrink-0" />
              <div>
                <h4 className="font-semibold text-red-700">소규모 공급업체</h4>
                <p className="text-gray-700 text-sm">SCF 참여 기회가 제한된 약소 공급업체들은 단순 지급 조건 연장으로 현금 흐름 부담</p>
              </div>
            </div>
          </div>
          <div className="bg-red-50 p-4 rounded-lg">
            <div className="flex items-start">
              <XCircle className="h-5 w-5 text-red-500 mr-2 mt-0.5 flex-shrink-0" />
              <div>
                <h4 className="font-semibold text-red-700">낮은 금융비용 공급업체</h4>
                <p className="text-gray-700 text-sm">이미 강한 신용등급을 가진 공급업체들에게는 SCF 혜택이 상대적으로 적음</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Conclusion Card */}
      <div className="bg-gradient-to-r from-indigo-600 to-blue-500 rounded-xl p-6 text-white shadow-lg">
        <h3 className="text-2xl font-bold mb-4">결론</h3>
        <p className="mb-4">P&G의 SCF 프로그램은 주요 당사자인 P&G, 참여 공급업체, SCF 은행 모두에게 이익을 제공하는 "win-win-win" 모델입니다.</p>
        <p className="mb-4">특히 Fibria와 같이 개발도상국에 위치한 공급업체들에게 유동성 확보와 낮은 자금조달 비용이라는 큰 이점을 제공합니다.</p>
        <p>일부 당사자들에게 간접적인 영향이 있을 수 있으나, 전체적인 가치 창출과 공급망 효율성 측면에서는 긍정적인 효과가 더 큽니다.</p>
      </div>
    </div>
  );
};

export default WinWinWinAnalysis;
