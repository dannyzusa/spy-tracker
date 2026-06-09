import yfinance as yf
from datetime import datetime

def fetch_live_market_data():
    try:
        spy = yf.Ticker("SPY")
        hist = spy.history(period="5d")
        if hist.empty:
            return
            
        current_spy_price = round(spy.fast_info['lastPrice'], 2)
        session_high = round(hist['High'].iloc[-1], 2)
        session_low = round(hist['Low'].iloc[-1], 2)
        
    except Exception as e:
        print(f"// Pipeline Error: {str(e)}")
        return

    # Institutional Level Modeling Math
    gamma_flip   = round(current_spy_price, 2)
    put_wall     = round(current_spy_price * 0.993, 2)
    call_wall    = round(current_spy_price * 1.015, 2)
    macro_peak   = 760.40  
    fib_236      = round(macro_peak - ((macro_peak - session_low) * 0.236), 2)
    fib_382      = round(macro_peak - ((macro_peak - session_low) * 0.382), 2)
    hvn_support  = round(put_wall - 2.00, 2)
    macro_poc    = round(put_wall - 15.00, 2)
    system_floor = round(put_wall * 0.952, 2)
    gap_ceiling  = round(session_high + 3.66, 2)

    # OUTPUT: Pure Pine Script Variables for Instant Copy-Paste
    print("\n" + "// " + "="*50)
    print(f"// COPY FROM HERE DOWN AND PASTE INTO TRADINGVIEW | {datetime.now().strftime('%Y-%m-%d')}")
    print("// " + "="*50)
    print(f'gammaFlip   = {gamma_flip}')
    print(f'putWall     = {put_wall}')
    print(f'callWall    = {call_wall}')
    print(f'sessionHigh = {session_high}')
    print(f'fib382      = {fib_382}')
    print(f'fib236      = {fib_236}')
    print(f'gapCeiling  = {gap_ceiling}')
    print(f'hvnSupport  = {hvn_support}')
    print(f'macroPOC    = {macro_poc}')
    print(f'systemFloor = {system_floor}')
    print("// " + "="*50 + "\n")

if __name__ == "__main__":
    fetch_live_market_data()
