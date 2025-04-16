import json
from data_provider import MarketDataProvider

class FibriaFinancialComponentGenerator:
    """피브리아 재무 분석을 위한 Chart.js HTML 컴포넌트를 생성하는 클래스"""
    
    def __init__(self, data_provider: MarketDataProvider):
        """
        Args:
            data_provider: 데이터를 제공하는 객체
        """
        self.data_provider = data_provider
    
    def generate_html(self) -> str:
        """Chart.js를 사용한 HTML 코드를 생성하여 반환"""
        html_template = self._get_html_template()
        
        # 데이터 딕셔너리 생성
        data_dict = {
            'fibriaFinancialData': self.data_provider.fibria_financial_data,
            'fibriaSCFImpactData': self.data_provider.fibria_scf_impact_data,
            'fibriaMarketData': self.data_provider.fibria_market_data
        }
        
        # JSON 데이터를 HTML에 삽입
        for key, value in data_dict.items():
            placeholder = f"{key.upper()}_PLACEHOLDER"
            
            try:
                json_data = json.dumps(value, ensure_ascii=False)
            except Exception as e:
                print(f"JSON 직렬화 오류 ({key}): {e}")
                json_data = "[]"
            
            if placeholder in html_template:
                html_template = html_template.replace(placeholder, json_data)
                print(f"플레이스홀더 {placeholder} 치환 완료")
            else:
                print(f"경고: 플레이스홀더 {placeholder}를 찾을 수 없음")
        
        return html_template
    
    def _get_html_template(self) -> str:
        """Fibria 재무 분석 HTML 템플릿 반환"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>피브리아 셀룰로즈 재무 분석</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Chart.js 라이브러리 로드 -->
            <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.0/dist/chart.min.js"></script>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .chart-container {
                    margin-bottom: 30px;
                }
                .chart-title {
                    font-size: 18px;
                    font-weight: bold;
                    text-align: center;
                    margin-bottom: 10px;
                }
                .grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                }
                .insight-box {
                    background-color: #f0f4f8;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 20px;
                }
                .insight-title {
                    font-weight: bold;
                    color: #2c5282;
                    margin-bottom: 5px;
                }
                .warning-box {
                    background-color: #fff8e1;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 20px;
                }
                .success-box {
                    background-color: #e6f4ea;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 20px;
                }
                .section-title {
                    font-size: 24px;
                    font-weight: bold;
                    text-align: center;
                    color: #2c5282;
                    margin: 20px 0;
                }
                ul {
                    margin-top: 5px;
                }
                @media (max-width: 768px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }
                }
            </style>
        </head>
        <body>
            <div style="padding: 20px;">
                <h2 class="section-title">피브리아 셀룰로즈 재무 분석 (2012-2015)</h2>
                
                <!-- 매출 및 이익 추이 -->
                <div class="chart-container">
                    <div class="chart-title">1. 매출 및 이익 추이 (단위: 백만 레알)</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="incomeChart"></canvas>
                    </div>
                </div>

                <!-- 수익성 비율 -->
                <div class="chart-container">
                    <div class="chart-title">2. 수익성 비율 추이 (%)</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="marginsChart"></canvas>
                    </div>
                </div>

                <!-- 환율 및 펄프 가격 추이 -->
                <div class="chart-container">
                    <div class="chart-title">3. 환율 및 펄프 가격 추이</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="marketDataChart"></canvas>
                    </div>
                </div>

                <!-- SCF 프로그램 영향 분석 -->
                <div class="chart-container">
                    <div class="chart-title">4. SCF 프로그램 영향 분석 (단위: 백만 달러)</div>
                    <div class="grid">
                        <div>
                            <div style="height: 300px;">
                                <canvas id="financingCostChart"></canvas>
                            </div>
                        </div>
                        <div>
                            <div style="height: 300px;">
                                <canvas id="annualSavingsChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 핵심 인사이트 요약 -->
                <div class="insight-box">
                    <h3 class="section-title">핵심 인사이트</h3>
                    <div class="grid">
                        <div class="insight-box">
                            <div class="insight-title">사업 성과의 양면성</div>
                            <p>2012-2015년 영업이익 크게 개선 (345 → 1698백만 레알)</p>
                            <p style="font-size: 0.9em; color: #666;">→ 하지만 환율 손실로 당기순이익은 변동성 큼</p>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">환율 영향</div>
                            <p>레알/달러 환율 상승 (1.96 → 2.60)</p>
                            <p style="font-size: 0.9em; color: #666;">→ 달러 매출에 유리하나 달러 부채에 불리</p>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">수익성 개선</div>
                            <p>매출총이익률 15.2% → 31.0%로 크게 상승</p>
                            <p style="font-size: 0.9em; color: #666;">→ 운영 효율성 향상 및 펄프 가격 상승 효과</p>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">SCF 프로그램 효과</div>
                            <p>연간 약 120백만 달러 자금조달 비용 절감</p>
                            <p style="font-size: 0.9em; color: #666;">→ 현금흐름 개선 및 유동성 강화</p>
                        </div>
                    </div>
                </div>

                <!-- SCF 프로그램의 전략적 의미 -->
                <div class="warning-box">
                    <h3 class="section-title">피브리아에 대한 SCF 프로그램의 전략적 의미</h3>
                    <ul style="list-style-type: disc; padding-left: 20px;">
                        <li><span style="font-weight: bold;">높은 부채 비용 절감</span>: 일반 기업 대출(2-3%) 대비 훨씬 낮은 0.35% 할인율로 자금조달 가능</li>
                        <li><span style="font-weight: bold;">환율 변동성 대응</span>: 달러 표시 매출채권의 빠른 현금화로 환율 리스크 감소</li>
                        <li><span style="font-weight: bold;">신용등급 상승 지원</span>: 유동성 개선이 신용등급 향상에 기여 (BB → BBB-)</li>
                        <li><span style="font-weight: bold;">현금전환주기 단축</span>: 매출채권 회수 기간 60일→15일로 단축</li>
                        <li><span style="font-weight: bold;">글로벌 은행과의 관계 강화</span>: 시티그룹과의 거래 관계 심화</li>
                    </ul>
                </div>

                <!-- 주요 도전 과제 -->
                <div class="success-box">
                    <h3 class="section-title">피브리아의 주요 도전 과제</h3>
                    <ul style="list-style-type: disc; padding-left: 20px;">
                        <li><span style="font-weight: bold;">환율 리스크</span>: 레알화 약세로 달러 표시 부채 부담 증가</li>
                        <li><span style="font-weight: bold;">변동성 높은 순이익</span>: 견고한 영업이익에도 불구하고 환율 손실로 인한 순이익 변동성</li>
                        <li><span style="font-weight: bold;">유동성 관리</span>: 2008년 금융위기 이후 자금 조달의 어려움 경험</li>
                        <li><span style="font-weight: bold;">장기적 신용 관계</span>: 다양한 은행과의 관계 구축 필요성</li>
                    </ul>
                </div>
            </div>

            <script>
                // 데이터 로드
                const fibriaFinancialData = FIBRIAFINANCIALDATA_PLACEHOLDER;
                const fibriaSCFImpactData = FIBRIASCFIMPACTDATA_PLACEHOLDER;
                const fibriaMarketData = FIBRIAMARKETDATA_PLACEHOLDER;
                
                // 1. 매출 및 이익 차트
                const incomeChartCtx = document.getElementById('incomeChart').getContext('2d');
                new Chart(incomeChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaFinancialData.map(item => item.year),
                        datasets: [
                            {
                                label: '매출',
                                data: fibriaFinancialData.map(item => item.revenue),
                                backgroundColor: '#8884d8',
                                order: 1
                            },
                            {
                                label: '매출총이익',
                                data: fibriaFinancialData.map(item => item.grossProfit),
                                backgroundColor: '#82ca9d',
                                order: 2
                            },
                            {
                                label: '영업이익',
                                data: fibriaFinancialData.map(item => item.operatingIncome),
                                backgroundColor: '#ffc658',
                                order: 3
                            },
                            {
                                label: '당기순이익',
                                data: fibriaFinancialData.map(item => item.netIncome),
                                backgroundColor: '#ff8042',
                                order: 4
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: false,
                                min: -1000,
                                max: 9000,
                                title: {
                                    display: true,
                                    text: '백만 레알'
                                }
                            }
                        },
                        plugins: {
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': R$ ' + context.raw.toLocaleString() + ' 백만';
                                    }
                                }
                            }
                        }
                    }
                });
                
                // 2. 수익성 비율 차트
                const marginsChartCtx = document.getElementById('marginsChart').getContext('2d');
                new Chart(marginsChartCtx, {
                    type: 'line',
                    data: {
                        labels: fibriaFinancialData.map(item => item.year),
                        datasets: [
                            {
                                label: '매출총이익률',
                                data: fibriaFinancialData.map(item => item.grossMargin),
                                borderColor: '#82ca9d',
                                backgroundColor: 'rgba(130, 202, 157, 0.2)',
                                borderWidth: 2,
                                pointRadius: 5,
                                tension: 0.1
                            },
                            {
                                label: '영업이익률',
                                data: fibriaFinancialData.map(item => item.operatingMargin),
                                borderColor: '#ffc658',
                                backgroundColor: 'rgba(255, 198, 88, 0.2)',
                                borderWidth: 2,
                                pointRadius: 5,
                                tension: 0.1
                            },
                            {
                                label: '순이익률',
                                data: fibriaFinancialData.map(item => item.netMargin),
                                borderColor: '#ff8042',
                                backgroundColor: 'rgba(255, 128, 66, 0.2)',
                                borderWidth: 2,
                                pointRadius: 5,
                                tension: 0.1
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                min: -15,
                                max: 35,
                                title: {
                                    display: true,
                                    text: '%'
                                }
                            }
                        },
                        plugins: {
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': ' + context.raw + '%';
                                    }
                                }
                            }
                        }
                    }
                });
                
                // 3. 환율 및 펄프 가격 차트
                const marketDataChartCtx = document.getElementById('marketDataChart').getContext('2d');
                new Chart(marketDataChartCtx, {
                    type: 'line',
                    data: {
                        labels: fibriaMarketData.map(item => item.year),
                        datasets: [
                            {
                                label: '환율(레알/달러)',
                                data: fibriaMarketData.map(item => item.exchangeRate),
                                borderColor: '#8884d8',
                                backgroundColor: 'rgba(136, 132, 216, 0.2)',
                                borderWidth: 2,
                                pointRadius: 5,
                                yAxisID: 'y',
                                tension: 0.1
                            },
                            {
                                label: '펄프 가격(USD/톤)',
                                data: fibriaMarketData.map(item => item.pulpPrice),
                                borderColor: '#82ca9d',
                                backgroundColor: 'rgba(130, 202, 157, 0.2)',
                                borderWidth: 2,
                                pointRadius: 5,
                                yAxisID: 'y1',
                                tension: 0.1
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                type: 'linear',
                                display: true,
                                position: 'left',
                                title: {
                                    display: true,
                                    text: '환율 (레알/달러)'
                                }
                            },
                            y1: {
                                type: 'linear',
                                display: true,
                                position: 'right',
                                min: 700,
                                max: 850,
                                title: {
                                    display: true,
                                    text: 'USD/톤'
                                },
                                grid: {
                                    drawOnChartArea: false
                                }
                            }
                        }
                    }
                });
                
                // 4. 자금조달 비용 비교 차트
                const financingCostChartCtx = document.getElementById('financingCostChart').getContext('2d');
                new Chart(financingCostChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaSCFImpactData.map(item => item.year),
                        datasets: [
                            {
                                label: 'SCF 없음 (2.5% 금리)',
                                data: fibriaSCFImpactData.map(item => item.withoutSCF.financingCost),
                                backgroundColor: '#ff8042'
                            },
                            {
                                label: 'SCF 이용 (0.35% 할인율)',
                                data: fibriaSCFImpactData.map(item => item.withSCF.financingCost),
                                backgroundColor: '#82ca9d'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            title: {
                                display: true,
                                text: '자금조달 비용 비교'
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': $' + context.raw.toFixed(2) + ' 백만';
                                    }
                                }
                            }
                        },
                        scales: {
                            y: {
                                title: {
                                    display: true,
                                    text: '백만 달러'
                                }
                            }
                        }
                    }
                });
                
                // 5. 연간 절감액 차트
                const annualSavingsChartCtx = document.getElementById('annualSavingsChart').getContext('2d');
                // 연간 절감액 계산
                const annualSavingsData = fibriaSCFImpactData.filter(item => item.year !== '2012').map(item => ({
                    year: item.year,
                    savings: item.withoutSCF.financingCost - item.withSCF.financingCost
                }));
                
                new Chart(annualSavingsChartCtx, {
                    type: 'bar',
                    data: {
                        labels: annualSavingsData.map(item => item.year),
                        datasets: [
                            {
                                label: 'SCF 통한 연간 절감액',
                                data: annualSavingsData.map(item => item.savings),
                                backgroundColor: '#8884d8'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            title: {
                                display: true,
                                text: '연간 절감액'
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': $' + context.raw.toFixed(2) + ' 백만';
                                    }
                                }
                            }
                        },
                        scales: {
                            y: {
                                title: {
                                    display: true,
                                    text: '백만 달러'
                                }
                            }
                        }
                    }
                });
            </script>
        </body>
        </html>
        """ 