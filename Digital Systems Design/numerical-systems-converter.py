from math import floor

def decimalToBinary1(n):
    pass

# Convert number from decimal system to binary system using method #2
# Divide the original number by 2 and save the remainder as the most significant bit
def decimalToBinary2(n):
    result = []
    while n != 0:
        r = n % 2
        n = floor(n / 2)
        result.append(f"{r}")
    result.reverse()
    return ''.join(result)