# HTML을 파일로 저장하여 테스트하는 코드
from react_component import ReactComponentGenerator
from data_provider import MarketDataProvider

# 데이터 및 HTML 생성
data_provider = MarketDataProvider()
generator = ReactComponentGenerator(data_provider)
html_code = generator.generate_html()

# HTML 파일로 저장
with open("test_chart.html", "w", encoding="utf-8") as f:
    f.write(html_code)

print("HTML 파일이 생성되었습니다. 브라우저에서 직접 열어보세요.")