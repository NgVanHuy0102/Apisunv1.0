from random import randint, choice
import time

# Phiên bắt đầu từ số nào đó (ví dụ: 2724477)
start_phien = 2724477
start_time = time.time()

history = []

def get_current_phien():
    elapsed = int((time.time() - start_time) // 60)
    return start_phien + elapsed

def roll_dice():
    return [randint(1, 6) for _ in range(3)]

def du_doan(history):
    if len(history) >= 3 and history[-3:] == ["t", "t", "t"]:
        return "xỉu", "Cầu 3 tài → đoán xỉu"
    elif len(history) >= 2 and history[-2:] == ["x", "x"]:
        return "tài", "Cầu 2 xỉu → đoán tài"
    else:
        return choice(["tài", "xỉu"]), "Random do không có cầu"

def get_taixiu():
    phien = get_current_phien()
    dice = roll_dice()
    total = sum(dice)
    ketqua = "tài" if total >= 11 else "xỉu"
    
    history.append("t" if ketqua == "tài" else "x")
    if len(history) > 20:
        history.pop(0)

    du_doan_result, ly_do = du_doan(history)

    return {
        "phien": phien,
        "dice": dice,
        "ketqua": ketqua,
        "du_doan": du_doan_result,
        "ly_do": ly_do,
        "history": history[-10:],
        "cre": "ngvanhuy"
    }

# In kết quả ra màn hình
print(get_taixiu())