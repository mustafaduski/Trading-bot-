import ccxt
import time

def analyze_market():
    print("🚀 Quantum Bot Engine Initialized...")
    
    # پەیوەندی بە باینانس
    exchange = ccxt.binance()
    
    symbols = ['BTC/USDT', 'ETH/USDT']
    
    print("-" * 30)
    for symbol in symbols:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']
            change = ticker['percentage']
            
            print(f"📊 Asset: {symbol}")
            print(f"💰 Current Price: ${price}")
            print(f"📈 24h Change: {change}%")
            
            # لۆژیکی سادەی کڕین و فرۆشتن (لێرەدا دەتوانیت ئالگۆریتمی تر دابنێیت)
            if change < -5:
                print(f"⚠️ SIGNAL: Oversold detected on {symbol}. Potential BUY.")
            elif change > 5:
                print(f"⚠️ SIGNAL: Resistance reached on {symbol}. Potential SELL.")
            else:
                print(f"✅ SIGNAL: Market is stable. Monitoring...")
            print("-" * 30)
            
        except Exception as e:
            print(f"❌ Error fetching {symbol}: {e}")

if __name__ == "__main__":
    # ئەمە یەکجار شیکردنەوە دەکات و دەوەستێت (بۆ ئەوەی گیتھەب ئەکشن ئیشی پێ بکات)
    analyze_market()
