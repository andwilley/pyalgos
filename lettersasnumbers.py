in1 = "12374"
in2 = "2"
in3 = "34"
in4 = "312745"

def get_number_of_encodings(input):
    MAX_VAL = 52
    if len(input) < 2:
        return len(input)

    # base cases, index 0, 1
    dp = [1, 2 if int(input[:2]) <= MAX_VAL else 1]

    for i, char in enumerate(input[2:], 2):
        dp_size = len(dp)
        two_digit = input[i - 1:i + 1] if i > 0 else MAX_VAL + 1
        both_are_valid = int(two_digit) <= MAX_VAL
        new_total = dp[dp_size - 1] + dp[dp_size - 2] if both_are_valid else dp[dp_size - 1]
        dp.append(new_total)
    return dp[-1]

print(get_number_of_encodings(in1))
