import streamlit as st
import pandas as pd
import json

class PGSCFEconomicsQ4Generator:
    """P&G SCF 경제적 효과 분석 컴포넌트 생성기 - Q4 버전"""
    
    def __init__(self, data_provider=None):
        """초기화 함수"""
        self.data_provider = data_provider
        
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
            <h1>P&G SCF 프로그램의 Win-Win-Win 분석</h1>
        """
        
        # 여섯 번째 섹션 - SCF 경제적 효과 요약
        html_code += """
            <div class="container">
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
        
        # 닫는 태그 추가
        html_code += """
        </body>
        </html>
        """
        
        return html_code
    
def pg_scf_economics_q4_viz():
    """Streamlit 앱에서 호출할 P&G SCF 경제적 효과 시각화 함수 - Q4 버전"""
    st.title("P&G SCF 프로그램의 Win-Win-Win 분석")
    
    # 컴포넌트 생성기 초기화
    generator = PGSCFEconomicsQ4Generator()
    
    # HTML 코드 생성
    html_code = generator.generate_html()
    
    # HTML 렌더링
    st.components.v1.html(html_code, height=800, scrolling=True)

if __name__ == "__main__":
    pg_scf_economics_q4_viz() 