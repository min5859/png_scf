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
    
    def setup_page(self):
        """페이지 기본 설정"""
        st.set_page_config(
            page_title="시장 금리 현황 분석",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        #st.title("시장 금리 현황 분석")
    
    def render_tabs(self):
        """탭 렌더링"""
        # 탭 생성 - Exhibit 1부터 Exhibit 8까지 생성
        tab_titles = [f"Exhibit {i}" for i in range(1, 9)]
        tabs = st.tabs(tab_titles)
        
        # Exhibit 1 - P&G 재무 지표 시각화
        with tabs[0]:
            st.header("P&G 재무 지표 시각화 (Exhibit 1)")
            self.render_exhibit_1()
        
        # Exhibit 2 - P&G 대차대조표 분석
        with tabs[1]:
            st.header("P&G 대차대조표 분석 (Exhibit 2)")
            self.render_exhibit_2()
        
        # Exhibit 3 - P&G 운전자본 분석
        with tabs[2]:
            st.header("P&G 운전자본 분석 (Exhibit 3)")
            self.render_exhibit_3()
        
        # Exhibit 4 - P&G SCF 경제적 효과 분석
        with tabs[3]:
            self.render_exhibit_4()
        
        # Exhibit 5 - Fibria 재무 분석
        with tabs[4]:
            st.header("Fibria 셀룰로즈 재무 분석 (Exhibit 5)")
            self.render_exhibit_5()
        
        # Exhibit 6 - Fibria 대차대조표 분석
        with tabs[5]:
            st.header("Fibria 셀룰로즈 대차대조표 분석 (Exhibit 6)")
            self.render_exhibit_6()
        
        # Exhibit 7 - Fibria 운전자본 분석
        with tabs[6]:
            st.header("Fibria 운전자본 분석 (Exhibit 7)")
            self.render_exhibit_7()
        
        # Exhibit 8 탭
        with tabs[7]:
            st.header("시장 금리 현황 분석 (Exhibit 8)")
            self.render_exhibit_8()
    
    def render_exhibit_1(self):
        """Exhibit 1 - P&G 재무 지표 시각화 (Chart.js 사용)"""
        # Chart.js를 사용한 HTML 코드 생성
        html_code = self.pg_financial_generator.generate_html()
        
        # 디버깅 옵션 추가 - 고유 키 추가
        debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit1")
        
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
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit2")
            
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
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit3")
            
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
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit4")
            
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
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit5")
            
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
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit6")
            
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
            debug_mode = st.sidebar.checkbox("디버깅 모드", value=False, key="debug_mode_exhibit7")
            
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
    
    def run(self):
        """애플리케이션 실행"""
        self.setup_page()
        self.render_tabs()
