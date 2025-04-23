import json
from data_provider import MarketDataProvider

class FibriaWorkingCapitalComponentGenerator:
    """피브리아 운전자본 분석 컴포넌트 생성기"""
    
    def __init__(self, data_provider):
        """초기화"""
        self.data_provider = data_provider
    
    def generate_html(self):
        """Chart.js를 사용한 HTML 코드 생성"""
        
        # 데이터 가져오기
        working_capital_data = self.data_provider.get_working_capital_data()
        scf_impact_data = self.data_provider.get_scf_impact_data()
        working_capital_need_data = self.data_provider.get_working_capital_need_data()
        financial_crisis_periods = self.data_provider.get_financial_crisis_periods()
        
        # Chart.js 코드를 별도 변수로 분리
        chart_js_code = self._generate_chart_js_code(
            working_capital_data, 
            scf_impact_data, 
            working_capital_need_data, 
            financial_crisis_periods
        )
        
        # HTML 템플릿 
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation"></script>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: white;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .chart-container {{
                    margin-bottom: 40px;
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .chart-row {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 20px;
                    margin-bottom: 20px;
                }}
                .chart-column {{
                    flex: 1;
                    min-width: 300px;
                }}
                h2 {{
                    color: #2c3e50;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                h3 {{
                    color: #3498db;
                    margin-bottom: 20px;
                }}
                .card {{
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    padding: 15px;
                    margin-bottom: 15px;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                }}
                .card h4 {{
                    color: #2980b9;
                    margin-top: 0;
                }}
                .insights-container {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                    gap: 15px;
                    margin-bottom: 30px;
                }}
                .implications {{
                    background-color: #ebf5fb;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 30px;
                }}
                .implications h3 {{
                    color: #2471a3;
                }}
                ul.implication-list {{
                    list-style-type: none;
                    padding-left: 0;
                }}
                ul.implication-list li {{
                    margin-bottom: 10px;
                    padding-left: 24px;
                    position: relative;
                }}
                ul.implication-list li:before {{
                    content: "•";
                    position: absolute;
                    left: 0;
                    color: #3498db;
                    font-weight: bold;
                }}
                .bank-implications {{
                    background-color: #e8f8f5;
                }}
                .bank-implications h3 {{
                    color: #16a085;
                }}
                .event-legend {{
                    display: flex;
                    justify-content: center;
                    margin-top: 15px;
                }}
                .event-legend div {{
                    display: flex;
                    align-items: center;
                    margin: 0 15px;
                }}
                .event-legend .color-box {{
                    width: 16px;
                    height: 16px;
                    margin-right: 8px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>피브리아 현금전환주기 분석 (Exhibit 7)</h2>
                
                <!-- 1. 현금전환주기 추이 -->
                <div class="chart-container">
                    <h3>1. 현금전환주기 추이 (2005-2015, 단위: 일)</h3>
                    <div style="height: 300px; position: relative;">
                        <canvas id="cccTrendChart"></canvas>
                    </div>
                    <div class="mt-4 p-4 bg-blue-50 rounded-lg">
                        <p class="text-center text-sm text-blue-800">
                            <strong>계산식:</strong> 현금전환주기(CCC) = DSO + DSI - DPO<br/>
                            <strong>2012년:</strong> 57일 + 85일 - 38일 = 104일<br/>
                            <strong>2014년:</strong> 40일 + 85일 - 38일 = 87일 (17일 감소)
                        </p>
                    </div>
                    <div class="event-legend">
                        <div>
                            <div class="color-box" style="background-color: rgba(255,0,0,0.3);"></div>
                            <span>금융위기 기간</span>
                        </div>
                        <div>
                            <div class="color-box" style="background-color: rgba(0,255,0,0.3);"></div>
                            <span>SCF 프로그램 도입</span>
                        </div>
                    </div>
                </div>
                
                <!-- 2. 구성 요소별 추이 -->
                <div class="chart-container">
                    <h3>2. 현금전환주기 구성 요소별 추이 (단위: 일)</h3>
                    <div style="height: 300px; position: relative;">
                        <canvas id="componentsChart"></canvas>
                    </div>
                    <div class="mt-4 p-4 bg-blue-50 rounded-lg">
                        <p class="text-center text-sm text-blue-800">
                            <strong>DSO (매출채권회수기간):</strong> 2012년 57일 → 2014년 40일 (17일 감소)<br/>
                            <strong>DSI (재고자산회전기간):</strong> 85일로 일정 유지<br/>
                            <strong>DPO (매입채무지급기간):</strong> 38일로 일정 유지
                        </p>
                    </div>
                </div>
                
                <!-- 3. SCF 프로그램 도입 전후 비교 -->
                <div class="chart-container">
                    <h3>3. SCF 프로그램 도입 전후 비교 (2012 vs 2014)</h3>
                    <div class="chart-row">
                        <div class="chart-column">
                            <div style="height: 300px; position: relative;">
                                <canvas id="scfComparisonChart"></canvas>
                            </div>
                        </div>
                        <div class="chart-column">
                            <div style="height: 300px; position: relative;">
                                <canvas id="scfImprovementChart"></canvas>
                            </div>
                        </div>
                    </div>
                    <div class="mt-4 p-4 bg-blue-50 rounded-lg">
                        <p class="text-center text-sm text-blue-800">
                            <strong>핵심 변화:</strong> DSO가 57일에서 40일로 17일 감소 (SCF의 직접적 효과)<br/>
                            <strong>DSI와 DPO:</strong> SCF와 직접적인 관련이 없으며 큰 변화 없음<br/>
                            <strong>총 효과:</strong> CCC가 104일에서 87일로 17일 감소
                        </p>
                    </div>
                </div>
                
                <!-- 4. SCF 프로그램이 P&G 거래에 미치는 영향 분석 -->
                <div class="chart-container">
                    <h3>4. SCF 프로그램이 P&G 거래에 미치는 영향 분석</h3>
                    <div class="chart-row">
                        <div class="chart-column">
                            <div style="height: 300px; position: relative;">
                                <canvas id="scfImpactCycleChart"></canvas>
                            </div>
                        </div>
                        <div class="chart-column">
                            <div style="height: 300px; position: relative;">
                                <canvas id="scfImpactCapitalChart"></canvas>
                            </div>
                        </div>
                    </div>
                    <div class="mt-4 p-4 bg-blue-50 rounded-lg">
                        <p class="text-center text-sm text-blue-800">
                            <strong>효과:</strong> P&G SCF 사용 시 필요 운전자본 $82.2M → $37.0M으로 $45.2M 감소<br/>
                            <strong>계산:</strong> $300M × (CCC ÷ 365일) = 필요 운전자본<br/>
                            <strong>비교:</strong> 일반 결제(100일) → SCF 사용(45일) = 55일 감소
                        </p>
                    </div>
                </div>
                
                <!-- 5. 운전자본 부담 변화 -->
                <div class="chart-container">
                    <h3>5. SCF 프로그램으로 인한 운전자본 부담 변화</h3>
                    <div style="height: 300px; position: relative;">
                        <canvas id="workingCapitalBurdenChart"></canvas>
                    </div>
                    <div class="mt-4 p-4 bg-yellow-50 rounded-lg">
                        <p class="text-center text-sm text-yellow-800">
                            <strong>SCF 효과 가정:</strong> 2013년(10일 감소), 2014-2015년(17일 감소)<br/>
                            <strong>운전자본 계산식:</strong> 현금전환주기 × (연간 매출 ÷ 365일)<br/>
                            <strong>환율 영향:</strong><br/>
                            - 유리한 점: 달러 기반 매출의 레알화 가치 증가 → 레알화 기준 수익 증가<br/>
                            - 불리한 점: 달러 기반 부채의 레알화 가치 증가 → 부채 부담 증가 (Fibria 부채의 90% 이상이 달러 표시)
                        </p>
                    </div>
                </div>
                
                <!-- 6. 자금조달 옵션 비교 -->
                <div class="chart-container">
                    <h3>6. 자금조달 옵션 비교</h3>
                    <div style="height: 300px; position: relative;">
                        <canvas id="financingRatesChart"></canvas>
                    </div>
                    <div class="mt-4 p-4 bg-green-50 rounded-lg">
                        <p class="text-center text-sm text-green-800">
                            <strong>할인율 0.1%p 차이의 영향 계산:</strong><br/>
                            $300M × 0.001 × (100일 ÷ 365일) ≈ $82,192<br/>
                            자금 회전 효과 고려 시 약 $30만/연간 비용 영향 추정
                        </p>
                    </div>
                </div>
                
                <!-- 핵심 인사이트 -->
                <div class="chart-container">
                    <h3>핵심 인사이트</h3>
                    <div class="insights-container">
                        <div class="card">
                            <h4>SCF의 직접적인 효과</h4>
                            <p>DSO(매출채권회수기간) 57일 → 40일 (17일 감소)</p>
                            <p style="color: #7f8c8d;">→ SCF의 핵심 효과는 매출채권 회수기간 단축</p>
                        </div>
                        <div class="card">
                            <h4>P&G 거래의 효과</h4>
                            <p>결제 기간 105일에도 SCF로 5일 내 현금화</p>
                            <p style="color: #7f8c8d;">→ 현금흐름 크게 개선</p>
                        </div>
                        <div class="card">
                            <h4>금융 혁신의 가치</h4>
                            <p>물리적 공급망은 유지(DSI 변화 없음)하면서 금융 흐름만 최적화</p>
                            <p style="color: #7f8c8d;">→ 혁신적 접근법의 사례</p>
                        </div>
                        <div class="card">
                            <h4>운전자본 감소</h4>
                            <p>2014년 기준 약 $146M의 운전자본 감소 효과</p>
                            <p style="color: #7f8c8d;">→ 부채 상환, 투자 등에 활용 가능</p>
                        </div>
                    </div>
                </div>
                
                <!-- 케이스와의 연결성 -->
                <div class="chart-container implications">
                    <h3>케이스와의 연결성 및 시사점</h3>
                    <ul class="implication-list">
                        <li><strong>부채 부담에 대한 대응</strong>: 현금전환주기 개선을 통해 운전자본 필요성 감소 → 부채 의존도 완화</li>
                        <li><strong>금융위기 교훈</strong>: 2008-2009년 위기 이후 유동성 관리의 중요성 인식 → SCF 프로그램의 전략적 활용</li>
                        <li><strong>P&G와의 협상력</strong>: 결제 기간 연장(105일)에도 SCF로 현금흐름 개선 → 거래 조건에 유연하게 대응</li>
                        <li><strong>고정된 운영 구조</strong>: 재고자산회전기간(80일)은 큰 변화 없음 → 공급망 자체의 물리적 제약 존재</li>
                        <li><strong>금융 혁신의 가치</strong>: SCF를 통해 물리적 공급망은 유지하면서 금융 흐름은 최적화 → 혁신적 접근법의 사례</li>
                    </ul>
                </div>
                
                <!-- SCF 은행 선택에 관한 시사점 -->
                <div class="chart-container implications bank-implications">
                    <h3>SCF 은행 선택에 관한 시사점</h3>
                    <div class="insights-container">
                        <div class="card">
                            <h4>플랫폼 안정성</h4>
                            <p>운전자본 관리를 위한 핵심 도구로서의 SCF</p>
                            <p style="color: #7f8c8d;">→ 시티그룹의 검증된 플랫폼 vs JPMorgan의 새로운 관계</p>
                        </div>
                        <div class="card">
                            <h4>유동성 중요성</h4>
                            <p>역사적 데이터가 보여주는 유동성 확보의 중요성</p>
                            <p style="color: #7f8c8d;">→ 신속하고 안정적인 매출채권 결제 능력 중시</p>
                        </div>
                        <div class="card">
                            <h4>할인율 최적화</h4>
                            <p>운전자본 금액에 비해 할인율의 경제적 영향</p>
                            <p style="color: #7f8c8d;">→ 0.1%p 할인율 차이가 연간 약 $30만 비용 영향</p>
                        </div>
                        <div class="card">
                            <h4>은행 관계 다변화</h4>
                            <p>금융위기 시 다양한 금융 파트너의 중요성</p>
                            <p style="color: #7f8c8d;">→ 새로운 은행 관계 구축을 통한 위험 분산</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
                {chart_js_code}
            </script>
        </body>
        </html>
        """
        
        return html
    
    def _generate_chart_js_code(self, working_capital_data, scf_impact_data, working_capital_need_data, financial_crisis_periods):
        """Chart.js 코드 생성"""
        # 데이터를 JSON 문자열로 변환
        working_capital_data_json = json.dumps(working_capital_data)
        scf_impact_data_json = json.dumps(scf_impact_data)
        working_capital_need_data_json = json.dumps(working_capital_need_data)
        financial_crisis_periods_json = json.dumps(financial_crisis_periods)
        
        # Chart.js 코드
        return f"""
        // 데이터 정의
        const workingCapitalData = {working_capital_data_json};
        const scfImpactData = {scf_impact_data_json};
        const workingCapitalNeedData = {working_capital_need_data_json};
        const financialCrisisPeriods = {financial_crisis_periods_json};
        
        // 차트 색상 정의
        const colors = {{
            ccc: 'rgba(0, 0, 0, 0.8)',
            dso: 'rgba(153, 153, 153, 1)',
            dsi: 'rgba(204, 204, 204, 1)',
            dpo: 'rgba(0, 0, 0, 1)',
            positive: 'rgba(130, 202, 157, 1)',
            negative: 'rgba(255, 128, 66, 1)',
            withoutSCF: 'rgba(255, 128, 66, 1)',
            withSCF: 'rgba(130, 202, 157, 1)'
        }};
        
        // 1. 현금전환주기 추이 차트
        const cccTrendCtx = document.getElementById('cccTrendChart').getContext('2d');
        new Chart(cccTrendCtx, {{
            type: 'line',
            data: {{
                labels: workingCapitalData.map(d => d.year),
                datasets: [
                    {{
                        label: '현금전환주기(CCC)',
                        data: workingCapitalData.map(d => d.ccc),
                        borderColor: colors.ccc,
                        borderWidth: 3,
                        fill: false,
                        tension: 0.4
                    }},
                    {{
                        label: '매출채권회수기간(DSO)',
                        data: workingCapitalData.map(d => d.dso),
                        borderColor: colors.dso,
                        borderWidth: 2,
                        fill: false,
                        tension: 0.3
                    }},
                    {{
                        label: '재고자산회전기간(DSI)',
                        data: workingCapitalData.map(d => d.dsi),
                        borderColor: colors.dsi,
                        borderWidth: 2,
                        borderDash: [5, 5],
                        fill: false,
                        tension: 0.3
                    }},
                    {{
                        label: '매입채무지급기간(DPO)',
                        data: workingCapitalData.map(d => d.dpo),
                        borderColor: colors.dpo,
                        borderWidth: 1,
                        borderDash: [2, 2],
                        fill: false,
                        tension: 0.3
                    }}
                ]
            }},
            options: {{
                plugins: {{
                    annotation: {{
                        annotations: financialCrisisPeriods.map((period, index) => {{
                            const startIndex = workingCapitalData.findIndex(d => d.year === period.startYear);
                            const endIndex = workingCapitalData.findIndex(d => d.year === period.endYear);
                            
                            return {{
                                type: 'box',
                                xMin: startIndex - 0.0,
                                xMax: period.event === '금융위기' ?
                                    endIndex + 0.5 : workingCapitalData.length,
                                backgroundColor: period.event === '금융위기' ? 
                                    'rgba(255, 0, 0, 0.1)' : 'rgba(0, 128, 0, 0.1)',
                                borderWidth: 0
                            }};
                        }})
                    }}
                }},
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{
                            display: true,
                            text: '일수'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // 2. 구성 요소별 추이 차트
        const componentsCtx = document.getElementById('componentsChart').getContext('2d');
        new Chart(componentsCtx, {{
            type: 'line',
            data: {{
                labels: workingCapitalData.map(d => d.year),
                datasets: [
                    {{
                        label: '매출채권회수기간(DSO)',
                        data: workingCapitalData.map(d => d.dso),
                        borderColor: colors.dso,
                        borderWidth: 2,
                        tension: 0.3,
                        fill: false
                    }},
                    {{
                        label: '재고자산회전기간(DSI)',
                        data: workingCapitalData.map(d => d.dsi),
                        borderColor: colors.dsi,
                        borderWidth: 2,
                        borderDash: [5, 5],
                        tension: 0.3,
                        fill: false
                    }},
                    {{
                        label: '매입채무지급기간(DPO)',
                        data: workingCapitalData.map(d => d.dpo),
                        borderColor: colors.dpo,
                        borderWidth: 1,
                        borderDash: [2, 2],
                        tension: 0.3,
                        fill: false
                    }}
                ]
            }},
            options: {{
                scales: {{
                    y: {{
                        beginAtZero: true,
                        title: {{
                            display: true,
                            text: '일수'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // 3. SCF 프로그램 도입 전후 비교 (2012 vs 2014)
        const data2012 = workingCapitalData.find(d => d.year === '2012');
        const data2014 = workingCapitalData.find(d => d.year === '2014');
        
        const comparisonData = [
            {{ category: 'DSO', before: data2012.dso, after: data2014.dso }},
            {{ category: 'DSI', before: data2012.dsi, after: data2014.dsi }},
            {{ category: 'DPO', before: data2012.dpo, after: data2014.dpo }},
            {{ category: 'CCC', before: data2012.ccc, after: data2014.ccc }}
        ];
        
        // 3.1. 변화 비교 차트
        const scfComparisonCtx = document.getElementById('scfComparisonChart').getContext('2d');
        new Chart(scfComparisonCtx, {{
            type: 'bar',
            data: {{
                labels: comparisonData.map(d => d.category),
                datasets: [
                    {{
                        label: 'SCF 도입 전 (2012)',
                        data: comparisonData.map(d => d.before),
                        backgroundColor: 'rgba(136, 132, 216, 0.7)'
                    }},
                    {{
                        label: 'SCF 도입 후 (2014)',
                        data: comparisonData.map(d => d.after),
                        backgroundColor: 'rgba(130, 202, 157, 0.7)'
                    }}
                ]
            }},
            options: {{
                plugins: {{
                    title: {{
                        display: true,
                        text: '현금전환주기 구성 요소 변화'
                    }}
                }},
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '일수'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // 3.2. 개선 일수 차트
        const changes = comparisonData.map(d => ({{
            category: d.category,
            change: d.after - d.before
        }}));
        
        const scfImprovementCtx = document.getElementById('scfImprovementChart').getContext('2d');
        new Chart(scfImprovementCtx, {{
            type: 'bar',
            data: {{
                labels: changes.map(d => d.category),
                datasets: [{{
                    label: '2012-2014 변화 (일)',
                    data: changes.map(d => d.change),
                    backgroundColor: changes.map(d => d.change < 0 ? colors.negative : colors.positive)
                }}]
            }},
            options: {{
                plugins: {{
                    title: {{
                        display: true,
                        text: '각 요소별 개선 일수'
                    }}
                }},
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '일수 변화'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // 4. SCF 프로그램이 P&G 거래에 미치는 영향 분석
        // 4.1. 현금전환주기 비교
        const scfImpactCycleCtx = document.getElementById('scfImpactCycleChart').getContext('2d');
        new Chart(scfImpactCycleCtx, {{
            type: 'bar',
            data: {{
                labels: scfImpactData.map(d => d.scenario),
                datasets: [{{
                    label: '현금전환주기 (일)',
                    data: scfImpactData.map(d => d.cashCycle),
                    backgroundColor: 'rgba(136, 132, 216, 0.7)'
                }}]
            }},
            options: {{
                plugins: {{
                    title: {{
                        display: true,
                        text: '현금전환주기 비교'
                    }}
                }},
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '일수'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // 4.2. 필요 운전자본 금액
        const scfImpactCapitalCtx = document.getElementById('scfImpactCapitalChart').getContext('2d');
        new Chart(scfImpactCapitalCtx, {{
            type: 'bar',
            data: {{
                labels: scfImpactData.map(d => d.scenario),
                datasets: [{{
                    label: '필요 운전자본 (백만 달러)',
                    data: scfImpactData.map(d => d.cashNeeded),
                    backgroundColor: 'rgba(130, 202, 157, 0.7)'
                }}]
            }},
            options: {{
                plugins: {{
                    title: {{
                        display: true,
                        text: '필요 운전자본 금액'
                    }}
                }},
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '백만 달러'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        
        // 5. 운전자본 부담 변화
        const workingCapitalBurdenCtx = document.getElementById('workingCapitalBurdenChart').getContext('2d');
        new Chart(workingCapitalBurdenCtx, {{
            type: 'bar',
            data: {{
                labels: workingCapitalNeedData.map(d => d.year),
                datasets: [
                    {{
                        label: 'SCF 없는 경우 필요 운전자본',
                        data: workingCapitalNeedData.map(d => d.withoutSCF),
                        backgroundColor: colors.withoutSCF
                    }},
                    {{
                        label: 'SCF 활용 시 필요 운전자본',
                        data: workingCapitalNeedData.map(d => d.withSCF),
                        backgroundColor: colors.withSCF
                    }}
                ]
            }},
            options: {{
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '백만 달러'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});

        // 6. 자금조달 옵션 비교 차트
        const financingRatesData = [
            {{
                'scenario': 'SCF 프로그램',
                'rate': 1.3,
                'ratingBase': 'P&G AA- 등급',
                'calcBase': 'LIBOR + 1% 스프레드',
                'annualSavings': '약 $30만 (연간)'
            }},
            {{
                'scenario': 'Fibria 일반 자금조달',
                'rate': 2.5,
                'ratingBase': 'Fibria BBB- 등급',
                'calcBase': '미 달러화 3% 내외',
                'annualSavings': '-'
            }},
            {{
                'scenario': '일반 팩토링',
                'rate': 3.5,
                'ratingBase': '-',
                'calcBase': '투자등급 고객 기준',
                'annualSavings': '-'
            }}
        ];

        const financingRatesCtx = document.getElementById('financingRatesChart').getContext('2d');
        new Chart(financingRatesCtx, {{
            type: 'bar',
            data: {{
                labels: financingRatesData.map(d => d.scenario),
                datasets: [{{
                    label: '자금조달 이자율 (%)',
                    data: financingRatesData.map(d => d.rate),
                    backgroundColor: 'rgba(136, 132, 216, 0.7)'
                }}]
            }},
            options: {{
                plugins: {{
                    tooltip: {{
                        callbacks: {{
                            label: function(context) {{
                                const data = financingRatesData[context.dataIndex];
                                return [
                                    context.raw + '%',
                                    '기준: ' + data.calcBase,
                                    '연간 절감: ' + data.annualSavings
                                ];
                            }}
                        }}
                    }}
                }},
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: '이자율 (%)'
                        }}
                    }}
                }},
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                responsive: true,
                maintainAspectRatio: false
            }}
        }});
        """ 