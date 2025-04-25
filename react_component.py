import json
from data_provider import MarketDataProvider

class ReactComponentGenerator:
    """React 컴포넌트 HTML 코드를 생성하는 클래스"""
    
    def __init__(self, data_provider: MarketDataProvider):
        """
        Args:
            data_provider: 시장 데이터를 제공하는 객체
        """
        self.data_provider = data_provider
    
    def generate_html(self) -> str:
        """React 컴포넌트를 포함한 HTML 코드를 생성하여 반환"""
        html_template = self._get_html_template()
        data_dict = self.data_provider.get_all_data()
        
        # 데이터 디버깅 (로그에 데이터 출력)
        for key, value in data_dict.items():
            print(f"데이터 키: {key}, 타입: {type(value)}, 길이: {len(value) if hasattr(value, '__len__') else 'N/A'}")
            print(f"데이터 샘플: {str(value)[:100]}...")
        
        # 데이터를 HTML에 삽입 - JSON 문자열로 변환하여 삽입
        for key, value in data_dict.items():
            placeholder = f"{key.upper()}_PLACEHOLDER"
            
            # JSON 직렬화 시 오류 방지를 위한 안전한 변환
            try:
                json_data = json.dumps(value, ensure_ascii=False)
                # JSON 문자열에서 따옴표를 HTML 엔티티로 변환하여 충돌 방지
                # json_data = json_data.replace('"', '&quot;')
            except Exception as e:
                print(f"JSON 직렬화 오류 ({key}): {e}")
                # 오류 발생 시 빈 배열로 대체
                json_data = "[]"
            
            # 플레이스홀더 치환
            if placeholder in html_template:
                html_template = html_template.replace(placeholder, json_data)
                print(f"플레이스홀더 {placeholder} 치환 완료")
            else:
                print(f"경고: 플레이스홀더 {placeholder}를 찾을 수 없음")
        
        return html_template
    
    def _get_html_template(self) -> str:
        """HTML 템플릿 반환 - 수정된 버전"""
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Market Rates Analysis</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <!-- Chart.js 라이브러리만 로드 -->
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
                .chart-subtitle {
                    font-size: 16px;
                    font-weight: bold;
                    text-align: center;
                    margin-bottom: 5px;
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
                ul {
                    margin-top: 5px;
                }
                @media (max-width: 768px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }
                }
                .react-title {
                    font-size: 2.5rem;
                    font-weight: bold;
                    color: #111827;
                    margin-bottom: 1.5rem;
                }
                .react-value {
                    font-size: 1.8rem;
                    font-weight: bold;
                    color: #2563EB;
                }
                .react-description {
                    font-size: 1.3rem;
                    color: #4B5563;
                    line-height: 1.5;
                }
            </style>
        </head>
        <body>
            <div id="root">
                <div style="padding: 10px;">
                    <!-- 차트 컨테이너 -->
                    <div class="chart-container">
                        <div class="chart-title">1. 미국 국채 수익률 곡선 (2015년 8월 7일)</div>
                        <div style="height: 400px; width: 100%;">
                            <canvas id="treasuryYieldsChart"></canvas>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <div class="chart-title">2. 신용등급별 회사채 수익률 (1년 만기)</div>
                        <div style="height: 400px; width: 100%;">
                            <canvas id="corporateBondYieldsChart"></canvas>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <div class="chart-title">3. 단기 금리 현황</div>
                        <div style="height: 400px; width: 100%;">
                            <canvas id="shortTermRatesChart"></canvas>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <div class="chart-title">4. SCF 할인율 시뮬레이션</div>
                        <div class="grid">
                            <div>
                                <div class="chart-subtitle">SCF 할인율 구성 요소</div>
                                <div style="height: 300px;">
                                    <canvas id="scfRateSimulationChart1"></canvas>
                                </div>
                            </div>
                            <div>
                                <div class="chart-subtitle">시나리오별 연간 SCF 비용 (P&G 거래 기준)</div>
                                <div style="height: 300px;">
                                    <canvas id="scfRateSimulationChart2"></canvas>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <div class="chart-title">5. 신용등급별 자금조달 비용 비교</div>
                        <div style="height: 400px; width: 100%;">
                            <canvas id="ratingsComparisonChart"></canvas>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <div class="chart-title">6. 3개월 LIBOR 추이 (2012-2015)</div>
                        <div style="height: 300px; width: 100%;">
                            <canvas id="historicalLiborChart"></canvas>
                        </div>
                    </div>
                    
                    <!-- 핵심 인사이트 -->
                    <div class="chart-container">
                        <div class="chart-title">핵심 인사이트</div>
                        <div class="grid">
                            <div class="insight-box">
                                <div class="insight-title">저금리 환경</div>
                                <p>3개월 LIBOR 0.30%의 역사적 저점 수준</p>
                                <p style="font-size: 0.9em; color: #666;">→ SCF 협상에 유리한 시점</p>
                            </div>
                            <div class="insight-box">
                                <div class="insight-title">신용등급 프리미엄</div>
                                <p>AAA에서 CCC까지 4.1%p 이상의 수익률 차이</p>
                                <p style="font-size: 0.9em; color: #666;">→ P&G의 AA- 등급 활용 가치 입증</p>
                            </div>
                            <div class="insight-box">
                                <div class="insight-title">SCF 비용 구성</div>
                                <p>현재 시장에서 3개월 LIBOR + 0.7~0.8%p 협상 가능성</p>
                                <p style="font-size: 0.9em; color: #666;">→ 현 계약(1.0%p 스프레드)보다 0.2~0.3%p 절감 가능</p>
                            </div>
                            <div class="insight-box">
                                <div class="insight-title">단기 금리 전망</div>
                                <p>수익률 곡선이 우상향하는 형태로 금리 인상 예상</p>
                                <p style="font-size: 0.9em; color: #666;">→ 장기 계약 조건 확보의 중요성</p>
                            </div>
                        </div>
                    </div>
                    
                    <!-- SCF 은행 선택에 관한 시사점 -->
                    <div class="chart-container">
                        <div class="chart-title">SCF 은행 선택에 관한 시사점</div>
                        <div class="warning-box">
                            <ul>
                                <li><strong>스프레드 협상 여지</strong>: 현재 시장 상황은 0.2~0.3%p 스프레드 인하 협상에 유리 → P&G 거래액($300M) 기준 연간 $60-90만 절감 가능</li>
                                <li><strong>신용등급 활용 가치</strong>: BBB- 등급(피브리아)과 AA- 등급(P&G) 사이 약 0.5%p 비용 차이 → SCF를 통한 신용등급 차이 활용으로 연간 $150만 이상 절감</li>
                                <li><strong>금리 상승 리스크</strong>: 수익률 곡선이 시사하는 향후 금리 인상 가능성 → 장기 고정 스프레드 계약의 가치</li>
                                <li><strong>은행 경쟁 활용</strong>: 저금리 환경에서 은행 간 경쟁 활용 → 시티그룹과 JPMorgan Chase 양측 입찰을 통한 최적 조건 확보</li>
                                <li><strong>총비용 관점</strong>: 단순 할인율 외에도 서비스, 안정성, 관계 등 고려 → 할인율 0.05%p 차이는 연간 $15만 수준으로 다른 요소와 균형 필요</li>
                            </ul>
                        </div>
                    </div>
                    
                    <!-- 최적 결정 방향 -->
                    <div class="chart-container">
                        <div class="chart-title">최적 결정 방향</div>
                        <div class="grid">
                            <div class="success-box">
                                <h4 style="margin: 0 0 10px 0;">선택지 1: 시티그룹 유지 + 조건 개선</h4>
                                <ul>
                                    <li>현 스프레드(1.00%)에서 최소 0.2%p 인하 협상</li>
                                    <li>장기 관계 및 브라질 본사 거래 활용</li>
                                    <li>안정적인 서비스 및 검증된 플랫폼 유지</li>
                                    <li>약 $60만/년 비용 절감 효과</li>
                                </ul>
                            </div>
                            <div class="success-box">
                                <h4 style="margin: 0 0 10px 0;">선택지 2: JPMorgan으로 전환 + 관계 다변화</h4>
                                <ul>
                                    <li>더 공격적인 스프레드(0.7-0.8%) 확보 가능</li>
                                    <li>금융 파트너 다변화로 리스크 분산</li>
                                    <li>새로운 관계 구축에 따른 초기 비용 감수</li>
                                    <li>약 $60-90만/년 비용 절감 효과</li>
                                </ul>
                            </div>
                        </div>
                        <div class="success-box" style="margin-top: 20px;">
                            <h4 style="margin: 0 0 10px 0; text-align: center;">균형 잡힌 접근법</h4>
                            <p>
                                양 은행 모두에게 제안 요청 → 시티그룹에 JPMorgan 조건 공개 → 최적 조건 확보 → 
                                비용 차이가 크지 않을 경우 시티그룹 유지하며 일부 거래를 JPMorgan으로 분산 → 
                                장기적으로 두 은행 간 경쟁 구도 유지
                            </p>
                        </div>
                    </div>
                    
                    <!-- 로딩 표시 (기본적으로 숨김) -->
                    <div id="loading-indicator" style="display: none; text-align: center; padding: 30px; font-size: 18px; color: #666;">
                        <div>데이터를 로드 중입니다...</div>
                        <div style="width: 50%; height: 4px; margin: 10px auto; background: #f0f0f0; border-radius: 2px; overflow: hidden; position: relative;">
                            <div style="position: absolute; left: 0; top: 0; height: 100%; width: 30%; background: #8884d8; animation: loading 1.5s infinite;"></div>
                        </div>
                        <style>
                            @keyframes loading {
                                0% { left: -30%; }
                                100% { left: 100%; }
                            }
                        </style>
                    </div>
                    
                    <!-- 오류 표시 (기본적으로 숨김) -->
                    <div id="error-display" style="display: none; padding: 20px; background: #fff3f3; border: 1px solid #ffcdd2; border-radius: 8px; color: #b71c1c; margin: 20px;">
                        <h3>오류가 발생했습니다</h3>
                        <p id="error-message"></p>
                        <p><small>브라우저 콘솔(F12)에서 자세한 오류 정보를 확인하세요.</small></p>
                    </div>
                </div>
            </div>

            <!-- 데이터 스크립트 태그: 숨겨진 형태로 React 컴포넌트에 데이터 전달 -->
            <script id="treasury-yields-data" type="application/json">
                TREASURYYIELDSDATA_PLACEHOLDER
            </script>
            <script id="corporate-bond-yields-data" type="application/json">
                CORPORATEBONDYIELDSDATA_PLACEHOLDER
            </script>
            <script id="short-term-rates-data" type="application/json">
                SHORTTERMRATESDATA_PLACEHOLDER
            </script>
            <script id="scf-rate-simulation-data" type="application/json">
                SCFRATESIMULATIONDATA_PLACEHOLDER
            </script>
            <script id="ratings-comparison-data" type="application/json">
                RATINGSCOMPARISONDATA_PLACEHOLDER
            </script>
            <script id="historical-libor-data" type="application/json">
                HISTORICALLIBORDATA_PLACEHOLDER
            </script>

            <script>
                // 디버그 모드
                const DEBUG_MODE = true;
                
                // 디버그 로그 함수
                function debugLog(message, data) {
                    if (DEBUG_MODE) {
                        console.log(`[DEBUG] ${message}`, data || '');
                    }
                }
                
                // 디버그 오류 로그 함수
                function debugError(message, error) {
                    console.error(`[ERROR] ${message}`, error || '');
                }
                
                // 샘플 데이터 - 플레이스홀더 치환이 실패한 경우를 대비
                const SAMPLE_DATA = {
                    treasuryYieldsData: [
                        { maturity: '1M', yield: 0.01 },
                        { maturity: '3M', yield: 0.05 },
                        { maturity: '6M', yield: 0.10 },
                        { maturity: '1Y', yield: 0.30 },
                        { maturity: '2Y', yield: 0.65 },
                        { maturity: '5Y', yield: 1.50 },
                        { maturity: '10Y', yield: 2.20 },
                        { maturity: '30Y', yield: 2.85 }
                    ],
                    corporateBondYieldsData: [
                        { rating: 'AAA', yield: 0.75 },
                        { rating: 'AA', yield: 1.05 },
                        { rating: 'A', yield: 1.40 },
                        { rating: 'BBB', yield: 2.10 },
                        { rating: 'BB', yield: 3.25 },
                        { rating: 'B', yield: 4.20 },
                        { rating: 'CCC', yield: 4.85 }
                    ],
                    shortTermRatesData: [
                        { type: 'Overnight', rate: 0.15 },
                        { type: '1주', rate: 0.20 },
                        { type: '2주', rate: 0.22 },
                        { type: '1개월', rate: 0.25 },
                        { type: '3개월', rate: 0.30 }
                    ],
                    scfRateSimulationData: [
                        { scenario: '현재', libor: 0.30, spread: 1.00, costYear: 1.30 },
                        { scenario: '협상 A', libor: 0.30, spread: 0.80, costYear: 1.10 },
                        { scenario: '협상 B', libor: 0.30, spread: 0.70, costYear: 1.00 }
                    ],
                    ratingsComparisonData: [
                        { rating: 'AAA', borrowingCost: 0.75, scfDiscount: 0.75, costDifference: 0.00 },
                        { rating: 'AA', borrowingCost: 1.05, scfDiscount: 0.80, costDifference: 0.25 },
                        { rating: 'A', borrowingCost: 1.40, scfDiscount: 0.85, costDifference: 0.55 },
                        { rating: 'BBB', borrowingCost: 2.10, scfDiscount: 0.90, costDifference: 1.20 },
                        { rating: 'BB', borrowingCost: 3.25, scfDiscount: 1.10, costDifference: 2.15 }
                    ],
                    historicalLiborData: [
                        { date: '2012년', libor3m: 0.40 },
                        { date: '2013년', libor3m: 0.35 },
                        { date: '2014년', libor3m: 0.32 },
                        { date: '2015년', libor3m: 0.30 }
                    ]
                };
                
                // 데이터 로드 및 파싱 함수
                function getDataFromJson() {
                    debugLog('데이터 파싱 시작');
                    const dataMap = {
                        'treasuryYieldsData': 'treasury-yields-data', 
                        'corporateBondYieldsData': 'corporate-bond-yields-data',
                        'shortTermRatesData': 'short-term-rates-data',
                        'scfRateSimulationData': 'scf-rate-simulation-data',
                        'ratingsComparisonData': 'ratings-comparison-data',
                        'historicalLiborData': 'historical-libor-data'
                    };
                    
                    const result = {};
                    let useSampleData = false;
                    
                    // 각 데이터 요소를 개별적으로 로드하고 오류 처리
                    for (const [key, id] of Object.entries(dataMap)) {
                        try {
                            const element = document.getElementById(id);
                            if (!element) {
                                debugError(`Element with id ${id} not found`);
                                result[key] = SAMPLE_DATA[key] || [];
                                useSampleData = true;
                                continue;
                            }
                            
                            const content = element.textContent.trim();
                            if (!content || content.includes('PLACEHOLDER')) {
                                debugError(`Element with id ${id} has invalid content: ${content.substring(0, 20)}...`);
                                result[key] = SAMPLE_DATA[key] || [];
                                useSampleData = true;
                                continue;
                            }
                            
                            // 디버깅을 위해 원본 데이터 출력
                            debugLog(`Raw data for ${key}`, content.substring(0, 50) + '...');
                            
                            // JSON 파싱 시도
                            try {
                                result[key] = JSON.parse(content);
                                debugLog(`Parsed ${key} successfully`, result[key]);
                            } catch (parseError) {
                                debugError(`JSON parsing error for ${key}`, parseError);
                                result[key] = SAMPLE_DATA[key] || [];
                                useSampleData = true;
                            }
                        } catch (error) {
                            debugError(`Error processing ${key}`, error);
                            result[key] = SAMPLE_DATA[key] || [];
                            useSampleData = true;
                        }
                    }
                    
                    if (useSampleData) {
                        debugLog('⚠️ 일부 샘플 데이터를 사용합니다!', result);
                    }
                    
                    debugLog('데이터 파싱 완료', Object.keys(result));
                    return result;
                }
                
                // 차트 생성 함수들
                function createTreasuryYieldsChart(data) {
                    console.log('Treasury data:', data);
                    
                    // 데이터가 배열인지 확인하고 아니면 빈 배열로 기본값 설정
                    const chartData = Array.isArray(data) ? data : [];
                    const ctx = document.getElementById('treasuryYieldsChart').getContext('2d');
                    
                    return new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: chartData.map(item => item.maturity || ''),
                            datasets: [{
                                label: '수익률',
                                data: chartData.map(item => item.yield || 0),
                                backgroundColor: 'rgba(136, 132, 216, 0.2)',
                                borderColor: '#8884d8',
                                borderWidth: 2,
                                tension: 0.1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 3,
                                    title: {
                                        display: true,
                                        text: '수익률 (%)'
                                    }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: '만기'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
                
                function createCorporateBondYieldsChart(data) {
                    console.log('Corporate bond data:', data);
                    
                    // 데이터가 배열인지 확인하고 아니면 빈 배열로 기본값 설정
                    const chartData = Array.isArray(data) ? data : [];
                    const ctx = document.getElementById('corporateBondYieldsChart').getContext('2d');
                    
                    return new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: chartData.map(item => item.rating || ''),
                            datasets: [{
                                label: '수익률',
                                data: chartData.map(item => item.yield || 0),
                                backgroundColor: '#82ca9d',
                                borderColor: '#82ca9d',
                                borderWidth: 1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 5,
                                    title: {
                                        display: true,
                                        text: '수익률 (%)'
                                    }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: '신용등급'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
                
                function createShortTermRatesChart(data) {
                    console.log('Short term rates data:', data);
                    
                    // 데이터가 배열인지 확인하고 아니면 빈 배열로 기본값 설정
                    const chartData = Array.isArray(data) ? data : [];
                    const ctx = document.getElementById('shortTermRatesChart').getContext('2d');
                    
                    return new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: chartData.map(item => item.type || ''),
                            datasets: [{
                                label: '금리',
                                data: chartData.map(item => item.rate || 0),
                                backgroundColor: '#8884d8',
                                borderColor: '#8884d8',
                                borderWidth: 1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 0.6,
                                    title: {
                                        display: true,
                                        text: '금리 (%)'
                                    }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: '유형'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
                
                function createScfRateSimulationCharts(data) {
                    console.log('SCF rate simulation data:', data);
                    
                    // 데이터가 배열인지 확인하고 아니면 빈 배열로 기본값 설정
                    const chartData = Array.isArray(data) ? data : [];
                    
                    // 첫 번째 차트: SCF 할인율 구성 요소
                    const ctx1 = document.getElementById('scfRateSimulationChart1').getContext('2d');
                    const chart1 = new Chart(ctx1, {
                        type: 'bar',
                        data: {
                            labels: chartData.map(item => item.scenario || ''),
                            datasets: [
                                {
                                    label: 'LIBOR',
                                    data: chartData.map(item => item.libor || 0),
                                    backgroundColor: '#8884d8',
                                    borderColor: '#8884d8',
                                    borderWidth: 1,
                                    stack: 'stack0'
                                },
                                {
                                    label: '스프레드',
                                    data: chartData.map(item => item.spread || 0),
                                    backgroundColor: '#82ca9d',
                                    borderColor: '#82ca9d',
                                    borderWidth: 1,
                                    stack: 'stack0'
                                }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 2,
                                    stacked: true,
                                    title: {
                                        display: true,
                                        text: '비율 (%)'
                                    }
                                },
                                x: {
                                    stacked: true,
                                    title: {
                                        display: true,
                                        text: '시나리오'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.dataset.label}: ${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                    
                    // 두 번째 차트: 시나리오별 연간 SCF 비용
                    const ctx2 = document.getElementById('scfRateSimulationChart2').getContext('2d');
                    const chart2 = new Chart(ctx2, {
                        type: 'bar',
                        data: {
                            labels: chartData.map(item => item.scenario || ''),
                            datasets: [{
                                label: '연간 비용 (% of 거래액)',
                                data: chartData.map(item => item.costYear || 0),
                                backgroundColor: '#ff8042',
                                borderColor: '#ff8042',
                                borderWidth: 1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 1.5,
                                    title: {
                                        display: true,
                                        text: '비율 (%)'
                                    }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: '시나리오'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                    
                    return [chart1, chart2];
                }
                
                function createRatingsComparisonChart(data) {
                    console.log('Ratings comparison data:', data);
                    
                    // 데이터가 배열인지 확인하고 아니면 빈 배열로 기본값 설정
                    const chartData = Array.isArray(data) ? data : [];
                    const ctx = document.getElementById('ratingsComparisonChart').getContext('2d');
                    
                    return new Chart(ctx, {
                        type: 'bar',
                        data: {
                            labels: chartData.map(item => item.rating || ''),
                            datasets: [
                                {
                                    label: '일반 자금조달 비용',
                                    data: chartData.map(item => item.borrowingCost || 0),
                                    backgroundColor: '#ff8042',
                                    borderColor: '#ff8042',
                                    borderWidth: 1
                                },
                                {
                                    label: 'SCF 할인율',
                                    data: chartData.map(item => item.scfDiscount || 0),
                                    backgroundColor: '#82ca9d',
                                    borderColor: '#82ca9d',
                                    borderWidth: 1
                                },
                                {
                                    label: '비용 차이',
                                    data: chartData.map(item => item.costDifference || 0),
                                    backgroundColor: '#8884d8',
                                    borderColor: '#8884d8',
                                    borderWidth: 1
                                }
                            ]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 3,
                                    title: {
                                        display: true,
                                        text: '비율 (%)'
                                    }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: '신용등급'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.dataset.label}: ${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
                
                function createHistoricalLiborChart(data) {
                    console.log('Historical LIBOR data:', data);
                    
                    // 데이터가 배열인지 확인하고 아니면 빈 배열로 기본값 설정
                    const chartData = Array.isArray(data) ? data : [];
                    const ctx = document.getElementById('historicalLiborChart').getContext('2d');
                    
                    return new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: chartData.map(item => item.date || ''),
                            datasets: [{
                                label: '3개월 LIBOR',
                                data: chartData.map(item => item.libor3m || 0),
                                backgroundColor: 'rgba(136, 132, 216, 0.2)',
                                borderColor: '#8884d8',
                                borderWidth: 2,
                                tension: 0.1
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            scales: {
                                y: {
                                    beginAtZero: true,
                                    max: 0.5,
                                    title: {
                                        display: true,
                                        text: 'LIBOR (%)'
                                    }
                                },
                                x: {
                                    title: {
                                        display: true,
                                        text: '날짜'
                                    }
                                }
                            },
                            plugins: {
                                tooltip: {
                                    callbacks: {
                                        label: function(context) {
                                            return `${context.formattedValue}%`;
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
                
                // 메인 함수 - 페이지 로드 시 실행
                document.addEventListener('DOMContentLoaded', function() {
                    console.log('페이지 로드됨, 데이터 로드 시작...');
                    
                    // 로딩 표시기 보이기
                    const loadingIndicator = document.getElementById('loading-indicator');
                    if (loadingIndicator) {
                        loadingIndicator.style.display = 'block';
                    }
                    
                    // 데이터 태그 내용 출력 (디버깅용)
                    const dataIds = [
                        'treasury-yields-data',
                        'corporate-bond-yields-data',
                        'short-term-rates-data',
                        'scf-rate-simulation-data',
                        'ratings-comparison-data',
                        'historical-libor-data'
                    ];
                    
                    dataIds.forEach(id => {
                        const element = document.getElementById(id);
                        if (element) {
                            const content = element.textContent.trim();
                            const preview = content.length > 20 ? 
                                content.substring(0, 20) + '...' : content;
                            console.log(`${id} 내용: ${preview}`);
                            console.log(`${id} 내용 길이: ${content.length}`);
                            console.log(`${id} 플레이스홀더 포함 여부: ${content.includes('PLACEHOLDER')}`);
                        } else {
                            console.log(`${id} 요소를 찾을 수 없음`);
                        }
                    });
                    
                    try {
                        // 데이터 로드
                        setTimeout(() => {
                            try {
                                const allData = getDataFromJson();
                                
                                // 데이터 구조 확인 - 로깅을 추가하여 실제 데이터 구조를 확인
                                console.log('데이터 확인: ', JSON.stringify(allData));
                                
                                // 필수 데이터 확인
                                const requiredKeys = [
                                    'treasuryYieldsData', 
                                    'corporateBondYieldsData',
                                    'shortTermRatesData'
                                ];
                                
                                const missingData = requiredKeys.filter(
                                    key => !allData[key]
                                );
                                
                                if (missingData.length > 0) {
                                    throw new Error(`필수 데이터가 누락되었습니다: ${missingData.join(', ')}`);
                                }
                                
                                console.log('데이터 로드 완료, 차트 생성 시작...');
                                
                                // 차트 생성
                                try {
                                    const treasuryYieldsChart = createTreasuryYieldsChart(allData.treasuryYieldsData);
                                    console.log('Treasury Yields 차트 생성 완료');
                                } catch (error) {
                                    console.error('Treasury Yields 차트 생성 오류:', error);
                                }
                                
                                try {
                                    const corporateBondYieldsChart = createCorporateBondYieldsChart(allData.corporateBondYieldsData);
                                    console.log('Corporate Bond Yields 차트 생성 완료');
                                } catch (error) {
                                    console.error('Corporate Bond Yields 차트 생성 오류:', error);
                                }
                                
                                try {
                                    const shortTermRatesChart = createShortTermRatesChart(allData.shortTermRatesData);
                                    console.log('Short Term Rates 차트 생성 완료');
                                } catch (error) {
                                    console.error('Short Term Rates 차트 생성 오류:', error);
                                }
                                
                                try {
                                    const scfRateSimulationCharts = createScfRateSimulationCharts(allData.scfRateSimulationData);
                                    console.log('SCF Rate Simulation 차트 생성 완료');
                                } catch (error) {
                                    console.error('SCF Rate Simulation 차트 생성 오류:', error);
                                }
                                
                                try {
                                    const ratingsComparisonChart = createRatingsComparisonChart(allData.ratingsComparisonData);
                                    console.log('Ratings Comparison 차트 생성 완료');
                                } catch (error) {
                                    console.error('Ratings Comparison 차트 생성 오류:', error);
                                }
                                
                                try {
                                    const historicalLiborChart = createHistoricalLiborChart(allData.historicalLiborData);
                                    console.log('Historical Libor 차트 생성 완료');
                                } catch (error) {
                                    console.error('Historical Libor 차트 생성 오류:', error);
                                }
                                
                                console.log('모든 차트 생성 과정 완료');
                                
                                // 로딩 표시기 숨기기
                                loadingIndicator.style.display = 'none';
                            } catch (innerError) {
                                console.error('내부 데이터 처리 오류:', innerError);
                                
                                // 로딩 표시기 숨기기
                                loadingIndicator.style.display = 'none';
                                
                                // 오류 표시
                                const errorDisplay = document.getElementById('error-display');
                                const errorMessage = document.getElementById('error-message');
                                errorMessage.textContent = innerError.message;
                                errorDisplay.style.display = 'block';
                            }
                        }, 500);
                    } catch (error) {
                        console.error('최상위 오류 발생:', error);
                        
                        // 로딩 표시기 숨기기
                        loadingIndicator.style.display = 'none';
                        
                        // 오류 표시
                        const errorDisplay = document.getElementById('error-display');
                        const errorMessage = document.getElementById('error-message');
                        errorMessage.textContent = error.message;
                        errorDisplay.style.display = 'block';
                    }
                });
            </script>
        </body>
        </html>
        """