# Python compund interest calculator

# principle = int(input('Enter your principle: '))
# int_rate = int(input('Enter your interest rate: '))
# time = int(input('Enter your number of years: '))

# Amount = principle * (1 + int_rate/100)**time

# comp_int = Amount - principle

# print(f'Your final amount is ${Amount:.2f}')
# print(f'Your compound interest is ${comp_int:.2f}')

principle = 0 
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input('Enter the principle amount: '))
#     if principle <= 0:
#         print('Principle can\'t be less than or equal to zero')

# while rate <= 0:
#     rate = float(input('Enter the Interest rate: '))
#     if rate <= 0:
#         print('Interest rate can\'t be less than or equal to zero')
        
# while time <= 0:
#     time = int(input('Enter the time in yearst: '))
#     if time <= 0:
#         print('Time can\'t be less than or equal to zero')

while True:
    principle = float(input('Enter the principle amount: '))
    if principle <= 0:
        print('Principle can\'t be less than to zero')
    else:
        break
while True:
    rate = float(input('Enter the Interest rate: '))
    if rate <= 0:
        print('Interest rate can\'t be less than to zero')
    else:
        break 
while True:
    time = int(input('Enter the time in yearst: '))
    if time <= 0:
        print('Time can\'t be less than to zero')
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f'Balance after {time} year/s: ${total:.2f}')