from chain import Chain

chain = Chain(20)

for i in range(5):
    # data = input("Add something to the chain: ")
    chain.add_to_pool(str(i))
    chain.mine()
