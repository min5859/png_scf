import json
from typing import Dict, Any

class PGSCFEconomicsQ2Generator:
    """Q2 시각화를 위한 Chart.js 컴포넌트 생성기"""
    
    def __init__(self):
        """초기화"""
        self.data = {
            "payment_terms": {
                "before": 45,
                "after": 75,
                "change": 30
            },
            "pg_impact": {
                "positive": [
                    {"title": "매입채무 증가", "value": "40억 달러", "detail": "87억 → 127억 달러"},
                    {"title": "현금 유보 효과", "value": "40억 달러", "detail": "영업활동 현금흐름 개선"},
                    {"title": "이자 비용 절감", "value": "1,000만~2,000만 달러/년", "detail": "AA등급 기준 0.25%~0.50% × 40억 달러"},
                    {"title": "현금전환주기 개선", "value": "30일 감소", "detail": "12.6일 → -17.4일"}
                ],
                "negative": [
                    {"title": "유동비율 악화", "detail": "유동부채 증가로 인한 단기 재무 건전성 지표 하락"},
                    {"title": "공급업체 관계 악화", "detail": "공급업체의 현금흐름 압박으로 인한 관계 악화"},
                    {"title": "공급망 안정성 저하", "detail": "공급업체의 재무 건전성 악화로 인한 공급 불안정"},
                    {"title": "장기적 가격 인상 압력", "detail": "공급업체의 비용 증가가 장기적으로 가격 인상으로 전가될 가능성"}
                ]
            },
            "fibria_impact": {
                "negative": [
                    {"title": "매출채권 증가", "value": "3,700만 달러", "detail": "지급기간 45일 연장으로 인한 매출채권 75% 증가"},
                    {"title": "추가 자금조달 필요", "value": "3,700만 달러", "detail": "운전자본 3,700만 달러 추가 필요"},
                    {"title": "이자 비용 증가", "value": "74~111만 달러/년", "detail": "BBB- 등급 기준 2.0%~3.0% × 3,700만 달러"},
                    {"title": "현금전환주기 악화", "value": "45일 증가", "detail": "100일 → 145일"},
                    {"title": "유동비율 악화", "value": "1.55 → 1.35", "detail": "단기 재무 건전성 저하"}
                ],
                "considerations": [
                    {"title": "환율 리스크 증가", "detail": "부채의 90%가 USD 표시 → 브라질 헤알화 대비 USD 강세 시 부담 가중"},
                    {"title": "유동성 관리 어려움", "detail": "이미 재무적 어려움 상황에서 더 큰 압박 직면"},
                    {"title": "산업 특성", "detail": "원자재 생산자로서 이미 긴 현금전환주기(100일) 부담"},
                    {"title": "P&G 의존도", "detail": "P&G는 Fibria 매출의 약 10%를 차지 → 협상력 불균형"}
                ]
            },
            "interest_cost_comparison": {
                "pg_savings": {"min": 10, "max": 20, "unit": "백만 달러"},
                "fibria_cost": {"min": 0.74, "max": 1.11, "unit": "백만 달러"}
            }
        }
    
    def generate_html(self) -> str:
        """Chart.js를 사용한 HTML 코드 생성"""
        # 데이터를 JSON 형식으로 변환
        pg_positive_labels = json.dumps([item['title'] for item in self.data['pg_impact']['positive']])
        pg_negative_labels = json.dumps([item['title'] for item in self.data['pg_impact']['negative']])
        fibria_negative_labels = json.dumps([item['title'] for item in self.data['fibria_impact']['negative']])
        fibria_considerations_labels = json.dumps([item['title'] for item in self.data['fibria_impact']['considerations']])
        
        return f"""
        <div class="container mx-auto p-4">
            <h1 class="text-2xl font-bold text-center mb-8">Q2: P&G의 결제 조건 연장이 재무상태에 미치는 영향</h1>
            
            <!-- 결제 조건 변경 -->
            <div class="bg-white rounded-lg p-6 mb-8 shadow-md">
                <h2 class="text-xl font-bold mb-4 text-blue-700">SCF 프로그램 없는 결제 조건 연장의 영향</h2>
                <div class="flex justify-center mb-6">
                    <div class="w-1/2">
                        <canvas id="paymentTermsChart"></canvas>
                    </div>
                </div>
                <p class="text-center">P&G는 공급업체에 대한 지급을 평균 30일 연장함으로써<br />약 40억 달러의 현금을 30일 더 보유할 수 있게 됨</p>
            </div>
            
            <!-- P&G 영향 -->
            <div class="bg-white rounded-lg p-6 mb-8 shadow-md">
                <h2 class="text-xl font-bold mb-4 text-blue-700">P&G에 미치는 영향</h2>
                <div class="flex">
                    <div class="w-1/2 pr-4">
                        <canvas id="pgPositiveImpactChart"></canvas>
                    </div>
                    <div class="w-1/2 pl-4">
                        <canvas id="pgNegativeImpactChart"></canvas>
                    </div>
                </div>
            </div>
            
            <!-- Fibria 영향 -->
            <div class="bg-white rounded-lg p-6 mb-8 shadow-md">
                <h2 class="text-xl font-bold mb-4 text-blue-700">Fibria에 미치는 영향</h2>
                <div class="flex">
                    <div class="w-1/2 pr-4">
                        <canvas id="fibriaNegativeImpactChart"></canvas>
                    </div>
                    <div class="w-1/2 pl-4">
                        <canvas id="fibriaConsiderationsChart"></canvas>
                    </div>
                </div>
            </div>
            
            <!-- 이자비용 비교 -->
            <div class="bg-white rounded-lg p-6 mb-8 shadow-md">
                <h2 class="text-xl font-bold mb-4 text-blue-700">이자비용 차이의 불균형</h2>
                <div class="flex justify-center">
                    <div class="w-4/5">
                        <canvas id="interestCostComparisonChart"></canvas>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script>
            // 결제 조건 차트
            const paymentTermsCtx = document.getElementById('paymentTermsChart').getContext('2d');
            new Chart(paymentTermsCtx, {{
                type: 'bar',
                data: {{
                    labels: ['기존', '변경'],
                    datasets: [{{
                        label: '결제 기간 (일)',
                        data: [{self.data['payment_terms']['before']}, {self.data['payment_terms']['after']}],
                        backgroundColor: ['rgba(54, 162, 235, 0.5)', 'rgba(255, 99, 132, 0.5)'],
                        borderColor: ['rgba(54, 162, 235, 1)', 'rgba(255, 99, 132, 1)'],
                        borderWidth: 1
                    }}]
                }},
                options: {{
                    responsive: true,
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            title: {{
                                display: true,
                                text: '일'
                            }}
                        }}
                    }}
                }}
            }});

            // P&G 긍정적 영향 차트
            const pgPositiveCtx = document.getElementById('pgPositiveImpactChart').getContext('2d');
            new Chart(pgPositiveCtx, {{
                type: 'radar',
                data: {{
                    labels: {pg_positive_labels},
                    datasets: [{{
                        label: '긍정적 영향',
                        data: [100, 100, 100, 100],
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgba(75, 192, 192, 1)'
                    }}]
                }},
                options: {{
                    responsive: true,
                    scales: {{
                        r: {{
                            beginAtZero: true,
                            max: 100
                        }}
                    }}
                }}
            }});

            // P&G 부정적 영향 차트
            const pgNegativeCtx = document.getElementById('pgNegativeImpactChart').getContext('2d');
            new Chart(pgNegativeCtx, {{
                type: 'radar',
                data: {{
                    labels: {pg_negative_labels},
                    datasets: [{{
                        label: '부정적 영향',
                        data: [80, 80, 80, 80],
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        pointBackgroundColor: 'rgba(255, 99, 132, 1)',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: 'rgba(255, 99, 132, 1)'
                    }}]
                }},
                options: {{
                    responsive: true,
                    scales: {{
                        r: {{
                            beginAtZero: true,
                            max: 100
                        }}
                    }}
                }}
            }});

            // Fibria 부정적 영향 차트
            const fibriaNegativeCtx = document.getElementById('fibriaNegativeImpactChart').getContext('2d');
            new Chart(fibriaNegativeCtx, {{
                type: 'bar',
                data: {{
                    labels: {fibria_negative_labels},
                    datasets: [{{
                        label: '부정적 영향',
                        data: [100, 100, 100, 100, 100],
                        backgroundColor: 'rgba(255, 99, 132, 0.5)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }}]
                }},
                options: {{
                    responsive: true,
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            max: 100
                        }}
                    }}
                }}
            }});

            // Fibria 고려사항 차트
            const fibriaConsiderationsCtx = document.getElementById('fibriaConsiderationsChart').getContext('2d');
            new Chart(fibriaConsiderationsCtx, {{
                type: 'doughnut',
                data: {{
                    labels: {fibria_considerations_labels},
                    datasets: [{{
                        data: [25, 25, 25, 25],
                        backgroundColor: [
                            'rgba(255, 206, 86, 0.5)',
                            'rgba(75, 192, 192, 0.5)',
                            'rgba(153, 102, 255, 0.5)',
                            'rgba(255, 159, 64, 0.5)'
                        ],
                        borderColor: [
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                            'rgba(153, 102, 255, 1)',
                            'rgba(255, 159, 64, 1)'
                        ],
                        borderWidth: 1
                    }}]
                }},
                options: {{
                    responsive: true
                }}
            }});

            // 이자비용 비교 차트
            const interestCostCtx = document.getElementById('interestCostComparisonChart').getContext('2d');
            new Chart(interestCostCtx, {{
                type: 'bar',
                data: {{
                    labels: ['P&G 이자 절감', 'Fibria 이자 부담'],
                    datasets: [{{
                        label: '연간 이자비용 (백만 달러)',
                        data: [
                            {self.data['interest_cost_comparison']['pg_savings']['max']},
                            {self.data['interest_cost_comparison']['fibria_cost']['max']}
                        ],
                        backgroundColor: [
                            'rgba(75, 192, 192, 0.5)',
                            'rgba(255, 99, 132, 0.5)'
                        ],
                        borderColor: [
                            'rgba(75, 192, 192, 1)',
                            'rgba(255, 99, 132, 1)'
                        ],
                        borderWidth: 1
                    }}]
                }},
                options: {{
                    responsive: true,
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            title: {{
                                display: true,
                                text: '백만 달러/년'
                            }}
                        }}
                    }}
                }}
            }});
        </script>
        """ 