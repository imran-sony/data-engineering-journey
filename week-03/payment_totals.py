raw_sales = """  ord100045 ; 2026-10-07 ;  RAHIM  uddin ; Miniket Chal 5kg ; 2 ; ৳ 1,240.50 ; BKASH ; delivered
ORD100046;2026-10-07;nusrat akter;Soybean Oil 2L;  1  ;৳350.00;nagad;delivered
  ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED
ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled
ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00;Card;delivered
  ORD100050 ;2026-10-09;  mim   begum ; Alu 2kg ; 2 ; ৳ 138.50 ; BKASH ;delivered
ord100051 ; 2026-10-10 ; FAHIM ahmed ; Chaa Pata 400g ; 1 ; ৳ 232.25 ; Rocket ; returned
ORD100052;2026-10-10;jannat  islam;Doodh 1L;  6  ; ৳ 558.00 ;nagad;delivered
  ord100053 ; 2026-10-11 ;  Sabbir   Rahman ; Peyaj 1kg ; 3 ;৳ 219.75; CASH ON DELIVERY ; delivered
ORD100054 ; 2026-10-11 ; afsana  chowdhury ; Apel 1kg ; 2 ; ৳ 1,105.00 ; bKash ; delivered"""

with open("raw_sales.txt", "w", encoding="utf-8") as fh:
    fh.write(raw_sales)

print("✅ raw_sales.txt তৈরি হয়েছে")
print(f"    লাইন সংখ্যা: {len(raw_sales.splitlines())}")

with open("raw_sales.txt", encoding="utf-8") as fh:
    lines = fh.read().strip().split("\n")

bkash_total = 0.0
bkash_count = 0
nagad_total = 0.0
nagad_count = 0
card_total = 0.0
card_count = 0
rocket_total = 0.0
rocket_count = 0
cash_on_delivery_total = 0.0
cash_on_delivery_count = 0
total_amount = 0.0

for raw in lines:
    parts   = raw.split(";")
    amount  = float(parts[5].strip().replace("৳", "").replace(",", ""))
    payment = parts[6].strip().lower()
    status  = parts[7].strip().lower()

    if status == "cancelled":
        continue

    total_amount = total_amount + amount

    if payment == "bkash":
      bkash_total = bkash_total + amount
      bkash_count = bkash_count + 1

    elif payment == "nagad":
      nagad_total = nagad_total + amount
      nagad_count = nagad_count + 1

    elif payment == "card":
      card_total = card_total + amount
      card_count = card_count + 1

    elif payment == "rocket":
      rocket_total = rocket_total + amount
      rocket_count = rocket_count + 1

    elif payment == "cash on delivery":
      cash_on_delivery_total = cash_on_delivery_total + amount
      cash_on_delivery_count = cash_on_delivery_count + 1

print(f"bkash  {bkash_count}টা  ৳{bkash_total:.2f}")
print(f"nagad  {nagad_count}টা  ৳{nagad_total:.2f}")
print(f"card   {card_count}টা  ৳{card_total:.2f}")
print(f"rocket {rocket_count}টা  ৳{rocket_total:.2f}")
print(f"cash on delivery {cash_on_delivery_count}টা  ৳{cash_on_delivery_total:.2f}")
print(f"সব মিলিয়ে: ৳{total_amount:.2f}")

def clean_id(text):
    return text.strip().upper()

def clean_payment(text):
    return text.strip().lower()

def clean_status(text):
    return text.strip().lower()

def clean_amount(text):
    text = text.replace("৳", "").replace(",", "").strip()
    return float(text)

def taka(amount):
    return f"৳{amount:.2f}"

