import json
from data_provider import MarketDataProvider

class FibriaBalanceSheetComponentGenerator:
    """피브리아 대차대조표 분석을 위한 Chart.js HTML 컴포넌트를 생성하는 클래스"""
    
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
            'fibriaBalanceSheetData': self.data_provider.fibria_balance_sheet_data,
            'fibriaWorkingCapitalData': self.data_provider.fibria_working_capital_data,
            'fibriaSCFAnalysisData': self.data_provider.fibria_scf_analysis_data
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
        """Fibria 대차대조표 분석 HTML 템플릿 반환"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Fibria Cellulose Balance Sheet</title>
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
                    list-style-type: disc;
                    padding-left: 20px;
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
                <h2 class="section-title">Fibria Cellulose Balance Sheet (2012-2015)</h2>
                
                <!-- 자산, 부채, 자본 추이 -->
                <div class="chart-container">
                    <div class="chart-title">1. 자산, 부채, 자본 추이 (단위: 백만 레알)</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="balanceSheetChart"></canvas>
                    </div>
                </div>

                <!-- 유동자산 구성 -->
                <div class="chart-container">
                    <div class="chart-title">2. 유동자산 구성 변화 (단위: 백만 레알)</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="currentAssetsChart"></canvas>
                    </div>
                </div>

                <!-- 부채 구성 -->
                <div class="chart-container">
                    <div class="chart-title">3. 부채 구성 변화 (단위: 백만 레알)</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="liabilitiesChart"></canvas>
                    </div>
                </div>

                <!-- 유동성 지표 -->
                <div class="chart-container">
                    <div class="chart-title">4. 유동성 및 부채 지표 추이</div>
                    <div class="grid">
                        <div>
                            <div style="height: 300px;">
                                <canvas id="currentRatioChart"></canvas>
                            </div>
                        </div>
                        <div>
                            <div style="height: 300px;">
                                <canvas id="debtToCapitalChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 운전자본 항목 -->
                <div class="chart-container">
                    <div class="chart-title">5. 운전자본 항목 추이 (단위: 백만 레알)</div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="workingCapitalChart"></canvas>
                    </div>
                </div>

                <!-- SCF 영향 분석 -->
                <div class="chart-container">
                    <div class="chart-title">6. SCF 프로그램 영향 분석 (P&G 거래 기준)</div>
                    <div class="grid">
                        <div>
                            <div style="height: 300px;">
                                <canvas id="daysOutstandingChart"></canvas>
                            </div>
                        </div>
                        <div>
                            <div style="height: 300px;">
                                <canvas id="financingCostChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 핵심 인사이트 요약 -->
                <div class="insight-box">
                    <h3 class="section-title">핵심 인사이트</h3>
                    <div class="grid">
                        <div class="insight-box">
                            <div class="insight-title">유동성 개선</div>
                            <p>2013년 유동비율 1.31에서 2015년 1.85로 개선</p>
                            <p style="font-size: 0.9em; color: #666;">→ SCF 프로그램의 긍정적 영향 확인</p>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">자본 구조 개선</div>
                            <p>부채비율 41.5%에서 38.2%로 감소</p>
                            <p style="font-size: 0.9em; color: #666;">→ 신용등급 개선(BBB-)에 기여</p>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">현금 흐름 변동</div>
                            <p>2014년 현금 급감 후 2015년 다시 증가</p>
                            <p style="font-size: 0.9em; color: #666;">→ 유동성 관리의 중요성 부각</p>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">달러 부채 부담</div>
                            <p>전체 부채의 90% 이상이 달러 표시 부채</p>
                            <p style="font-size: 0.9em; color: #666;">→ 환율 상승시 부채 부담 증가</p>
                        </div>
                    </div>
                </div>

                <!-- SCF 프로그램의 전략적 의미 -->
                <div class="warning-box">
                    <h3 class="section-title">SCF 프로그램의 전략적 의미</h3>
                    <ul>
                        <li><span style="font-weight: bold;">유동성 확보</span>: 매출채권 60일→15일로 단축으로 약 $37백만 빠른 현금 확보</li>
                        <li><span style="font-weight: bold;">이자 비용 절감</span>: 연간 약 $1.5백만의 자금조달 비용 절감</li>
                        <li><span style="font-weight: bold;">대차대조표 개선</span>: 매출채권 감소로 유동비율 개선 및 부채의존도 감소</li>
                        <li><span style="font-weight: bold;">환율 위험 관리</span>: 달러 매출의 빠른 현금화로 환율 변동 위험 완화</li>
                        <li><span style="font-weight: bold;">신용 관계 확대</span>: 시티그룹 외에 JPMorgan Chase와의 관계 구축 기회</li>
                    </ul>
                </div>

                <!-- 의사결정 포인트 -->
                <div class="success-box">
                    <h3 class="section-title">케이스의 의사결정 포인트</h3>
                    <p style="margin-bottom: 10px;">피브리아는 현재 SCF 프로그램을 재검토하고 다음 결정을 내려야 합니다:</p>
                    <div class="grid">
                        <div style="background-color: white; padding: 15px; border-radius: 8px;">
                            <h4 style="font-weight: bold; color: #2a693c; margin-top: 0;">1. 은행 유지 vs. 변경</h4>
                            <p>현재: 시티그룹 (0.35% 할인율)</p>
                            <p>대안: JPMorgan Chase (할인율 미정)</p>
                            <p style="font-size: 0.9em; color: #666;">고려사항: 할인율, 관계 유지, 다양한 은행 관계의 가치</p>
                        </div>
                        <div style="background-color: white; padding: 15px; border-radius: 8px;">
                            <h4 style="font-weight: bold; color: #2a693c; margin-top: 0;">2. 계약 조건 재협상</h4>
                            <p>현재 시장 환경: LIBOR 하락 (Exhibit 8)</p>
                            <p>가능성: 더 낮은 할인율 협상</p>
                            <p style="font-size: 0.9em; color: #666;">고려사항: 시장 금리, P&G와의 관계, 장기적 파트너십</p>
                        </div>
                    </div>
                </div>
            </div>

            <script>
                // 데이터 로드
                const fibriaBalanceSheetData = FIBRIABALANCESHEETDATA_PLACEHOLDER;
                const fibriaWorkingCapitalData = FIBRIAWORKINGCAPITALDATA_PLACEHOLDER;
                const fibriaSCFAnalysisData = FIBRIASCFANALYSISDATA_PLACEHOLDER;
                
                // 1. 자산, 부채, 자본 추이 차트
                const balanceSheetChartCtx = document.getElementById('balanceSheetChart').getContext('2d');
                new Chart(balanceSheetChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaBalanceSheetData.map(item => item.year),
                        datasets: [
                            {
                                label: '총자산',
                                data: fibriaBalanceSheetData.map(item => item.totalAssets),
                                backgroundColor: '#8884d8'
                            },
                            {
                                label: '총부채',
                                data: fibriaBalanceSheetData.map(item => item.totalLiabilities),
                                backgroundColor: '#ff8042'
                            },
                            {
                                label: '자본',
                                data: fibriaBalanceSheetData.map(item => item.totalEquity),
                                backgroundColor: '#82ca9d'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                beginAtZero: true,
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
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 2. 유동자산 구성 차트
                const currentAssetsChartCtx = document.getElementById('currentAssetsChart').getContext('2d');
                new Chart(currentAssetsChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaBalanceSheetData.map(item => item.year),
                        datasets: [
                            {
                                label: '현금 및 단기투자',
                                data: fibriaBalanceSheetData.map(item => item.cash),
                                backgroundColor: '#8884d8',
                                stack: 'Stack 0'
                            },
                            {
                                label: '매출채권',
                                data: fibriaBalanceSheetData.map(item => item.accountsReceivable),
                                backgroundColor: '#82ca9d',
                                stack: 'Stack 0'
                            },
                            {
                                label: '재고자산',
                                data: fibriaBalanceSheetData.map(item => item.inventory),
                                backgroundColor: '#ffc658',
                                stack: 'Stack 0'
                            },
                            {
                                label: '기타유동자산',
                                data: fibriaBalanceSheetData.map(item => item.otherCurrentAssets),
                                backgroundColor: '#ff8042',
                                stack: 'Stack 0'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                stacked: true,
                                title: {
                                    display: true,
                                    text: '백만 레알'
                                }
                            },
                            x: {
                                stacked: true
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
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 3. 부채 구성 차트
                const liabilitiesChartCtx = document.getElementById('liabilitiesChart').getContext('2d');
                new Chart(liabilitiesChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaBalanceSheetData.map(item => item.year),
                        datasets: [
                            {
                                label: '매입채무',
                                data: fibriaBalanceSheetData.map(item => item.accountsPayable),
                                backgroundColor: '#8884d8',
                                stack: 'Stack 0'
                            },
                            {
                                label: '단기차입금',
                                data: fibriaBalanceSheetData.map(item => item.shortTermDebt),
                                backgroundColor: '#82ca9d',
                                stack: 'Stack 0'
                            },
                            {
                                label: '기타유동부채',
                                data: fibriaBalanceSheetData.map(item => item.otherCurrentLiabilities),
                                backgroundColor: '#ffc658',
                                stack: 'Stack 0'
                            },
                            {
                                label: '장기차입금',
                                data: fibriaBalanceSheetData.map(item => item.longTermDebt),
                                backgroundColor: '#ff8042',
                                stack: 'Stack 0'
                            },
                            {
                                label: '기타비유동부채',
                                data: fibriaBalanceSheetData.map(item => item.otherLTLiabilities),
                                backgroundColor: '#0088FE',
                                stack: 'Stack 0'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                stacked: true,
                                title: {
                                    display: true,
                                    text: '백만 레알'
                                }
                            },
                            x: {
                                stacked: true
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
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 4-1. 유동비율 차트
                const currentRatioChartCtx = document.getElementById('currentRatioChart').getContext('2d');
                new Chart(currentRatioChartCtx, {
                    type: 'line',
                    data: {
                        labels: fibriaBalanceSheetData.map(item => item.year),
                        datasets: [
                            {
                                label: '유동비율',
                                data: fibriaBalanceSheetData.map(item => item.currentRatio),
                                borderColor: '#8884d8',
                                backgroundColor: 'rgba(136, 132, 216, 0.2)',
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
                                min: 0,
                                max: 3,
                                title: {
                                    display: true,
                                    text: '배'
                                }
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: '유동비율'
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': ' + context.raw.toFixed(2) + '배';
                                    }
                                }
                            }
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 4-2. 부채비율 차트
                const debtToCapitalChartCtx = document.getElementById('debtToCapitalChart').getContext('2d');
                new Chart(debtToCapitalChartCtx, {
                    type: 'line',
                    data: {
                        labels: fibriaBalanceSheetData.map(item => item.year),
                        datasets: [
                            {
                                label: '부채비율',
                                data: fibriaBalanceSheetData.map(item => item.debtToCapital),
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
                                min: 30,
                                max: 45,
                                title: {
                                    display: true,
                                    text: '%'
                                }
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: '부채비율'
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': ' + context.raw.toFixed(1) + '%';
                                    }
                                }
                            }
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 5. 운전자본 항목 차트
                const workingCapitalChartCtx = document.getElementById('workingCapitalChart').getContext('2d');
                new Chart(workingCapitalChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaWorkingCapitalData.map(item => item.year),
                        datasets: [
                            {
                                label: '매출채권',
                                data: fibriaWorkingCapitalData.map(item => item.accountsReceivable),
                                backgroundColor: '#82ca9d'
                            },
                            {
                                label: '재고자산',
                                data: fibriaWorkingCapitalData.map(item => item.inventory),
                                backgroundColor: '#ffc658'
                            },
                            {
                                label: '매입채무',
                                data: fibriaWorkingCapitalData.map(item => item.accountsPayable),
                                backgroundColor: '#8884d8'
                            },
                            {
                                label: '순운전자본',
                                data: fibriaWorkingCapitalData.map(item => item.netWorkingCapital),
                                backgroundColor: '#ff8042'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
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
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 6-1. 매출채권 회수 기간 차트
                const daysOutstandingChartCtx = document.getElementById('daysOutstandingChart').getContext('2d');
                new Chart(daysOutstandingChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaSCFAnalysisData.map(item => item.category),
                        datasets: [
                            {
                                label: '매출채권 회수 기간',
                                data: fibriaSCFAnalysisData.map(item => item.daysOutstanding),
                                backgroundColor: '#8884d8'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                title: {
                                    display: true,
                                    text: '일'
                                }
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: '매출채권 회수 기간'
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': ' + context.raw + ' 일';
                                    }
                                }
                            }
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
                
                // 6-2. 자금조달 비용 차트
                const financingCostChartCtx = document.getElementById('financingCostChart').getContext('2d');
                new Chart(financingCostChartCtx, {
                    type: 'bar',
                    data: {
                        labels: fibriaSCFAnalysisData.map(item => item.category),
                        datasets: [
                            {
                                label: '자금조달 비용',
                                data: fibriaSCFAnalysisData.map(item => item.financingCost),
                                backgroundColor: '#ff8042'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        scales: {
                            y: {
                                title: {
                                    display: true,
                                    text: '백만 달러'
                                }
                            }
                        },
                        plugins: {
                            title: {
                                display: true,
                                text: '자금조달 비용 (연간, 백만 달러)'
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return context.dataset.label + ': $' + context.raw.toFixed(2) + ' 백만';
                                    }
                                }
                            }
                        },
                        interaction: {
                            intersect: false,
                            mode: 'index'
                        }
                    }
                });
            </script>
        </body>
        </html>
        """ 