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

                /* 메시지 카드 스타일 */
                .message-card {
                    background: white;
                    border-radius: 12px;
                    padding: 20px;
                    margin-bottom: 20px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    border-left: 4px solid;
                    transition: transform 0.2s ease-in-out;
                }
                .message-card:hover {
                    transform: translateY(-2px);
                }
                .message-card.blue {
                    border-left-color: #4299e1;
                }
                .message-card.green {
                    border-left-color: #48bb78;
                }
                .message-card.red {
                    border-left-color: #f56565;
                }
                .message-card.purple {
                    border-left-color: #9f7aea;
                }
                .message-card.yellow {
                    border-left-color: #ecc94b;
                }
                .message-card.indigo {
                    border-left-color: #667eea;
                }
                .message-card-title {
                    font-size: 1.8rem;
                    font-weight: bold;
                    color: #2563EB;
                    margin-bottom: 1rem;
                }
                .message-card-content {
                    font-size: 1.3rem;
                    line-height: 1.5;
                    color: #4B5563;
                }
                .message-card-points {
                    font-size: 1.3rem;
                    line-height: 1.5;
                    color: #4B5563;
                }
                .message-card-points li {
                    margin-bottom: 0.5rem;
                }
                .message-card-calc {
                    background: #f7fafc;
                    border-radius: 8px;
                    padding: 15px;
                    margin-top: 15px;
                    font-family: monospace;
                }
                .message-card-calc-title {
                    font-weight: 600;
                    margin-bottom: 8px;
                    color: #2d3748;
                }
            </style>
        </head>
        <body>
            <div style="padding: 20px;">
                <h2 class="section-title">Fibria Cellulose Balance Sheet (2012-2015)</h2>
                
                <!-- 자산, 부채, 자본 추이 -->
                <div class="chart-container bg-blue-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-3 text-center text-blue-800">1. 자산, 부채, 자본 추이 (단위: 백만 레알)</h3>
                    <div class="message-card blue">
                        <div class="message-card-title">차트 설명</div>
                        <div class="message-card-content">
                            이 차트는 피브리아의 총자산, 총부채, 자본의 연도별 변화를 보여줍니다. 
                            2012년부터 2014년까지 총자산이 감소하다가 2015년에 소폭 증가했으며, 
                            총부채는 지속적으로 감소 추세를 보였습니다. 이는 회사의 부채 관리 노력을 보여줍니다.
                        </div>
                        <div class="message-card-title mt-4">주요 포인트</div>
                        <ul class="message-card-points">
                            <li>총자산: 2012년 R$28,145백만에서 2015년 6월 R$26,501백만으로 5.8% 감소</li>
                            <li>총부채: 2012년 R$12,974백만에서 2015년 6월 R$11,937백만으로 8.0% 감소</li>
                            <li>자본: 상대적으로 안정적인 수준 유지 (R$14,500백만 ~ R$15,200백만 범위)</li>
                        </ul>
                    </div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="balanceSheetChart"></canvas>
                    </div>
                </div>

                <!-- 유동자산 구성 -->
                <div class="chart-container bg-green-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-3 text-center text-green-800">2. 유동자산 구성 변화 (단위: 백만 레알)</h3>
                    <div class="message-card green">
                        <div class="message-card-title">차트 설명</div>
                        <div class="message-card-content">
                            이 차트는 피브리아의 유동자산 구성 요소(현금, 매출채권, 재고자산, 기타유동자산)의 
                            연도별 변화를 보여줍니다. 특히 눈에 띄는 점은 2012년에서 2014년까지 현금의 대폭 감소와 
                            2014년 매출채권의 큰 폭 감소입니다.
                        </div>
                        <div class="message-card-title mt-4">주요 포인트</div>
                        <ul class="message-card-points">
                            <li>현금: 2012년 R$3,296백만에서 2014년 R$745백만으로 77.4% 감소 후 2015년 다시 증가</li>
                            <li>매출채권: 2013년 R$1,477백만에서 2014년 R$695백만으로 53.0% 급감 (SCF 프로그램 영향)</li>
                            <li>재고자산: 상대적으로 안정적인 수준을 유지 (R$1,183백만~R$1,455백만)</li>
                        </ul>
                    </div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="currentAssetsChart"></canvas>
                    </div>
                </div>

                <!-- 부채 구성 -->
                <div class="chart-container bg-red-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-3 text-center text-red-800">3. 부채 구성 변화 (단위: 백만 레알)</h3>
                    <div class="message-card red">
                        <div class="message-card-title">차트 설명</div>
                        <div class="message-card-content">
                            이 차트는 피브리아의 부채 구성(매입채무, 단기차입금, 기타유동부채, 장기차입금, 기타비유동부채)의 
                            연도별 변화를 보여줍니다. 특히 2013년에 단기차입금이 크게 증가했다가 2014년에 감소한 것이 주목할 만합니다.
                        </div>
                        <div class="message-card-title mt-4">주요 포인트</div>
                        <ul class="message-card-points">
                            <li>단기차입금: 2013년에 R$2,973백만으로 급증 후 2014년 R$966백만으로 67.5% 감소</li>
                            <li>장기차입금: 2012년 R$9,630백만에서 2013년 R$6,801백만으로 감소 후 다시 증가 추세</li>
                            <li>매입채무: 점진적으로 증가 (R$436백만에서 R$637백만으로 46.1% 증가)</li>
                        </ul>
                    </div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="liabilitiesChart"></canvas>
                    </div>
                </div>

                <!-- 유동성 지표 -->
                <div class="chart-container bg-purple-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-3 text-center text-purple-800">4. 유동성 및 부채 지표 추이</h3>
                    <div class="message-card purple">
                        <div class="message-card-title">차트 설명</div>
                        <div class="message-card-content">
                            이 차트들은 피브리아의 유동비율과 부채비율의 변화를 보여줍니다. 
                            2013년에 유동비율이 크게 하락했다가 이후 지속적으로 개선되는 추세를 보이며, 
                            부채비율은 꾸준히 감소하여 회사의 재무 안정성이 개선되고 있음을 나타냅니다.
                        </div>
                        <div class="message-card-title mt-4">주요 포인트</div>
                        <ul class="message-card-points">
                            <li>유동비율: 2012년 2.52배에서 2013년 1.31배로 급감 후, 2015년 6월 1.85배로 회복</li>
                            <li>부채비율: 2012년 41.5%에서 2014년 36.3%로 감소 후, 2015년 6월 38.2%로 소폭 증가</li>
                            <li>이러한 지표 개선은 SCF 프로그램 도입과 회사의 재무 관리 노력이 결합된 결과</li>
                        </ul>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white p-4 rounded-lg">
                            <h4 class="font-semibold text-center mb-2 text-purple-700">유동비율 (Current Ratio)</h4>
                            <p class="text-sm text-gray-600 mb-4 text-center">유동자산 ÷ 유동부채, 높을수록 단기 지급능력이 양호</p>
                            <div style="height: 300px;">
                                <canvas id="currentRatioChart"></canvas>
                            </div>
                        </div>
                        <div class="bg-white p-4 rounded-lg">
                            <h4 class="font-semibold text-center mb-2 text-purple-700">부채비율 (Debt-to-Capital)</h4>
                            <p class="text-sm text-gray-600 mb-4 text-center">총부채 ÷ (부채+자본), 낮을수록 재무 안정성이 양호</p>
                            <div style="height: 300px;">
                                <canvas id="debtToCapitalChart"></canvas>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 운전자본 항목 -->
                <div class="chart-container bg-yellow-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-3 text-center text-yellow-800">5. 운전자본 항목 추이 (단위: 백만 레알)</h3>
                    <div class="message-card yellow">
                        <div class="message-card-title">차트 설명</div>
                        <div class="message-card-content">
                            이 차트는 피브리아의 순운전자본과 그 구성요소(매출채권, 재고자산, 매입채무)의 
                            변화를 보여줍니다. 순운전자본은 '매출채권 + 재고자산 - 매입채무'로 계산되며, 
                            일상적인 운영 활동에 필요한 자금을 의미합니다.
                        </div>
                        <div class="message-card-title mt-4">주요 포인트</div>
                        <ul class="message-card-points">
                            <li>순운전자본: 2013년 R$2,156백만으로 정점을 찍은 후 2014년 R$1,341백만으로 37.8% 감소</li>
                            <li>매출채권: 2013년에 크게 증가했다가 2014년에 급감 (SCF 프로그램의 영향)</li>
                            <li>재고자산: 전반적으로 안정적인 수준 유지 (R$1,183백만~R$1,455백만)</li>
                            <li>운전자본 감소는 기업의 자금 효율성 증가를 의미</li>
                        </ul>
                        <div class="message-card-calc">
                            <div class="message-card-calc-title">순운전자본 계산 방식:</div>
                            <p>순운전자본 = 매출채권 + 재고자산 - 매입채무</p>
                            <ul class="message-card-points">
                                <li>2012년: R$964백만 + R$1,183백만 - R$436백만 = R$1,711백만</li>
                                <li>2013년: R$1,477백만 + R$1,266백만 - R$587백만 = R$2,156백만</li>
                                <li>2014년: R$695백만 + R$1,239백만 - R$593백만 = R$1,341백만</li>
                                <li>2015년(6월): R$875백만 + R$1,455백만 - R$637백만 = R$1,693백만</li>
                            </ul>
                        </div>
                    </div>
                    <div style="height: 400px; width: 100%;">
                        <canvas id="workingCapitalChart"></canvas>
                    </div>
                </div>

                <!-- SCF 영향 분석 -->
                <div class="chart-container bg-indigo-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-3 text-center text-indigo-800">6. SCF 프로그램 영향 분석 (P&G 거래 기준)</h3>
                    <div class="message-card indigo">
                        <div class="message-card-title">차트 설명</div>
                        <div class="message-card-content">
                            이 차트들은 SCF 프로그램 도입 전후의 매출채권 회수 기간과 
                            자금조달 비용 변화를 보여줍니다. P&G와의 연간 거래 규모 3억 달러를 기준으로 분석했습니다.
                        </div>
                        <div class="message-card-title mt-4">계산 방식</div>
                        <ul class="message-card-points">
                            <li>매출채권 가치: 연간 매출액(3억 달러) × 회수 기간(일) ÷ 365일</li>
                            <li>SCF 이전: 3억 달러 × 60일 ÷ 365일 ≈ 4,932만 달러</li>
                            <li>SCF 이후: 3억 달러 × 15일 ÷ 365일 ≈ 1,233만 달러</li>
                            <li>자금조달 비용: 매출채권 가치 × 연간 자금조달 비율(SCF 이전 2.5%, SCF 이후 0.35%)</li>
                        </ul>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="bg-white p-4 rounded-lg">
                            <h4 class="font-semibold text-center mb-2 text-indigo-700">매출채권 회수 기간</h4>
                            <p class="text-sm text-gray-600 mb-4 text-center">P&G에 제품 판매 후 대금을 받기까지 걸리는 평균 일수</p>
                            <div style="height: 300px;">
                                <canvas id="daysOutstandingChart"></canvas>
                            </div>
                            <div class="message-card indigo mt-4">
                                <div class="message-card-title">영향 분석</div>
                                <ul class="message-card-points">
                                    <li>SCF 프로그램을 통해 매출채권 회수 기간이 60일에서 15일로 75% 단축</li>
                                    <li>이는 피브리아의 현금흐름 개선과 운전자본 감소에 크게 기여</li>
                                </ul>
                            </div>
                        </div>
                        <div class="bg-white p-4 rounded-lg">
                            <h4 class="font-semibold text-center mb-2 text-indigo-700">자금조달 비용 (연간, 백만 달러)</h4>
                            <p class="text-sm text-gray-600 mb-4 text-center">매출채권 할인에 따른 연간 금융 비용</p>
                            <div style="height: 300px;">
                                <canvas id="financingCostChart"></canvas>
                            </div>
                            <div class="message-card indigo mt-4">
                                <div class="message-card-title">영향 분석</div>
                                <ul class="message-card-points">
                                    <li>SCF 이전: 4,932만 달러 × 2.5% ≈ 123만 달러/년</li>
                                    <li>SCF 이후: 1,233만 달러 × 0.35% ≈ 4.3만 달러/년</li>
                                    <li>연간 약 119만 달러의 자금조달 비용 절감 (96.5% 감소)</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- SCF 프로그램의 전략적 의미 -->
                <div class="w-full bg-yellow-50 p-6 rounded-xl shadow-md">
                    <h3 class="text-2xl font-semibold mb-4 text-center text-yellow-800">SCF 프로그램의 전략적 의미</h3>
                    <div class="bg-white p-4 rounded-lg mb-4">
                        <p class="mb-3 text-gray-700">
                            피브리아에게 P&G의 SCF 프로그램은 단순한 금융 거래를 넘어 전략적 가치를 제공합니다. 
                            아래는 SCF 프로그램이 피브리아에게 주는 주요 전략적 이점입니다.
                        </p>
                    </div>
                    <ul class="list-none space-y-3">
                        <li class="bg-white p-4 rounded-lg shadow flex items-start">
                            <div class="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">1</div>
                            <div>
                                <span class="font-semibold text-lg">유동성 확보:</span> 
                                <p>매출채권 60일→15일로 단축으로 약 $37백만 빠른 현금 확보</p>
                                <p class="text-sm text-gray-600 mt-1">계산: $300백만 × (60-15)/365 = $36.99백만의 운전자본 감소</p>
                            </div>
                        </li>
                        <li class="bg-white p-4 rounded-lg shadow flex items-start">
                            <div class="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">2</div>
                            <div>
                                <span class="font-semibold text-lg">이자 비용 절감:</span> 
                                <p>연간 약 $1.19백만의 자금조달 비용 절감</p>
                                <p class="text-sm text-gray-600 mt-1">계산: ($49.32백만 × 2.5%) - ($12.33백만 × 0.35%) = $1.19백만</p>
                            </div>
                        </li>
                        <li class="bg-white p-4 rounded-lg shadow flex items-start">
                            <div class="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">3</div>
                            <div>
                                <span class="font-semibold text-lg">대차대조표 개선:</span> 
                                <p>매출채권 감소로 유동비율 개선 및 부채의존도 감소</p>
                                <p class="text-sm text-gray-600 mt-1">2013년 이후 유동비율 증가(1.31→1.85)와 부채비율 감소(40.3%→38.2%)</p>
                            </div>
                        </li>
                        <li class="bg-white p-4 rounded-lg shadow flex items-start">
                            <div class="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">4</div>
                            <div>
                                <span class="font-semibold text-lg">환율 위험 관리:</span> 
                                <p>달러 매출의 빠른 현금화로 환율 변동 위험 완화</p>
                                <p class="text-sm text-gray-600 mt-1">브라질 레알/달러 환율 상승(1.96→2.69)에 따른 달러 부채 리스크 일부 상쇄</p>
                            </div>
                        </li>
                        <li class="bg-white p-4 rounded-lg shadow flex items-start">
                            <div class="bg-yellow-200 text-yellow-800 rounded-full h-8 w-8 flex items-center justify-center mr-3 mt-1 flex-shrink-0">5</div>
                            <div>
                                <span class="font-semibold text-lg">신용 관계 확대:</span> 
                                <p>시티그룹 외에 JPMorgan Chase와의 관계 구축 기회</p>
                                <p class="text-sm text-gray-600 mt-1">다양한 글로벌 은행과의 관계는 금융 위기 상황에서 대안적 자금원 확보에 중요</p>
                            </div>
                        </li>
                    </ul>
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