def read_lines(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.readlines()

def is_cancelled(status):
    return status.strip().lower() == "cancelled"

def main():
    lines = read_lines("raw_sales.txt")
    bkash_total = 0.0
    bkash_count = 0
    nagad_total = 0.0
    nagad_count = 0
    card_total = 0.0
    card_count = 0
    rocket_total = 0.0
    rocket_count = 0
    cash_on_delivery_total = 0.0
    cash_on_delivery_count = 0
    total_amount = 0.0

    for raw in lines:
        parts = raw.strip().split(";")
        amount = clean_amount(parts[5])
        payment = clean_payment(parts[6])
        status = clean_status(parts[7])

        if is_cancelled(status):
            continue

        total_amount = total_amount + amount

        if payment == "bkash":
            bkash_total = bkash_total + amount
            bkash_count = bkash_count + 1

        elif payment == "nagad":
            nagad_total = nagad_total + amount
            nagad_count = nagad_count + 1

        elif payment == "card":
            card_total = card_total + amount
            card_count = card_count + 1

        elif payment == "rocket":
            rocket_total = rocket_total + amount
            rocket_count = rocket_count + 1

        elif payment == "cash on delivery":
            cash_on_delivery_total = cash_on_delivery_total + amount
            cash_on_delivery_count = cash_on_delivery_count + 1

    print(f"bkash  {bkash_count}টা  {taka(bkash_total)}")
    print(f"nagad  {nagad_count}টা  {taka(nagad_total)}")
    print(f"card   {card_count}টা  {taka(card_total)}")
    print(f"rocket {rocket_count}টা  {taka(rocket_total)}")
    print(f"cash on delivery {cash_on_delivery_count}টা {taka(cash_on_delivery_total)}")
    print(f"সব মিলিয়ে: {taka(total_amount)}")

if __name__ == "__main__":
    main()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile my_tools.py
# 
# def clean_id(text):
#     return text.strip().upper()
# 
# def clean_payment(text):
#     return text.strip().lower()
# 
# def clean_status(text):
#     return text.strip().lower()
# 
# def clean_amount(text):
#     text = text.replace("৳", "").replace(",", "").strip()
#     return float(text)
# 
# def taka(amount):
#     return f"৳{amount:.2f}"
# 
# def read_lines(path):
#     with open(path, "r", encoding="utf-8") as fh:
#         return fh.readlines()
# 
# def is_cancelled(status):
#     return status.strip().lower() == "cancelled"
# 
# if __name__ == "__main__":
#     print(clean_id(" ord100045 "))
#     print(clean_payment(" BKASH "))
#     print(clean_status(" DELIVERED "))
#     print(clean_amount(" ৳ 1,240.50 "))
#     print(taka(1240.5))
#     print(is_cancelled("cancelled"))

import my_tools

def main():
    lines = my_tools.read_lines("raw_sales.txt")
    bkash_total = 0.0
    bkash_count = 0
    nagad_total = 0.0
    nagad_count = 0
    card_total = 0.0
    card_count = 0
    rocket_total = 0.0
    rocket_count = 0
    cash_on_delivery_total = 0.0
    cash_on_delivery_count = 0
    total_amount = 0.0

    for raw in lines:
        parts = raw.strip().split(";")
        amount = my_tools.clean_amount(parts[5])
        payment = my_tools.clean_payment(parts[6])
        status = my_tools.clean_status(parts[7])

        if my_tools.is_cancelled(status):
            continue

        total_amount = total_amount + amount

        if payment == "bkash":
            bkash_total = bkash_total + amount
            bkash_count = bkash_count + 1

        elif payment == "nagad":
            nagad_total = nagad_total + amount
            nagad_count = nagad_count + 1

        elif payment == "card":
            card_total = card_total + amount
            card_count = card_count + 1

        elif payment == "rocket":
            rocket_total = rocket_total + amount
            rocket_count = rocket_count + 1

        elif payment == "cash on delivery":
            cash_on_delivery_total = cash_on_delivery_total + amount
            cash_on_delivery_count = cash_on_delivery_count + 1

    print(f"bkash  {bkash_count}টা  {my_tools.taka(bkash_total)}")
    print(f"nagad  {nagad_count}টা  {my_tools.taka(nagad_total)}")
    print(f"card   {card_count}টা  {my_tools.taka(card_total)}")
    print(f"rocket {rocket_count}টা  {my_tools.taka(rocket_total)}")
    print(f"cash on delivery {cash_on_delivery_count}টা {my_tools.taka(cash_on_delivery_total)}")
    print(f"সব মিলিয়ে: {my_tools.taka(total_amount)}")

if __name__ == "__main__":
    main()

import importlib
importlib.reload(my_tools)