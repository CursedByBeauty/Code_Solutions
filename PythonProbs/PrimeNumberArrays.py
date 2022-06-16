def SortedPrimes(input_array):
    result = []
    current = 0
    for num in input_array:
        if num == 0 or num == 1:
            continue
        else:
            current = primeChecker(num)
            if current != None:
                result.append(current)
    result.sort()
    return result 

# HELPER FUNCTION TO CHECK INDIVIDUAL NUMBER IN SORTEDPRIMES
def primeChecker(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0: 
            is_prime = False 
    if is_prime == True:
        return number

def PrimeFactors(input_array):
    result = []
    current = []
    for num in input_array:
        current = factorChecker(num)
        if len(current) != 0:
            result.append(current)
    return result  # array of arrays
    # if a prime factor goes into a number more than once, it is only included once
    # [6, 8, 9] -> [[2, 3], [2], [3]]
    
# HELPER FUNCTION FOR PRIMEFACTORS TO CHECK NUMBERS INDIVIDUALLY
def factorChecker(number):
    factors = []
    for i in range(2, number + 1):
        if number % i == 0:
            count = 1
            for j in range(2, int(i/2 + 1)):
                if (i % j == 0):
                    count = 0
                    break
            if count == 1:
                factors.append(i)
    return factors
factorChecker(8)


input = [3,4,5,6,8,9]
result = SortedPrimes(input)
print(result)

result = PrimeFactors(input)
print(result)
