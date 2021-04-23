# NOTES

## Elements of the Algorithmic Trading System
 
 1. STRATEGY ENGINE
    It is contains the main trading concept

 2. BRIDGE
    It is connect the trading engine and the broker interface and
    load all data to the database

 3. DATA ENGINE
    It is store the trading data
    
 4. ANALYIZER ENGINE
    It is analyizing the trading data
     /* Risk, Drawdown, Drawdown peridos, Volatility === SHARPE RATIO */

 5. VISUAL INTERFACE
    It can represent the process of the trading, the market and the system status


## Mistakes of the algo trading system

1. OVERFITTING
    Fit to much on the historical data during the backtesting,

2. WALKFORWARD TESTING
    Instead of backtesting which is based on relativley small amount of histrorical data
    I should use walkforward testing (paper testing) which is far more reliable and true.

3. TOO BIG TOO EARLY
    I should start with real money after a good amount of testing paper testing and it must be start with 
    very low risk.

4. NOT TRUSTING IN THE ALGORITHM
    If it start it must be run without hesitation because in order to create relaible amoutn of trade to be analized it must be untouched by the human ego.
