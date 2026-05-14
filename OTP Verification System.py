import random
m = 2

otp = random.randint(100000,999999)
print("Your OTP is: ",otp)

for i in range(3):
    n = int(input("Enter your OTP: "))
    if n == otp:
        print(" ✅ OTP verified successfully")
    else:
        print("❌ Invalid OTP.",m ,"chances left")
        m = m - 1