import json
from typing import Dict, Any

class PGSCFEconomicsQ2Generator:
    """Q2 시각화를 위한 메시지 카드 컴포넌트 생성기"""
    
    def __init__(self):
        """초기화"""
        self.data = {
            "payment_terms": {
                "before": 45,
                "after": 75,
                "change": 30
            },
            "pg_impact": {
                "positive": [
                    {"title": "매입채무 증가", "value": "40억 달러", "detail": "87억 → 127억 달러"},
                    {"title": "현금 유보 효과", "value": "40억 달러", "detail": "영업활동 현금흐름 개선"},
                    {"title": "이자 비용 절감", "value": "1,000만~2,000만 달러/년", "detail": "AA등급 기준 0.25%~0.50% × 40억 달러"},
                    {"title": "현금전환주기 개선", "value": "30일 감소", "detail": "12.6일 → -17.4일"}
                ],
                "negative": [
                    {"title": "유동비율 악화", "detail": "유동부채 증가로 인한 단기 재무 건전성 지표 하락"},
                    {"title": "공급업체 관계 악화", "detail": "공급업체의 현금흐름 압박으로 인한 관계 악화"},
                    {"title": "공급망 안정성 저하", "detail": "공급업체의 재무 건전성 악화로 인한 공급 불안정"},
                    {"title": "장기적 가격 인상 압력", "detail": "공급업체의 비용 증가가 장기적으로 가격 인상으로 전가될 가능성"}
                ]
            },
            "fibria_impact": {
                "negative": [
                    {"title": "매출채권 증가", "value": "3,700만 달러", "detail": "지급기간 45일 연장으로 인한 매출채권 75% 증가"},
                    {"title": "추가 자금조달 필요", "value": "3,700만 달러", "detail": "운전자본 3,700만 달러 추가 필요"},
                    {"title": "이자 비용 증가", "value": "74~111만 달러/년", "detail": "BBB- 등급 기준 2.0%~3.0% × 3,700만 달러"},
                    {"title": "현금전환주기 악화", "value": "45일 증가", "detail": "100일 → 145일"},
                    {"title": "유동비율 악화", "value": "1.55 → 1.35", "detail": "단기 재무 건전성 저하"}
                ],
                "considerations": [
                    {"title": "환율 리스크 증가", "detail": "부채의 90%가 USD 표시 → 브라질 헤알화 대비 USD 강세 시 부담 가중"},
                    {"title": "유동성 관리 어려움", "detail": "이미 재무적 어려움 상황에서 더 큰 압박 직면"},
                    {"title": "산업 특성", "detail": "원자재 생산자로서 이미 긴 현금전환주기(100일) 부담"},
                    {"title": "P&G 의존도", "detail": "P&G는 Fibria 매출의 약 10%를 차지 → 협상력 불균형"}
                ]
            },
            "interest_cost_comparison": {
                "pg_savings": {"min": 10, "max": 20, "unit": "백만 달러"},
                "fibria_cost": {"min": 0.74, "max": 1.11, "unit": "백만 달러"}
            }
        }
    
    def generate_html(self) -> str:
        """메시지 카드 형식의 HTML 코드 생성"""
        return f"""
        <style>
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
                font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
            }}
            
            .title {{
                color: #4263EB;
                font-size: 2rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 2rem;
            }}
            
            .card {{
                background: #F8F9FF;
                border-radius: 1rem;
                padding: 2rem;
                margin-bottom: 2rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            
            .card-title {{
                font-size: 1.5rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 1.5rem;
            }}
            
            .payment-terms {{
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 2rem;
                margin-bottom: 1.5rem;
            }}
            
            .term-box {{
                background: #F1F3F5;
                padding: 1rem 2rem;
                border-radius: 0.5rem;
                text-align: center;
            }}
            
            .term-label {{
                font-weight: bold;
                margin-bottom: 0.5rem;
            }}
            
            .term-value {{
                font-size: 2rem;
                font-weight: bold;
            }}
            
            .arrow {{
                font-size: 2rem;
                color: #4263EB;
            }}
            
            .description {{
                text-align: center;
                font-size: 1.1rem;
                color: #495057;
                margin-top: 1rem;
            }}
            
            .impact-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 1.5rem;
                margin-top: 1.5rem;
            }}
            
            .impact-item {{
                background: white;
                padding: 1.5rem;
                border-radius: 0.5rem;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            }}
            
            .impact-item.positive {{
                border-left: 4px solid #40C057;
            }}
            
            .impact-item.negative {{
                border-left: 4px solid #FA5252;
            }}
            
            .impact-item.consideration {{
                border-left: 4px solid #FD7E14;
            }}
            
            .impact-title {{
                font-weight: bold;
                margin-bottom: 0.5rem;
            }}
            
            .impact-value {{
                font-size: 1.2rem;
                color: #4263EB;
                margin-bottom: 0.5rem;
            }}
            
            .impact-detail {{
                color: #666;
                font-size: 0.9rem;
            }}
            
            .flex-container {{
                display: flex;
                gap: 2rem;
                margin-top: 1.5rem;
            }}
            
            .flex-half {{
                flex: 1;
            }}
            
            .comparison-box {{
                background: #F8F9FA;
                padding: 1.5rem;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
            }}
            
            .comparison-title {{
                font-weight: bold;
                color: #4263EB;
                margin-bottom: 1rem;
            }}
            
            .comparison-value {{
                font-size: 1.5rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }}
            
            .comparison-detail {{
                color: #666;
                font-size: 0.9rem;
            }}
        </style>
        
        <div class="container">
            <h1 class="title">SCF 프로그램 없는 결제 조건 연장의 영향</h1>
            
            <!-- 결제 조건 변경 -->
            <div class="card">
                <h2 class="card-title">결제 조건 변경</h2>
                <div class="payment-terms">
                    <div class="term-box">
                        <div class="term-label">기존</div>
                        <div class="term-value">{self.data['payment_terms']['before']}일</div>
                    </div>
                    <div class="arrow">→</div>
                    <div class="term-box">
                        <div class="term-label">변경</div>
                        <div class="term-value">{self.data['payment_terms']['after']}일</div>
                    </div>
                </div>
                <div class="description">
                    평균 지급 기간 {self.data['payment_terms']['change']}일 연장
                </div>
                <div class="description">
                    P&G는 공급업체에 대한 지급을 평균 30일 연장함으로써<br>
                    약 40억 달러의 현금을 30일 더 보유할 수 있게 됨
                </div>
            </div>
            
            <!-- P&G 영향 -->
            <div class="card">
                <h2 class="card-title">P&G에 미치는 영향</h2>
                <div class="flex-container">
                    <div class="flex-half">
                        <h3 class="card-title" style="color: #40C057">긍정적 영향</h3>
                        <div class="impact-grid">
                            {self._generate_impact_items(self.data['pg_impact']['positive'], 'positive')}
                        </div>
                    </div>
                    <div class="flex-half">
                        <h3 class="card-title" style="color: #FA5252">부정적 영향</h3>
                        <div class="impact-grid">
                            {self._generate_impact_items(self.data['pg_impact']['negative'], 'negative')}
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Fibria 영향 -->
            <div class="card">
                <h2 class="card-title">Fibria에 미치는 영향</h2>
                <div class="flex-container">
                    <div class="flex-half">
                        <h3 class="card-title" style="color: #FA5252">부정적 영향</h3>
                        <div class="impact-grid">
                            {self._generate_impact_items(self.data['fibria_impact']['negative'], 'negative')}
                        </div>
                    </div>
                    <div class="flex-half">
                        <h3 class="card-title" style="color: #FD7E14">추가 고려사항</h3>
                        <div class="impact-grid">
                            {self._generate_impact_items(self.data['fibria_impact']['considerations'], 'consideration')}
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 이자비용 차이의 불균형 -->
            <div class="card">
                <h2 class="card-title">이자비용 차이의 불균형</h2>
                <div class="flex-container">
                    <div class="flex-half">
                        <div class="comparison-box">
                            <div class="comparison-title">P&G 이자 절감</div>
                            <div class="comparison-value">
                                {self.data['interest_cost_comparison']['pg_savings']['min']}~
                                {self.data['interest_cost_comparison']['pg_savings']['max']} 
                                {self.data['interest_cost_comparison']['pg_savings']['unit']}
                            </div>
                            <div class="comparison-detail">AA등급 기준 0.25%~0.50% × 40억 달러</div>
                        </div>
                    </div>
                    <div class="flex-half">
                        <div class="comparison-box">
                            <div class="comparison-title">Fibria 이자 부담</div>
                            <div class="comparison-value">
                                {self.data['interest_cost_comparison']['fibria_cost']['min']}~
                                {self.data['interest_cost_comparison']['fibria_cost']['max']} 
                                {self.data['interest_cost_comparison']['fibria_cost']['unit']}
                            </div>
                            <div class="comparison-detail">BBB- 등급 기준 2.0%~3.0% × 3,700만 달러</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _generate_impact_items(self, items: list, item_type: str) -> str:
        """영향 항목들의 HTML 생성"""
        html = ""
        for item in items:
            html += f"""
                <div class="impact-item {item_type}">
                    <div class="impact-title">{item['title']}</div>
                    {'<div class="impact-value">' + item['value'] + '</div>' if 'value' in item else ''}
                    <div class="impact-detail">{item['detail']}</div>
                </div>
            """
        return html 