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
                .quote-box {
                    background-color: #fff5f5;
                    border-radius: 8px;
                    border-left: 4px solid #ff6b6b;
                    padding: 15px;
                    margin-bottom: 20px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
                }
                .quote {
                    font-style: italic;
                    color: #c92a2a;
                    margin-bottom: 10px;
                    line-height: 1.6;
                }
                .quote-author {
                    text-align: right;
                    font-weight: bold;
                    color: #666;
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
                .formula-box {
                    background-color: #fff5f5;
                    border-radius: 8px;
                    padding: 15px;
                    margin: 20px 0;
                    border-left: 4px solid #ff6b6b;
                }
                .formula {
                    font-family: 'Courier New', monospace;
                    font-size: 16px;
                    color: #c92a2a;
                    text-align: center;
                    margin: 10px 0;
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
                            <div class="insight-title">금융 위기 이후 성장 둔화</div>
                            <div class="insight-content">2008년 금융 위기 이후 P&G의 성장이 둔화되면서 $10 billion 비용 절감 계획 수립</div>
                            <div class="note">→ 대규모 비용 절감이 필요한 상황에서 운전자본 최적화가 중요한 전략</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">벤치마킹 분석 결과</div>
                            <div class="insight-content">P&G의 평균 지불 기간: 45일</div>
                            <div class="insight-content">경쟁사 평균 지불 기간: 75-100일</div>
                            <div class="note">→ 경쟁사 대비 빠른 지불로 인한 현금흐름 압박</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">TSR (Total Shareholder Return)</div>
                            <div class="formula-box">
                                <div class="formula">TSR = (기말 주가 - 기초 주가 + 배당금) ÷ 기초 주가</div>
                            </div>
                            <div class="insight-content">배당금 지급은 증가하는 추세 (주당 1.97달러에서 2.59달러로)</div>
                            <div class="insight-content">2015년에는 수익 감소로 배당성향(Payout Ratio)이 104%로 급증</div>
                            <div class="note">→ 높은 TSR 유지를 위해 현금흐름 개선이 필수적</div>
                        </div>
                        <div class="insight-box">
                            <div class="insight-title">현금흐름 관리 필요성</div>
                            <div class="insight-content">매출의 약 80%가 비용 관련 (COGS + SG&A)</div>
                            <div class="insight-content">배당금 지급을 위한 충분한 현금흐름 확보 필요</div>
                            <div class="note">→ 공급망 금융으로 현금흐름 개선 가능</div>
                        </div>
                        <div class="quote-box">
                            <div class="quote">
                                "우리의 지불 조건이 이렇게 다른 이유는 우리 구매 담당자들이 항상 가격, 품질, 배송, 서비스, 대응성, 혁신에 초점을 맞추었기 때문입니다."
                            </div>
                            <div class="quote-author">- Doug Gerstle, P&G 부사장 겸 재무보조</div>
                            <div class="insight-content" style="margin-top: 15px;">
                                P&G의 구매 부서는 공급업체와의 협상에서 결제 조건보다 제품과 서비스의 품질적 측면에 더 중점을 두었습니다.
                            </div>
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