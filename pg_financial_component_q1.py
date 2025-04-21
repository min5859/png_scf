import json
from data_provider import MarketDataProvider

class PGFinancialComponentGeneratorQ1:
    """P&G 재무 데이터용 Chart.js 컴포넌트 생성 클래스 (Q1 탭)"""
    
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
            <title>P&G Income Statement (Q1)</title>
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
                @media (max-width: 768px) {
                    .grid {
                        grid-template-columns: 1fr;
                    }
                }
            </style>
        </head>
        <body>
            <div id="root">
                <!-- 메인 타이틀 -->
                <div style="text-align: center; margin-bottom: 30px;">
                    <h1 style="color: #003366; font-size: 28px; font-weight: 700;">비용 절감 이니셔티브</h1>
                </div>
                
                <!-- 차트 컨테이너 6: 주요 인사이트 -->
                <div class="chart-container">
                    <div class="grid">
                        <div class="insight-box">
                            <div class="insight-title">매출 정체 및 하락</div>
                            <div class="insight-content">매출 성장이 정체되고 있음 (2012-2015년 사이 실질적 감소)</div>
                            <div class="note">→ 성장이 없는 상황에서 이익을 유지하기 위해 비용 및 운전자본 효율화가 필수적</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">안정적인 이익률</div>
                            <div class="insight-content">영업이익률은 17-19% 대를 안정적으로 유지</div>
                            <div class="note">→ AA- 신용등급 유지에 기여</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">주주 수익률(TSR) 중시</div>
                            <div class="insight-content">배당금 지급은 증가하는 추세 (주당 1.97달러에서 2.59달러로)</div>
                            <div class="insight-content">2015년에는 수익 감소로 배당성향(Payout Ratio)이 104%로 급증</div>
                            <div class="note">→ 현금 확보와 배당금 유지를 위해 운전자본 최적화가 중요한 전략</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">현금흐름 관리 필요성</div>
                            <div class="insight-content">매출의 약 80%가 비용 관련 (COGS + SG&A)</div>
                            <div class="note">→ 공급망 금융으로 현금흐름 개선 가능</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <script>
                // JSON 데이터 파싱
                const pgFinancialData = PG_FINANCIAL_DATA_PLACEHOLDER;
            </script>
        </body>
        </html>
        """ 