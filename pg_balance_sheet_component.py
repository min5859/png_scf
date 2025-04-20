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
        <h2>P&G 대차대조표 분석 (2011-2015)</h2>
        
        <!-- 자산, 부채, 자본 추이 -->
        <div class="chart-container">
            <h3>1. 자산, 부채, 자본 추이 (단위: 백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="assetsLiabilitiesChart"></canvas>
            </div>
        </div>
        
        <!-- 유동자산 vs 유동부채 -->
        <div class="chart-container">
            <h3>2. 유동자산 vs 유동부채 (단위: 백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="currentAssetsLiabilitiesChart"></canvas>
            </div>
        </div>
        
        <!-- 운전자본 관련 항목 -->
        <div class="chart-container">
            <h3>3. 운전자본 관련 항목 추이 (단위: 백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="workingCapitalComponentsChart"></canvas>
            </div>
        </div>
        
        <!-- 현금전환주기 -->
        <div class="chart-container">
            <h3>4. 현금전환주기(CCC) 추이 (단위: 일)</h3>
            <div style="height: 300px; width: 100%;">
                <canvas id="cashConversionCycleChart"></canvas>
            </div>
        </div>
        
        <!-- 현금 보유량과 부채 -->
        <div class="chart-container">
            <h3>5. 현금 보유량과 부채 (단위: 백만 달러)</h3>
            <div style="height: 400px; width: 100%;">
                <canvas id="cashDebtChart"></canvas>
            </div>
        </div>
        
        <!-- 인사이트 요약 -->
        <div class="box-blue">
            <h3 style="color: #1e40af;">핵심 인사이트</h3>
            <div class="insight-grid">
                <div class="insight-card">
                    <h4 class="insight-title">현금 보유량 증가</h4>
                    <p>2011년 27억 달러에서 2015년 116억 달러로 4배 이상 증가</p>
                    <p class="insight-note">→ 유동성 관리 강화 및 불확실성 대비</p>
                </div>
                <div class="insight-card">
                    <h4 class="insight-title">현금전환주기 개선</h4>
                    <p>2011년 22.4일에서 2015년 -3.5일로 대폭 개선</p>
                    <p class="insight-note">→ 공급망 금융의 효과 입증</p>
                </div>
                <div class="insight-card">
                    <h4 class="insight-title">매출채권 감소</h4>
                    <p>2014년 대비 2015년 매출채권 15억 달러 감소</p>
                    <p class="insight-note">→ 매출채권 회수 효율성 향상</p>
                </div>
                <div class="insight-card">
                    <h4 class="insight-title">유동비율 개선</h4>
                    <p>2011년 0.80에서 2015년 1.00으로 개선</p>
                    <p class="insight-note">→ 단기 재무 건전성 강화</p>
                </div>
            </div>
        </div>
        
        <!-- SCF 프로그램과의 연결성 -->
        <div class="box-yellow">
            <h3 style="color: #854d0e;">공급망 금융(SCF) 프로그램과의 연관성</h3>
            <ul class="list-disc">
                <li class="list-item-space"><span class="font-semibold">매입채무 유지</span>: 결제 기간 연장에도 매입채무 금액 유지 (약 82-83억 달러)</li>
                <li class="list-item-space"><span class="font-semibold">현금 증가</span>: 운전자본 최적화로 2014-2015년 현금 보유량 증가</li>
                <li class="list-item-space"><span class="font-semibold">재고자산 관리</span>: 2015년 재고자산 감소로 운전자본 추가 개선</li>
                <li class="list-item-space"><span class="font-semibold">부채비율 안정성</span>: 부채비율(32.5%)을 유지하며 신용등급(AA-) 보호</li>
                <li class="list-item-space"><span class="font-semibold">가시적 효과</span>: 현금전환주기 마이너스로 전환 - 공급업체 자금으로 운영 가능</li>
            </ul>
        </div>
    </div>
    
    <script>
        // JSON 데이터 파싱
        let balanceSheetData;
        let workingCapitalData;
        
        try {
            balanceSheetData = JSON.parse('__BALANCE_SHEET_DATA__');
            workingCapitalData = JSON.parse('__WORKING_CAPITAL_DATA__');
        } catch (e) {
            console.error('데이터 파싱 오류:', e);
            balanceSheetData = [];
            workingCapitalData = [];
        }
        
        // 금액 포맷팅 함수
        function formatCurrency(value) {
            return '$' + value.toLocaleString() + ' 백만';
        }
        
        function formatBillions(value) {
            return '$' + (value / 1000).toFixed(1) + 'B';
        }
        
        // 자산, 부채, 자본 추이 차트
        const assetsLiabilitiesCtx = document.getElementById('assetsLiabilitiesChart').getContext('2d');
        new Chart(assetsLiabilitiesCtx, {
            type: 'bar',
            data: {
                labels: balanceSheetData.map(item => item.year),
                datasets: [
                    {
                        label: '총자산',
                        data: balanceSheetData.map(item => item.totalAssets),
                        backgroundColor: '#8884d8',
                        borderColor: '#8884d8',
                        borderWidth: 1
                    },
                    {
                        label: '총부채',
                        data: balanceSheetData.map(item => item.totalLiabilities),
                        backgroundColor: '#ff8042',
                        borderColor: '#ff8042',
                        borderWidth: 1
                    },
                    {
                        label: '자본',
                        data: balanceSheetData.map(item => item.totalEquity),
                        backgroundColor: '#82ca9d',
                        borderColor: '#82ca9d',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return '$' + (value / 1000) + 'B';
                            }
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                label += formatCurrency(context.raw);
                                return label;
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
        
        // 유동자산 vs 유동부채 차트
        const currentAssetsLiabilitiesCtx = document.getElementById('currentAssetsLiabilitiesChart').getContext('2d');
        new Chart(currentAssetsLiabilitiesCtx, {
            type: 'bar',
            data: {
                labels: balanceSheetData.map(item => item.year),
                datasets: [
                    {
                        label: '유동자산',
                        data: balanceSheetData.map(item => item.currentAssets),
                        backgroundColor: '#8884d8',
                        borderColor: '#8884d8',
                        borderWidth: 1
                    },
                    {
                        label: '유동부채',
                        data: balanceSheetData.map(item => item.currentLiabilities),
                        backgroundColor: '#ff8042',
                        borderColor: '#ff8042',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return '$' + (value / 1000) + 'B';
                            }
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                label += formatCurrency(context.raw);
                                return label;
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
        const workingCapitalComponentsCtx = document.getElementById('workingCapitalComponentsChart').getContext('2d');
        new Chart(workingCapitalComponentsCtx, {
            type: 'bar',
            data: {
                labels: workingCapitalData.map(item => item.year),
                datasets: [
                    {
                        label: '매출채권',
                        data: workingCapitalData.map(item => item.accountsReceivable),
                        backgroundColor: '#8884d8',
                        borderColor: '#8884d8',
                        borderWidth: 1
                    },
                    {
                        label: '재고자산',
                        data: workingCapitalData.map(item => item.inventory),
                        backgroundColor: '#82ca9d',
                        borderColor: '#82ca9d',
                        borderWidth: 1
                    },
                    {
                        label: '매입채무',
                        data: workingCapitalData.map(item => item.accountsPayable),
                        backgroundColor: '#ff8042',
                        borderColor: '#ff8042',
                        borderWidth: 1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return '$' + (value / 1000) + 'B';
                            }
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                label += formatCurrency(context.raw);
                                return label;
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
        
        // 현금전환주기 차트
        const cashConversionCycleCtx = document.getElementById('cashConversionCycleChart').getContext('2d');
        new Chart(cashConversionCycleCtx, {
            type: 'line',
            data: {
                labels: workingCapitalData.map(item => item.year),
                datasets: [
                    {
                        label: '현금전환주기',
                        data: workingCapitalData.map(item => item.cashConversionCycle),
                        backgroundColor: 'rgba(136, 132, 216, 0.2)',
                        borderColor: '#8884d8',
                        borderWidth: 2,
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        tension: 0.1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        min: -5,
                        max: 25
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                label += context.raw + ' 일';
                                return label;
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
        
        // 현금 보유량과 부채 차트
        const cashDebtCtx = document.getElementById('cashDebtChart').getContext('2d');
        new Chart(cashDebtCtx, {
            type: 'line',
            data: {
                labels: balanceSheetData.map(item => item.year),
                datasets: [
                    {
                        label: '현금 및 단기투자',
                        data: balanceSheetData.map(item => item.cash),
                        backgroundColor: 'rgba(130, 202, 157, 0.2)',
                        borderColor: '#82ca9d',
                        borderWidth: 2,
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        tension: 0.1
                    },
                    {
                        label: '총부채',
                        data: balanceSheetData.map(item => item.totalDebt),
                        backgroundColor: 'rgba(255, 128, 66, 0.2)',
                        borderColor: '#ff8042',
                        borderWidth: 2,
                        pointRadius: 6,
                        pointHoverRadius: 8,
                        tension: 0.1
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        beginAtZero: true,
                        ticks: {
                            callback: function(value) {
                                return '$' + (value / 1000) + 'B';
                            }
                        }
                    }
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                let label = context.dataset.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                label += formatCurrency(context.raw);
                                return label;
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