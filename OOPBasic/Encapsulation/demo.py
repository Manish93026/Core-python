def check_status(a, b, flag):
    # Condition 1: Exactly one of a or b is non-negative AND flag is False
    if ((a >= 0) ^ (b >= 0)) and not flag:
        return True
    
    # Condition 2: Both a and b are negative AND flag is True
    if (a < 0 and b < 0) and flag:
        return True

    return False


# -------- User Input --------
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
flag_input = input("Enter flag (True/False): ")

# Convert user input to boolean
flag = flag_input.lower() == "true"

# -------- Output --------
result = check_status(a, b, flag)
print("Output:", result)







# class Solution:
#     def CheckStatus(self, a, b, flag):
#         a = int(input("Enter the first number: "))
#         b = int(input("Enter the second number: "))
        
#         if a > 0 or b > 0:
#             print("a =", a, "b =", b, flag)
#         elif a < 0 or b < 0:
#             print("a =", a, "b =", b, flag)
#         else:
#             print("a =", a, "b =", b, flag)


# sol = Solution()
# sol.CheckStatus(0, 0, )  # Call the function to trigger inputs
