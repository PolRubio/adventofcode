# data = ["1abc2",
# "pqr3stu8vwx",
# "a1b2c3d4e5f",
# "treb7uchet"]

data = open("day-1/data-day1.txt", "r").readlines()

calibration_values = []

# Solution 1
for line in data:
    calibration_value = ''
    for char in line:
        if char.isnumeric():
            calibration_value += char
            break
    
    for char in line[::-1]:
        if char.isnumeric():
            calibration_value += char
            break
    
    calibration_values.append(int(calibration_value))

print("Solution 1: ", sum(calibration_values))

# Solution 2
