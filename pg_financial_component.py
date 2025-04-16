import json
from data_provider import MarketDataProvider

class PGFinancialComponentGenerator:
    """P&G 재무 데이터용 Chart.js 컴포넌트 생성 클래스"""
    
    def __init__(self, data_provider: MarketDataProvider):
        """
        Args:
            data_provider: 시장 데이터를 제공하는 객체
        """
        self.data_provider = data_provider
    
    def generate_html(self) -> str:
        """Chart.js 컴포넌트를 포함한 HTML 코드를 생성하여 반환"""
        html_template = self._get_html_template()
        pg_financial_data = self.data_provider.pg_financial_data
        
        # 데이터를 JSON 문자열로 변환하여 삽입
        try:
            json_data = json.dumps(pg_financial_data, ensure_ascii=False)
        except Exception as e:
            print(f"JSON 직렬화 오류: {e}")
            json_data = "[]"
        
        # 데이터 플레이스홀더 치환
        html_template = html_template.replace("PG_FINANCIAL_DATA_PLACEHOLDER", json_data)
        
        return html_template
    
    def _get_html_template(self) -> str:
        """HTML 템플릿 반환"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>P&G 재무 지표 시각화</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Chart.js 라이브러리 로드 -->
            <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.0/dist/chart.min.js"></script>
            <style>
                body {
                    font-family: 'Noto Sans KR', Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f8f9fa;
                }
                .chart-container {
                    background-color: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                    margin-bottom: 30px;
                }
                .chart-title {
                    color: #003366;
                    font-size: 22px;
                    font-weight: 700;
                    text-align: center;
                    margin-bottom: 20px;
                    border-bottom: 2px solid #e0e0e0;
                    padding-bottom: 10px;
                }
                .chart-subtitle {
                    color: #0066cc;
                    font-size: 18px;
                    font-weight: 600;
                    text-align: center;
                    margin-bottom: 15px;
                }
                .chart-note {
                    text-align: center;
                    font-size: 14px;
                    color: #666;
                    font-style: italic;
                    margin-top: 10px;
                }
                .grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 25px;
                }
                .insight-box {
                    background-color: #f0f4f8;
                    border-radius: 8px;
                    border-left: 4px solid #0066cc;
                    padding: 15px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                }
                .insight-title {
                    font-weight: bold;
                    color: #003366;
                    font-size: 17px;
                    margin-bottom: 10px;
                }
                .insight-content {
                    font-size: 15px;
                    line-height: 1.5;
                }
                .note {
                    font-size: 14px;
                    color: #666;
                    font-style: italic;
                    margin-top: 5px;
                }
                .strategy-box {
                    background-color: #fff8e1;
                    border-radius: 8px;
                    border-left: 4px solid #f9a825;
                    padding: 20px;
                    margin-top: 25px;
                }
                .strategy-title {
                    font-weight: bold;
                    color: #e65100;
                    font-size: 18px;
                    margin-bottom: 15px;
                    text-align: center;
                }
                ul.strategy-list {
                    margin: 0;
                    padding-left: 20px;
                }
                ul.strategy-list li {
                    margin-bottom: 10px;
                    font-size: 15px;
                    line-height: 1.5;
                }
                ul.strategy-list li strong {
                    color: #e65100;
                }
                .timeline-container {
                    background-color: #f5f5f5;
                    border-radius: 8px;
                    padding: 20px;
                    margin-top: 30px;
                }
                .timeline-title {
                    font-weight: bold;
                    color: #333;
                    font-size: 18px;
                    margin-bottom: 15px;
                    text-align: center;
                }
                .timeline-event {
                    background-color: #e3f2fd;
                    border-radius: 6px;
                    padding: 10px 15px;
                    display: inline-block;
                    margin: 0 auto;
                    text-align: center;
                    font-weight: bold;
                    color: #0d47a1;
                }
                .effect-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 15px;
                    margin-top: 20px;
                }
                .effect-box {
                    background-color: white;
                    border-radius: 6px;
                    padding: 15px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                }
                .effect-title {
                    font-weight: bold;
                    color: #333;
                    margin-bottom: 10px;
                }
                @media (max-width: 768px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }
                    .effect-grid {
                        grid-template-columns: 1fr;
                    }
                }
            </style>
        </head>
        <body>
            <div id="root">
                <!-- 메인 타이틀 -->
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="color: #003366; font-size: 28px; font-weight: 700;">P&G 재무 지표 시각화 (2011-2015)</h1>
                </div>
                
                <!-- 차트 컨테이너 1: 주요 재무 지표 추이 -->
                <div class="chart-container">
                    <div class="chart-title">1. 주요 재무 지표 추이 (단위: 백만 달러)</div>
                    <div style="height: 500px; width: 100%;">
                        <canvas id="financialMetricsChart"></canvas>
                    </div>
                    <div class="chart-note">
                        * 2015년 순이익 급감은 베네수엘라 사업 회계방식 변경으로 인한 21억 달러 일회성 비용 때문
                    </div>
                </div>
                
                <!-- 차트 컨테이너 2: 수익성 비율 추이 -->
                <div class="chart-container">
                    <div class="chart-title">2. 수익성 비율 추이 (%)</div>
                    <div style="height: 500px; width: 100%;">
                        <canvas id="profitabilityRatiosChart"></canvas>
                    </div>
                    <div class="chart-note">
                        * 2015년 순이익률 하락은 일회성 비용 때문이며, 매출총이익률과 영업이익률은 비교적 안정적으로 유지됨
                    </div>
                </div>
                
                <!-- 차트 컨테이너 3: 임직원 수 추이 -->
                <div class="chart-container">
                    <div class="chart-title">3. 임직원 수 및 매출 추이</div>
                    <div style="height: 450px; width: 100%;">
                        <canvas id="employeesChart"></canvas>
                    </div>
                    <div class="chart-note">
                        * 2011-2015년 사이 임직원 수 15% 감소 (129,000명 → 110,000명)
                    </div>
                </div>

                <!-- 차트 컨테이너 4: 주주 가치 지표 -->
                <div class="chart-container">
                    <div class="chart-title">4. 주주 가치 지표</div>
                    <div style="height: 450px; width: 100%;">
                        <canvas id="shareholderValueChart"></canvas>
                    </div>
                    <div class="chart-note">
                        * 순이익 감소에도 불구하고 배당금은 꾸준히 증가 (주주 가치 유지 노력)
                    </div>
                </div>
                
                <!-- 차트 컨테이너 5: 주요 인사이트 -->
                <div class="chart-container">
                    <div class="chart-title">5. 주요 인사이트</div>
                    <div class="grid">
                        <div class="insight-box">
                            <div class="insight-title">매출 정체 및 하락</div>
                            <div class="insight-content">2012년 이후 매출 성장이 정체되고 2015년에는 5.3% 감소</div>
                            <div class="note">→ 비용 절감 및 운전자본 최적화 필요성 증가</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">안정적인 이익률</div>
                            <div class="insight-content">영업이익률은 17-19% 대를 안정적으로 유지</div>
                            <div class="note">→ AA- 신용등급 유지에 기여</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">2015년 순이익 급감</div>
                            <div class="insight-content">순이익이 70억 달러로 감소 (전년 대비 -40%)</div>
                            <div class="note">→ 운전자본 관리의 중요성 부각</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">현금흐름 관리 필요성</div>
                            <div class="insight-content">매출의 약 80%가 비용 관련 (COGS + SG&A)</div>
                            <div class="note">→ 공급망 금융으로 현금흐름 개선 가능</div>
                        </div>
                    </div>
                </div>
                
                <!-- 차트 컨테이너 6: SCF 프로그램의 전략적 중요성 -->
                <div class="chart-container">
                    <div class="chart-title">6. SCF 프로그램의 전략적 중요성</div>
                    <div class="strategy-box">
                        <div class="strategy-title">P&G의 SCF 프로그램 추진 필요성</div>
                        <ul class="strategy-list">
                            <li><strong>운전자본 최적화</strong>: 매출 하락 시기에 현금흐름 확보 필수</li>
                            <li><strong>신용등급 활용</strong>: AA- 등급으로 SCF 프로그램 유리하게 구축</li>
                            <li><strong>공급업체 관계 유지</strong>: 결제기간 연장에도 조기지불 옵션 제공</li>
                            <li><strong>자본 효율성</strong>: 손익계산서에 영향 없이 현금흐름 개선</li>
                            <li><strong>산업 리더십</strong>: 경쟁사 대비 혁신적인 공급망 금융 접근법</li>
                        </ul>
                    </div>
                </div>
                
                <!-- 차트 컨테이너 7: SCF 프로그램 도입 시점 및 효과 -->
                <div class="chart-container">
                    <div class="chart-title">7. SCF 프로그램 도입 및 효과</div>
                    <div class="timeline-container">
                        <div style="text-align: center; margin-bottom: 20px;">
                            <div class="timeline-event">2013년 4월: P&G SCF 프로그램 도입 시점</div>
                        </div>
                        
                        <div class="timeline-title">주요 재무적 효과</div>
                        <div class="effect-grid">
                            <div class="effect-box">
                                <div class="effect-title">단기 효과</div>
                                <ul>
                                    <li>손익계산서에는 직접적인 영향이 즉시 나타나지 않음</li>
                                    <li>공급업체 지불 조건: 45일 → 75일 연장</li>
                                    <li>운전자본 개선 및 현금흐름 효율화</li>
                                </ul>
                            </div>
                            <div class="effect-box">
                                <div class="effect-title">장기 효과</div>
                                <ul>
                                    <li>공급업체 관계 강화 (윈-윈-윈 솔루션)</li>
                                    <li>운영 효율성 개선 (인보이스 처리 등)</li>
                                    <li>공급망 안정성 및 지속가능성 개선</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
                // JSON 데이터 파싱
                const pgFinancialData = PG_FINANCIAL_DATA_PLACEHOLDER;
                
                // Canvas 요소 가져오기
                const financialMetricsCtx = document.getElementById('financialMetricsChart').getContext('2d');
                const profitabilityRatiosCtx = document.getElementById('profitabilityRatiosChart').getContext('2d');
                const employeesCtx = document.getElementById('employeesChart').getContext('2d');
                const shareholderValueCtx = document.getElementById('shareholderValueChart').getContext('2d');
                
                // 데이터 추출
                const years = pgFinancialData.map(item => item.year);
                const revenues = pgFinancialData.map(item => item.revenue);
                const grossProfits = pgFinancialData.map(item => item.grossProfit);
                const operatingIncomes = pgFinancialData.map(item => item.operatingIncome);
                const netIncomes = pgFinancialData.map(item => item.netIncome);
                
                const grossMargins = pgFinancialData.map(item => item.grossMargin);
                const operatingMargins = pgFinancialData.map(item => item.operatingMargin);
                const netMargins = pgFinancialData.map(item => item.netMargin);
                
                const employees = pgFinancialData.map(item => item.employees);
                const eps = pgFinancialData.map(item => item.eps);
                const dividends = pgFinancialData.map(item => item.dividend);
                
                // 금액 포맷팅 함수
                function formatCurrency(value) {
                    if (value >= 1000) {
                        return (value / 1000).toFixed(1) + '십억';
                    }
                    return value;
                }
                
                // 1. 주요 재무 지표 차트
                new Chart(financialMetricsCtx, {
                    type: 'bar',
                    data: {
                        labels: years,
                        datasets: [
                            {
                                label: '매출',
                                data: revenues,
                                backgroundColor: 'rgba(54, 162, 235, 0.7)',
                                borderColor: 'rgba(54, 162, 235, 1)',
                                borderWidth: 1
                            },
                            {
                                label: '매출총이익',
                                data: grossProfits,
                                backgroundColor: 'rgba(75, 192, 192, 0.7)',
                                borderColor: 'rgba(75, 192, 192, 1)',
                                borderWidth: 1
                            },
                            {
                                label: '영업이익',
                                data: operatingIncomes,
                                backgroundColor: 'rgba(255, 159, 64, 0.7)',
                                borderColor: 'rgba(255, 159, 64, 1)',
                                borderWidth: 1
                            },
                            {
                                label: '당기순이익',
                                data: netIncomes,
                                backgroundColor: 'rgba(153, 102, 255, 0.7)',
                                borderColor: 'rgba(153, 102, 255, 1)',
                                borderWidth: 1
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'top',
                                labels: {
                                    font: {
                                        size: 14
                                    }
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        label += '$' + context.raw.toLocaleString() + ' 백만';
                                        return label;
                                    }
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: {
                                    display: false
                                },
                                title: {
                                    display: true,
                                    text: '연도',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                }
                            },
                            y: {
                                beginAtZero: true,
                                title: {
                                    display: true,
                                    text: '금액 (백만 달러)',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                },
                                ticks: {
                                    callback: function(value) {
                                        return formatCurrency(value);
                                    }
                                }
                            }
                        }
                    }
                });
                
                // 2. 수익성 비율 차트
                new Chart(profitabilityRatiosCtx, {
                    type: 'line',
                    data: {
                        labels: years,
                        datasets: [
                            {
                                label: '매출총이익률',
                                data: grossMargins,
                                borderColor: 'rgba(54, 162, 235, 1)',
                                backgroundColor: 'rgba(54, 162, 235, 0.1)',
                                borderWidth: 3,
                                pointRadius: 6,
                                pointHoverRadius: 8,
                                tension: 0.1,
                                fill: false
                            },
                            {
                                label: '영업이익률',
                                data: operatingMargins,
                                borderColor: 'rgba(75, 192, 192, 1)',
                                backgroundColor: 'rgba(75, 192, 192, 0.1)',
                                borderWidth: 3,
                                pointRadius: 6,
                                pointHoverRadius: 8,
                                tension: 0.1,
                                fill: false
                            },
                            {
                                label: '순이익률',
                                data: netMargins,
                                borderColor: 'rgba(255, 99, 132, 1)',
                                backgroundColor: 'rgba(255, 99, 132, 0.1)',
                                borderWidth: 3,
                                pointRadius: 6,
                                pointHoverRadius: 8,
                                tension: 0.1,
                                fill: false
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'top',
                                labels: {
                                    font: {
                                        size: 14
                                    }
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        label += context.raw.toFixed(1) + '%';
                                        return label;
                                    }
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: {
                                    display: false
                                },
                                title: {
                                    display: true,
                                    text: '연도',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                }
                            },
                            y: {
                                min: 0,
                                max: 60,
                                title: {
                                    display: true,
                                    text: '비율 (%)',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                },
                                ticks: {
                                    callback: function(value) {
                                        return value + '%';
                                    }
                                }
                            }
                        }
                    }
                });
                
                // 3. 임직원 수 차트
                new Chart(employeesCtx, {
                    type: 'line',
                    data: {
                        labels: years,
                        datasets: [
                            {
                                type: 'bar',
                                label: '매출',
                                data: revenues,
                                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                                borderColor: 'rgba(54, 162, 235, 1)',
                                borderWidth: 1,
                                yAxisID: 'revenue'
                            },
                            {
                                type: 'line',
                                label: '임직원 수',
                                data: employees,
                                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                                borderColor: 'rgba(153, 102, 255, 1)',
                                borderWidth: 3,
                                pointRadius: 6,
                                pointHoverRadius: 8,
                                tension: 0.1,
                                fill: false,
                                yAxisID: 'employees'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'top',
                                labels: {
                                    font: {
                                        size: 14
                                    }
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        if (context.dataset.label === '임직원 수') {
                                            label += context.raw.toLocaleString() + '명';
                                        } else {
                                            label += '$' + context.raw.toLocaleString() + ' 백만';
                                        }
                                        return label;
                                    }
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: {
                                    display: false
                                },
                                title: {
                                    display: true,
                                    text: '연도',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                }
                            },
                            revenue: {
                                type: 'linear',
                                position: 'left',
                                title: {
                                    display: true,
                                    text: '매출 (백만 달러)',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                },
                                grid: {
                                    display: false
                                },
                                ticks: {
                                    callback: function(value) {
                                        return formatCurrency(value);
                                    }
                                }
                            },
                            employees: {
                                type: 'linear',
                                position: 'right',
                                title: {
                                    display: true,
                                    text: '임직원 수 (명)',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                },
                                min: 100000,
                                max: 140000,
                                ticks: {
                                    callback: function(value) {
                                        return value.toLocaleString() + '명';
                                    }
                                }
                            }
                        }
                    }
                });
                
                // 4. 주주 가치 지표 차트
                new Chart(shareholderValueCtx, {
                    type: 'bar',
                    data: {
                        labels: years,
                        datasets: [
                            {
                                type: 'bar',
                                label: '주당순이익(EPS)',
                                data: eps,
                                backgroundColor: 'rgba(255, 159, 64, 0.7)',
                                borderColor: 'rgba(255, 159, 64, 1)',
                                borderWidth: 1,
                                yAxisID: 'eps'
                            },
                            {
                                type: 'line',
                                label: '주당배당금(DPS)',
                                data: dividends,
                                backgroundColor: 'rgba(255, 99, 132, 0.1)',
                                borderColor: 'rgba(255, 99, 132, 1)',
                                borderWidth: 3,
                                pointRadius: 6,
                                pointHoverRadius: 8,
                                tension: 0.1,
                                fill: false,
                                yAxisID: 'dps'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'top',
                                labels: {
                                    font: {
                                        size: 14
                                    }
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        label += '$' + context.raw.toFixed(2);
                                        return label;
                                    }
                                }
                            }
                        },
                        scales: {
                            x: {
                                grid: {
                                    display: false
                                },
                                title: {
                                    display: true,
                                    text: '연도',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                }
                            },
                            eps: {
                                type: 'linear',
                                position: 'left',
                                title: {
                                    display: true,
                                    text: '주당순이익 ($)',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                },
                                min: 0,
                                max: 5,
                                ticks: {
                                    callback: function(value) {
                                        return '$' + value.toFixed(2);
                                    }
                                }
                            },
                            dps: {
                                type: 'linear',
                                position: 'right',
                                title: {
                                    display: true,
                                    text: '주당배당금 ($)',
                                    font: {
                                        size: 14,
                                        weight: 'bold'
                                    }
                                },
                                min: 1.5,
                                max: 3,
                                grid: {
                                    display: false
                                },
                                ticks: {
                                    callback: function(value) {
                                        return '$' + value.toFixed(2);
                                    }
                                }
                            }
                        }
                    }
                });
            </script>
        </body>
        </html>
        """ 