# Factorial

# 6! = 1 * 2 * 3 * 4 * 5 * 6


num = 5

fact_result = 0

for i in range(1, num + 1):
    fact_result *= 1 # 1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24, ...
    
print(fact_result)