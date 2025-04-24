import json
from data_provider import MarketDataProvider

class PGBalanceSheetComponentGenerator:
    """P&G 대차대조표 시각화 컴포넌트 생성 클래스"""
    
    def __init__(self, data_provider=None):
        """
        Args:
            data_provider: 시장 데이터를 제공하는 객체
        """
        self.data_provider = data_provider or MarketDataProvider()
    
    def generate_html(self):
        """Chart.js 컴포넌트를 포함한 HTML 코드를 생성하여 반환"""
        html_template = self._get_html_template()
        
        # 데이터를 JSON 문자열로 변환하여 삽입
        try:
            balance_sheet_data = json.dumps(self.data_provider.pg_balance_sheet_data)
            working_capital_data = json.dumps(self.data_provider.pg_working_capital_data)
        except Exception as e:
            print(f"JSON 직렬화 오류: {e}")
            balance_sheet_data = "[]"
            working_capital_data = "[]"
        
        # 데이터 플레이스홀더 치환
        html_template = html_template.replace("__BALANCE_SHEET_DATA__", balance_sheet_data)
        html_template = html_template.replace("__WORKING_CAPITAL_DATA__", working_capital_data)
        
        return html_template
    
    def _get_html_template(self):
        """HTML 템플릿 반환"""
        return """
<!DOCTYPE html>
<html>
<head>
    <title>P&G 대차대조표 분석</title>
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
        
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 40px;
            padding: 24px;
            background-color: white;
        }
        
        h2 {
            font-size: 1.5rem;
            font-weight: 700;
            text-align: center;
            color: #1e40af;
            margin-bottom: 0;
        }
        
        h3 {
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 12px;
            text-align: center;
        }
        
        .chart-container {
            width: 100%;
            margin-bottom: 16px;
        }
        
        .insight-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            width: 100%;
        }
        
        .insight-card {
            background-color: white;
            padding: 16px;
            border-radius: 4px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        .insight-title {
            font-weight: 700;
            color: #1d4ed8;
        }
        
        .insight-note {
            font-size: 0.875rem;
            color: #6b7280;
            margin-top: 8px;
        }
        
        .box-blue {
            background-color: #eff6ff;
            padding: 24px;
            border-radius: 8px;
            width: 100%;
        }
        
        .box-yellow {
            background-color: #fefce8;
            padding: 24px;
            border-radius: 8px;
            width: 100%;
        }
        
        .list-disc {
            padding-left: 24px;
            list-style-type: disc;
        }
        
        .list-item-space {
            margin-bottom: 8px;
        }
        
        .font-semibold {
            font-weight: 600;
        }
        
        @media (max-width: 768px) {
            .insight-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>P&G Balance Sheet (2011-2015)</h2>
        
        <!-- 자산 구조 변화 -->
        <div class="chart-container">
            <h3>1. P&G 자산 구조 변화 (백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="assetStructureChart"></canvas>
            </div>
        </div>
        
        <!-- 부채 및 자본 구조 -->
        <div class="chart-container">
            <h3>2. P&G 부채 및 자본 구조 (백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="liabEquityStructureChart"></canvas>
            </div>
        </div>
        
        <!-- 운전자본 관련 항목 -->
        <div class="chart-container">
            <h3>3. P&G 운전자본 관련 항목 변화</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="workingCapitalChart"></canvas>
            </div>
        </div>
        
        <!-- 현금 및 부채 추이 -->
        <div class="chart-container">
            <h3>4. P&G 현금 및 부채 추이</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="cashDebtChart"></canvas>
            </div>
        </div>
        
        <!-- SCF 도입 전후 비교 -->
        <div class="chart-container">
            <h3>5. SCF 도입 전후 비교 (2012 vs 2014, 백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="scfComparisonChart"></canvas>
            </div>
        </div>
        
        <!-- 핵심 인사이트 -->
        <div class="box-blue">
            <h3 style="color: #1e40af;">핵심 인사이트</h3>
            <div class="insight-grid">
                <div class="insight-card">
                    <h4 class="insight-title">운전자본 개선</h4>
                    <p>유동비율 0.80(2011) → 1.00(2015)으로 개선</p>
                    <p class="insight-note">→ SCF 프로그램이 운전자본 개선에 기여</p>
                </div>
                <div class="insight-card">
                    <h4 class="insight-title">현금보유 증가</h4>
                    <p>현금 및 투자자산이 4배 이상 증가 ($2.8B → $11.6B)</p>
                    <p class="insight-note">→ 금융 유연성 및 위기 대응력 강화</p>
                </div>
                <div class="insight-card">
                    <h4 class="insight-title">매출채권 관리 개선</h4>
                    <p>2015년 매출채권 $4,861백만, 2014년 대비 24% 감소</p>
                    <p class="insight-note">→ 효율적인 현금회수 체계 구축</p>
                </div>
                <div class="insight-card">
                    <h4 class="insight-title">순부채 감소</h4>
                    <p>순부채가 $29.2B(2011) → $18.7B(2015)로 크게 감소</p>
                    <p class="insight-note">→ 재무 건전성 강화 및 이자비용 절감</p>
                </div>
            </div>
        </div>
        
        <!-- SCF와 대차대조표의 연관성 -->
        <div class="box-yellow">
            <h3 style="color: #854d0e;">SCF와 대차대조표의 연관성</h3>
            <ul class="list-disc">
                <li class="list-item-space"><span class="font-semibold">매입채무 관리</span>: SCF를 통해 매입채무 지급 기간 연장(45일→75일)하면서도 공급업체와의 관계 유지</li>
                <li class="list-item-space"><span class="font-semibold">현금 관리 최적화</span>: 향상된 현금 보유력이 더 큰 재무적 유연성 제공</li>
                <li class="list-item-space"><span class="font-semibold">AA- 신용등급 유지</span>: 안정적인 부채구조 및 레버리지(~2.0)가 높은 신용등급 유지에 기여</li>
                <li class="list-item-space"><span class="font-semibold">운전자본 효율성</span>: 유동자산 대비 유동부채 비율 개선으로 자금 운용 효율성 향상</li>
                <li class="list-item-space"><span class="font-semibold">장기적 재무 구조 강화</span>: SCF는 단기적 현금흐름을 넘어 장기적 재무 건전성에 기여</li>
            </ul>
        </div>
    </div>
    
    <script>
        // JSON 데이터 파싱
        let balanceSheetData;
        
        try {
            balanceSheetData = JSON.parse('__BALANCE_SHEET_DATA__');
        } catch (e) {
            console.error('데이터 파싱 오류:', e);
            balanceSheetData = [];
        }
        
        // 금액 포맷팅 함수
        function formatCurrency(value) {
            return '$' + value.toLocaleString() + ' 백만';
        }
        
        // 데이터 전처리
        const processedData = balanceSheetData.map(item => ({
            ...item,
            // netDebt는 이미 데이터에 있으므로 계산 불필요
            currentRatio: item.currentRatio || (item.currentAssets / item.currentLiabilities)
        }));

        // 데이터 확인 로그
        console.log('Working Capital Data:', processedData.map(item => ({
            year: item.year,
            receivable: item.accountsReceivable,
            inventory: item.inventory,
            payable: item.accountsPayable,
            currentRatio: item.currentRatio
        })));
        
        // 자산 구조 차트
        const assetStructureCtx = document.getElementById('assetStructureChart').getContext('2d');
        new Chart(assetStructureCtx, {
            type: 'bar',
            data: {
                labels: balanceSheetData.map(item => item.year),
                datasets: [
                    {
                        label: '유동자산 비율',
                        data: balanceSheetData.map(item => Math.round(item.currentAssets / item.totalAssets * 100)),
                        type: 'line',
                        borderColor: '#ff9800',
                        borderWidth: 3,
                        yAxisID: 'y1',
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        pointBackgroundColor: '#ff9800',
                        pointBorderColor: '#ffffff',
                        pointBorderWidth: 2,
                        zIndex: 2
                    },
                    {
                        label: '유동자산',
                        data: balanceSheetData.map(item => item.currentAssets),
                        backgroundColor: '#90caf9',
                        stack: 'a',
                        zIndex: 1
                    },
                    {
                        label: '비유동자산',
                        data: balanceSheetData.map(item => item.totalAssets - item.currentAssets),
                        backgroundColor: '#2196f3',
                        stack: 'a',
                        zIndex: 1
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
                            text: '백만 달러'
                        }
                    },
                    y1: {
                        position: 'right',
                        beginAtZero: true,
                        max: 30,
                        title: {
                            display: true,
                            text: '비율 (%)'
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label.includes('비율')) {
                                    return label + ': ' + context.raw + '%';
                                }
                                return label + ': ' + formatCurrency(context.raw);
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
        
        // 부채 및 자본 구조 차트
        const liabEquityStructureCtx = document.getElementById('liabEquityStructureChart').getContext('2d');
        new Chart(liabEquityStructureCtx, {
            type: 'bar',
            data: {
                labels: balanceSheetData.map(item => item.year),
                datasets: [
                    {
                        label: '유동부채',
                        data: balanceSheetData.map(item => item.currentLiabilities),
                        backgroundColor: '#f44336',
                        stack: 'a'
                    },
                    {
                        label: '비유동부채',
                        data: balanceSheetData.map(item => item.totalLiabilities - item.currentLiabilities),
                        backgroundColor: '#ff9800',
                        stack: 'a'
                    },
                    {
                        label: '자본',
                        data: balanceSheetData.map(item => item.totalEquity),
                        backgroundColor: '#4caf50',
                        stack: 'a'
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
                            text: '백만 달러'
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + formatCurrency(context.raw);
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
        
        // 운전자본 관련 항목 차트
        const workingCapitalCtx = document.getElementById('workingCapitalChart').getContext('2d');
        new Chart(workingCapitalCtx, {
            type: 'bar',
            data: {
                labels: processedData.map(item => item.year),
                datasets: [
                    {
                        label: '매출채권',
                        data: processedData.map(item => item.accountsReceivable),
                        backgroundColor: '#90caf9',
                        order: 2,
                        yAxisID: 'y'
                    },
                    {
                        label: '재고자산',
                        data: processedData.map(item => item.inventory),
                        backgroundColor: '#c8e6c9',
                        order: 2,
                        yAxisID: 'y'
                    },
                    {
                        label: '매입채무',
                        data: processedData.map(item => item.accountsPayable),
                        backgroundColor: '#f44336',
                        order: 2,
                        yAxisID: 'y'
                    },
                    {
                        label: '순운전자본',
                        data: processedData.map(item => item.currentAssets - item.currentLiabilities),
                        type: 'line',
                        borderColor: '#9c27b0',
                        borderWidth: 2,
                        fill: false,
                        tension: 0.4,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        yAxisID: 'y',
                        order: 1
                    },
                    {
                        label: '유동비율',
                        data: processedData.map(item => item.currentRatio),
                        type: 'line',
                        borderColor: '#ff9800',
                        borderWidth: 3,
                        yAxisID: 'y1',
                        fill: false,
                        tension: 0.4,
                        pointRadius: 4,
                        pointHoverRadius: 6,
                        order: 0
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: true,
                            drawBorder: true
                        }
                    },
                    y: {
                        position: 'left',
                        beginAtZero: true,
                        grid: {
                            display: true,
                            drawBorder: true
                        },
                        title: {
                            display: true,
                            text: '백만 달러'
                        },
                        ticks: {
                            callback: function(value) {
                                return value.toLocaleString();
                            }
                        }
                    },
                    y1: {
                        position: 'right',
                        beginAtZero: true,
                        min: 0,
                        max: 1.2,
                        grid: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: '유동비율'
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        mode: 'index',
                        intersect: false,
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label === '유동비율') {
                                    return label + ': ' + context.raw.toFixed(2);
                                }
                                return label + ': ' + formatCurrency(context.raw);
                            }
                        }
                    },
                    legend: {
                        display: true,
                        position: 'top'
                    }
                }
            }
        });
        
        // 현금 및 부채 추이 차트
        const cashDebtCtx = document.getElementById('cashDebtChart').getContext('2d');
        new Chart(cashDebtCtx, {
            type: 'bar',
            data: {
                labels: processedData.map(item => item.year),
                datasets: [
                    {
                        label: '현금 및 투자자산',
                        data: processedData.map(item => item.cashAndInvestments),
                        backgroundColor: '#4caf50',
                        order: 1
                    },
                    {
                        label: '총부채',
                        data: processedData.map(item => item.totalDebt),
                        backgroundColor: '#f44336',
                        order: 1
                    },
                    {
                        label: '순부채',
                        data: processedData.map(item => item.netDebt),
                        type: 'line',
                        borderColor: '#9c27b0',
                        borderWidth: 2,
                        fill: false,
                        tension: 0.4,
                        order: 0
                    },
                    {
                        label: '현금자산 비율',
                        data: processedData.map(item => (item.cashAndInvestments / item.totalAssets * 100).toFixed(1)),
                        type: 'line',
                        borderColor: '#2196f3',
                        borderWidth: 2,
                        yAxisID: 'y1',
                        fill: false,
                        tension: 0.4,
                        order: 0
                    },
                    {
                        label: '부채자본비율',
                        data: processedData.map(item => item.debtToTotalCapital),
                        type: 'line',
                        borderColor: '#ff9800',
                        borderWidth: 2,
                        yAxisID: 'y1',
                        fill: false,
                        tension: 0.4,
                        order: 0
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: true,
                            drawBorder: true
                        }
                    },
                    y: {
                        position: 'left',
                        min: 0,
                        max: 35000,
                        grid: {
                            display: true,
                            drawBorder: true
                        },
                        title: {
                            display: true,
                            text: '백만 달러'
                        },
                        ticks: {
                            callback: function(value) {
                                return value.toLocaleString();
                            }
                        }
                    },
                    y1: {
                        position: 'right',
                        min: 0,
                        max: 40,
                        grid: {
                            display: false
                        },
                        title: {
                            display: true,
                            text: '비율 (%)'
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        mode: 'index',
                        intersect: false,
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label.includes('비율')) {
                                    return label + ': ' + context.raw + '%';
                                }
                                return label + ': ' + formatCurrency(context.raw);
                            }
                        }
                    },
                    legend: {
                        display: true,
                        position: 'top'
                    }
                }
            }
        });
        
        // SCF 도입 전후 비교 차트
        const scfComparisonData = [
            { name: '매출채권', before: 6068, after: 6386, change: 318 },
            { name: '재고', before: 6721, after: 6759, change: 38 },
            { name: '매입채무', before: 7920, after: 8461, change: 541 },
            { name: '운전자본', before: -2997, after: -2109, change: 888 }
        ];
        
        const scfComparisonCtx = document.getElementById('scfComparisonChart').getContext('2d');
        new Chart(scfComparisonCtx, {
            type: 'bar',
            data: {
                labels: scfComparisonData.map(item => item.name),
                datasets: [
                    {
                        label: 'SCF 도입 전 (2012)',
                        data: scfComparisonData.map(item => item.before),
                        backgroundColor: '#90caf9'
                    },
                    {
                        label: 'SCF 도입 후 (2014)',
                        data: scfComparisonData.map(item => item.after),
                        backgroundColor: '#2196f3'
                    },
                    {
                        label: '변화',
                        data: scfComparisonData.map(item => item.change),
                        backgroundColor: '#4caf50'
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
                            text: '백만 달러'
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return context.dataset.label + ': ' + formatCurrency(context.raw);
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