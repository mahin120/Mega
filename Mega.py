import time
import random
from datetime import datetime, timedelta

# বাংলাদেশ সময় হিসাব করার ফাংশন
def get_bangladesh_time():
    return datetime.utcnow() + timedelta(hours=6)

# Mega Wheel এর সম্ভাব্য নম্বর লিস্ট
possible_numbers = [1, 2, 5, 8, 10, 15, 20, 30, 40]

# ANSI রঙের কোড (লাল)
RED = '\u001B[91m'
RESET = '\u001B[0m'

# ২৪ ঘন্টার সিগনাল সংরক্ষণ
signals_24h = []

# সিগনাল জেনারেটিং ফাংশন (এখানে ডেমো হিসেবে র‍্যান্ডম)
def generate_signal():
    return random.choice(possible_numbers)

# সিগনালগুলো নতুন যুক্ত করার ফাংশন
def add_signal():
    now = get_bangladesh_time()
    signal_time = now + timedelta(seconds=10)  # ১০ সেকেন্ড আগে বলা হবে অর্থাৎ ভবিষ্যতের সময় দেখানো হবে
    signal_number = generate_signal()
    signals_24h.append((signal_time, signal_number))
    # ২৪ ঘন্টা আগের সিগনাল ডিলিট করা
    cutoff = now - timedelta(hours=24)
    while signals_24h and signals_24h[0][0] < cutoff:
        signals_24h.pop(0)

# সিগনাল প্রিন্ট করার ফাংশন
def display_signals():
    now = get_bangladesh_time()
    print(f"বাংলাদেশ সময়: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("১xBet Mega Wheel সিগনাল (১০ সেকেন্ড আগে বলা হয়):")
    print("-" * 40)
    for s_time, number in signals_24h:
        # যদি সময় এখন থেকে কমপক্ষে ১০ সেকেন্ড পরে হয় (আস্তে আস্তে বলবে)
        if s_time > now:
            time_str = s_time.strftime('%H:%M:%S')
            print(f"সময়: {time_str} | আসতে পারে নম্বর: {RED}{number}{RESET}")
    print("-" * 40)

def main():
    print("Mega Wheel সিগনাল স্ক্রিপ্ট বাংলাদেশ সময় অনুযায়ী চলছে...")
    try:
        while True:
            add_signal()
            display_signals()
            time.sleep(10)  # প্রতি ১০ সেকেন্ড আপডেট
            print("
" * 2)
    except KeyboardInterrupt:
        print("স্ক্রিপ্ট বন্ধ করা হলো।")

if __name__ == "__main__":
    main()
