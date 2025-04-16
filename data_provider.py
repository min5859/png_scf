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
        
        # P&G 대차대조표 데이터
        self.pg_balance_sheet_data = [
            {
                "year": "2011",
                "currentAssets": 21970,
                "totalAssets": 138354,
                "currentLiabilities": 27293,
                "totalLiabilities": 71977,
                "totalEquity": 66377,
                "cash": 2768,
                "totalDebt": 21941,
                "debtToCapitalRatio": 0.325
            },
            {
                "year": "2012",
                "currentAssets": 21910,
                "totalAssets": 132244,
                "currentLiabilities": 24907,
                "totalLiabilities": 69041,
                "totalEquity": 63203,
                "cash": 4436,
                "totalDebt": 31536,
                "debtToCapitalRatio": 0.325
            },
            {
                "year": "2013",
                "currentAssets": 22096,
                "totalAssets": 139263,
                "currentLiabilities": 26982,
                "totalLiabilities": 73673,
                "totalEquity": 65590,
                "cash": 5947,
                "totalDebt": 31512,
                "debtToCapitalRatio": 0.324
            },
            {
                "year": "2014",
                "currentAssets": 22059,
                "totalAssets": 144266,
                "currentLiabilities": 25231,
                "totalLiabilities": 75647,
                "totalEquity": 68619,
                "cash": 8548,
                "totalDebt": 31645,
                "debtToCapitalRatio": 0.327
            },
            {
                "year": "2015",
                "currentAssets": 18865,
                "totalAssets": 129495,
                "currentLiabilities": 18849,
                "totalLiabilities": 64756,
                "totalEquity": 64739,
                "cash": 11653,
                "totalDebt": 31110,
                "debtToCapitalRatio": 0.325
            }
        ]
        
        # P&G 운전자본 데이터 (기존 데이터)
        self.pg_working_capital_data_old = [
            {
                "year": "2011",
                "accountsReceivable": 6275,
                "inventory": 7379,
                "accountsPayable": 8022,
                "daysReceivables": 27.8,
                "daysInventory": 32.6,
                "daysPayables": 38.0,
                "cashConversionCycle": 22.4
            },
            {
                "year": "2012",
                "accountsReceivable": 6068,
                "inventory": 6721,
                "accountsPayable": 7920,
                "daysReceivables": 26.5,
                "daysInventory": 29.2,
                "daysPayables": 37.0,
                "cashConversionCycle": 18.7
            },
            {
                "year": "2013",
                "accountsReceivable": 6508,
                "inventory": 6909,
                "accountsPayable": 8777,
                "daysReceivables": 28.2,
                "daysInventory": 29.9,
                "daysPayables": 41.0,
                "cashConversionCycle": 17.1
            },
            {
                "year": "2014",
                "accountsReceivable": 6386,
                "inventory": 6759,
                "accountsPayable": 8461,
                "daysReceivables": 28.1,
                "daysInventory": 29.7,
                "daysPayables": 40.0,
                "cashConversionCycle": 17.8
            },
            {
                "year": "2015",
                "accountsReceivable": 4861,
                "inventory": 5454,
                "accountsPayable": 8256,
                "daysReceivables": 23.3,
                "daysInventory": 26.2,
                "daysPayables": 53.0,
                "cashConversionCycle": -3.5
            }
        ]
        
        # P&G 확장된 운전자본 데이터 (2000-2015년, Exhibit3 차트용)
        self.pg_extended_working_capital_data = [
            {"year": "2000", "dso": 26.6, "dio": 60.6, "dpo": 38.4, "ccc": 48.8, "adjustedDpo": 32.5},
            {"year": "2001", "dso": 27.3, "dio": 58.9, "dpo": 36.1, "ccc": 50.1, "adjustedDpo": 30.8},
            {"year": "2002", "dso": 28.0, "dio": 61.6, "dpo": 39.3, "ccc": 50.3, "adjustedDpo": 33.2},
            {"year": "2003", "dso": 25.6, "dio": 60.0, "dpo": 46.1, "ccc": 39.5, "adjustedDpo": 38.5},
            {"year": "2004", "dso": 28.8, "dio": 63.9, "dpo": 52.5, "ccc": 40.2, "adjustedDpo": 43.1},
            {"year": "2005", "dso": 26.9, "dio": 65.6, "dpo": 49.8, "ccc": 42.7, "adjustedDpo": 41.1},
            {"year": "2006", "dso": 30.6, "dio": 69.3, "dpo": 54.1, "ccc": 45.8, "adjustedDpo": 44.5},
            {"year": "2007", "dso": 32.3, "dio": 69.8, "dpo": 58.4, "ccc": 43.7, "adjustedDpo": 47.9},
            {"year": "2008", "dso": 31.1, "dio": 78.2, "dpo": 63.0, "ccc": 46.4, "adjustedDpo": 51.8},
            {"year": "2009", "dso": 27.8, "dio": 64.9, "dpo": 56.4, "ccc": 36.3, "adjustedDpo": 47.2},
            {"year": "2010", "dso": 25.1, "dio": 62.9, "dpo": 71.4, "ccc": 16.6, "adjustedDpo": 58.1},
            {"year": "2011", "dso": 28.2, "dio": 67.6, "dpo": 73.5, "ccc": 22.4, "adjustedDpo": 59.7},
            {"year": "2012", "dso": 27.0, "dio": 59.2, "dpo": 69.8, "ccc": 16.4, "adjustedDpo": 57.1},
            {"year": "2013", "dso": 29.6, "dio": 63.1, "dpo": 80.1, "ccc": 12.6, "adjustedDpo": 64.9},
            {"year": "2014", "dso": 29.0, "dio": 60.7, "dpo": 76.0, "ccc": 13.7, "adjustedDpo": 62.3},
            {"year": "2015", "dso": 23.3, "dio": 52.0, "dpo": 78.8, "ccc": -3.5, "adjustedDpo": 64.8}
        ]
        
        # 기존 데이터 구조 호환성을 위해 pg_working_capital_data를 그대로 유지
        self.pg_working_capital_data = self.pg_working_capital_data_old
        
        # Fibria 재무 분석 데이터 (단위: 백만 레알)
        self.fibria_financial_data = [
            { 
                "year": "2012", 
                "revenue": 6174, 
                "cogs": 5237, 
                "grossProfit": 937, 
                "sgaExpense": 579, 
                "operatingIncome": 345, 
                "netIncome": -705,
                "grossMargin": 15.2,
                "operatingMargin": 5.6,
                "netMargin": -11.4,
                "exchangeRate": 1.955,
                "revenueUSD": 3159,
                "pulpSales": 5357,
                "pulpPrice": 780
            },
            { 
                "year": "2013", 
                "revenue": 6317, 
                "cogs": 5302, 
                "grossProfit": 1535, 
                "sgaExpense": 642, 
                "operatingIncome": 914, 
                "netIncome": -706,
                "grossMargin": 22.2,
                "operatingMargin": 13.2,
                "netMargin": -10.2,
                "exchangeRate": 2.1605,
                "revenueUSD": 2924,
                "pulpSales": 5198,
                "pulpPrice": 770
            },
            { 
                "year": "2014", 
                "revenue": 7084, 
                "cogs": 5546, 
                "grossProfit": 1538, 
                "sgaExpense": 644, 
                "operatingIncome": 1660, 
                "netIncome": 156,
                "grossMargin": 21.7,
                "operatingMargin": 23.4,
                "netMargin": 2.2,
                "exchangeRate": 2.3547,
                "revenueUSD": 3009,
                "pulpSales": 5305,
                "pulpPrice": 741
            },
            { 
                "year": "2015 (6월까지)", 
                "revenue": 8054, 
                "cogs": 5560, 
                "grossProfit": 2494, 
                "sgaExpense": 703, 
                "operatingIncome": 1698, 
                "netIncome": -449,
                "grossMargin": 31.0,
                "operatingMargin": 21.1,
                "netMargin": -5.6,
                "exchangeRate": 2.5989,
                "revenueUSD": 3099,
                "pulpSales": 5370,
                "pulpPrice": 793
            }
        ]

        # Fibria SCF 프로그램 영향 분석 (2013년 SCF 도입)
        self.fibria_scf_impact_data = [
            { 
                "year": "2012", 
                "withoutSCF": {
                    "financingCost": 154.35,  # 가정: 60일 매출채권, 2.5% 금리
                    "cashFlow": 3004.65
                },
                "withSCF": {
                    "financingCost": 154.35,
                    "cashFlow": 3004.65
                }
            },
            { 
                "year": "2013", 
                "withoutSCF": {
                    "financingCost": 146.20,  # 60일, 2.5% 금리
                    "cashFlow": 2777.80
                },
                "withSCF": {
                    "financingCost": 34.02,  # 15일, 0.35% 할인율 (도입 중)
                    "cashFlow": 2889.98
                }
            },
            { 
                "year": "2014", 
                "withoutSCF": {
                    "financingCost": 150.45,  # 60일, 2.5% 금리
                    "cashFlow": 2858.55
                },
                "withSCF": {
                    "financingCost": 31.59,  # 15일, 0.35% 할인율
                    "cashFlow": 2977.41
                }
            },
            { 
                "year": "2015", 
                "withoutSCF": {
                    "financingCost": 154.95,  # 60일, 2.5% 금리
                    "cashFlow": 2944.05
                },
                "withSCF": {
                    "financingCost": 32.54,  # 15일, 0.35% 할인율
                    "cashFlow": 3066.46
                }
            }
        ]
        
        # 환율 및 펄프 가격 추이
        self.fibria_market_data = [
            { "year": "2012", "exchangeRate": 1.955, "pulpPrice": 780 },
            { "year": "2013", "exchangeRate": 2.1605, "pulpPrice": 770 },
            { "year": "2014", "exchangeRate": 2.3547, "pulpPrice": 741 },
            { "year": "2015", "exchangeRate": 2.5989, "pulpPrice": 793 }
        ]

        # Fibria 대차대조표 데이터 (단위: 백만 레알)
        self.fibria_balance_sheet_data = [
            { 
                "year": "2012", 
                "currentAssets": 6246,
                "cash": 3296,
                "accountsReceivable": 964,
                "inventory": 1183,
                "otherCurrentAssets": 803,
                "totalAssets": 28145,
                "currentLiabilities": 2475,
                "accountsPayable": 436,
                "shortTermDebt": 1138,
                "otherCurrentLiabilities": 901,
                "longTermDebt": 9630,
                "otherLTLiabilities": 869,
                "totalLiabilities": 12974,
                "totalEquity": 15171,
                "currentRatio": 2.52,
                "totalDebt": 10768,
                "debtToCapital": 41.5,
                "exchangeRate": 1.955
            },
            { 
                "year": "2013", 
                "currentAssets": 5807,
                "cash": 2099,
                "accountsReceivable": 1477,
                "inventory": 1266,
                "otherCurrentAssets": 965,
                "totalAssets": 26750,
                "currentLiabilities": 4448,
                "accountsPayable": 587,
                "shortTermDebt": 2973,
                "otherCurrentLiabilities": 888,
                "longTermDebt": 6801,
                "otherLTLiabilities": 1010,
                "totalLiabilities": 12259,
                "totalEquity": 14491,
                "currentRatio": 1.31,
                "totalDebt": 9773,
                "debtToCapital": 40.3,
                "exchangeRate": 2.1605
            },
            { 
                "year": "2014", 
                "currentAssets": 3261,
                "cash": 745,
                "accountsReceivable": 695,
                "inventory": 1239,
                "otherCurrentAssets": 582,
                "totalAssets": 25594,
                "currentLiabilities": 2099,
                "accountsPayable": 593,
                "shortTermDebt": 966,
                "otherCurrentLiabilities": 540,
                "longTermDebt": 7361,
                "otherLTLiabilities": 1518,
                "totalLiabilities": 10978,
                "totalEquity": 14616,
                "currentRatio": 1.55,
                "totalDebt": 8327,
                "debtToCapital": 36.3,
                "exchangeRate": 2.3547
            },
            { 
                "year": "2015 (6월)", 
                "currentAssets": 3862,
                "cash": 1386,
                "accountsReceivable": 875,
                "inventory": 1455,
                "otherCurrentAssets": 146,
                "totalAssets": 26501,
                "currentLiabilities": 2086,
                "accountsPayable": 637,
                "shortTermDebt": 894,
                "otherCurrentLiabilities": 555,
                "longTermDebt": 8121,
                "otherLTLiabilities": 1730,
                "totalLiabilities": 11937,
                "totalEquity": 14563,
                "currentRatio": 1.85,
                "totalDebt": 9015,
                "debtToCapital": 38.2,
                "exchangeRate": 2.6913
            }
        ]

        # Fibria 운전자본 항목 데이터
        self.fibria_working_capital_data = [
            {
                "year": "2012",
                "accountsReceivable": 964,
                "inventory": 1183,
                "accountsPayable": 436,
                "netWorkingCapital": 1711
            },
            {
                "year": "2013",
                "accountsReceivable": 1477,
                "inventory": 1266,
                "accountsPayable": 587,
                "netWorkingCapital": 2156
            },
            {
                "year": "2014",
                "accountsReceivable": 695,
                "inventory": 1239,
                "accountsPayable": 593,
                "netWorkingCapital": 1341
            },
            {
                "year": "2015 (6월)",
                "accountsReceivable": 875,
                "inventory": 1455,
                "accountsPayable": 637,
                "netWorkingCapital": 1693
            }
        ]

        # Fibria SCF 영향 분석 데이터
        self.fibria_scf_analysis_data = [
            {
                "category": "SCF 이전",
                "daysOutstanding": 60,
                "arValue": 49.32,  # P&G 매출 3억 달러, 60일 회수
                "financingCost": 1.23,  # 2.5% 자금조달 비용
                "liquidityImpact": "Low"
            },
            {
                "category": "SCF 이후",
                "daysOutstanding": 15,
                "arValue": 12.33,  # P&G 매출 3억 달러, 15일 회수
                "financingCost": 0.04,  # 0.35% SCF 할인율
                "liquidityImpact": "High"
            }
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
            'pgFinancialData': self.pg_financial_data,
            'pgBalanceSheetData': self.pg_balance_sheet_data,
            'pgWorkingCapitalData': self.pg_working_capital_data,
            'pgExtendedWorkingCapitalData': self.pg_extended_working_capital_data,
            'fibriaFinancialData': self.fibria_financial_data,
            'fibriaSCFImpactData': self.fibria_scf_impact_data,
            'fibriaMarketData': self.fibria_market_data,
            'fibriaBalanceSheetData': self.fibria_balance_sheet_data,
            'fibriaWorkingCapitalData': self.fibria_working_capital_data,
            'fibriaSCFAnalysisData': self.fibria_scf_analysis_data
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
            'pg_financial': pd.DataFrame(self.pg_financial_data),
            'pg_balance_sheet': pd.DataFrame(self.pg_balance_sheet_data),
            'pg_working_capital': pd.DataFrame(self.pg_working_capital_data),
            'pg_extended_working_capital': pd.DataFrame(self.pg_extended_working_capital_data),
            'fibria_financial': pd.DataFrame(self.fibria_financial_data),
            'fibria_scf_impact': pd.DataFrame(self.fibria_scf_impact_data),
            'fibria_market': pd.DataFrame(self.fibria_market_data),
            'fibria_balance_sheet': pd.DataFrame(self.fibria_balance_sheet_data),
            'fibria_working_capital': pd.DataFrame(self.fibria_working_capital_data),
            'fibria_scf_analysis': pd.DataFrame(self.fibria_scf_analysis_data)
        }
