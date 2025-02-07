def solve(numheads, numlegs):
    ch = (4 * numheads - numlegs) / 2
    rb = numheads - ch
    print(f"number of chickens: {ch}")
    print(f"number of rabbits: {rb}")
heads = int(input())
legs = int(input())
solve(heads, legs)