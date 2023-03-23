from enum import Enum

'''
https://developer.tdameritrade.com/content/place-order-samples
'''


class session(str,Enum):
    NORMAL='NORMAL'
    AM='AM'
    PM='PM'
    SEAMLESS='SEAMLESS'

class duration(str,Enum):
    DAY='DAY'
    GOOD_TILL_CANCEL='GOOD_TILL_CANCEL'
    FILL_OR_KILL='FILL_OR_KILL'

class orderType(str,Enum):
    MARKET='MARKET'
    LIMIT='LIMIT'
    STOP='STOP'
    STOP_LIMIT='STOP_LIMIT'
    TRAILING_STOP='TRAILING_STOP'
    MARKET_ON_CLOSE='MARKET_ON_CLOSE'
    EXERCISE='EXERCISE'
    TRAILING_STOP_LIMIT='TRAILING_STOP_LIMIT'
    NET_DEBIT='NET_DEBIT'
    NET_CREDIT='NET_CREDIT'
    NET_ZERO='NET_ZERO'


class complexOrderStrategyType(str,Enum): 
    NONE='NONE'
    COVERED='COVERED'
    VERTICAL='VERTICAL'
    BACK_RATIO='BACK_RATIO'
    CALENDAR='CALENDAR'
    DIAGONAL='DIAGONAL'
    STRADDLE='STRADDLE'
    STRANGLE='STRANGLE'
    COLLAR_SYNTHETIC='COLLAR_SYNTHETIC'
    BUTTERFLY='BUTTERFLY'
    CONDOR='CONDOR'
    IRON_CONDOR='IRON_CONDOR'
    VERTICAL_ROLL='VERTICAL_ROLL'
    COLLAR_WITH_STOCK='COLLAR_WITH_STOCK'
    DOUBLE_DIAGONAL='DOUBLE_DIAGONAL'
    UNBALANCED_BUTTERFLY='UNBALANCED_BUTTERFLY'
    UNBALANCED_CONDOR='UNBALANCED_CONDOR'
    UNBALANCED_IRON_CONDOR='UNBALANCED_IRON_CONDOR'
    UNBALANCED_VERTICAL_ROLL='UNBALANCED_VERTICAL_ROLL'
    CUSTOM='CUSTOM'


class orderStrategyType(str,Enum):
    SINGLE='SINGLE'
    OCO='OCO'
    TRIGGER='TRIGGER'


class specialInstruction(str,Enum):
    ALL_OR_NONE='ALL_OR_NONE'
    DO_NOT_REDUCE='DO_NOT_REDUCE'
    ALL_OR_NONE_DO_NOT_REDUCE='ALL_OR_NONE_DO_NOT_REDUCE'
