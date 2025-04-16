import json
from data_provider import MarketDataProvider

class PGBalanceSheetComponentGenerator:
    """P&G 대차대조표 데이터를 시각화하는 컴포넌트 생성기"""
    
    def __init__(self, data_provider=None):
        """데이터 제공자로 초기화"""
        self.data_provider = data_provider or MarketDataProvider()
        self.data = self.data_provider.get_all_data()
    
    def generate_html(self):
        """HTML 컴포넌트 생성"""
        balance_sheet_data = json.dumps(self.data["pgBalanceSheetData"])
        working_capital_data = json.dumps(self.data["pgWorkingCapitalData"])
        
        html_template = self._get_html_template()
        
        # 데이터를 템플릿에 삽입
        html = html_template.replace("__BALANCE_SHEET_DATA__", balance_sheet_data)
        html = html.replace("__WORKING_CAPITAL_DATA__", working_capital_data)
        
        return html
    
    def _get_html_template(self):
        """HTML 템플릿 가져오기"""
        return """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>P&G 대차대조표 분석 (2011-2015)</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        h1, h2, h3 {
            color: #0066cc;
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
        .chart-container {
            position: relative;
            margin: 20px 0 40px;
            background-color: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        .chart-row {
            display: flex;
            flex-wrap: wrap;
            margin: 0 -10px;
        }
        .chart-column {
            flex: 1;
            min-width: 300px;
            padding: 10px;
        }
        .insights-section {
            background-color: #f0f7ff;
            border-left: 4px solid #0066cc;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }
        .strategy-section {
            background-color: #f0fff4;
            border-left: 4px solid #00aa66;
            padding: 15px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }
        .metric-card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 15px;
            margin-bottom: 20px;
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #0066cc;
        }
        .metric-title {
            font-size: 14px;
            color: #666;
        }
        .tab-container {
            margin: 20px 0;
        }
        .tab-buttons {
            display: flex;
            border-bottom: 1px solid #ddd;
        }
        .tab-button {
            padding: 10px 20px;
            background-color: #f1f1f1;
            border: none;
            cursor: pointer;
            margin-right: 5px;
            border-radius: 5px 5px 0 0;
        }
        .tab-button.active {
            background-color: #0066cc;
            color: white;
        }
        .tab-content {
            display: none;
            padding: 20px;
            border: 1px solid #ddd;
            border-top: none;
            border-radius: 0 0 5px 5px;
        }
        .tab-content.active {
            display: block;
        }
        @media (max-width: 768px) {
            .chart-column {
                flex: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>P&G 대차대조표 분석 (2011-2015)</h1>
        
        <div class="chart-row">
            <div class="chart-column">
                <div class="chart-container">
                    <h2>자산, 부채, 자본 추이</h2>
                    <canvas id="balanceSheetOverview"></canvas>
                </div>
            </div>
            <div class="chart-column">
                <div class="chart-container">
                    <h2>유동자산 vs 유동부채</h2>
                    <canvas id="currentAssetsLiabilities"></canvas>
                </div>
            </div>
        </div>
        
        <div class="chart-row">
            <div class="chart-column">
                <div class="chart-container">
                    <h2>부채 자본 비율</h2>
                    <canvas id="debtToCapitalChart"></canvas>
                </div>
            </div>
            <div class="chart-column">
                <div class="chart-container">
                    <h2>현금전환주기 (CCC)</h2>
                    <canvas id="cashConversionCycleChart"></canvas>
                </div>
            </div>
        </div>
        
        <div class="chart-row">
            <div class="chart-column">
                <div class="chart-container">
                    <h2>운전자본 구성요소</h2>
                    <canvas id="workingCapitalComponentsChart"></canvas>
                </div>
            </div>
            <div class="chart-column">
                <div class="chart-container">
                    <h2>일수 지표 분석</h2>
                    <canvas id="daysMetricsChart"></canvas>
                </div>
            </div>
        </div>
        
        <div class="insights-section">
            <h2>운전자본 관리 인사이트</h2>
            <p>P&G는 2011년부터 2015년까지 현금전환주기(CCC)를 22.4일에서 -3.5일로 크게 개선했습니다. 이는 다음과 같은 요인에 기인합니다:</p>
            <ul>
                <li><strong>매출채권 관리 개선:</strong> 매출채권 회수 기간이 27.8일에서 23.3일로 감소</li>
                <li><strong>재고 관리 효율화:</strong> 재고 회전 기간이 32.6일에서 26.2일로 감소</li>
                <li><strong>매입채무 관리 최적화:</strong> 매입 지급 기간이 38.0일에서 53.0일로 증가</li>
            </ul>
            <p>특히 2015년에는 현금전환주기가 마이너스로 전환되어, 공급업체의 자금을 활용하여 운영 자금을 확보하는 효율적인 운전자본 관리를 달성했습니다.</p>
        </div>
        
        <div class="strategy-section">
            <h2>SCF(Supply Chain Finance) 전략 제안</h2>
            <p>P&G의 운전자본 관리 데이터를 기반으로 다음과 같은 SCF 전략을 제안합니다:</p>
            <ol>
                <li><strong>다이나믹 디스카운팅 프로그램:</strong> 공급업체에게 조기 지불 옵션을 제공하여 할인을 받고, 유동성을 개선</li>
                <li><strong>역 팩토링 솔루션:</strong> 공급업체에게 낮은 금리로 자금을 제공하는 동시에 P&G의 지불 기간 연장</li>
                <li><strong>재고 파이낸싱:</strong> 재고 보유 비용을 줄이면서 적정 재고 수준을 유지할 수 있는 재고 금융 솔루션 도입</li>
                <li><strong>매출채권 관리 최적화:</strong> 고객 신용 관리와 조기 결제 인센티브를 통한 매출채권 회수 기간 단축</li>
            </ol>
            <p>이러한 SCF 전략은 현금 흐름을 더욱 개선하고, 운영 효율성을 높이며, 공급망 전체의 금융 안정성을 강화할 것입니다.</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // 데이터 파싱
            const balanceSheetData = __BALANCE_SHEET_DATA__;
            const workingCapitalData = __WORKING_CAPITAL_DATA__;
            
            // 차트 데이터 준비
            const years = balanceSheetData.map(item => item.year);
            const totalAssets = balanceSheetData.map(item => item.totalAssets);
            const totalLiabilities = balanceSheetData.map(item => item.totalLiabilities);
            const totalEquity = balanceSheetData.map(item => item.totalEquity);
            const currentAssets = balanceSheetData.map(item => item.currentAssets);
            const currentLiabilities = balanceSheetData.map(item => item.currentLiabilities);
            const debtToCapitalRatio = balanceSheetData.map(item => item.debtToCapitalRatio * 100);
            
            const accountsReceivable = workingCapitalData.map(item => item.accountsReceivable);
            const inventory = workingCapitalData.map(item => item.inventory);
            const accountsPayable = workingCapitalData.map(item => item.accountsPayable);
            const daysReceivables = workingCapitalData.map(item => item.daysReceivables);
            const daysInventory = workingCapitalData.map(item => item.daysInventory);
            const daysPayables = workingCapitalData.map(item => item.daysPayables);
            const cashConversionCycle = workingCapitalData.map(item => item.cashConversionCycle);
            
            // 자산, 부채, 자본 추이 차트
            new Chart(document.getElementById('balanceSheetOverview'), {
                type: 'bar',
                data: {
                    labels: years,
                    datasets: [
                        {
                            label: '총 자산',
                            data: totalAssets,
                            backgroundColor: 'rgba(54, 162, 235, 0.7)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        },
                        {
                            label: '총 부채',
                            data: totalLiabilities,
                            backgroundColor: 'rgba(255, 99, 132, 0.7)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        },
                        {
                            label: '총 자본',
                            data: totalEquity,
                            backgroundColor: 'rgba(75, 192, 192, 0.7)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: '금액 (백만 달러)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'P&G 자산, 부채, 자본 추이 (2011-2015)'
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': $' + context.raw.toLocaleString() + ' 백만';
                                }
                            }
                        }
                    }
                }
            });
            
            // 유동자산 vs 유동부채 차트
            new Chart(document.getElementById('currentAssetsLiabilities'), {
                type: 'line',
                data: {
                    labels: years,
                    datasets: [
                        {
                            label: '유동 자산',
                            data: currentAssets,
                            borderColor: 'rgba(54, 162, 235, 1)',
                            backgroundColor: 'rgba(54, 162, 235, 0.1)',
                            fill: true,
                            tension: 0.1
                        },
                        {
                            label: '유동 부채',
                            data: currentLiabilities,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            backgroundColor: 'rgba(255, 99, 132, 0.1)',
                            fill: true,
                            tension: 0.1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: '금액 (백만 달러)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'P&G 유동자산 vs 유동부채 (2011-2015)'
                        }
                    }
                }
            });
            
            // 부채 자본 비율 차트
            new Chart(document.getElementById('debtToCapitalChart'), {
                type: 'line',
                data: {
                    labels: years,
                    datasets: [
                        {
                            label: '부채 자본 비율 (%)',
                            data: debtToCapitalRatio,
                            borderColor: 'rgba(153, 102, 255, 1)',
                            backgroundColor: 'rgba(153, 102, 255, 0.2)',
                            fill: true,
                            tension: 0.1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: '비율 (%)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'P&G 부채 자본 비율 (2011-2015)'
                        }
                    }
                }
            });
            
            // 현금전환주기 차트
            new Chart(document.getElementById('cashConversionCycleChart'), {
                type: 'line',
                data: {
                    labels: years,
                    datasets: [
                        {
                            label: '현금전환주기 (일)',
                            data: cashConversionCycle,
                            borderColor: 'rgba(255, 159, 64, 1)',
                            backgroundColor: 'rgba(255, 159, 64, 0.2)',
                            fill: true,
                            tension: 0.1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            title: {
                                display: true,
                                text: '일수'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'P&G 현금전환주기 (2011-2015)'
                        },
                        annotation: {
                            annotations: {
                                line1: {
                                    type: 'line',
                                    yMin: 0,
                                    yMax: 0,
                                    borderColor: 'rgb(150, 150, 150)',
                                    borderWidth: 2,
                                    borderDash: [5, 5]
                                }
                            }
                        }
                    }
                }
            });
            
            // 운전자본 구성요소 차트
            new Chart(document.getElementById('workingCapitalComponentsChart'), {
                type: 'bar',
                data: {
                    labels: years,
                    datasets: [
                        {
                            label: '매출채권',
                            data: accountsReceivable,
                            backgroundColor: 'rgba(54, 162, 235, 0.7)',
                            borderColor: 'rgba(54, 162, 235, 1)',
                            borderWidth: 1
                        },
                        {
                            label: '재고자산',
                            data: inventory,
                            backgroundColor: 'rgba(75, 192, 192, 0.7)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        },
                        {
                            label: '매입채무',
                            data: accountsPayable,
                            backgroundColor: 'rgba(255, 99, 132, 0.7)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: '금액 (백만 달러)'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'P&G 운전자본 구성요소 (2011-2015)'
                        }
                    }
                }
            });
            
            // 일수 지표 분석 차트
            new Chart(document.getElementById('daysMetricsChart'), {
                type: 'line',
                data: {
                    labels: years,
                    datasets: [
                        {
                            label: '매출채권 회수 기간 (일)',
                            data: daysReceivables,
                            borderColor: 'rgba(54, 162, 235, 1)',
                            backgroundColor: 'transparent',
                            tension: 0.1
                        },
                        {
                            label: '재고 회전 기간 (일)',
                            data: daysInventory,
                            borderColor: 'rgba(75, 192, 192, 1)',
                            backgroundColor: 'transparent',
                            tension: 0.1
                        },
                        {
                            label: '매입 지급 기간 (일)',
                            data: daysPayables,
                            borderColor: 'rgba(255, 99, 132, 1)',
                            backgroundColor: 'transparent',
                            tension: 0.1
                        }
                    ]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: '일수'
                            }
                        }
                    },
                    plugins: {
                        title: {
                            display: true,
                            text: 'P&G 일수 지표 분석 (2011-2015)'
                        }
                    }
                }
            });
        });
    </script>
</body>
</html>
        """ 