import streamlit as st
from data_provider import MarketDataProvider
from react_component import ReactComponentGenerator

class StreamlitApp:
    """Streamlit 애플리케이션 클래스"""
    
    def __init__(self):
        """애플리케이션 초기화"""
        self.data_provider = MarketDataProvider()
        self.react_generator = ReactComponentGenerator(self.data_provider)
    
    def setup_page(self):
        """페이지 기본 설정"""
        st.set_page_config(
            page_title="시장 금리 현황 분석",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        st.title("시장 금리 현황 분석 (Exhibit 8)")
    
    def render_react_component(self):
        """React 컴포넌트 렌더링"""
        html_code = self.react_generator.generate_html()
        
        # 디버깅 옵션 추가
        debug_mode = st.sidebar.checkbox("디버깅 모드", value=False)
        
        if debug_mode:
            st.sidebar.subheader("디버깅 정보")
            st.sidebar.json(self.data_provider.get_all_data())
            
            # HTML 코드 길이 표시
            st.sidebar.text(f"HTML 코드 길이: {len(html_code)} 문자")
            
            # HTML 코드 일부 표시
            with st.sidebar.expander("HTML 코드 미리보기"):
                st.code(html_code[:1000] + "...", language="html")
        
        # 높이 및 스크롤링 옵션 조정 가능
        height = st.sidebar.slider("차트 영역 높이", 2000, 5000, 3000, 100) if debug_mode else 3000
        
        # React 컴포넌트 렌더링 - 오류 처리 추가
        try:
            st.components.v1.html(html_code, height=height, scrolling=True)
        except Exception as e:
            st.error(f"React 컴포넌트 렌더링 중 오류가 발생했습니다: {str(e)}")
            
            if debug_mode:
                st.exception(e)
    
    def show_additional_info(self):
        """추가 정보 표시"""
        st.markdown("---")
        
        # 데이터 미리보기 섹션 추가
        st.markdown("### 데이터 미리보기")
        data_frames = self.data_provider.get_data_frames()
        
        # 확장 가능한 섹션으로 각 데이터프레임 표시
        for name, df in data_frames.items():
            with st.expander(f"{name} 데이터"):
                st.dataframe(df)
    
    def run(self):
        """애플리케이션 실행"""
        self.setup_page()
        self.render_react_component()
        self.show_additional_info()
