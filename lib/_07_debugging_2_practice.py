# Using the interactive debugger built into VSCode rather than gaining visibility with print statements

def factorial(n):
    product = 1

    # Debugging identified the problem as being that n is decremented before being multiplied by the product. Resulting in
    # the first multiplication being 1*4 instead of 1*5 and the final being product*0 instead of product*1
    # while n > 0:
    #     n -= 1
    #     product *= n
    while n > 0:
        product *= n
        n -= 1
    return product

print(factorial(5))
# Expected: 120 (the result of: 5 * 4 * 3 * 2 * 1)
# Actual: 24