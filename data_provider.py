import pandas as pd
from typing import Dict, Any, List

class MarketDataProvider:
    """시장 금리 분석에 필요한 데이터를 제공하는 클래스"""
    
    def __init__(self):
        """데이터 초기화"""
        self._initialize_data()
    
    def _initialize_data(self):
        """모든 차트 데이터 초기화"""
        # 미국 국채 수익률 데이터 (2015년 8월 7일 기준)
        self.treasury_yields_data = [
            {"maturity": "1개월", "yield": 0.05},
            {"maturity": "3개월", "yield": 0.12},
            {"maturity": "6개월", "yield": 0.17},
            {"maturity": "1년", "yield": 0.33},
            {"maturity": "5년", "yield": 1.52},
            {"maturity": "10년", "yield": 2.16},
            {"maturity": "30년", "yield": 2.86}
        ]
        
        # 회사채 수익률 데이터 (1년 만기)
        self.corporate_bond_yields_data = [
            {"rating": "AAA", "yield": 0.48},
            {"rating": "AA", "yield": 0.63},
            {"rating": "A", "yield": 0.74},
            {"rating": "BBB", "yield": 1.13},
            {"rating": "BB", "yield": 2.80},
            {"rating": "B", "yield": 3.74},
            {"rating": "CCC", "yield": 4.58}
        ]
        
        # 단기 금리 데이터
        self.short_term_rates_data = [
            {"type": "1개월 LIBOR", "rate": 0.19},
            {"type": "3개월 LIBOR", "rate": 0.30},
            {"type": "6개월 LIBOR", "rate": 0.49},
            {"type": "30일 AA CP", "rate": 0.18},
            {"type": "60일 AA CP", "rate": 0.23},
            {"type": "90일 AA CP", "rate": 0.30}
        ]
        
        # SCF 할인율 시뮬레이션 데이터
        self.scf_rate_simulation_data = [
            {"scenario": "현재 (2013 계약)", "libor": 0.30, "spread": 1.00, "totalRate": 1.30, "period": 100, "discount": 0.35, "costYear": 1.05},
            {"scenario": "갱신 시나리오 1", "libor": 0.30, "spread": 0.80, "totalRate": 1.10, "period": 100, "discount": 0.30, "costYear": 0.90},
            {"scenario": "갱신 시나리오 2", "libor": 0.30, "spread": 0.70, "totalRate": 1.00, "period": 100, "discount": 0.27, "costYear": 0.81}
        ]
        
        # 신용등급별 SCF 비용 비교
        self.ratings_comparison_data = [
            {"rating": "P&G (AA-)", "borrowingCost": 0.63, "scfDiscount": 0.30, "costDifference": 0.33},
            {"rating": "Fibria (BBB-)", "borrowingCost": 1.13, "scfDiscount": 0.30, "costDifference": 0.83},
            {"rating": "BB 등급 기업", "borrowingCost": 2.80, "scfDiscount": 0.30, "costDifference": 2.50}
        ]
        
        # 역사적 LIBOR 추이 데이터 (가상)
        self.historical_libor_data = [
            {"date": "2012", "libor3m": 0.43},
            {"date": "2013", "libor3m": 0.27},
            {"date": "2014", "libor3m": 0.23},
            {"date": "2015 (8월)", "libor3m": 0.30}
        ]
        
        # P&G 재무 지표 데이터 (확장된 버전)
        self.pg_financial_data = [
            {"year": "2011", "revenue": 81104, "grossProfit": 41245, "operatingIncome": 15495, "netIncome": 11797, "grossMargin": 50.9, "operatingMargin": 19.1, "netMargin": 14.5, "employees": 129000, "eps": 4.12, "dividend": 1.97},
            {"year": "2012", "revenue": 82006, "grossProfit": 40595, "operatingIncome": 14611, "netIncome": 10756, "grossMargin": 49.5, "operatingMargin": 17.8, "netMargin": 13.1, "employees": 126000, "eps": 3.82, "dividend": 2.14},
            {"year": "2013", "revenue": 80116, "grossProfit": 40125, "operatingIncome": 14125, "netIncome": 11412, "grossMargin": 50.1, "operatingMargin": 17.6, "netMargin": 14.1, "employees": 121000, "eps": 4.04, "dividend": 2.29},
            {"year": "2014", "revenue": 80510, "grossProfit": 39899, "operatingIncome": 15497, "netIncome": 11643, "grossMargin": 49.6, "operatingMargin": 19.2, "netMargin": 14.5, "employees": 118000, "eps": 4.19, "dividend": 2.45},
            {"year": "2015", "revenue": 76279, "grossProfit": 38031, "operatingIncome": 14873, "netIncome": 7036, "grossMargin": 49.9, "operatingMargin": 19.5, "netMargin": 9.2, "employees": 110000, "eps": 2.50, "dividend": 2.59}
        ]
    
    def get_all_data(self) -> Dict[str, Any]:
        """모든 데이터를 딕셔너리 형태로 반환"""
        return {
            'treasuryYieldsData': self.treasury_yields_data,
            'corporateBondYieldsData': self.corporate_bond_yields_data,
            'shortTermRatesData': self.short_term_rates_data,
            'scfRateSimulationData': self.scf_rate_simulation_data,
            'ratingsComparisonData': self.ratings_comparison_data,
            'historicalLiborData': self.historical_libor_data,
            'pgFinancialData': self.pg_financial_data
        }
    
    def get_data_frames(self) -> Dict[str, pd.DataFrame]:
        """모든 데이터를 DataFrame 형태로 반환"""
        return {
            'treasury_yields': pd.DataFrame(self.treasury_yields_data),
            'corporate_bond_yields': pd.DataFrame(self.corporate_bond_yields_data),
            'short_term_rates': pd.DataFrame(self.short_term_rates_data),
            'scf_rate_simulation': pd.DataFrame(self.scf_rate_simulation_data),
            'ratings_comparison': pd.DataFrame(self.ratings_comparison_data),
            'historical_libor': pd.DataFrame(self.historical_libor_data),
            'pg_financial': pd.DataFrame(self.pg_financial_data)
        }
