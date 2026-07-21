from market_regime_intelligence.domain.dataset  import Dataset
from market_regime_intelligence.domain.enums    import DatasetCategory
from market_regime_intelligence.domain.registry import DatasetRegistry
from market_regime_intelligence.domain.dataset import Dataset
from market_regime_intelligence.domain.enums import DatasetCategory

datasets = DatasetRegistry(
    [
        # ==========================================================
        # INDIAN INDICES
        # ==========================================================
        Dataset(
            category=DatasetCategory.INDICES,
            name="nifty",
            symbol="^NSEI",
            description="NIFTY 50 Index",
        ),
        Dataset(
            category=DatasetCategory.INDICES,
            name="banknifty",
            symbol="^NSEBANK",
            description="NIFTY Bank Index",
        ),
        Dataset(
            category=DatasetCategory.INDICES,
            name="sensex",
            symbol="^BSESN",
            description="BSE Sensex",
        ),
        Dataset(
            category=DatasetCategory.INDICES,
            name="midcap100",
            symbol="NIFTY_MIDCAP_100.NS",
            description="NIFTY Midcap 100",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.INDICES,
            name="smallcap100",
            symbol="^CNXSC",
            description="NIFTY Smallcap 100",
            provider="nse",
        ),

        # ==========================================================
        # VOLATILITY
        # ==========================================================

        Dataset(
            category=DatasetCategory.VOLATILITY,
            name="indiavix",
            symbol="^INDIAVIX",
            description="India VIX",
        ),
        Dataset(
            category=DatasetCategory.VOLATILITY,
            name="vix",
            symbol="^VIX",
            description="CBOE Volatility Index",
        ),
        # ==========================================================
        # GLOBAL INDICES
        # ==========================================================
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="sp500",
            symbol="^GSPC",
            description="S&P 500",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="nasdaq",
            symbol="^IXIC",
            description="NASDAQ Composite",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="dowjones",
            symbol="^DJI",
            description="Dow Jones Industrial Average",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="nikkei225",
            symbol="^N225",
            description="Nikkei 225",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="hangseng",
            symbol="^HSI",
            description="Hang Seng Index",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="shanghai",
            symbol="000001.SS",
            description="Shanghai Composite",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="ftse100",
            symbol="^FTSE",
            description="FTSE 100",
        ),
        Dataset(
            category=DatasetCategory.GLOBAL,
            name="dax",
            symbol="^GDAXI",
            description="German DAX",
        ),

        # ==========================================================
        # COMMODITIES
        # ==========================================================

        Dataset(
            category=DatasetCategory.COMMODITIES,
            name="gold",
            symbol="GC=F",
            description="Gold Futures",
        ),
        Dataset(
            category=DatasetCategory.COMMODITIES,
            name="silver",
            symbol="SI=F",
            description="Silver Futures",
        ),
        Dataset(
            category=DatasetCategory.COMMODITIES,
            name="brent",
            symbol="BZ=F",
            description="Brent Crude Oil",
        ),
        Dataset(
            category=DatasetCategory.COMMODITIES,
            name="wti",
            symbol="CL=F",
            description="WTI Crude Oil",
        ),
        Dataset(
            category=DatasetCategory.COMMODITIES,
            name="naturalgas",
            symbol="NG=F",
            description="Natural Gas Futures",
        ),

        # ==========================================================
        # CURRENCY
        # ==========================================================

        Dataset(
            category=DatasetCategory.CURRENCY,
            name="usdinr",
            symbol="INR=X",
            description="USD/INR Exchange Rate",
        ),
        Dataset(
            category=DatasetCategory.CURRENCY,
            name="dxy",
            symbol="DX-Y.NYB",
            description="US Dollar Index",
        ),
        Dataset(
            category=DatasetCategory.CURRENCY,
            name="eurusd",
            symbol="EURUSD=X",
            description="EUR/USD Exchange Rate",
        ),
        Dataset(
            category=DatasetCategory.CURRENCY,
            name="usdjpy",
            symbol="JPY=X",
            description="USD/JPY Exchange Rate",
        ),

        # ==========================================================
        # BONDS
        # ==========================================================

        Dataset(
            category=DatasetCategory.MACRO,
            name="us10y",
            symbol="^TNX",
            description="US 10-Year Treasury Yield",
        ),
        Dataset(
            category=DatasetCategory.MACRO,
            name="us3month",
            symbol="^IRX",
            description="US 3-Month Treasury Bill",
        ),
        Dataset(
            category=DatasetCategory.MACRO,
            name="india10y",
            symbol="INDIA_10Y",
            description="India 10-Year Government Bond",
            provider="rbi",
        ),

        # ==========================================================
        # OPTIONS
        # ==========================================================

        Dataset(
            category=DatasetCategory.OPTIONS,
            name="pcr",
            symbol="PCR",
            description="Put Call Ratio",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.OPTIONS,
            name="maxpain",
            symbol="MAXPAIN",
            description="Maximum Pain",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.OPTIONS,
            name="atm_iv",
            symbol="ATM_IV",
            description="ATM Implied Volatility",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.OPTIONS,
            name="call_oi",
            symbol="CALL_OI",
            description="Call Open Interest",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.OPTIONS,
            name="put_oi",
            symbol="PUT_OI",
            description="Put Open Interest",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.OPTIONS,
            name="oi_change",
            symbol="OI_CHANGE",
            description="Open Interest Change",
            provider="nse",
        ),

        # ==========================================================
        # FII / DII FLOWS
        # ==========================================================

        Dataset(
            category=DatasetCategory.FLOW,
            name="fii_cash",
            symbol="FII_CASH",
            description="FII Cash Market Activity",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.FLOW,
            name="dii_cash",
            symbol="DII_CASH",
            description="DII Cash Market Activity",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.FLOW,
            name="fii_futures",
            symbol="FII_FUTURES",
            description="FII Index Futures Position",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.FLOW,
            name="fii_options",
            symbol="FII_OPTIONS",
            description="FII Index Options Position",
            provider="nse",
        ),
        # ==========================================================
        # MARKET BREADTH
        # ==========================================================
        Dataset(
            category=DatasetCategory.BREADTH,
            name="advance_decline",
            symbol="ADV_DEC",
            description="Advance Decline Ratio",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.BREADTH,
            name="above50dma",
            symbol="ABOVE50DMA",
            description="Stocks Above 50 DMA",
            provider="nse",
        ),
        Dataset(
            category=DatasetCategory.BREADTH,
            name="above200dma",
            symbol="ABOVE200DMA",
            description="Stocks Above 200 DMA",
            provider="nse",
        ),
    ]
)