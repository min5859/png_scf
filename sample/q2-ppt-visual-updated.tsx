import React from 'react';

const PPTVisuals = () => {
  return (
    <div className="bg-gray-100 p-6 rounded-lg">
      <h1 className="text-2xl font-bold text-center mb-8">Q2: P&G의 결제 조건 연장이 재무상태에 미치는 영향</h1>
      
      {/* 슬라이드 1: 개요 */}
      <div className="bg-white rounded-lg p-6 mb-8 shadow-md">
        <h2 className="text-xl font-bold mb-4 text-blue-700">SCF 프로그램 없는 결제 조건 연장의 영향</h2>
        <div className="flex items-center justify-center mb-6">
          <div className="text-center p-4 bg-blue-100 rounded-lg mx-2 w-1/2">
            <h3 className="font-bold mb-2">결제 조건 변경</h3>
            <div className="flex justify-center items-center">
              <div className="bg-gray-200 p-3 rounded-lg mr-4">
                <span className="font-bold">기존</span>
                <p className="text-2xl font-bold">45일</p>
              </div>
              <div className="text-2xl">→</div>
              <div className="bg-gray-200 p-3 rounded-lg ml-4">
                <span className="font-bold">변경</span>
                <p className="text-2xl font-bold">75일</p>
              </div>
            </div>
            <p className="mt-2">평균 지급 기간 30일 연장</p>
          </div>
        </div>
        <p className="text-center">P&G는 공급업체에 대한 지급을 평균 30일 연장함으로써<br />약 50억 달러의 현금을 30일 더 보유할 수 있게 됨</p>
        <p className="text-center text-sm text-gray-600 mt-2">(연간 구매액 600억 달러 ÷ 12개월 ≈ 50억 달러)</p>
      </div>
      
      {/* 슬라이드 2: P&G에 미치는 영향 */}
      <div className="bg-white rounded-lg p-6 mb-8 shadow-md">
        <h2 className="text-xl font-bold mb-4 text-blue-700">P&G에 미치는 영향</h2>
        <div className="flex flex-wrap">
          <div className="w-1/2 p-2">
            <div className="bg-green-100 p-4 rounded-lg h-full">
              <h3 className="font-bold text-green-800 mb-3">긍정적 영향</h3>
              <ul className="space-y-4">
                <li className="flex items-start">
                  <div className="bg-green-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">매입채무 50억 달러 증가</span>
                    <p className="text-sm">P&G의 매입채무가 83억에서 133억 달러로 증가</p>
                    <p className="text-xs text-gray-600">(Exhibit 2: 2015년 AP 83억 달러에서 30일 추가 지급분 50억 달러 증가)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-green-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">현금 50억 달러 유보 효과</span>
                    <p className="text-sm">지급 지연으로 인한 영업활동 현금흐름 개선</p>
                    <p className="text-xs text-gray-600">(연간 구매액 600억 달러 ÷ 12개월 × 30일 연장)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-green-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">이자 비용 절감: 연간 1,250만~2,500만 달러</span>
                    <p className="text-sm">AA등급 기준 0.25%~0.50% × 50억 달러</p>
                    <p className="text-xs text-gray-600">(Exhibit 8: AA 신용등급 금리 참조)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-green-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-green-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">현금전환주기(CCC) 개선</span>
                    <p className="text-sm">12.6일 → -17.4일 (30일 감소)</p>
                    <p className="text-xs text-gray-600">(Exhibit 3: 2013년 CCC 12.6일에서 30일 개선)</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div className="w-1/2 p-2">
            <div className="bg-red-50 p-4 rounded-lg h-full">
              <h3 className="font-bold text-red-800 mb-3">잠재적 부정 영향</h3>
              <ul className="space-y-4">
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">유동비율(Current Ratio) 악화 가능성</span>
                    <p className="text-sm">유동부채 증가로 인한 단기 재무 건전성 지표 하락</p>
                    <p className="text-xs text-gray-600">(Exhibit 2: 2015년 현재 유동비율 1.00에서 악화 가능)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">공급업체 관계 악화 위험</span>
                    <p className="text-sm">공급업체의 현금흐름 압박으로 인한 관계 악화</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">공급망 안정성 저하</span>
                    <p className="text-sm">공급업체의 재무 건전성 악화로 인한 공급 불안정</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">장기적 가격 인상 압력</span>
                    <p className="text-sm">공급업체의 비용 증가가 장기적으로 가격 인상으로 전가될 가능성</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      
      {/* 슬라이드 3: Fibria에 미치는 영향 */}
      <div className="bg-white rounded-lg p-6 mb-8 shadow-md">
        <h2 className="text-xl font-bold mb-4 text-blue-700">Fibria에 미치는 영향</h2>
        <div className="flex flex-wrap">
          <div className="w-1/2 p-2">
            <div className="bg-red-50 p-4 rounded-lg h-full">
              <h3 className="font-bold text-red-800 mb-3">부정적 영향</h3>
              <ul className="space-y-4">
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">매출채권 3,700만 달러 증가</span>
                    <p className="text-sm">지급기간 45일 연장으로 인한 매출채권 증가</p>
                    <p className="text-xs text-gray-600">(연간 P&G 매출 3억 달러 × 45일 ÷ 365일 ≈ 3,700만 달러)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">추가 자금조달 필요</span>
                    <p className="text-sm">운전자본 3,700만 달러 추가 필요</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">이자 비용 증가: 연간 74~111만 달러</span>
                    <p className="text-sm">BBB- 등급 기준 2.0%~3.0% × 3,700만 달러</p>
                    <p className="text-xs text-gray-600">(Exhibit 8: BBB 신용등급 금리 약 1.13%, 케이스 내 언급 2~3%)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">현금전환주기(CCC) 악화</span>
                    <p className="text-sm">100일 → 145일 (45일 증가)</p>
                    <p className="text-xs text-gray-600">(Exhibit 7: 2014년 CCC 약 100일에서 45일 악화)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-red-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-red-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">유동비율 악화</span>
                    <p className="text-sm">1.55 → 약 1.35 (단기 재무 건전성 저하)</p>
                    <p className="text-xs text-gray-600">(Exhibit 6: 2014년 유동비율 1.55, 매출채권 증가로 악화)</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
          <div className="w-1/2 p-2">
            <div className="bg-yellow-50 p-4 rounded-lg h-full">
              <h3 className="font-bold text-yellow-800 mb-3">추가적 고려사항</h3>
              <ul className="space-y-4">
                <li className="flex items-start">
                  <div className="bg-yellow-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-yellow-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">환율 리스크 증가</span>
                    <p className="text-sm">부채의 90%가 USD 표시 → 브라질 헤알화 대비 USD 강세 시 부담 가중</p>
                    <p className="text-xs text-gray-600">(케이스 7페이지: 부채의 90% 이상이 USD 표시)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-yellow-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-yellow-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">유동성 관리 어려움</span>
                    <p className="text-sm">이미 재무적 어려움 상황에서 더 큰 압박 직면</p>
                    <p className="text-xs text-gray-600">(케이스 7페이지: 2008년 금융위기 이후 유동성 문제 경험)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-yellow-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-yellow-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">산업 특성</span>
                    <p className="text-sm">원자재 생산자로서 이미 긴 현금전환주기(100일) 부담</p>
                    <p className="text-xs text-gray-600">(케이스 7페이지: 생산 및 운송 과정에 약 80일 소요)</p>
                  </div>
                </li>
                <li className="flex items-start">
                  <div className="bg-yellow-200 p-2 rounded-full mr-2 mt-1">
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 text-yellow-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                  </div>
                  <div>
                    <span className="font-bold">P&G 의존도</span>
                    <p className="text-sm">P&G는 Fibria 매출의 약 10%를 차지 → 협상력 불균형</p>
                    <p className="text-xs text-gray-600">(케이스 7페이지: P&G 매출은 Fibria 총 매출의 약 10%)</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      
      {/* 슬라이드 4: 이자비용 불균형 */}
      <div className="bg-white rounded-lg p-6 mb-8 shadow-md">
        <h2 className="text-xl font-bold mb-4 text-blue-700">이자비용 차이의 불균형</h2>
        <div className="flex justify-center mb-6">
          <div className="w-4/5">
            <div className="relative pt-4">
              <div className="bg-gray-200 h-6 rounded-full">
                <div className="bg-green-500 h-6 rounded-l-full" style={{width: '95%'}}></div>
              </div>
              <div className="flex justify-between mt-2 text-sm">
                <span>P&G 이자 절감: 약 1,250만~2,500만 달러/년</span>
                <span className="font-bold text-green-600">95%</span>
              </div>
              
              <div className="bg-gray-200 h-6 rounded-full mt-6">
                <div className="bg-red-500 h-6 rounded-l-full" style={{width: '5%'}}></div>
              </div>
              <div className="flex justify-between mt-2 text-sm">
                <span>Fibria 이자 부담: 약 74만~111만 달러/년</span>
                <span className="font-bold text-red-600">5%</span>
              </div>
            </div>
            
            <div className="mt-10 bg-blue-50 p-4 rounded-lg">
              <h3 className="font-bold mb-2">불균형의 주요 원인</h3>
              <div className="grid grid-cols-2 gap-4">
                <div className="flex items-start">
                  <div className="bg-blue-200 p-2 rounded-full mr-2 mt-1">
                    <span className="font-bold text-blue-700">1</span>
                  </div>
                  <div>
                    <span className="font-bold">기업 규모 차이</span>
                    <p className="text-sm">P&G(800억 달러) vs Fibria(30억 달러)</p>
                    <p className="text-xs text-gray-600">(Exhibit 1, 5: 2015년 매출 기준)</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <div className="bg-blue-200 p-2 rounded-full mr-2 mt-1">
                    <span className="font-bold text-blue-700">2</span>
                  </div>
                  <div>
                    <span className="font-bold">신용등급 차이</span>
                    <p className="text-sm">P&G(AA-: 0.25~0.5%) vs Fibria(BBB-: 2~3%)</p>
                    <p className="text-xs text-gray-600">(Exhibit 2, 6: 신용등급 정보)</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <div className="bg-blue-200 p-2 rounded-full mr-2 mt-1">
                    <span className="font-bold text-blue-700">3</span>
                  </div>
                  <div>
                    <span className="font-bold">자금조달 시장 접근성</span>
                    <p className="text-sm">P&G(글로벌 자본시장) vs Fibria(제한적 접근)</p>
                    <p className="text-xs text-gray-600">(케이스 7페이지: 금융위기 시 자금조달 어려움 언급)</p>
                  </div>
                </div>
                <div className="flex items-start">
                  <div className="bg-blue-200 p-2 rounded-full mr-2 mt-1">
                    <span className="font-bold text-blue-700">4</span>
                  </div>
                  <div>
                    <span className="font-bold">국가 리스크</span>
                    <p className="text-sm">미국 기업 vs 브라질 기업(신흥시장 리스크)</p>
                    <p className="text-xs text-gray-600">(환율 변동성: 2012년 1.96 → 2015년 2.69 헤알/달러)</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      {/* 슬라이드 5: 결론 */}
      <div className="bg-white rounded-lg p-6 shadow-md">
        <h2 className="text-xl font-bold mb-4 text-blue-700">결론: SCF 프로그램의 필요성</h2>
        <div className="flex flex-wrap">
          <div className="w-full p-2">
            <div className="bg-gray-100 p-4 rounded-lg">
              <div className="flex mb-6">
                <div className="w-1/2 p-2">
                  <div className="bg-green-100 p-4 rounded-lg">
                    <h3 className="font-bold text-center mb-2">P&G</h3>
                    <p className="text-center">50억 달러 × 30일 = <span className="text-green-600 font-bold">큰 이익</span></p>
                    <p className="text-xs text-center text-gray-600">(600억 달러 연간 구매액 ÷ 12개월 × 1개월)</p>
                  </div>
                </div>
                <div className="w-1/2 p-2">
                  <div className="bg-red-100 p-4 rounded-lg">
                    <h3 className="font-bold text-center mb-2">Fibria</h3>
                    <p className="text-center">3,700만 달러 × 45일 = <span className="text-red-600 font-bold">큰 부담</span></p>
                    <p className="text-xs text-center text-gray-600">(3억 달러 P&G 매출 × 45일 ÷ 365일)</p>
                  </div>
                </div>
              </div>
              
              <div className="bg-yellow-50 p-4 rounded-lg mb-6">
                <h3 className="font-bold text-center mb-2">문제 상황</h3>
                <p className="text-center">P&G와 공급업체 간 불균형 → 장기적 공급망 약화 위험</p>
              </div>
              
              <div className="bg-blue-50 p-4 rounded-lg">
                <h3 className="font-bold text-center mb-2">해결책</h3>
                <p className="text-center">SCF 프로그램 도입으로 <span className="font-bold">Win-Win-Win</span> 관계 구축 필요</p>
                <div className="flex justify-center mt-4">
                  <div className="flex items-center">
                    <div className="bg-blue-200 rounded-full p-2 h-12 w-12 flex items-center justify-center mx-2">
                      <span className="font-bold">P&G</span>
                    </div>
                    <div className="text-2xl mx-1">+</div>
                    <div className="bg-blue-200 rounded-full p-2 h-12 w-12 flex items-center justify-center mx-2">
                      <span className="font-bold">SCF</span>
                    </div>
                    <div className="text-2xl mx-1">+</div>
                    <div className="bg-blue-200 rounded-full p-2 h-12 w-12 flex items-center justify-center mx-2">
                      <span className="font-bold">Fibria</span>
                    </div>
                  </div>
                </div>
                <ul className="mt-4 space-y-2 text-sm">
                  <li className="flex items-start">
                    <div className="bg-blue-200 p-1 rounded-full mr-2 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    </div>
                    <div>
                      <span className="font-bold">P&G</span>: 결제 조건 연장을 통한 운전자본 개선 목표 달성
                    </div>
                  </li>
                  <li className="flex items-start">
                    <div className="bg-blue-200 p-1 rounded-full mr-2 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    </div>
                    <div>
                      <span className="font-bold">Fibria</span>: P&G의 신용등급(AA-)을 활용한 저비용 자금조달로 부담 경감 (0.35% 비용 vs 기존 2~3% 팩토링 비용)
                    </div>
                  </li>
                  <li className="flex items-start">
                    <div className="bg-blue-200 p-1 rounded-full mr-2 mt-1">
                      <svg xmlns="http://www.w3.org/2000/svg" className="h-3 w-3 text-blue-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                      </svg>
                    </div>
                    <div>
                      <span className="font-bold">SCF 은행</span>: 안정적인 수수료 수입 확보 및 신규 고객 관계 구축
                    </div>
                  </li>
                </ul>