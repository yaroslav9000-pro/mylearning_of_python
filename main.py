print('welcome to tip calculator!!!')
bill = input('How much is your bill?\n')
people_num = int(input('Between how many people you would like to share the bill.\n'))
tip = int(input('What percentage tip you would like to give, 10/12/15?\n')) / 100
total_sum = float(bill) * (1 + tip)
each_person_pay = round(total_sum / people_num)
print('Each person should pay: {}'.format(each_person_pay))