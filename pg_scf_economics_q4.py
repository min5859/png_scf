import streamlit as st
from typing import Dict, Any
import json
import os

class PGSCFEconomicsQ4Generator:
    """P&G SCF 경제적 효과 시각화를 위한 HTML 생성기 - Q4 버전"""
    
    def __init__(self):
        self.template = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>P&G SCF Win-Win-Win 분석</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                .card {
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }
                .card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                }
                .impact-meter {
                    height: 10px;
                    background: #f0f0f0;
                    border-radius: 5px;
                    margin: 10px 0;
                    overflow: hidden;
                }
                .impact-meter-fill {
                    height: 100%;
                    transition: width 1s ease-in-out;
                }
                .negative {
                    background: linear-gradient(to right, #ff6b6b, #ff8787);
                }
                .positive {
                    background: linear-gradient(to right, #69db7c, #8ce99a);
                }
                .key-point {
                    font-size: 1.1em;
                    color: #333;
                    margin: 10px 0;
                    padding-left: 20px;
                    position: relative;
                }
                .key-point:before {
                    content: "•";
                    position: absolute;
                    left: 0;
                    color: #4dabf7;
                }
            </style>
        </head>
        <body class="bg-gradient-to-br from-blue-50 to-indigo-50 p-6">
            <div class="max-w-7xl mx-auto">
                <!-- Header -->
                <div class="text-center mb-8">
                    <h1 class="text-3xl font-bold text-indigo-800 mb-2">P&G 공급망 금융(SCF) 프로그램</h1>
                    <h2 class="text-2xl font-semibold text-indigo-600">"Win-Win-Win" 분석</h2>
                    <div class="mt-4 flex justify-center">
                        <div class="bg-white px-6 py-2 rounded-full shadow-md">
                            <p class="text-gray-700 font-medium">2012년 발표된 5년간 <span class="text-green-600 font-bold">$100억</span> 비용 절감 프로그램의 일환</p>
                        </div>
                    </div>
                </div>

                <!-- Triple Win Cards -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <!-- P&G Win -->
                    <div class="card bg-white rounded-xl shadow-md overflow-hidden border-t-4 border-blue-500">
                        <div class="p-5">
                            <div class="flex items-center mb-4">
                                <div class="bg-blue-100 p-3 rounded-full mr-4">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                                    </svg>
                                </div>
                                <h3 class="text-xl font-bold text-blue-800">P&G의 이점</h3>
                            </div>
                            <ul class="space-y-3">
                                <li class="key-point">운전자본 개선 (DPO 45일→75일)</li>
                                <li class="key-point">업계 평균(75~100일)에 맞춰 경쟁력 강화</li>
                                <li class="key-point">공급업체 관계 유지 및 강화</li>
                                <li class="key-point">현금 흐름 개선 및 비용 절감</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Suppliers Win -->
                    <div class="card bg-white rounded-xl shadow-md overflow-hidden border-t-4 border-green-500">
                        <div class="p-5">
                            <div class="flex items-center mb-4">
                                <div class="bg-green-100 p-3 rounded-full mr-4">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </div>
                                <h3 class="text-xl font-bold text-green-800">공급업체의 이점</h3>
                            </div>
                            <ul class="space-y-3">
                                <li class="key-point">P&G의 AA- 신용등급 활용한 낮은 자금 조달 비용</li>
                                <li class="key-point">15일 또는 75일 중 선택적 지급 유연성</li>
                                <li class="key-point">신속한 현금화 가능 (Fibria: 5일 내 현금화)</li>
                                <li class="key-point">미수금 감소로 대차대조표 개선</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Banks Win -->
                    <div class="card bg-white rounded-xl shadow-md overflow-hidden border-t-4 border-purple-500">
                        <div class="p-5">
                            <div class="flex items-center mb-4">
                                <div class="bg-purple-100 p-3 rounded-full mr-4">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                                    </svg>
                                </div>
                                <h3 class="text-xl font-bold text-purple-800">SCF 은행의 이점</h3>
                            </div>
                            <ul class="space-y-3">
                                <li class="key-point">P&G의 낮은 위험 프로필 활용한 새로운 비즈니스</li>
                                <li class="key-point">1% 스프레드를 통한 안정적인 수익</li>
                                <li class="key-point">P&G의 수천 개 공급업체와 새로운 관계 구축</li>
                                <li class="key-point">P&G의 높은 신용등급으로 금융 위험 최소화</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Key Success Factors -->
                <div class="bg-white rounded-xl p-6 shadow-md mb-8">
                    <h3 class="text-xl font-bold text-amber-800 mb-6 text-center">SCF 프로그램 핵심 성공 요인</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                        <div class="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
                            <div class="bg-amber-100 p-3 rounded-full mb-3">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                                </svg>
                            </div>
                            <h4 class="font-semibold text-amber-700 text-center mb-2">P&G의 높은 신용등급 (AA-)</h4>
                            <p class="text-gray-700 text-sm text-center">공급업체에게 낮은 할인율을 제공하고 은행에게는 안정적인 신용 위험 제공</p>
                        </div>
                        <div class="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
                            <div class="bg-amber-100 p-3 rounded-full mb-3">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                </svg>
                            </div>
                            <h4 class="font-semibold text-amber-700 text-center mb-2">경쟁적인 SCF 은행 구조</h4>
                            <p class="text-gray-700 text-sm text-center">시티그룹과 JP모건/도이치뱅크의 경쟁으로 공급업체에게 유리한 조건 제공</p>
                        </div>
                        <div class="flex flex-col items-center bg-amber-50 p-4 rounded-lg">
                            <div class="bg-amber-100 p-3 rounded-full mb-3">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                            </div>
                            <h4 class="font-semibold text-amber-700 text-center mb-2">공급업체 선택 자유도 보장</h4>
                            <p class="text-gray-700 text-sm text-center">SCF 참여 여부, 은행 선택, 할인 시점 등에 대한 자율성 부여</p>
                        </div>
                    </div>
                </div>

                <!-- Infographics -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <!-- P&G Financial Impact -->
                    <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-xl transition-shadow flex flex-col items-center">
                        <h3 class="text-lg font-semibold text-blue-800 mb-4">P&G 연간 구매 금액</h3>
                        <div class="text-4xl font-bold text-blue-600 mb-2">$60억</div>
                        <div class="flex items-center justify-center bg-blue-50 w-full p-3 rounded-lg">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-blue-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                            </svg>
                            <span class="text-gray-700 font-medium">지급 기간 30일 연장 시 약 <span class="text-blue-600 font-bold">$4.9억</span> 운전자본 개선</span>
                        </div>
                    </div>

                    <!-- SCF Program Adoption -->
                    <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-xl transition-shadow flex flex-col items-center">
                        <h3 class="text-lg font-semibold text-green-800 mb-4">SCF 프로그램 도입 현황</h3>
                        <div class="relative h-32 w-32 mb-3">
                            <canvas id="adoptionChart"></canvas>
                        </div>
                        <div class="text-center text-gray-700">
                            <p>전체 공급업체 중 약 <b>700개 업체</b> 참여</p>
                            <p>연간 <b>$13억</b> 구매액(전체의 약 20%)</p>
                        </div>
                    </div>

                    <!-- Timeline -->
                    <div class="bg-white rounded-xl p-5 shadow-md hover:shadow-xl transition-shadow">
                        <h3 class="text-lg font-semibold text-purple-800 mb-4 text-center">SCF 프로그램 타임라인</h3>
                        <div class="relative">
                            <div class="absolute left-4 top-0 bottom-0 w-0.5 bg-purple-200"></div>
                            <div class="space-y-4 ml-10">
                                <div class="relative">
                                    <div class="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                    </div>
                                    <p class="text-sm text-gray-500">2012</p>
                                    <p class="text-gray-700">$100억 비용 절감 프로그램 발표</p>
                                </div>
                                <div class="relative">
                                    <div class="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                    </div>
                                    <p class="text-sm text-gray-500">2013년 4월</p>
                                    <p class="text-gray-700">SCF 프로그램 론칭 및 지급 기간 연장 발표</p>
                                </div>
                                <div class="relative">
                                    <div class="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                    </div>
                                    <p class="text-sm text-gray-500">2013년 중반</p>
                                    <p class="text-gray-700">Fibria SCF 프로그램 참여</p>
                                </div>
                                <div class="relative">
                                    <div class="absolute -left-10 mt-1 h-6 w-6 rounded-full bg-purple-500 flex items-center justify-center">
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-3 w-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                    </div>
                                    <p class="text-sm text-gray-500">2015년 중반</p>
                                    <p class="text-gray-700">약 700개 업체 참여, 2단계 확장 계획</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Potential Losers -->
                <div class="bg-white rounded-xl p-6 shadow-md mb-8">
                    <h3 class="text-xl font-bold text-red-800 mb-4">손해를 볼 수 있는 당사자</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div class="bg-red-50 p-4 rounded-lg">
                            <div class="flex items-start">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 mr-2 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <div>
                                    <h4 class="font-semibold text-red-700">지역 은행들</h4>
                                    <p class="text-gray-700 text-sm">기존에 공급업체에 대출 사업 기회 감소, 특히 개발도상국 은행들이 타격</p>
                                </div>
                            </div>
                        </div>
                        <div class="bg-red-50 p-4 rounded-lg">
                            <div class="flex items-start">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 mr-2 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <div>
                                    <h4 class="font-semibold text-red-700">소규모 공급업체</h4>
                                    <p class="text-gray-700 text-sm">SCF 참여 기회가 제한된 약소 공급업체들은 단순 지급 조건 연장으로 현금 흐름 부담</p>
                                </div>
                            </div>
                        </div>
                        <div class="bg-red-50 p-4 rounded-lg">
                            <div class="flex items-start">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-500 mr-2 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <div>
                                    <h4 class="font-semibold text-red-700">낮은 금융비용 공급업체</h4>
                                    <p class="text-gray-700 text-sm">이미 강한 신용등급을 가진 공급업체들에게는 SCF 혜택이 상대적으로 적음</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Conclusion Card -->
                <div class="bg-gradient-to-r from-indigo-600 to-blue-500 rounded-xl p-6 text-white shadow-lg">
                    <h3 class="text-2xl font-bold mb-4">결론</h3>
                    <p class="mb-4">P&G의 SCF 프로그램은 주요 당사자인 P&G, 참여 공급업체, SCF 은행 모두에게 이익을 제공하는 "win-win-win" 모델입니다.</p>
                    <p class="mb-4">특히 Fibria와 같이 개발도상국에 위치한 공급업체들에게 유동성 확보와 낮은 자금조달 비용이라는 큰 이점을 제공합니다.</p>
                    <p>일부 당사자들에게 간접적인 영향이 있을 수 있으나, 전체적인 가치 창출과 공급망 효율성 측면에서는 긍정적인 효과가 더 큽니다.</p>
                </div>
            </div>

            <script>
                // 도입 현황 차트
                const ctx = document.getElementById('adoptionChart').getContext('2d');
                new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: ['참여', '미참여'],
                        datasets: [{
                            data: [20, 80],
                            backgroundColor: [
                                '#10B981',
                                '#E5E7EB'
                            ],
                            borderWidth: 0
                        }]
                    },
                    options: {
                        cutout: '70%',
                        plugins: {
                            legend: {
                                display: false
                            }
                        }
                    }
                });

                // 애니메이션 효과
                document.addEventListener('DOMContentLoaded', function() {
                    const cards = document.querySelectorAll('.card');
                    const meters = document.querySelectorAll('.impact-meter-fill');
                    
                    cards.forEach(card => {
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                    });
                    
                    meters.forEach(meter => {
                        meter.style.width = '0';
                    });
                    
                    setTimeout(() => {
                        cards.forEach((card, index) => {
                            setTimeout(() => {
                                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                                card.style.opacity = '1';
                                card.style.transform = 'translateY(0)';
                            }, index * 200);
                        });
                        
                        meters.forEach((meter, index) => {
                            setTimeout(() => {
                                meter.style.transition = 'width 1s ease-in-out';
                                meter.style.width = meter.getAttribute('data-width') || '80%';
                            }, (index + 2) * 200);
                        });
                    }, 100);
                });
            </script>
        </body>
        </html>
        """
    
    def generate_html(self) -> str:
        """HTML 코드를 생성합니다."""
        return self.template

def pg_scf_economics_q4_viz():
    """Streamlit 앱에서 호출할 P&G SCF 경제적 효과 시각화 함수 - Q4 버전"""
    st.title("P&G SCF 프로그램의 Win-Win-Win 분석")
    
    # 컴포넌트 생성기 초기화
    generator = PGSCFEconomicsQ4Generator()
    
    # HTML 코드 생성
    html_code = generator.generate_html()
    
    # HTML 렌더링
    st.components.v1.html(html_code, height=3000, scrolling=True)

if __name__ == "__main__":
    pg_scf_economics_q4_viz() 