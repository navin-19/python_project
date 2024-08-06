import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol = "!@#$%^&*()_+-[]"
number = "1234567890"
all = lower + upper + symbol + number
length = 8
password = "".join(random.sample(all,length))
print(f"password is created : {password}")
