from enum import Enum

class DatasetCategory(str, Enum):
    BREADTH     = "breadth"
    COMMODITIES = "commodities"
    CURRENCY    = "currency"
    FLOW        = "flow"
    GLOBAL      = "global"
    INDICES     = "indices"
    MACRO       = "macro"
    OPTIONS     = "options"
    VOLATILITY  = "volatility"
