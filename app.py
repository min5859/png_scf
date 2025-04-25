import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from data_provider import MarketDataProvider
from react_component import ReactComponentGenerator
from pg_financial_component import PGFinancialComponentGenerator
from pg_balance_sheet_component import PGBalanceSheetComponentGenerator
from pg_working_capital_component import PGWorkingCapitalComponentGenerator
from fibria_financial_component import FibriaFinancialComponentGenerator
from fibria_balance_sheet_component import FibriaBalanceSheetComponentGenerator
from fibria_working_capital_chart_component import FibriaWorkingCapitalComponentGenerator
from pg_scf_economics import PGSCFEconomicsGenerator
from pg_scf_economics_q4 import PGSCFEconomicsQ4Generator
from pg_financial_component_q1 import PGFinancialComponentGeneratorQ1
from pg_scf_economics_q3 import PGSCFEconomicsQ3Generator
from pg_scf_economics_q2 import PGSCFEconomicsQ2Generator
from PIL import Image
import os
import numpy as np
from fibria_scf_analysis_component import FibriaSCFAnalysisComponent

class StreamlitApp:
    """Streamlit 애플리케이션 클래스"""
    
    def __init__(self):
        """애플리케이션 초기화"""
        self.data_provider = MarketDataProvider()
        self.react_generator = ReactComponentGenerator(self.data_provider)
        self.pg_financial_generator = PGFinancialComponentGenerator(self.data_provider)
        self.pg_balance_sheet_generator = PGBalanceSheetComponentGenerator(self.data_provider)
        self.pg_working_capital_generator = PGWorkingCapitalComponentGenerator(self.data_provider)
        self.fibria_financial_generator = FibriaFinancialComponentGenerator(self.data_provider)
        self.fibria_balance_sheet_generator = FibriaBalanceSheetComponentGenerator(self.data_provider)
        self.fibria_working_capital_generator = FibriaWorkingCapitalComponentGenerator(self.data_provider)
        self.pg_financial_generator_q1 = PGFinancialComponentGeneratorQ1(self.data_provider)
    
    def setup_page(self):
        """페이지 기본 설정"""
        st.set_page_config(
            page_title="P&G Case Analysis",
            page_icon="📊",
            layout="wide",
            initial_sidebar_state="collapsed"  # 사이드바를 초기에 숨깁니다
        )
        #st.title("시장 금리 현황 분석")
    
    def render_buttons(self):
        """버튼 렌더링"""
        # Q 버튼 생성 - Q1부터 Q6까지
        q_button_titles = [f"Q{i}" for i in range(1, 7)]
        
        # Exhibit 버튼 생성 - Exhibit 1부터 Exhibit 8까지
        button_titles = [f"Exhibit {i}" for i in range(1, 9)]
        
        # 모든 버튼을 하나의 행에 배치하기 위한 컨테이너 생성 (14개 컬럼)
        cols = st.columns(14)
        
        # Q1 버튼
        if cols[0].button(q_button_titles[0]):
            st.header("Q1 - P&G가 2013년 4월 공급업체 지불 기간을 연장한 이유")
            self.render_q1()
        
        # Q2 버튼
        if cols[1].button(q_button_titles[1]):
            self.render_q2()
        
        # Q3 버튼
        if cols[2].button(q_button_titles[2]):
            self.render_q3()
        
        # Q4 버튼
        if cols[3].button(q_button_titles[3]):
            self.render_q4()
        
        # Q5 버튼
        if cols[4].button(q_button_titles[4]):
            self.render_q5()
        
        # Q6 버튼
        if cols[5].button(q_button_titles[5]):
            self.render_q6()
        
        # Exhibit 1 - P&G 재무 지표 시각화
        if cols[6].button(button_titles[0]):
            #st.header("P&G Income Statement (Exhibit 1)")
            self.render_exhibit_1()
        
        # Exhibit 2 - P&G 대차대조표 분석
        if cols[7].button(button_titles[1]):
            #st.header("P&G 대차대조표 분석 (Exhibit 2)")
            self.render_exhibit_2()
        
        # Exhibit 3 - P&G 운전자본 분석
        if cols[8].button(button_titles[2]):
            #st.header("P&G 운전자본 분석 (Exhibit 3)")
            self.render_exhibit_3()
        
        # Exhibit 4 - P&G SCF 경제적 효과 분석
        if cols[9].button("Example"):
            self.render_exhibit_4()
        
        # Exhibit 5 - Fibria 재무 분석
        if cols[10].button(button_titles[4]):
            #st.header("Fibria 셀룰로즈 재무 분석 (Exhibit 5)")
            self.render_exhibit_5()
        
        # Exhibit 6 - Fibria 대차대조표 분석
        if cols[11].button(button_titles[5]):
            #st.header("Fibria 셀룰로즈 대차대조표 분석 (Exhibit 6)")
            self.render_exhibit_6()
        
        # Exhibit 7 - Fibria 운전자본 분석
        if cols[12].button(button_titles[6]):
            #st.header("Fibria 운전자본 분석 (Exhibit 7)")
            self.render_exhibit_7()
        
        # Exhibit 8 - 시장 금리 현황 분석
        if cols[13].button(button_titles[7]):
            #st.header("시장 금리 현황 분석 (Exhibit 8)")
            self.render_exhibit_8()
    
    def render_exhibit_1(self):
        """Exhibit 1 - P&G 재무 지표 시각화 (Chart.js 사용)"""
        # Chart.js를 사용한 HTML 코드 생성
        html_code = self.pg_financial_generator.generate_html()
        
        # 디버깅 옵션 추가 - 고유 키 추가
        debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit1")
        
        if debug_mode:
            st.sidebar.subheader("디버깅 정보")
            st.sidebar.json(self.data_provider.pg_financial_data)
            
            # HTML 코드 길이 표시
            st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
            
            # HTML 코드 일부 표시
            with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                st.code(html_code[:1000] + "...", language="html")
        
        # HTML 렌더링 높이 설정 - 고유 키 추가
        height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 2500, 100, key="height_slider_exhibit1") if debug_mode else 2500
        
        # Chart.js HTML 렌더링 - 오류 처리 추가
        try:
            st.components.v1.html(html_code, height=height, scrolling=True)
        except Exception as e:
            st.error(f"Chart.js 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            
            if debug_mode:
                st.exception(e)
        
        # 데이터 테이블 표시 (디버깅 모드에서만)
        #if debug_mode:
        #    with st.expander("P&G 재무 데이터 표", expanded=False):
        #        st.dataframe(pd.DataFrame(self.data_provider.pg_financial_data))

        # Fibria 재무 분석 내용 추가
        with st.expander("Procter & Gamble Income Statement (2011-2015)", expanded=False):
            st.markdown("""
            ### Procter & Gamble Income Statement (2011-2015) (단위: 백만 달러)
            
            | 구분 | 2011 | 2012 | 2013 | 2014 | 2015 |
            |------|------|------|------|------|------|
            | **손익계산서 (Income Statement)** |  |  |  |  |  |
            | 매출 (Revenue) | $81,104 | $82,006 | $80,116 | $80,510 | $76,279 |
            | 제품 판매원가 (Cost of Products Sold) | $39,859 | $41,411 | $39,991 | $40,611 | $38,248 |
            | **매출총이익 (Gross Profit)** | **$41,245** | **$40,595** | **$40,125** | **$39,899** | **$38,031** |
            | 판매관리비 (SG&A Expense) | $25,750 | $25,984 | $26,000 | $24,402 | $23,158 |
            | **영업이익 (Operating Income)** | **$15,495** | **$14,611** | **$14,125** | **$15,497** | **$14,873** |
            | 순이자비용 (Net Interest Expense) | ($769) | ($692) | ($579) | ($609) | ($475) |
            | 기타수익 및 특별항목 (Other Income & Unusual Items) | $271 | ($1,391) | $633 | ($551) | ($2,552) |
            | **세전이익 (Profit before Tax)** | **$14,997** | **$12,528** | **$14,179** | **$14,337** | **$11,846** |
            | 법인세비용 (Income Tax Expense) | $3,299 | $3,378 | $3,226 | $3,019 | $2,916 |
            | 소수주주지분 (Minority Interest) | ($130) | ($148) | ($90) | ($142) | ($108) |
            | 중단사업이익 (Earnings from Discont. Ops.) | $229 | $1,754 | $449 | $467 | ($1,786) |
            | **순이익 (Net Income)** | **$11,797** | **$10,756** | **$11,312** | **$11,643** | **$7,036** |
            | **주당 지표 (Per Share Items)** |  |  |  |  |  |
            | 기본 주당순이익 (Basic EPS) | 4.12 | 3.82 | 4.04 | 4.19 | 2.50 |
            | 평균 유통주식수-기본 (Avg. # Basic Shares Outstanding) | 2,804 | 2,751 | 2,743 | 2,720 | 2,712 |
            | 주당 배당금 (Dividend per Share) | $1.97 | $2.14 | $2.29 | $2.45 | $2.59 |
            | 배당성향 (Payout Ratio) | 48% | 56% | 57% | 59% | 104% |
            | 주가 (Stock Price, $/share) | $63.57 | $61.25 | $76.99 | $78.59 | $78.24 |
            | **기타 현금흐름 항목 (Other Cash Flow Items)** |  |  |  |  |  |
            | 감가상각비 (Depreciation & Amortization) | $2,838 | $3,204 | $2,982 | $3,141 | $3,134 |
            | 자본지출 (Capital Expenditures) | $3,306 | $3,964 | $4,008 | $3,848 | $3,736 |
            | 광고비 (Advertising Expense) | $9,210 | $9,222 | $9,364 | $8,979 | $8,290 |
            | **재무비율 및 정보 (Financial Ratios & Information)** |  |  |  |  |  |
            | 매출 성장률 (Revenue Growth) | 4.6% | 1.1% | -2.3% | 0.5% | -5.3% |
            | 매출총이익률 (Gross Margin) | 50.9% | 49.5% | 50.1% | 49.6% | 49.9% |
            | 영업이익률 (Operating Margin) | 19.1% | 17.8% | 17.6% | 19.2% | 19.5% |
            | 순이익률 (Net Margin, ROS) | 14.5% | 13.1% | 14.1% | 14.5% | 9.2% |
            | 총자산수익률 (Return on Assets, ROA) | 8.5% | 8.1% | 8.1% | 8.1% | 5.4% |
            | 자기자본수익률 (Return on Equity, ROE) | 17.3% | 16.8% | 16.5% | 16.6% | 11.2% |
            | 이자보상배율 (Interest Cover) | 20.1 | 21.1 | 24.4 | 25.4 | 31.3 |
            | 유효세율 (Effective Tax Rate) | 22.0% | 27.0% | 22.8% | 21.1% | 24.6% |
            | 직원 수 (Number of Employees) | 129,000 | 126,000 | 121,000 | 118,000 | 110,000 |
            
            **참고**: 
            - P&G는 2015년 베네수엘라 사업 관련 회계처리 방식 변경으로 21억 달러의 일회성 비용을 계상했습니다. 환전 또는 배당금 지급 불가로 인해 P&G는 베네수엘라 자회사의 연결을 중단하고 원가법으로 회계처리를 시작했습니다.
           """)
   
    def render_exhibit_2(self):
        """Exhibit 2 - P&G 대차대조표 분석 (Chart.js 사용)"""
        try:
            # Chart.js를 사용한 HTML 코드 생성
            html_code = self.pg_balance_sheet_generator.generate_html()
            
            # 디버깅 옵션 추가 - 고유 키 추가
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit2")
            
            if debug_mode:
                st.sidebar.subheader("디버깅 정보")
                st.sidebar.json(self.data_provider.pg_balance_sheet_data)
                st.sidebar.json(self.data_provider.pg_working_capital_data)
                
                # HTML 코드 길이 표시
                st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
                
                # HTML 코드 일부 표시
                with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                    st.code(html_code[:1000] + "...", language="html")
            
            # HTML 렌더링 높이 설정 - 고유 키 추가
            height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_exhibit2") if debug_mode else 3000
            
            # Chart.js HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
            # 데이터 테이블 표시 (디버깅 모드에서만)
            #if debug_mode:
            #    with st.expander("P&G 대차대조표 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.pg_balance_sheet_data))
            #    with st.expander("P&G 운전자본 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.pg_working_capital_data))
                    
            # P&G Balance Sheet
            with st.expander("Procter & Gamble Balance Sheet (2011-2015)", expanded=False):
                st.markdown("""
### Procter & Gamble Balance Sheet (2011-2015) (단위: 백만 달러)

| **대차대조표 (Balance Sheet)** | **2011** | **2012** | **2013** | **2014** | **2015** |
|-------------------|----------|----------|----------|----------|----------|
| **자산 (Assets)** |  |  |  |  |  |
| 현금 및 단기투자 (Cash & ST Investments) | $2,768 | $4,436 | $5,947 | $10,686 | $11,612 |
| 매출채권 (Accounts Receivable) | $6,275 | $6,068 | $6,508 | $6,386 | $4,861 |
| 재고자산 (Inventory) | $7,379 | $6,721 | $6,909 | $6,759 | $5,454 |
| 선급비용 (Prepaid Expenses) | $4,408 | $3,684 | $3,678 | $3,345 | $2,853 |
| 기타유동자산 (Other Current Assets) | $1,140 | $1,001 | $948 | $4,441 | $4,866 |
| **유동자산 (Current Assets)** | **$21,970** | **$21,910** | **$23,990** | **$31,617** | **$29,646** |
| 순유형자산 (Net PP&E) | $21,293 | $20,377 | $21,666 | $22,304 | $20,268 |
| 영업권 및 무형자산 (Goodwill & Intangibles) | $90,182 | $84,761 | $86,760 | $84,547 | $74,145 |
| 기타비유동자산 (Other LT Assets) | $4,909 | $5,196 | $6,847 | $5,798 | $5,436 |
| **총자산 (Total Assets)** | **$138,354** | **$132,244** | **$139,263** | **$144,266** | **$129,495** |
| **부채 및 자본 (Liabilities & Net Worth)** |  |  |  |  |  |
| 매입채무 (Accounts Payable) | $8,022 | $7,920 | $8,777 | $8,461 | $8,257 |
| 미지급비용 (Accrued Expenses) | $5,696 | $4,304 | $5,161 | $5,336 | $4,564 |
| 단기차입금 (Short-term Borrowings) | $6,987 | $4,615 | $7,926 | $11,399 | $9,249 |
| 유동성장기부채 (Current Portion of LT Debt) | $2,994 | $4,083 | $4,506 | $4,307 | $2,752 |
| 기타유동부채 (Other Current Liabilities) | $3,594 | $3,985 | $3,667 | $4,223 | $4,968 |
| **유동부채 (Current Liabilities)** | **$27,293** | **$24,907** | **$30,037** | **$33,726** | **$29,790** |
| 장기부채 (Long Term Debt) | $22,033 | $21,080 | $19,111 | $19,811 | $18,297 |
| 연금부채 (Pension Liabilities) | $6,275 | $8,954 | $7,740 | $7,890 | $6,997 |
| 기타비유동부채 (Other LT Liabilities) | $14,752 | $13,268 | $13,666 | $12,863 | $11,361 |
| **총부채 (Total Liabilities)** | **$70,353** | **$68,209** | **$70,554** | **$74,290** | **$66,445** |
| 우선주 (Preferred Stock) | $1,234 | $1,195 | $1,137 | $1,111 | $1,077 |
| 보통주자본 (Common Equity) | $66,406 | $62,244 | $66,927 | $68,103 | $61,342 |
| 소수주주지분 (Minority Interest) | $361 | $596 | $645 | $762 | $631 |
| **총자본 (Total Equity)** | **$68,001** | **$64,035** | **$68,709** | **$69,976** | **$63,050** |
| **총부채 및 자본 (Total Liab. & Equity)** | **$138,354** | **$132,244** | **$139,263** | **$144,266** | **$129,495** |
| **재무비율 및 정보 (Financial Ratios & Information)** |  |  |  |  |  |
| 유동비율 (Current Ratio, CA/CL) | 0.80 | 0.88 | 0.80 | 0.94 | 1.00 |
| 총부채 (Total Debt) | $32,014 | $29,778 | $31,543 | $35,417 | $30,298 |
| 부채비율 (Debt-to-Total Capital, D/TC) | 32.0% | 31.7% | 31.5% | 33.6% | 32.5% |
| 순부채 (Net Debt, Debt - Cash) | $29,246 | $25,342 | $25,596 | $24,731 | $18,686 |
| 재무레버리지 (Fin. Leverage, Assets/Equity) | 2.03 | 2.07 | 2.03 | 2.06 | 2.05 |
| S&P 장기부채 신용등급 (Long-Term Debt Rating) | AA- | AA- | AA- | AA- | AA- |
| **운전자본 (Working Capital)** |  |  |  |  |  |
| 자산회전율 (Asset Turnover, Sales/Assets) | 0.59 | 0.62 | 0.58 | 0.56 | 0.59 |
| 재고회전율 (Inventory Turns, COGS/Inventory) | 5.40 | 6.16 | 5.79 | 6.01 | 7.01 |

                """)

        except Exception as e:
            st.error(f"P&G 대차대조표 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
            
    def render_exhibit_3(self):
        """Exhibit 3 - P&G 운전자본 분석"""
        try:
            # 운전자본 컴포넌트 HTML 코드 생성
            html_code = self.pg_working_capital_generator.generate_html()
            
            # 디버깅 옵션 추가 - 고유 키 추가
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit3")
            
            if debug_mode:
                st.sidebar.subheader("디버깅 정보")
                st.sidebar.json(self.data_provider.pg_working_capital_data)
                
                # HTML 코드 길이 표시
                st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
                
                # HTML 코드 일부 표시
                with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                    st.code(html_code[:1000] + "...", language="html")
            
            # HTML 렌더링 높이 설정 - 고유 키 추가
            height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_exhibit3") if debug_mode else 3000
            
            # HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
            # 데이터 테이블 표시 (디버깅 모드에서만)
            if debug_mode:
                with st.expander("P&G 운전자본 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.pg_working_capital_data))
                    
        except Exception as e:
            st.error(f"P&G 운전자본 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
    
    def render_exhibit_4(self):
        """Exhibit 4 - P&G SCF 경제적 효과 분석"""
        try:
            #st.header("P&G SCF 프로그램의 경제적 효과 분석 (Exhibit 4)")
            
            # SCF 다이어그램 이미지 표시
            #st.subheader("SCF 다이어그램")
            st.image("static/images/SCF.png", caption="Operational Flows in the SCF Program")
                    
            # Generator 객체 생성
            scf_economics_generator = PGSCFEconomicsGenerator()
            
            # Chart.js를 사용한 HTML 코드 생성
            html_code = scf_economics_generator.generate_html()
            
            # 디버깅 옵션 추가
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit4")
            
            if debug_mode:
                st.sidebar.subheader("디버깅 정보")
                
                # HTML 코드 길이 표시
                st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
                
                # HTML 코드 일부 표시
                with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                    st.code(html_code[:1000] + "...", language="html")
            
            # HTML 렌더링 높이 설정
            height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_exhibit4") if debug_mode else 3000
            
            # HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
        except Exception as e:
            st.error(f"P&G SCF 경제적 효과 분석 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
    
    def render_exhibit_5(self):
        """Exhibit 5 - Fibria 셀룰로즈 재무 분석"""
        try:
            # Chart.js를 사용한 HTML 코드 생성
            html_code = self.fibria_financial_generator.generate_html()
            
            # 디버깅 옵션 추가
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit5")
            
            if debug_mode:
                st.sidebar.subheader("디버깅 정보")
                st.sidebar.json(self.data_provider.fibria_financial_data)
                st.sidebar.json(self.data_provider.fibria_scf_impact_data)
                st.sidebar.json(self.data_provider.fibria_market_data)
                
                # HTML 코드 길이 표시
                st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
                
                # HTML 코드 일부 표시
                with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                    st.code(html_code[:1000] + "...", language="html")
            
            # HTML 렌더링 높이 설정
            height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_exhibit5") if debug_mode else 3000
            
            # HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
            # 데이터 테이블 표시 (디버깅 모드에서만)
            #if debug_mode:
            #    with st.expander("Fibria 재무 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.fibria_financial_data))
            #    with st.expander("Fibria SCF 영향 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.fibria_scf_impact_data))
            
            # Fibria 재무 분석 내용 추가
            with st.expander("Fibria Celulose 재무 분석 상세", expanded=False):
                st.markdown("""
                ## 주요 손익계산서 항목 (단위: 백만)

                | 항목 | 2012 (R$) | 2013 (R$) | 2014 (R$) | 2015.6 (R$) | 2015.6 (USD) |
                |------|-----------|-----------|-----------|-------------|--------------|
                | **매출(Revenue)** | 6,174 | 6,917 | 7,084 | 8,054 | 3,099 |
                | **매출원가(COGS)** | 5,237 | 5,382 | 5,546 | 5,560 | 2,139 |
                | **매출총이익(Gross Profit)** | 937 | 1,535 | 1,538 | 2,494 | 960 |
                | **영업이익(Operating Income)** | 345 | 914 | 1,660 | 1,698 | 653 |
                | **환율 손익(Currency Exchange)** | -735 | -933 | -722 | -1,926 | -741 |
                | **순이익(Net Income)** | -705 | -706 | 156 | -449 | -173 |

                ## 주요 수익성 지표

                | 지표 | 2012 | 2013 | 2014 | 2015.6 |
                |------|------|------|------|--------|
                | **매출 성장률** | - | 5.5% | 12.0% | 13.7% |
                | **매출총이익률(Gross Margin)** | 15.2% | 22.2% | 21.7% | 31.0% |
                | **영업이익률(Operating Margin)** | 5.6% | 13.2% | 23.4% | 21.1% |
                | **순이익률(Net Margin)** | -11.4% | -10.2% | 2.2% | -5.6% |
                | **총자산이익률(ROA)** | -2.5% | -2.6% | 0.6% | -1.7% |
                | **자기자본이익률(ROE)** | -4.6% | -4.9% | 1.1% | -3.1% |

                ## 운영 지표 및 기타 정보

                | 항목 | 2012 | 2013 | 2014 | 2015.6 |
                |------|------|------|------|--------|
                | **펄프 판매량(천 톤)** | 5,357 | 5,198 | 5,305 | 5,370 |
                | **유럽 펄프 가격(USD/톤)** | $780 | $770 | $741 | $793 |
                | **감가상각비(R$ 백만)** | 1,720 | 1,752 | 1,791 | 1,818 |
                | **자본지출(R$ 백만)** | 1,078 | 1,287 | 1,291 | 1,657 |
                | **평균 환율(R$/USD)** | 1.96 | 2.16 | 2.35 | 2.60 |

                ## 주요 재무 분석 시사점

                1. **영업 실적 개선**: 영업이익이 2012년 345백만 레알에서 2015년 6월 기준 1,698백만 레알로 크게 증가하며 영업이익률도 5.6%에서 21.1%로 상승

                2. **환율 위험 노출**: 브라질 레알화의 평가절하로 인한 환율 손실이 지속적으로 발생하여 순이익에 부정적 영향을 미침

                3. **매출 및 마진 향상**: 매출이 꾸준히 증가하고 매출총이익률이 15.2%에서 31.0%로 크게 개선됨

                4. **안정적인 판매량**: 펄프 판매량은 5,200-5,400천 톤 수준으로 비교적 안정적이며, 판매 가격은 2015년 회복세를 보임

                5. **투자 확대**: 자본지출이 2012년 대비 2015년에 50% 이상 증가하며 미래 성장을 위한 투자가 이루어짐
                """)
                    
        except Exception as e:
            st.error(f"Fibria 재무 분석 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
    
    def render_exhibit_6(self):
        """Exhibit 6 - Fibria 셀룰로즈 대차대조표 분석"""
        try:
            # Chart.js를 사용한 HTML 코드 생성
            html_code = self.fibria_balance_sheet_generator.generate_html()
            
            # 디버깅 옵션 추가
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit6")
            
            if debug_mode:
                st.sidebar.subheader("디버깅 정보")
                st.sidebar.json(self.data_provider.fibria_balance_sheet_data)
                st.sidebar.json(self.data_provider.fibria_working_capital_data)
                st.sidebar.json(self.data_provider.fibria_scf_analysis_data)
                
                # HTML 코드 길이 표시
                st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
                
                # HTML 코드 일부 표시
                with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                    st.code(html_code[:1000] + "...", language="html")
            
            # HTML 렌더링 높이 설정
            height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_exhibit6") if debug_mode else 3000
            
            # HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
            # 데이터 테이블 표시 (디버깅 모드에서만)
            #if debug_mode:
            #    with st.expander("Fibria 대차대조표 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.fibria_balance_sheet_data))
            #    with st.expander("Fibria 운전자본 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.fibria_working_capital_data))
            #    with st.expander("Fibria SCF 영향 분석 데이터", expanded=False):
            #        st.dataframe(pd.DataFrame(self.data_provider.fibria_scf_analysis_data))
            
            # Fibria 재무상태표 분석 내용 추가
            with st.expander("Fibria Celulose 재무상태표 상세 분석", expanded=False):
                st.markdown("""
                ## 1. 재무상태표 주요 데이터
                (단위: 백만 브라질 레알)

                | 재무상태표 항목 | 2012 | 2013 | 2014 | 2015년 6월 |
                |--------------|-------|-------|-------|------------|
                | **자산(Assets)** |
                | 현금 및 단기투자 | R$ 3,296 | R$ 2,099 | R$ 745 | R$ 1,386 |
                | 매출채권 | R$ 964 | R$ 1,477 | R$ 695 | R$ 875 |
                | 재고자산 | R$ 1,183 | R$ 1,266 | R$ 1,239 | R$ 1,455 |
                | 기타 유동자산 | R$ 803 | R$ 966 | R$ 583 | R$ 147 |
                | **유동자산 합계** | **R$ 6,246** | **R$ 5,807** | **R$ 3,261** | **R$ 3,862** |
                | 유형자산(순액) | R$ 14,891 | R$ 13,224 | R$ 12,959 | R$ 12,810 |
                | 영업권 및 무형자산 | R$ 4,717 | R$ 4,634 | R$ 4,552 | R$ 4,521 |
                | 기타 비유동자산 | R$ 2,290 | R$ 3,085 | R$ 4,822 | R$ 5,308 |
                | **자산 총계** | **R$ 28,145** | **R$ 26,750** | **R$ 25,594** | **R$ 26,501** |
                | **부채 및 자본(Liabilities & Net Worth)** |
                | 매입채무 | R$ 436 | R$ 587 | R$ 593 | R$ 637 |
                | 미지급비용 | R$ 139 | R$ 129 | R$ 135 | R$ 111 |
                | 단기차입금 | R$ 0 | R$ 196 | R$ 263 | R$ 153 |
                | 유동성장기부채 | R$ 1,138 | R$ 2,777 | R$ 703 | R$ 741 |
                | 기타 유동부채 | R$ 762 | R$ 760 | R$ 405 | R$ 445 |
                | **유동부채 합계** | **R$ 2,475** | **R$ 4,448** | **R$ 2,099** | **R$ 2,086** |
                | 장기차입금 | R$ 9,630 | R$ 6,801 | R$ 7,361 | R$ 8,121 |
                | 기타 비유동부채 | R$ 869 | R$ 1,010 | R$ 1,518 | R$ 1,730 |
                | **부채 총계** | **R$ 12,974** | **R$ 12,259** | **R$ 10,978** | **R$ 11,937** |
                | **자본 총계** | **R$ 15,171** | **R$ 14,491** | **R$ 14,616** | **R$ 14,563** |
                | **부채 및 자본 총계** | **R$ 28,145** | **R$ 26,750** | **R$ 25,594** | **R$ 26,501** |

                ## 2. 주요 재무비율

                | 재무비율 | 2012 | 2013 | 2014 | 2015년 6월 |
                |---------|------|------|------|-----------|
                | 유동비율(Current Ratio) | 2.52 | 1.31 | 1.55 | 1.85 |
                | 총부채(Total Debt) | R$ 10,768 | R$ 9,773 | R$ 8,327 | R$ 9,015 |
                | 부채비율(Debt-to-Total Capital) | 41.5% | 40.3% | 36.3% | 38.2% |
                | 재무레버리지(Assets/Equity) | 1.86 | 1.85 | 1.75 | 1.82 |
                | S&P 장기부채 신용등급 | BB | BB+ | BB+ | BBB- |
                | 자산회전율(Sales/Assets) | 0.22 | 0.26 | 0.28 | 0.34 |
                | 재고회전율(COGS/Inv.) | 4.43 | 4.25 | 4.48 | 3.87 |
                | 평균환율(레알/USD) | 1.9550 | 2.1605 | 2.3547 | 2.6913 |

                ## 3. 주요 재무 트렌드 분석

                ### 자산 구조 변화
                - **총자산**: 2012년 R$28,145백만에서 2015년 6월 R$26,501백만으로 5.8% 감소
                - **유형자산(PP&E)**: 2012년 R$14,891백만에서 2015년 6월 R$12,810백만으로 14.0% 감소
                - **현금 및 단기투자**: 2012년 R$3,296백만에서 2014년 R$745백만으로 급감한 후 2015년 6월 R$1,386백만으로 일부 회복

                ### 부채 및 자본 구조 변화
                - **총부채**: 2012년 R$12,974백만에서 2014년 R$10,978백만으로 감소 후 2015년 6월 R$11,937백만으로 소폭 증가
                - **장기차입금**: 2012년 R$9,630백만에서 2013년 R$6,801백만으로 크게 감소 후 2015년 6월 R$8,121백만으로 증가 추세
                - **자본총계**: 2012-2015년 동안 R$14,500백만~R$15,171백만 사이에서 비교적 안정적으로 유지

                ### 재무비율 개선
                - **유동비율**: 2012년 2.52에서 2013년 1.31로 하락 후 2015년 6월 1.85로 개선
                - **부채비율**: 2012년 41.5%에서 2014년 36.3%로 감소 후 2015년 6월 38.2%로 소폭 증가
                - **신용등급**: BB(2012)에서 BBB-(2015년 6월)로 투자적격등급으로 상승

                ### 환율 영향
                - 브라질 레알화는 2012년 1달러당 1.96레알에서 2015년 6월 2.69레알로 37.8% 평가절하
                - 이는 달러 기반 부채를 가진 Fibria에게 부정적인 영향을 미침

                ## 4. P&G의 SCF 프로그램 관점에서의 시사점

                1. Fibria는 신용등급이 개선되었음에도 현금 및 단기투자 감소와 매출채권의 변동성은 유동성 관리의 중요성을 보여줌
                2. P&G의 SCF 프로그램은 Fibria에게 다음과 같은 이점 제공:
                   - 매출채권 조기 현금화를 통한 유동성 개선
                   - P&G의 AA- 신용등급을 활용한 낮은 금융비용(자체 신용등급 BBB-보다 유리)
                   - 현금흐름 예측 가능성 향상
                   - 기존 신용한도에 영향 없이 추가 자금조달 가능

                이러한 분석을 통해 Fibria가 P&G의 SCF 프로그램에 참여함으로써 재무구조 개선과 운전자본 최적화에 긍정적인 효과를 얻고 있음을 알 수 있습니다.
                """)
                    
        except Exception as e:
            st.error(f"Fibria 대차대조표 분석 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
    
    def render_exhibit_7(self):
        """Exhibit 7 - Fibria 운전자본 분석"""
        try:
            # Chart.js를 사용한 HTML 코드 생성
            html_code = self.fibria_working_capital_generator.generate_html()
            
            # 디버깅 옵션 추가
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_exhibit7")
            
            if debug_mode:
                st.sidebar.subheader("디버깅 정보")
                st.sidebar.json(self.data_provider.get_working_capital_data())
                st.sidebar.json(self.data_provider.get_scf_impact_data())
                st.sidebar.json(self.data_provider.get_working_capital_need_data())
                
                # HTML 코드 길이 표시
                st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
                
                # HTML 코드 일부 표시
                with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                    st.code(html_code[:1000] + "...", language="html")
            
            # HTML 렌더링 높이 설정
            height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_exhibit7") if debug_mode else 3000
            
            # HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
            # 데이터 테이블 표시 (디버깅 모드에서만)
            if debug_mode:
                with st.expander("Fibria 운전자본 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.get_working_capital_data()))
                with st.expander("SCF 영향 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.get_scf_impact_data()))
                with st.expander("운전자본 필요량 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.get_working_capital_need_data()))
                    
        except Exception as e:
            st.error(f"Fibria 운전자본 분석 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
    
    def render_exhibit_8(self):
        """Exhibit 8 - 시장 금리 현황 분석"""
        
        #st.subheader("Market Analysis")
        
        # React 컴포넌트 생성
        html_code = self.react_generator.generate_html()
        
        # HTML 코드 렌더링
        debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit8")
        
        if debug_mode:
            st.sidebar.subheader("디버깅 정보")
            
            # HTML 코드 길이 표시
            st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
            
            # HTML 코드 일부 표시
            with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                st.code(html_code[:1000] + "...", language="html")
            
            # 기초 데이터 표시
            with st.sidebar.expander("금리 데이터", expanded=False):
                st.json(self.data_provider.rate_data)
        
        try:
            # HTML 렌더링 높이 설정
            height = st.sidebar.slider("차트 영역 높이", 500, 2000, 800, 100) if debug_mode else 800
            
            # HTML 렌더링
            st.components.v1.html(html_code, height=height, scrolling=True)
            
        except Exception as e:
            st.error(f"컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            st.exception(e)
    
    def render_q1(self):
        """Q1 - P&G가 2013년 4월 공급업체 지불 기간을 연장한 이유"""
        
        # Q1 탭용 재무 컴포넌트 표시
        st.components.v1.html(self.pg_financial_generator_q1.generate_html(), height=1000, scrolling=True)
        
        #st.markdown("""
        #### 주요 이유:
        
        #1. **운전자본 최적화**: 
        #   - P&G는 매출 성장이 정체되고 있는 상황에서 현금흐름을 개선하기 위해 운전자본 최적화가 필요했습니다.
        #   - 공급업체 지불 기간을 45일에서 75일로 연장함으로써 현금 유출을 지연시켜 운전자본을 개선할 수 있었습니다.
        
        #2. **신용등급 활용**: 
        #   - P&G는 AA- 신용등급을 보유하고 있어 공급업체에 유리한 금리로 조기지불 옵션을 제공할 수 있었습니다.
        #   - 이는 공급업체에게도 이점이 되는 윈-윈 솔루션이었습니다.
        
        #3. **공급업체 관계 유지**: 
        #   - 단순히 지불 기간을 연장하는 것이 아니라, 조기지불 옵션을 통해 공급업체의 자금 조달 비용을 절감할 수 있는 방안을 제시했습니다.
        #   - 이를 통해 공급업체 관계를 해치지 않고도 운전자본을 개선할 수 있었습니다.
        
        #4. **자본 효율성**: 
        #   - 손익계산서에 직접적인 영향을 주지 않으면서 현금흐름을 개선할 수 있는 방법이었습니다.
        #   - 특히 2015년 베네수엘라 사업 회계방식 변경으로 인한 일회성 비용 발생 전에 현금 버퍼를 확보하는 데 도움이 되었습니다.
        
        #5. **산업 리더십**: 
        #   - P&G는 공급망 금융에 대한 혁신적인 접근법을 통해 산업 내 리더십을 강화했습니다.
        #   - 이는 경쟁사 대비 차별화된 전략이 되었습니다.
        #""")
    
    def render_q2(self):
        """Q2 - 질문 2에 대한 응답"""
        # Generator 객체 생성
        scf_economics_generator = PGSCFEconomicsQ2Generator()
        
        # Chart.js를 사용한 HTML 코드 생성
        html_code = scf_economics_generator.generate_html()
        
        # 디버깅 옵션 추가
        debug_mode = st.sidebar.checkbox("디버깅 모드", value=True, key="debug_mode_q2")
        
        if debug_mode:
            st.sidebar.subheader("디버깅 정보")
            
            # HTML 코드 길이 표시
            st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
            
            # HTML 코드 일부 표시
            with st.sidebar.expander("HTML 코드 미리보기", expanded=False):
                st.code(html_code[:1000] + "...", language="html")
        
        # HTML 렌더링 높이 설정
        height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100, key="height_slider_q2") if debug_mode else 3000
        
        # HTML 렌더링
        st.components.v1.html(html_code, height=height, scrolling=True)
    
    def render_q3(self):
        """Q3 - 질문 3에 대한 응답"""
        st.header("Q3: P&G가 2013년 4월에 새로운 결제 조건과 함께 SCF 프로그램을 동시에 시작한 이유는 무엇인가요?")
        st.header("SCF 프로그램은 어떻게 운영되며 누가 혜택을 받나요? SCF 융자 금리는 경쟁력이 있나요?")
        
        # Generator 객체 생성
        scf_economics_generator = PGSCFEconomicsQ3Generator()
        
        # HTML 코드 생성
        html_code = scf_economics_generator.generate_html()
        
        # HTML 렌더링
        st.components.v1.html(html_code, height=2500, scrolling=True)
    
    def render_q4(self):
        """Q4 - P&G의 SCF가 win-win-win 프로그램인지 분석"""
        st.header("Q4: P&G는 SCF가 win-win-win 프로그램이라는 주장이 사실인가요? 손해를 보는 사람은 없나요?")
        
        # Generator 객체 생성
        scf_economics_generator = PGSCFEconomicsQ4Generator()
        
        # HTML 코드 생성
        html_code = scf_economics_generator.generate_html()
        
        # HTML 렌더링
        st.components.v1.html(html_code, height=3000, scrolling=True)
    
    def render_q5(self):
        """Q5 - 질문 5에 대한 응답"""
        # Generator 객체 생성
        fibria_scf_analysis = FibriaSCFAnalysisComponent()
        
        # HTML 코드 생성
        html_code = fibria_scf_analysis.generate_html()
        
        # HTML 렌더링
        st.components.v1.html(html_code, height=2500, scrolling=True)
    
    def render_q6(self):
        """Q6 - 대기업이 중소 공급업체에 지불 기간을 연장해야 하는지 여부"""
        st.header("Q6: P&G가 A/P를 신속하게 지급해야 한다는 주장의 근거는 무엇인가요?")
        
        # 이미지 파일 경로
        negative_cycle_path = "static/images/negative_cycle.png"
        positive_cycle_path = "static/images/positive_cycle.png"
        
        # 이미지가 없으면 생성
        if not os.path.exists(negative_cycle_path) or not os.path.exists(positive_cycle_path):
            self.create_cycle_images()
        
        # 이미지를 나란히 표시
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("늦게 지급한 경우")
            st.image(negative_cycle_path, caption="부정적 순환")
            
        with col2:
            st.subheader("일찍 지급한 경우")
            st.image(positive_cycle_path, caption="긍정적 순환")
        
        # Chart.js를 사용한 분석 내용 표시
        html_code = f"""
        <div style="padding: 20px;">
            <style>
                .analysis-container {{
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                }}
                .card {{
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    margin: 15px 0;
                    padding: 20px;
                    transition: transform 0.3s ease;
                }}
                .card:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                }}
                .impact-meter {{
                    height: 10px;
                    background: #f0f0f0;
                    border-radius: 5px;
                    margin: 10px 0;
                    overflow: hidden;
                }}
                .impact-meter-fill {{
                    height: 100%;
                    transition: width 1s ease-in-out;
                }}
                .negative {{
                    background: linear-gradient(to right, #ff6b6b, #ff8787);
                }}
                .positive {{
                    background: linear-gradient(to right, #69db7c, #8ce99a);
                }}
                .key-point {{
                    font-size: 1.1em;
                    color: #333;
                    margin: 10px 0;
                    padding-left: 20px;
                    position: relative;
                }}
                .key-point:before {{
                    content: "•";
                    position: absolute;
                    left: 0;
                    color: #4dabf7;
                }}
                .conclusion {{
                    background: #e7f5ff;
                    border-left: 4px solid #4dabf7;
                    padding: 20px;
                    margin-top: 30px;
                    border-radius: 4px;
                }}
                .metric-container {{
                    display: flex;
                    justify-content: space-between;
                    margin: 20px 0;
                }}
                .metric-box {{
                    text-align: center;
                    padding: 15px;
                    background: #f8f9fa;
                    border-radius: 8px;
                    flex: 1;
                    margin: 0 10px;
                }}
                .metric-value {{
                    font-size: 24px;
                    font-weight: bold;
                    color: #495057;
                }}
                .metric-label {{
                    font-size: 14px;
                    color: #868e96;
                    margin-top: 5px;
                }}
            </style>
            
            <div class="analysis-container">
                <div class="card">
                    <h3 style="color: #e03131;">늦게 지급한 경우의 영향</h3>
                    <div class="impact-meter">
                        <div class="impact-meter-fill negative" style="width: 80%;"></div>
                    </div>
                    <div class="key-point">결제 기간 연장으로 인한 공급업체 자금 부담 증가</div>
                    <div class="key-point">공급업체 수익성 저하로 인한 품질 하락</div>
                    <div class="key-point">P&G 제품 품질 저하 및 수익성 악화</div>
                    <div class="key-point">결과적으로 가격 인상 압박 발생</div>
                    
                </div>
                
                <div class="card">
                    <h3 style="color: #2f9e44;">일찍 지급한 경우의 영향</h3>
                    <div class="impact-meter">
                        <div class="impact-meter-fill positive" style="width: 90%;"></div>
                    </div>
                    <div class="key-point">SCF 프로그램을 통한 공급업체 유동성 확보</div>
                    <div class="key-point">공급업체 관계 강화 및 수익성 개선</div>
                    <div class="key-point">R&D 투자 증가로 인한 품질 향상</div>
                    <div class="key-point">P&G 제품 품질 및 수익성 강화</div>
                    <div class="key-point">운전자본 효율성 증가</div>
                    
                </div>
                
                <div class="conclusion">
                    <h3 style="color: #1971c2; margin-top: 0;">결론</h3>
                    <p style="line-height: 1.6;">
                        대기업이 공급업체에 대한 지불 기간을 연장하는 것은 단기적인 현금흐름 개선에는 도움이 될 수 있으나, 
                        장기적으로는 공급망 전체의 건강성을 해칠 수 있습니다.
                    </p>
                    <p style="line-height: 1.6;">
                        SCF 프로그램과 같은 혁신적인 금융 솔루션을 활용하면, 대기업은 운전자본을 효율적으로 관리하면서도 
                        공급업체와의 관계를 강화하고 전체 공급망의 경쟁력을 높일 수 있습니다.
                    </p>
                </div>
            </div>
            
            <script>
                // 애니메이션 효과 추가
                document.addEventListener('DOMContentLoaded', function() {{
                    const cards = document.querySelectorAll('.card');
                    const meters = document.querySelectorAll('.impact-meter-fill');
                    
                    // 카드 애니메이션
                    cards.forEach(card => {{
                        card.style.opacity = '0';
                        card.style.transform = 'translateY(20px)';
                    }});
                    
                    // 미터 애니메이션
                    meters.forEach(meter => {{
                        meter.style.width = '0';
                    }});
                    
                    // 순차적으로 애니메이션 실행
                    setTimeout(() => {{
                        cards.forEach((card, index) => {{
                            setTimeout(() => {{
                                card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
                                card.style.opacity = '1';
                                card.style.transform = 'translateY(0)';
                            }}, index * 200);
                        }});
                        
                        meters.forEach((meter, index) => {{
                            setTimeout(() => {{
                                meter.style.transition = 'width 1s ease-in-out';
                                meter.style.width = meter.getAttribute('data-width') || '80%';
                            }}, (index + 2) * 200);
                        }});
                    }}, 500);
                }});
            </script>
        </div>
        """
        
        # HTML 렌더링
        st.components.v1.html(html_code, height=1000, scrolling=True)

    def create_cycle_images(self):
        """순환 다이어그램 이미지 생성"""
        try:
            import matplotlib.pyplot as plt
            import numpy as np
            
            def create_cycle_diagram(items, is_negative=False):
                # 새로운 figure 생성
                plt.figure(figsize=(10, 10))
                
                # 원 그리기
                circle = plt.Circle((0.5, 0.5), 0.4, fill=False, color='red' if is_negative else 'blue')
                plt.gca().add_patch(circle)
                
                # 항목들을 원형으로 배치
                n = len(items)
                for i, item in enumerate(items):
                    angle = 2 * np.pi * i / n
                    x = 0.5 + 0.4 * np.cos(angle)
                    y = 0.5 + 0.4 * np.sin(angle)
                    plt.text(x, y, item, ha='center', va='center', bbox=dict(facecolor='white', alpha=0.7))
                
                # 중앙에 +/- 기호 추가
                plt.text(0.5, 0.5, '-' if is_negative else '+', 
                        ha='center', va='center', color='red' if is_negative else 'blue',
                        fontsize=24, fontweight='bold')
                
                plt.axis('equal')
                plt.axis('off')
                
                return plt.gcf()
            
            # 부정적 순환 다이어그램 생성
            negative_items = [
                '결제 기간 연장',
                '공급업체 자금 부담',
                '공급업체 수익성 저하',
                '공급업체 품질저하',
                'P&G 제품 품질저하',
                'P&G 수익성 악화',
                '가격인상'
            ]
            fig_negative = create_cycle_diagram(negative_items, True)
            fig_negative.savefig('static/images/negative_cycle.png', bbox_inches='tight', dpi=300)
            plt.close(fig_negative)
            
            # 긍정적 순환 다이어그램 생성
            positive_items = [
                '결제 기간 단축',
                'SCF 프로그램',
                '공급업체 유동성',
                '공급업체 관계 강화',
                '공급업체 수익성 강화',
                'R&D 투자',
                '공급업체 품질상승',
                'P&G 제품 품질 상승',
                'P&G 수익성 강화',
                'P&G 운전 자본 강화'
            ]
            fig_positive = create_cycle_diagram(positive_items, False)
            fig_positive.savefig('static/images/positive_cycle.png', bbox_inches='tight', dpi=300)
            plt.close(fig_positive)
            
        except Exception as e:
            st.error(f"이미지 생성 중 오류가 발생했습니다: {str(e)}")

    def run(self):
        """애플리케이션 실행"""
        self.setup_page()
        self.render_buttons()
