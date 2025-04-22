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
            body {{
                background-color: #F3F4F6;
                margin: 0;
                padding: 0;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 2rem;
                font-family: 'Pretendard', -apple-system, BlinkMacSystemFont, system-ui, Roboto, sans-serif;
            }}
            
            .title {{
                color: #111827;
                font-size: 2rem;
                font-weight: bold;
                text-align: center;
                margin-bottom: 2rem;
            }}
            
            .card {{
                background: white;
                border-radius: 0.75rem;
                padding: 1.5rem;
                margin-bottom: 2rem;
                box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            }}
            
            .card-title {{
                font-size: 1.25rem;
                font-weight: bold;
                color: #2563EB;
                margin-bottom: 1rem;
            }}
            
            .payment-terms {{
                display: flex;
                justify-content: center;
                align-items: center;
                gap: 1rem;
                margin: 1.5rem auto;
                max-width: 600px;
            }}
            
            .term-box {{
                background: #F3F4F6;
                padding: 0.75rem 1.5rem;
                border-radius: 0.5rem;
                text-align: center;
                flex: 1;
            }}
            
            .term-label {{
                font-weight: bold;
                color: #4B5563;
                margin-bottom: 0.25rem;
            }}
            
            .term-value {{
                font-size: 2rem;
                font-weight: bold;
                color: #111827;
            }}
            
            .arrow {{
                font-size: 1.5rem;
                color: #2563EB;
            }}
            
            .description {{
                text-align: center;
                font-size: 1rem;
                color: #4B5563;
                margin-top: 1rem;
                line-height: 1.5;
            }}
            
            .flex-container {{
                display: flex;
                gap: 1rem;
            }}
            
            .flex-half {{
                flex: 1;
            }}
            
            .impact-section {{
                background: #F9FAFB;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 1rem;
            }}
            
            .impact-section-title {{
                font-size: 1.1rem;
                font-weight: bold;
                margin-bottom: 1rem;
                padding: 0.5rem;
                border-radius: 0.25rem;
                text-align: center;
            }}
            
            .positive-title {{
                background: #DCFCE7;
                color: #166534;
            }}
            
            .negative-title {{
                background: #FEE2E2;
                color: #991B1B;
            }}
            
            .consideration-title {{
                background: #FEF3C7;
                color: #92400E;
            }}
            
            .impact-item {{
                background: white;
                padding: 1rem;
                border-radius: 0.5rem;
                margin-bottom: 0.75rem;
                box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
            }}
            
            .impact-item-title {{
                font-weight: 600;
                color: #111827;
                margin-bottom: 0.25rem;
                display: flex;
                align-items: center;
            }}
            
            .impact-item-value {{
                color: #2563EB;
                font-weight: 600;
                margin: 0.25rem 0;
            }}
            
            .impact-item-detail {{
                color: #6B7280;
                font-size: 0.875rem;
            }}
            
            .icon {{
                width: 1.25rem;
                height: 1.25rem;
                margin-right: 0.5rem;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                border-radius: 50%;
            }}
            
            .icon-positive {{
                background: #DCFCE7;
                color: #166534;
            }}
            
            .icon-negative {{
                background: #FEE2E2;
                color: #991B1B;
            }}
            
            .icon-consideration {{
                background: #FEF3C7;
                color: #92400E;
            }}
            
            .comparison-section {{
                background: #F9FAFB;
                padding: 1.5rem;
                border-radius: 0.5rem;
                margin-top: 1rem;
            }}
            
            .comparison-title {{
                font-weight: bold;
                color: #111827;
                margin-bottom: 0.5rem;
            }}
            
            .comparison-value {{
                font-size: 1.5rem;
                font-weight: bold;
                color: #2563EB;
                margin-bottom: 0.25rem;
            }}
            
            .comparison-detail {{
                color: #6B7280;
                font-size: 0.875rem;
            }}
            
            .progress-container {{
                margin: 2rem 0;
            }}
            
            .progress-bar {{
                width: 100%;
                height: 1.5rem;
                background: #E5E7EB;
                border-radius: 9999px;
                overflow: hidden;
                margin: 0.5rem 0;
            }}
            
            .progress-fill {{
                height: 100%;
                border-radius: 9999px;
                transition: width 0.3s ease;
            }}
            
            .progress-fill.pg {{
                background: #22C55E;
                width: 95%;
            }}
            
            .progress-fill.fibria {{
                background: #EF4444;
                width: 5%;
            }}
            
            .progress-label {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-top: 0.25rem;
            }}
            
            .progress-text {{
                font-size: 0.875rem;
                color: #4B5563;
            }}
            
            .progress-percentage {{
                font-weight: bold;
            }}
            
            .progress-percentage.pg {{
                color: #22C55E;
            }}
            
            .progress-percentage.fibria {{
                color: #EF4444;
            }}
            
            .reasons-grid {{
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 1rem;
                margin-top: 2rem;
                background: #EFF6FF;
                padding: 1.5rem;
                border-radius: 0.5rem;
            }}
            
            .reason-item {{
                display: flex;
                align-items: start;
                gap: 0.75rem;
            }}
            
            .reason-number {{
                background: #BFDBFE;
                color: #1D4ED8;
                width: 1.75rem;
                height: 1.75rem;
                border-radius: 9999px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-weight: bold;
                flex-shrink: 0;
            }}
            
            .reason-content {{
                flex: 1;
            }}
            
            .reason-title {{
                font-weight: bold;
                color: #1E40AF;
                margin-bottom: 0.25rem;
            }}
            
            .reason-detail {{
                font-size: 0.875rem;
                color: #4B5563;
            }}
        </style>
        
        <div class="container">
            <h1 class="title">Q2: P&G의 결제 조건 연장이 재무상태에 미치는 영향</h1>
            
            <!-- 결제 조건 변경 -->
            <div class="card">
                <h2 class="card-title">SCF 프로그램 없는 결제 조건 연장의 영향</h2>
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
                    평균 지급 기간 {self.data['payment_terms']['change']}일 연장<br>
                    P&G는 공급업체에 대한 지급을 평균 30일 연장함으로써<br>
                    약 40억 달러의 현금을 30일 더 보유할 수 있게 됨
                </div>
            </div>
            
            <!-- P&G 영향 -->
            <div class="card">
                <h2 class="card-title">P&G에 미치는 영향</h2>
                <div class="flex-container">
                    <div class="flex-half">
                        <div class="impact-section">
                            <div class="impact-section-title positive-title">긍정적 영향</div>
                            {self._generate_impact_items(self.data['pg_impact']['positive'], 'positive')}
                        </div>
                    </div>
                    <div class="flex-half">
                        <div class="impact-section">
                            <div class="impact-section-title negative-title">부정적 영향</div>
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
                        <div class="impact-section">
                            <div class="impact-section-title negative-title">부정적 영향</div>
                            {self._generate_impact_items(self.data['fibria_impact']['negative'], 'negative')}
                        </div>
                    </div>
                    <div class="flex-half">
                        <div class="impact-section">
                            <div class="impact-section-title consideration-title">추가 고려사항</div>
                            {self._generate_impact_items(self.data['fibria_impact']['considerations'], 'consideration')}
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- 이자비용 차이의 불균형 -->
            <div class="card">
                <h2 class="card-title">이자비용 차이의 불균형</h2>
                
                <div class="progress-container">
                    <div class="progress-bar">
                        <div class="progress-fill pg"></div>
                    </div>
                    <div class="progress-label">
                        <span class="progress-text">P&G 이자 절감: 약 1,000만~2,000만 달러/년</span>
                        <span class="progress-percentage pg">95%</span>
                    </div>
                    
                    <div class="progress-bar">
                        <div class="progress-fill fibria"></div>
                    </div>
                    <div class="progress-label">
                        <span class="progress-text">Fibria 이자 부담: 약 74만~111만 달러/년</span>
                        <span class="progress-percentage fibria">5%</span>
                    </div>
                </div>
                
                <div class="reasons-grid">
                    <h3 style="grid-column: span 2; font-weight: bold; margin-bottom: 1rem;">불균형의 주요 원인</h3>
                    
                    <div class="reason-item">
                        <div class="reason-number">1</div>
                        <div class="reason-content">
                            <div class="reason-title">기업 규모 차이</div>
                            <div class="reason-detail">P&G(800억 달러) vs Fibria(30억 달러)</div>
                        </div>
                    </div>
                    
                    <div class="reason-item">
                        <div class="reason-number">2</div>
                        <div class="reason-content">
                            <div class="reason-title">신용등급 차이</div>
                            <div class="reason-detail">P&G(AA-: 0.25~0.5%) vs Fibria(BBB-: 2~3%)</div>
                        </div>
                    </div>
                    
                    <div class="reason-item">
                        <div class="reason-number">3</div>
                        <div class="reason-content">
                            <div class="reason-title">자금조달 시장 접근성</div>
                            <div class="reason-detail">P&G(글로벌 자본시장) vs Fibria(제한적 접근)</div>
                        </div>
                    </div>
                    
                    <div class="reason-item">
                        <div class="reason-number">4</div>
                        <div class="reason-content">
                            <div class="reason-title">국가 리스크</div>
                            <div class="reason-detail">미국 기업 vs 브라질 기업(신흥시장 리스크)</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
    
    def _generate_impact_items(self, items: list, item_type: str) -> str:
        """영향 항목들의 HTML 생성"""
        icon_symbol = "+" if item_type == "positive" else "!" if item_type == "consideration" else "-"
        html = ""
        for item in items:
            html += f"""
                <div class="impact-item">
                    <div class="impact-item-title">
                        <span class="icon icon-{item_type}">{icon_symbol}</span>
                        {item['title']}
                    </div>
                    {'<div class="impact-item-value">' + item['value'] + '</div>' if 'value' in item else ''}
                    <div class="impact-item-detail">{item['detail']}</div>
                </div>
            """
        return html 