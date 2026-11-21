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

if __name__ == "__main__":
    print(clean_id(" ord100045 "))
    print(clean_payment(" BKASH "))
    print(clean_status(" DELIVERED "))
    print(clean_amount(" ৳ 1,240.50 "))
    print(taka(1240.5))
    print(is_cancelled("cancelled"))