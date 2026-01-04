# Who will pay the bill?
import random

friends =["Alice", "Bob", "Charlie", "David", "Emanuel"]

index = random.randint(0, len(friends)-1)
print(f"the bill will be paid by {friends[index]}.")

# it can also be done using random.choice
print(f"the bill will be paid by {random.choice(friends)}.")