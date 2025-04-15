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
        st.markdown("### 이 대시보드에 대한 정보")
        st.markdown("""
        이 대시보드는 Streamlit 내에서 React 컴포넌트를 사용하여 구현되었습니다. 
        Streamlit의 HTML 컴포넌트 내에서 React와 Recharts를 활용해 동적인 차트를 렌더링합니다.

        **주요 기술:**
        - Streamlit: 파이썬 기반 웹 애플리케이션 프레임워크
        - React: 사용자 인터페이스 구축을 위한 JavaScript 라이브러리
        - Recharts: React 기반 차트 라이브러리
        - Babel: JSX 코드를 브라우저에서 실행 가능한 JavaScript로 변환
        """)
        
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
        st.write("test")
        #self.render_react_component()
        self.show_additional_info()
