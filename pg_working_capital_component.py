import json
from typing import Dict, Any, List
from data_provider import MarketDataProvider

class PGWorkingCapitalComponentGenerator:
    """P&G 운전자본 관련 컴포넌트 생성 클래스"""
    
    def __init__(self, data_provider: MarketDataProvider):
        """
        초기화 메서드
        
        Args:
            data_provider: 데이터 제공자
        """
        self.data_provider = data_provider
        self.working_capital_data = data_provider.pg_working_capital_data
        self.extended_working_capital_data = data_provider.pg_extended_working_capital_data
    
    def generate_html(self) -> str:
        """
        P&G 운전자본 시각화를 위한 HTML 생성
        
        Returns:
            str: HTML 코드
        """
        # 데이터 준비
        extended_working_capital_json = json.dumps(self.extended_working_capital_data)
        
        # Timeline 데이터
        timeline_data = [
            {"year": "2010", "event": "비용 절감 필요성 대두"},
            {"year": "2012", "event": "100억 달러 비용 절감 프로그램 발표"},
            {"year": "2013", "event": "공급망 금융(SCF) 프로그램 도입, 지불 기간 45→75일 연장"},
            {"year": "2015", "event": "현금전환주기 마이너스(-3.5일) 달성"}
        ]
        
        timeline_json = json.dumps(timeline_data)
        
        # 차트 스크립트 생성
        chart_script = self._create_chart_script(extended_working_capital_json)
        
        # HTML 템플릿
        html = f"""
        <!DOCTYPE html>
        <html lang="ko">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>P&G 운전자본 관리 분석 (2000-2015)</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
            <script src="https://cdn.tailwindcss.com"></script>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif; }}
                .chart-container {{ height: 400px; width: 100%; margin-bottom: 2rem; }}
                .chart-row {{ display: flex; flex-wrap: wrap; margin: 0 -1rem; }}
                .chart-half {{ flex: 1 1 calc(50% - 2rem); min-width: 300px; margin: 0 1rem 2rem; }}
                .insights-container {{ margin-top: 2rem; }}
                .timeline-item {{ position: relative; padding-left: 3rem; margin-bottom: 2.5rem; }}
                .timeline-item:before {{ content: ''; position: absolute; left: 0; top: 0.25rem; width: 1.5rem; height: 1.5rem; border-radius: 50%; background-color: #3b82f6; }}
                .timeline-item:after {{ content: ''; position: absolute; left: 0.75rem; top: 1.75rem; bottom: -2.5rem; width: 2px; background-color: #3b82f6; }}
                .timeline-item:last-child:after {{ display: none; }}
                .timeline-number {{ position: absolute; left: 0; top: 0.25rem; width: 1.5rem; height: 1.5rem; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; }}
                @media (max-width: 768px) {{ .chart-half {{ min-width: 100%; }} }}
            </style>
        </head>
        <body class="bg-white p-6">
            <div class="max-w-7xl mx-auto">
                <h2 class="text-2xl font-bold text-center text-blue-800 mb-10">P&G 운전자본 관리 분석 (2000-2015)</h2>
                
                <!-- 운전자본 관리 핵심 지표 -->
                <div class="mb-10">
                    <h3 class="text-xl font-semibold mb-3 text-center">1. 운전자본 관리 핵심 지표 추이 (단위: 일)</h3>
                    <div class="chart-container">
                        <canvas id="wcMetricsChart"></canvas>
                    </div>
                </div>
                
                <!-- 현금전환주기 변화 -->
                <div class="mb-10">
                    <h3 class="text-xl font-semibold mb-3 text-center">2. 현금전환주기 변화 (2000-2015)</h3>
                    <div class="chart-container" style="height: 300px;">
                        <canvas id="cccChart"></canvas>
                    </div>
                </div>
                
                <!-- 매입채무지급기간(DPO) 변화 -->
                <div class="mb-10">
                    <h3 class="text-xl font-semibold mb-3 text-center">3. 매입채무지급기간(DPO) 변화 (2000-2015)</h3>
                    <div class="chart-container" style="height: 300px;">
                        <canvas id="dpoChart"></canvas>
                    </div>
                </div>
                
                <!-- 2015년 구성 요소 분석 -->
                <div class="mb-10">
                    <h3 class="text-xl font-semibold mb-3 text-center">4. 2015년 운전자본 구성 요소 비교</h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                        <div class="bg-blue-50 p-4 rounded-lg shadow text-center">
                            <h4 class="font-bold text-blue-700 text-lg">매출채권회수기간</h4>
                            <p class="text-3xl font-bold mt-2">23.3일</p>
                            <p class="text-sm text-gray-600 mt-2">2000년 대비 -3.3일</p>
                            <p class="text-sm text-gray-600">2010년 대비 -1.8일</p>
                        </div>
                        <div class="bg-green-50 p-4 rounded-lg shadow text-center">
                            <h4 class="font-bold text-green-700 text-lg">재고자산회전기간</h4>
                            <p class="text-3xl font-bold mt-2">52.0일</p>
                            <p class="text-sm text-gray-600 mt-2">2000년 대비 -8.6일</p>
                            <p class="text-sm text-gray-600">2010년 대비 -10.9일</p>
                        </div>
                        <div class="bg-orange-50 p-4 rounded-lg shadow text-center">
                            <h4 class="font-bold text-orange-700 text-lg">매입채무지급기간</h4>
                            <p class="text-3xl font-bold mt-2">78.8일</p>
                            <p class="text-sm text-gray-600 mt-2">2000년 대비 +40.4일</p>
                            <p class="text-sm text-gray-600">2010년 대비 +7.4일</p>
                        </div>
                    </div>
                    <div class="mt-4 bg-red-50 p-4 rounded-lg shadow text-center">
                        <h4 class="font-bold text-red-700 text-lg">현금전환주기(CCC)</h4>
                        <p class="text-3xl font-bold mt-2">-3.5일</p>
                        <p class="text-sm text-gray-600 mt-2">2000년 대비 -52.3일</p>
                        <p class="text-sm text-gray-600">2010년 대비 -20.1일</p>
                    </div>
                </div>
                
                <!-- 주요 이벤트 타임라인 -->
                <div class="mb-10">
                    <h3 class="text-xl font-semibold mb-3 text-center">5. 주요 이벤트 타임라인 (2010-2015)</h3>
                    <div class="relative pl-8 md:pl-16 py-4 border-l-2 border-blue-500 ml-6 md:ml-12">
                        <div id="timeline-container"></div>
                    </div>
                </div>
                
                <!-- 인사이트 요약 -->
                <div class="mb-10 bg-yellow-50 p-6 rounded-lg">
                    <h3 class="text-xl font-semibold mb-4 text-center text-yellow-800">핵심 인사이트</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div class="bg-white p-4 rounded shadow">
                            <h4 class="font-bold text-blue-700">매입채무지급기간(DPO) 지속적 증가</h4>
                            <p>2000년 38.4일 → 2010년 71.4일 → 2015년 78.8일</p>
                            <p class="text-sm text-gray-600 mt-2">→ 공급업체 결제 기간 연장 전략의 성공적 실행</p>
                        </div>
                        <div class="bg-white p-4 rounded shadow">
                            <h4 class="font-bold text-blue-700">현금전환주기(CCC) 혁신적 개선</h4>
                            <p>2000년 48.8일 → 2010년 16.6일 → 2015년 -3.5일</p>
                            <p class="text-sm text-gray-600 mt-2">→ 마이너스 CCC 달성으로 운전자본에서 현금 창출</p>
                        </div>
                        <div class="bg-white p-4 rounded shadow">
                            <h4 class="font-bold text-blue-700">SCF 프로그램 효과 (2013년 이후)</h4>
                            <p>DPO 증가 + 재고/매출채권 감소 → CCC 대폭 개선</p>
                            <p class="text-sm text-gray-600 mt-2">→ 공급업체 관계 유지하면서 현금흐름 최적화</p>
                        </div>
                        <div class="bg-white p-4 rounded shadow">
                            <h4 class="font-bold text-blue-700">2015년 운전자본 혁신</h4>
                            <p>DSO/DIO 최저치 + DPO 최고치 = 마이너스 CCC</p>
                            <p class="text-sm text-gray-600 mt-2">→ 매출 감소에도 현금흐름 개선 효과 입증</p>
                        </div>
                    </div>
                </div>
                
                <!-- SCF 프로그램 영향 분석 -->
                <div class="bg-blue-50 p-6 rounded-lg">
                    <h3 class="text-xl font-semibold mb-4 text-center text-blue-800">공급망 금융(SCF) 프로그램의 영향</h3>
                    <ul class="list-disc pl-6 space-y-3">
                        <li><span class="font-semibold">벤치마킹 결과 반영</span>: 경쟁사 대비 낮은 DPO(45일)를 75일로 연장</li>
                        <li><span class="font-semibold">주주수익률(TSR) 개선</span>: 현금흐름 증가로 배당금 지급 능력 강화</li>
                        <li><span class="font-semibold">운전자본 효율화</span>: 15년간 CCC 52일 개선 (48.8일 → -3.5일)</li>
                        <li><span class="font-semibold">공급업체 부담 경감</span>: 결제 연장과 동시에 조기 결제 옵션 제공</li>
                        <li><span class="font-semibold">산업 리더십</span>: 운전자본 관리에서 업계 최고 수준 달성</li>
                    </ul>
                </div>
            </div>
            
            <script>
                // 타임라인 데이터
                const timelineData = {timeline_json};
                
                // 타임라인 요소 생성
                const timelineContainer = document.getElementById('timeline-container');
                timelineData.forEach((item, index) => {{
                    const timelineItem = document.createElement('div');
                    timelineItem.className = 'timeline-item relative mb-10';
                    
                    const timelineNumber = document.createElement('div');
                    timelineNumber.className = 'timeline-number';
                    timelineNumber.textContent = index + 1;
                    
                    const timelineContent = document.createElement('div');
                    timelineContent.className = 'bg-blue-50 p-4 rounded-lg shadow';
                    
                    const timelineYear = document.createElement('h4');
                    timelineYear.className = 'font-bold text-blue-700';
                    timelineYear.textContent = item.year;
                    
                    const timelineEvent = document.createElement('p');
                    timelineEvent.textContent = item.event;
                    
                    timelineContent.appendChild(timelineYear);
                    timelineContent.appendChild(timelineEvent);
                    
                    timelineItem.appendChild(timelineNumber);
                    timelineItem.appendChild(timelineContent);
                    
                    timelineContainer.appendChild(timelineItem);
                }});
                
                {chart_script}
            </script>
        </body>
        </html>
        """
        
        return html
    
    def _create_chart_script(self, extended_working_capital_json: str) -> str:
        """
        차트 스크립트 생성
        
        Args:
            extended_working_capital_json: 확장된 운전자본 데이터 JSON 문자열
            
        Returns:
            str: 차트 스크립트
        """
        return f"""
            // 데이터 설정
            const data = {extended_working_capital_json};
            
            // 차트 색상 설정
            const colors = {{
                dso: 'rgba(136, 132, 216, 0.8)',
                dio: 'rgba(130, 202, 157, 0.8)',
                dpo: 'rgba(255, 128, 66, 0.8)',
                ccc: 'rgba(255, 0, 0, 0.8)',
                adjustedDpo: 'rgba(153, 102, 255, 0.8)'
            }};
            
            // 1. 운전자본 관리 핵심 지표 추이 차트
            const wcMetricsCtx = document.getElementById('wcMetricsChart').getContext('2d');
            new Chart(wcMetricsCtx, {{
                type: 'line',
                data: {{
                    labels: data.map(d => d.year),
                    datasets: [
                        {{
                            label: '매출채권회수기간(DSO)',
                            data: data.map(d => d.dso),
                            borderColor: colors.dso,
                            backgroundColor: colors.dso,
                            fill: false,
                            borderWidth: 2
                        }},
                        {{
                            label: '재고자산회전기간(DIO)',
                            data: data.map(d => d.dio),
                            borderColor: colors.dio,
                            backgroundColor: colors.dio,
                            fill: false,
                            borderWidth: 2
                        }},
                        {{
                            label: '매입채무지급기간(DPO)',
                            data: data.map(d => d.dpo),
                            borderColor: colors.dpo,
                            backgroundColor: colors.dpo,
                            fill: false,
                            borderWidth: 2
                        }},
                        {{
                            label: '현금전환주기(CCC)',
                            data: data.map(d => d.ccc),
                            borderColor: colors.ccc,
                            backgroundColor: colors.ccc,
                            fill: false,
                            borderWidth: 3
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'bottom'
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let value = context.raw;
                                    return context.dataset.label + ': ' + value + ' 일';
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            min: -10,
                            max: 90,
                            title: {{
                                display: true,
                                text: '일수'
                            }}
                        }}
                    }},
                    interaction: {{
                        intersect: false,
                        mode: 'index'
                    }}
                }}
            }});
            
            // 2. 현금전환주기 변화 차트
            const cccCtx = document.getElementById('cccChart').getContext('2d');
            new Chart(cccCtx, {{
                type: 'bar',
                data: {{
                    labels: data.map(d => d.year),
                    datasets: [
                        {{
                            label: '현금전환주기(CCC)',
                            data: data.map(d => d.ccc),
                            backgroundColor: colors.ccc,
                            borderColor: colors.ccc,
                            borderWidth: 1
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'bottom'
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let value = context.raw;
                                    return context.dataset.label + ': ' + value + ' 일';
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            min: -10,
                            max: 60,
                            title: {{
                                display: true,
                                text: '일수'
                            }}
                        }}
                    }}
                }}
            }});
            
            // 3. 매입채무지급기간(DPO) 변화 차트
            const dpoCtx = document.getElementById('dpoChart').getContext('2d');
            new Chart(dpoCtx, {{
                type: 'line',
                data: {{
                    labels: data.map(d => d.year),
                    datasets: [
                        {{
                            label: '매입채무지급기간(DPO)',
                            data: data.map(d => d.dpo),
                            borderColor: colors.dpo,
                            backgroundColor: colors.dpo,
                            fill: false,
                            borderWidth: 3
                        }},
                        {{
                            label: '조정된 DPO',
                            data: data.map(d => d.adjustedDpo),
                            borderColor: colors.adjustedDpo,
                            backgroundColor: colors.adjustedDpo,
                            fill: false,
                            borderWidth: 2,
                            pointRadius: 5
                        }}
                    ]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{
                        legend: {{
                            position: 'bottom'
                        }},
                        tooltip: {{
                            callbacks: {{
                                label: function(context) {{
                                    let value = context.raw;
                                    return context.dataset.label + ': ' + value + ' 일';
                                }}
                            }}
                        }}
                    }},
                    scales: {{
                        y: {{
                            min: 30,
                            max: 90,
                            title: {{
                                display: true,
                                text: '일수'
                            }}
                        }}
                    }}
                }}
            }});
        """ 