import streamlit as st
import pandas as pd
import json

class PGSCFEconomicsGenerator:
    """P&G SCF 경제적 효과 분석 컴포넌트 생성기"""
    
    def __init__(self, data_provider=None):
        """초기화 함수"""
        self.data_provider = data_provider
        
        # Table A: P&G Supply Chain Finance 예시 데이터
        self.table_a_data = [
            {
                "scenario": "기존 상태",
                "days": 45,
                "receivable": 45,
                "payable": 45,
                "financingCost": 2.92,
                "netAmount": 997.08,
                "description": "SCF 도입 전 기본 결제 조건"
            },
            {
                "scenario": "지불조건 연장(SCF 없음)",
                "days": 75,
                "receivable": 75,
                "payable": 45,
                "financingCost": 5.83,
                "netAmount": 994.17,
                "description": "SCF 없이 지불 기간만 연장 (공급업체 부담 증가)"
            },
            {
                "scenario": "SCF 프로그램 적용",
                "days": 75,
                "receivable": 15,
                "payable": 45,
                "financingCost": 2.17,
                "netAmount": 997.83,
                "description": "SCF 적용 시 (P&G는 75일 후 지불, 공급업체는 15일 후 은행에서 수령)"
            }
        ]
        
        # SCF 프로그램에 따른 지불 일정 시각화용 데이터
        self.payment_timeline_data = [
            {"name": "D+0", "scf": 0, "traditional": 0, "label": "인보이스 발행"},
            {"name": "D+15", "scf": 997.83, "traditional": 0, "label": "SCF 조기지불"},
            {"name": "D+45", "scf": 997.83, "traditional": 997.08, "label": "기존 지불기한"},
            {"name": "D+75", "scf": 997.83, "traditional": 994.17, "label": "연장된 지불기한"}
        ]
        
        # Table B: SCF 인보이스 할인율 계산 데이터
        self.table_b_data = {
            "daysFinanced": 60,
            "libor60Day": 0.30,
            "bankSpread": 1.00,
            "financingRate": 1.30,
            "discountPercentage": 0.22
        }
        
        # 할인율 구성 파이 차트용 데이터
        self.discount_rate_data = [
            {"name": "LIBOR 60일", "value": self.table_b_data["libor60Day"]},
            {"name": "은행 스프레드", "value": self.table_b_data["bankSpread"]}
        ]
        
        # 공급업체 관점에서 3가지 시나리오 비교 데이터
        self.supplier_perspective_data = [
            {
                "name": "기존 지불조건",
                "invoiceAmount": 1000,
                "daysToReceive": 45,
                "financingCost": 2.92,
                "netAmount": 997.08,
                "annualRate": 3.50
            },
            {
                "name": "SCF 없는 지불연장",
                "invoiceAmount": 1000,
                "daysToReceive": 75,
                "financingCost": 5.83,
                "netAmount": 994.17,
                "annualRate": 3.50
            },
            {
                "name": "SCF 프로그램",
                "invoiceAmount": 1000,
                "daysToReceive": 15,
                "financingCost": 2.17,
                "netAmount": 997.83,
                "annualRate": 1.30
            }
        ]
        
        # P&G 관점에서의 운전자본 영향 데이터
        self.pg_perspective_data = [
            {
                "name": "기존 지불조건",
                "DPO": 45,
                "workingCapitalImpact": 0,
                "cashOutflow": 1000,
                "cashOutflowDay": 45
            },
            {
                "name": "SCF 프로그램",
                "DPO": 75,
                "workingCapitalImpact": 30,
                "cashOutflow": 1000,
                "cashOutflowDay": 75
            }
        ]
        
        # 색상 설정
        self.colors = {
            "blue": "#2196f3",
            "lightBlue": "#90caf9",
            "green": "#4caf50",
            "lightGreen": "#c8e6c9",
            "red": "#f44336",
            "orange": "#ff9800",
            "purple": "#9c27b0",
            "grey": "#9e9e9e"
        }
        
        # 파이 차트 색상
        self.pie_colors = ["#0088FE", "#00C49F"]
    
    def generate_html(self):
        """Chart.js를 사용하여 HTML 코드 생성"""
        html_code = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-datalabels@2.0.0"></script>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }
                .container {
                    margin-bottom: 50px;
                }
                h1 {
                    color: #1565c0;
                    text-align: center;
                }
                h2 {
                    color: #1976d2;
                    margin-top: 30px;
                    margin-bottom: 20px;
                    padding-bottom: 10px;
                    border-bottom: 2px solid #e0e0e0;
                }
                .chart-container {
                    position: relative;
                    height: 400px;
                    width: 100%;
                    margin: 20px 0;
                }
                .grid-container {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                }
                .card {
                    background-color: #f5f5f5;
                    border-radius: 8px;
                    padding: 15px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .benefit-container {
                    background-color: #e3f2fd;
                    border-radius: 8px;
                    padding: 20px;
                    margin-bottom: 30px;
                }
                .simulation-container {
                    background-color: #fff8e1;
                    border-radius: 8px;
                    padding: 20px;
                }
                table {
                    width: 100%;
                    border-collapse: collapse;
                    margin: 20px 0;
                    background-color: white;
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }
                th {
                    background-color: #f5f5f5;
                }
                .highlight-row {
                    background-color: #e8f5e9;
                }
                .caption {
                    font-size: 0.9em;
                    color: #666;
                    margin-top: 10px;
                    text-align: center;
                    font-style: italic;
                }
                .flex-row {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin: 10px 0;
                }
                .color-box {
                    width: 16px;
                    height: 16px;
                    display: inline-block;
                }
            </style>
        </head>
        <body>
            <h1>P&G SCF 프로그램의 경제적 효과 분석</h1>
            
            <div class="container">
                <h2>1. 3가지 시나리오 비교 (인보이스 금액: $1,000)</h2>
                <div class="chart-container">
                    <canvas id="scenarioComparisonChart"></canvas>
                </div>
                <p class="caption">* SCF 프로그램을 통해 P&G는 지불기한을 연장하고, 공급업체는 더 빨리 현금 수령 가능</p>
            </div>
        """
        
        # 두 번째 차트 컨테이너를 추가
        html_code += """
            <div class="container">
                <h2>2. 공급업체 현금 수령 타임라인</h2>
                <div class="chart-container">
                    <canvas id="timelineChart"></canvas>
                </div>
                <div style="display: flex; justify-content: center; gap: 30px; margin-top: 15px;">
                    <div class="flex-row">
                        <div class="color-box" style="background-color: #4caf50;"></div>
                        <span>SCF: 15일 후 $997.83 수령</span>
                    </div>
                    <div class="flex-row">
                        <div class="color-box" style="background-color: #2196f3;"></div>
                        <span>기존: 45일 후 $997.08 수령</span>
                    </div>
                </div>
            </div>
        """
        
        # 세 번째 섹션 - SCF 할인율 구성
        html_code += """
            <div class="container">
                <h2>3. SCF 인보이스 할인율 구성 요소</h2>
                <div class="grid-container">
                    <div class="chart-container" style="height: 300px;">
                        <canvas id="discountRateChart"></canvas>
                    </div>
                    <div class="card">
                        <h3 style="text-align: center; margin-bottom: 15px;">SCF 할인율 계산</h3>
                        <table>
                            <tbody>
        """
        
        # 테이블 데이터 추가
        table_rows = [
            ("SCF 은행 금융 기간", f"{self.table_b_data['daysFinanced']}일"),
            ("LIBOR (60일)", f"{self.table_b_data['libor60Day']}%"),
            ("은행 스프레드", f"{self.table_b_data['bankSpread']}%"),
            ("SCF 파이낸싱 연이율", f"{self.table_b_data['financingRate']}%")
        ]
        
        for label, value in table_rows:
            html_code += f"""
                <tr>
                    <td style="font-weight: 600;">{label}</td>
                    <td style="text-align: right;">{value}</td>
                </tr>
            """
        
        # 할인율 강조 행
        html_code += f"""
                <tr style="background-color: #e3f2fd;">
                    <td style="font-weight: 700;">SCF 인보이스 할인율</td>
                    <td style="text-align: right; font-weight: 700;">{self.table_b_data['discountPercentage']}%</td>
                </tr>
                <tr>
                    <td colspan="2" style="font-size: 0.9em; color: #666;">
                        계산식: 할인율 = (연이율 × 금융기간) ÷ 360
                    </td>
                </tr>
            """
        
        # 테이블 닫기
        html_code += """
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        """
        
        # 네 번째 섹션 - 공급업체 관점 비교
        html_code += """
            <div class="container">
                <h2>4. 공급업체 관점에서의 비교</h2>
                <div class="grid-container">
                    <div class="chart-container">
                        <canvas id="supplierDaysChart"></canvas>
                    </div>
                    <div class="chart-container">
                        <canvas id="supplierFinanceChart"></canvas>
                    </div>
                </div>
                <p class="caption">* SCF 프로그램은 더 낮은 연이율(3.5% → 1.3%)과 더 빠른 수금(45일 → 15일)을 제공</p>
            </div>
        """
        
        # 다섯 번째 섹션 - P&G 관점에서의 효과
        html_code += """
            <div class="container">
                <h2>5. P&G 관점에서의 효과</h2>
                <div class="chart-container">
                    <canvas id="pgPerspectiveChart"></canvas>
                </div>
                <p class="caption">* P&G는 SCF를 통해 지불 기간(DPO)을 30일 연장하고 그만큼 운전자본을 개선</p>
            </div>
        """
        
        # 여섯 번째 섹션 - SCF 경제적 효과 요약
        html_code += """
            <div class="container">
                <h2>6. SCF 프로그램의 경제적 효과 요약</h2>
                <div class="benefit-container">
                    <div class="grid-container">
                        <div>
                            <h3>P&G의 이점</h3>
                            <ul>
                                <li>지불 기간 연장: 45일 → 75일 (+30일)</li>
                                <li>운전자본 개선 (30일 추가 현금 보유)</li>
                                <li>공급업체 관계 유지 및 강화</li>
                                <li>어음 할인료 부담 없음 (공급업체 비용)</li>
                            </ul>
                            
                            <h3 style="margin-top: 20px;">SCF 은행의 이점</h3>
                            <ul>
                                <li>안정적 수익: 1.0% 스프레드</li>
                                <li>P&G 신용등급(AA-)에 기반한 낮은 위험</li>
                                <li>공급업체와 새로운 관계 형성 기회</li>
                                <li>거래 규모 확대 가능성 (P&G 외 공급망)</li>
                            </ul>
                        </div>
                        <div>
                            <h3>공급업체의 이점</h3>
                            <ul>
                                <li>더 빠른 현금화: 45일 → 15일 (-30일)</li>
                                <li>더 낮은 금융 비용: 3.5% → 1.3% (P&G 신용등급 활용)</li>
                                <li>예측 가능한 현금흐름 확보</li>
                                <li>재무제표 개선 (매출채권 감소)</li>
                            </ul>
                            
                            <h3 style="margin-top: 20px;">핵심 성공 요인</h3>
                            <ul>
                                <li>P&G의 높은 신용등급(AA-)</li>
                                <li>경쟁적인 SCF 은행 구조 (시티그룹 vs JP모건)</li>
                                <li>공급업체의 선택 자유도 보장</li>
                                <li>"윈-윈-윈" 구조 설계</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        """
        
        # 일곱 번째 섹션 - 시뮬레이션
        html_code += """
            <div class="container">
                <h2>7. $300M 연간 거래 기준 SCF 효과 시뮬레이션</h2>
                <div class="simulation-container">
                    <table>
                        <thead>
                            <tr>
                                <th>시나리오</th>
                                <th>결제 조건</th>
                                <th>공급업체 수령 시점</th>
                                <th>금융 비용(연간)</th>
                                <th>P&G 운전자본 효과</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>기존 조건</td>
                                <td>45일</td>
                                <td>45일</td>
                                <td>$2.1M (3.5%)</td>
                                <td>-</td>
                            </tr>
                            <tr>
                                <td>SCF 없는 연장</td>
                                <td>75일</td>
                                <td>75일</td>
                                <td>$4.2M (3.5%)</td>
                                <td>+$25M (30일)</td>
                            </tr>
                            <tr class="highlight-row">
                                <td><strong>SCF 프로그램</strong></td>
                                <td><strong>75일</strong></td>
                                <td><strong>15일</strong></td>
                                <td><strong>$1.6M (1.3%)</strong></td>
                                <td><strong>+$25M (30일)</strong></td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="caption">* SCF 프로그램은 P&G에게 $25M의 운전자본 개선 효과를 제공하면서, 동시에 공급업체의 금융 비용을 기존 조건 대비 $0.5M 절감</p>
                </div>
            </div>
        """
        
        # JavaScript 차트 코드 추가
        html_code += f"""
        <script>
        // 문서가 로드된 후 차트 렌더링
        document.addEventListener('DOMContentLoaded', function() {{
            // 3가지 시나리오 비교 차트
            const scenarioCtx = document.getElementById('scenarioComparisonChart').getContext('2d');
            
            // 데이터 준비
            const labels = {json.dumps([item["scenario"] for item in self.table_a_data])};
            const daysData = {json.dumps([item["days"] for item in self.table_a_data])};
            const receivableData = {json.dumps([item["receivable"] for item in self.table_a_data])};
            const netAmountData = {json.dumps([item["netAmount"] for item in self.table_a_data])};
            
            // 차트 생성
            new Chart(scenarioCtx, {{
                type: 'bar',
                data: {{
                    labels: labels,
                    datasets: [
                        {{
                            label: 'P&G 지불기한',
                            backgroundColor: '{self.colors["blue"]}',
                            data: daysData,
                            yAxisID: 'y-left',
                        }},
                        {{
                            label: '공급업체 수금기한',
                            backgroundColor: '{self.colors["green"]}',
                            data: receivableData,
                            yAxisID: 'y-left',
                        }},
                        {{
                            type: 'line',
                            label: '공급업체 수령액',
                            borderColor: '{self.colors["red"]}',
                            backgroundColor: 'transparent',
                            data: netAmountData,
                            yAxisID: 'y-right',
                            tension: 0.1,
                            borderWidth: 3,
                            pointRadius: 5
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        y: {{
                            type: 'linear',
                            display: true,
                            position: 'left',
                            id: 'y-left',
                            title: {{
                                display: true,
                                text: '일수'
                            }}
                        }},
                        'y-right': {{
                            type: 'linear',
                            display: true,
                            position: 'right',
                            min: 992,
                            max: 1000,
                            grid: {{
                                drawOnChartArea: false
                            }},
                            title: {{
                                display: true,
                                text: '금액($)'
                            }}
                        }}
                    }},
                    plugins: {{
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let label = context.dataset.label || '';
                                    if (label) {{
                                        label += ': ';
                                    }}
                                    if (context.dataset.label === '공급업체 수령액') {{
                                        return label + '$' + context.parsed.y.toFixed(2);
                                    }} else {{
                                        return label + context.parsed.y + '일';
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
            // 타임라인 차트
            const timelineCtx = document.getElementById('timelineChart').getContext('2d');
            
            // 타임라인 데이터 준비
            const timeLabels = {json.dumps([item["name"] for item in self.payment_timeline_data])};
            const scfData = {json.dumps([item["scf"] for item in self.payment_timeline_data])};
            const traditionalData = {json.dumps([item["traditional"] for item in self.payment_timeline_data])};
            
            // 타임라인 차트 생성
            new Chart(timelineCtx, {{
                type: 'line',
                data: {{
                    labels: timeLabels,
                    datasets: [
                        {{
                            label: 'SCF 프로그램',
                            borderColor: '{self.colors["green"]}',
                            backgroundColor: 'rgba(76, 175, 80, 0.1)',
                            data: scfData,
                            borderWidth: 3,
                            pointRadius: 6,
                            pointBackgroundColor: '{self.colors["green"]}',
                            stepped: 'after'
                        }},
                        {{
                            label: '기존 지불조건',
                            borderColor: '{self.colors["blue"]}',
                            backgroundColor: 'rgba(33, 150, 243, 0.1)',
                            data: traditionalData,
                            borderWidth: 3,
                            pointRadius: 6,
                            pointBackgroundColor: '{self.colors["blue"]}',
                            stepped: 'after'
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        y: {{
                            beginAtZero: true,
                            max: 1100,
                            title: {{
                                display: true,
                                text: '금액($)'
                            }}
                        }}
                    }},
                    plugins: {{
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let label = context.dataset.label || '';
                                    if (label) {{
                                        label += ': ';
                                    }}
                                    const value = context.parsed.y;
                                    return label + (value > 0 ? '$' + value.toFixed(2) : '$0');
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
            // 할인율 파이 차트
            const discountRateCtx = document.getElementById('discountRateChart').getContext('2d');
            
            // 할인율 데이터
            const discountRateLabels = {json.dumps([item["name"] for item in self.discount_rate_data])};
            const discountRateValues = {json.dumps([item["value"] for item in self.discount_rate_data])};
            const discountRateColors = {json.dumps(self.pie_colors)};
            
            // 할인율 차트 생성
            new Chart(discountRateCtx, {{
                type: 'pie',
                data: {{
                    labels: discountRateLabels,
                    datasets: [{{
                        data: discountRateValues,
                        backgroundColor: discountRateColors,
                        borderWidth: 1
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'right',
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    const label = context.label || '';
                                    const value = context.raw;
                                    const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                    const percentage = Math.round((value / total) * 100);
                                    return label + ': ' + value + '% (' + percentage + '% 비중)';
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
            // 공급업체 관점 차트 1 - 대기 일수 및 연이율
            const supplierDaysCtx = document.getElementById('supplierDaysChart').getContext('2d');
            
            // 공급업체 데이터
            const supplierLabels = {json.dumps([item["name"] for item in self.supplier_perspective_data])};
            const supplierDaysData = {json.dumps([item["daysToReceive"] for item in self.supplier_perspective_data])};
            const supplierRateData = {json.dumps([item["annualRate"] for item in self.supplier_perspective_data])};
            
            // 공급업체 대기 일수 및 연이율 차트
            new Chart(supplierDaysCtx, {{
                type: 'bar',
                data: {{
                    labels: supplierLabels,
                    datasets: [
                        {{
                            label: '대기 일수',
                            backgroundColor: '{self.colors["blue"]}',
                            data: supplierDaysData,
                            yAxisID: 'y-days',
                        }},
                        {{
                            type: 'line',
                            label: '연이율(%)',
                            borderColor: '{self.colors["purple"]}',
                            backgroundColor: 'transparent',
                            data: supplierRateData,
                            yAxisID: 'y-rate',
                            borderWidth: 3,
                            pointRadius: 5
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        'y-days': {{
                            type: 'linear',
                            display: true,
                            position: 'left',
                            beginAtZero: true,
                            max: 80,
                            title: {{
                                display: true,
                                text: '대기 일수'
                            }}
                        }},
                        'y-rate': {{
                            type: 'linear',
                            display: true,
                            position: 'right',
                            beginAtZero: true,
                            max: 5,
                            grid: {{
                                drawOnChartArea: false
                            }},
                            title: {{
                                display: true,
                                text: '연이율(%)'
                            }}
                        }}
                    }},
                    plugins: {{
                        title: {{
                            display: true,
                            text: '대기 일수 및 연이율'
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let label = context.dataset.label || '';
                                    if (label) {{
                                        label += ': ';
                                    }}
                                    if (context.dataset.label === '대기 일수') {{
                                        return label + context.parsed.y + '일';
                                    }} else {{
                                        return label + context.parsed.y + '%';
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
            // 공급업체 관점 차트 2 - 금융 비용 및 수령액
            const supplierFinanceCtx = document.getElementById('supplierFinanceChart').getContext('2d');
            
            // 공급업체 금융 데이터
            const supplierCostData = {json.dumps([item["financingCost"] for item in self.supplier_perspective_data])};
            const supplierNetData = {json.dumps([item["netAmount"] for item in self.supplier_perspective_data])};
            
            // 공급업체 금융 비용 및 수령액 차트
            new Chart(supplierFinanceCtx, {{
                type: 'bar',
                data: {{
                    labels: supplierLabels,
                    datasets: [
                        {{
                            label: '금융 비용',
                            backgroundColor: '{self.colors["red"]}',
                            data: supplierCostData,
                            yAxisID: 'y-cost',
                        }},
                        {{
                            type: 'line',
                            label: '수령액',
                            borderColor: '{self.colors["green"]}',
                            backgroundColor: 'transparent',
                            data: supplierNetData,
                            yAxisID: 'y-net',
                            borderWidth: 3,
                            pointRadius: 5
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        'y-cost': {{
                            type: 'linear',
                            display: true,
                            position: 'left',
                            beginAtZero: true,
                            title: {{
                                display: true,
                                text: '금융 비용($)'
                            }}
                        }},
                        'y-net': {{
                            type: 'linear',
                            display: true,
                            position: 'right',
                            min: 992,
                            max: 1000,
                            grid: {{
                                drawOnChartArea: false
                            }},
                            title: {{
                                display: true,
                                text: '수령액($)'
                            }}
                        }}
                    }},
                    plugins: {{
                        title: {{
                            display: true,
                            text: '금융 비용 및 수령액'
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let label = context.dataset.label || '';
                                    if (label) {{
                                        label += ': ';
                                    }}
                                    return label + '$' + context.parsed.y.toFixed(2);
                                }}
                            }}
                        }}
                    }}
                }}
            }});
            
            // P&G 관점 차트
            const pgPerspectiveCtx = document.getElementById('pgPerspectiveChart').getContext('2d');
            
            // P&G 데이터
            const pgLabels = {json.dumps([item["name"] for item in self.pg_perspective_data])};
            const pgDPOData = {json.dumps([item["DPO"] for item in self.pg_perspective_data])};
            const pgWorkingCapitalData = {json.dumps([item["workingCapitalImpact"] for item in self.pg_perspective_data])};
            
            // P&G 차트 생성
            new Chart(pgPerspectiveCtx, {{
                type: 'bar',
                data: {{
                    labels: pgLabels,
                    datasets: [
                        {{
                            label: 'DPO',
                            backgroundColor: '{self.colors["purple"]}',
                            data: pgDPOData,
                            yAxisID: 'y-dpo',
                        }},
                        {{
                            label: '운전자본 개선',
                            backgroundColor: '{self.colors["green"]}',
                            data: pgWorkingCapitalData,
                            yAxisID: 'y-workingCapital',
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {{
                        'y-dpo': {{
                            type: 'linear',
                            display: true,
                            position: 'left',
                            beginAtZero: true,
                            max: 80,
                            title: {{
                                display: true,
                                text: 'DPO'
                            }}
                        }},
                        'y-workingCapital': {{
                            type: 'linear',
                            display: true,
                            position: 'right',
                            beginAtZero: true,
                            max: 50,
                            grid: {{
                                drawOnChartArea: false
                            }},
                            title: {{
                                display: true,
                                text: '운전자본 개선'
                            }}
                        }}
                    }},
                    plugins: {{
                        title: {{
                            display: true,
                            text: 'P&G 관점에서의 효과'
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let label = context.dataset.label || '';
                                    if (label) {{
                                        label += ': ';
                                    }}
                                    if (context.dataset.label === 'DPO') {{
                                        return label + context.parsed.y + '일';
                                    }} else {{
                                        return label + context.parsed.y + '%';
                                    }}
                                }}
                            }}
                        }}
                    }}
                }}
            }});
        }});
        </script>
        """
        
        # 닫는 태그 추가
        html_code += """
        </body>
        </html>
        """
        
        return html_code
    
def pg_scf_economics_viz():
    """Streamlit 앱에서 호출할 P&G SCF 경제적 효과 시각화 함수"""
    st.title("P&G SCF 프로그램의 경제적 효과 분석")
    
    # 컴포넌트 생성기 초기화
    generator = PGSCFEconomicsGenerator()
    
    # HTML 코드 생성
    html_code = generator.generate_html()
    
    # HTML 렌더링
    st.components.v1.html(html_code, height=2500, scrolling=True)

if __name__ == "__main__":
    pg_scf_economics_viz() 