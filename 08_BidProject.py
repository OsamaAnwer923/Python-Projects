logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
data = {}


def max_bid(data):
    for key in data:
        max = 0
        winner = ''
        bid_amount = data[key]
        if bid_amount>max:
            winner = key
            max=data[key]
    print(f"the winner is {winner} with a bid of {max}")
repeat = False
while repeat == False:
    name = input("what is your name?:")
    price = int(input("What's is your bid: $"))
    data[name]=price
    bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if bidders == 'no':
        max_bid(data)
        repeat = True
    else:
        repeat = False

