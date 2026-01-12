# The secret auction

another_bidder = 'yes';
bidders ={}
max_bidder =""
max_bid =0
while another_bidder == 'yes':
    bidder_name = input("What's your name? ")
    bid = input("What's your bid? ")

    bid_number = int(bid)
    bidders[bidder_name] = bid_number

    if bid_number > max_bid:
        max_bidder = bidder_name
        max_bid = bid_number


    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    print("\n"*100)



print(f"The winner is {max_bidder}, with a bid of {max_bid}.")
print(f"List of bidders and there bids")
for bidder in bidders:

    print(f"{bidder}: {bidders[bidder]}")


