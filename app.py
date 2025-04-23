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
            st.header("P&G 재무 지표 시각화 (Exhibit 1)")
            self.render_exhibit_1()
        
        # Exhibit 2 - P&G 대차대조표 분석
        if cols[7].button(button_titles[1]):
            st.header("P&G 대차대조표 분석 (Exhibit 2)")
            self.render_exhibit_2()
        
        # Exhibit 3 - P&G 운전자본 분석
        if cols[8].button(button_titles[2]):
            st.header("P&G 운전자본 분석 (Exhibit 3)")
            self.render_exhibit_3()
        
        # Exhibit 4 - P&G SCF 경제적 효과 분석
        if cols[9].button("Example"):
            self.render_exhibit_4()
        
        # Exhibit 5 - Fibria 재무 분석
        if cols[10].button(button_titles[4]):
            st.header("Fibria 셀룰로즈 재무 분석 (Exhibit 5)")
            self.render_exhibit_5()
        
        # Exhibit 6 - Fibria 대차대조표 분석
        if cols[11].button(button_titles[5]):
            st.header("Fibria 셀룰로즈 대차대조표 분석 (Exhibit 6)")
            self.render_exhibit_6()
        
        # Exhibit 7 - Fibria 운전자본 분석
        if cols[12].button(button_titles[6]):
            st.header("Fibria 운전자본 분석 (Exhibit 7)")
            self.render_exhibit_7()
        
        # Exhibit 8 - 시장 금리 현황 분석
        if cols[13].button(button_titles[7]):
            st.header("시장 금리 현황 분석 (Exhibit 8)")
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
        if debug_mode:
            with st.expander("P&G 재무 데이터 표", expanded=False):
                st.dataframe(pd.DataFrame(self.data_provider.pg_financial_data))
    
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
            if debug_mode:
                with st.expander("P&G 대차대조표 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.pg_balance_sheet_data))
                with st.expander("P&G 운전자본 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.pg_working_capital_data))
                    
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
            st.header("P&G SCF 프로그램의 경제적 효과 분석 (Exhibit 4)")
            
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
            if debug_mode:
                with st.expander("Fibria 재무 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.fibria_financial_data))
                with st.expander("Fibria SCF 영향 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.fibria_scf_impact_data))
                    
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
            if debug_mode:
                with st.expander("Fibria 대차대조표 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.fibria_balance_sheet_data))
                with st.expander("Fibria 운전자본 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.fibria_working_capital_data))
                with st.expander("Fibria SCF 영향 분석 데이터", expanded=False):
                    st.dataframe(pd.DataFrame(self.data_provider.fibria_scf_analysis_data))
                    
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
        
        st.subheader("Market Analysis")
        
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
        
        st.markdown("""
        ### 주요 이유:
        
        1. **운전자본 최적화**: 
           - P&G는 매출 성장이 정체되고 있는 상황에서 현금흐름을 개선하기 위해 운전자본 최적화가 필요했습니다.
           - 공급업체 지불 기간을 45일에서 75일로 연장함으로써 현금 유출을 지연시켜 운전자본을 개선할 수 있었습니다.
        
        2. **신용등급 활용**: 
           - P&G는 AA- 신용등급을 보유하고 있어 공급업체에 유리한 금리로 조기지불 옵션을 제공할 수 있었습니다.
           - 이는 공급업체에게도 이점이 되는 윈-윈 솔루션이었습니다.
        
        3. **공급업체 관계 유지**: 
           - 단순히 지불 기간을 연장하는 것이 아니라, 조기지불 옵션을 통해 공급업체의 자금 조달 비용을 절감할 수 있는 방안을 제시했습니다.
           - 이를 통해 공급업체 관계를 해치지 않고도 운전자본을 개선할 수 있었습니다.
        
        4. **자본 효율성**: 
           - 손익계산서에 직접적인 영향을 주지 않으면서 현금흐름을 개선할 수 있는 방법이었습니다.
           - 특히 2015년 베네수엘라 사업 회계방식 변경으로 인한 일회성 비용 발생 전에 현금 버퍼를 확보하는 데 도움이 되었습니다.
        
        5. **산업 리더십**: 
           - P&G는 공급망 금융에 대한 혁신적인 접근법을 통해 산업 내 리더십을 강화했습니다.
           - 이는 경쟁사 대비 차별화된 전략이 되었습니다.
        """)
    
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
