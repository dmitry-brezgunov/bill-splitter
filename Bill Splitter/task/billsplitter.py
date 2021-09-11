import random


def bill_splitter(x):
    if x < 1:
        return 'No one is joining for the party'

    print('Enter the name of every friend (including you), each on a new line:')
    friends = []
    for _ in range(x):
        friend = input()
        friends.append(friend)

    print('Enter the total bill value:')
    total_bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()

    if lucky == 'Yes':
        lucky_one = random.choice(friends)
        print(f'{lucky_one} is the lucky one!')
        split_bill = total_bill / (x - 1)
        bill = dict.fromkeys(friends, round(split_bill, 2))
        bill[lucky_one] = 0
    else:
        print('No one is going to be lucky')
        split_bill = total_bill / x
        bill = dict.fromkeys(friends, round(split_bill, 2))

    return bill


print('Enter the number of friends joining (including you):')
n = int(input())
print(bill_splitter(n))
