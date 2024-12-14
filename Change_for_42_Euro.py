# Excercise: https://www.hackinscience.org/exercises/change-for-42
#
#
# Solution:


class Branch:
    def __init__(self, coins: dict = {}) -> None:
        self.coins = coins.copy()

    def update(self, coin: int) -> None:
        if coin in self.coins:
            self.coins[coin] += 1
        else:
            self.coins[coin] = 1

# Slow
def var_gen(amount: int, index: int = 0, branch: tuple = tuple()) -> None: # populates vars with tuples, requires set() to remove duplicates
    for i in range(index, len(coins)):
        mod = amount - coins[i]
        # print(f"From {amount}, substracting {coins[i]}. Mod is {mod}. Current branch is {branch}")
        if mod < 0:
            continue
        elif mod == 0:
            new_branch = branch + (coins[i],)
            vars.append(tuple(sorted(new_branch)))
            # print(f"Adding branch {new_branch}")
        else:
            new_branch = branch + (coins[i],)
            var_gen(mod, i, new_branch)

# Slowest
def var_gen_2(amount: int, index: int = 0, branch: Branch = Branch()) -> None: # populates vars with dictionaries, requires Branch class
    for i in range(index, len(coins)):
        mod = amount - coins[i]
        print(f"From {amount}, subtracting {coins[i]}. Mod is {mod}. Current branch is {branch.coins}")
        if mod < 0:
            continue
        elif mod == 0:
            new_branch = Branch(branch.coins)
            new_branch.update(coins[i])
            print(f"Adding branch {new_branch.coins}")
            vars.append(new_branch.coins)
        else:
            new_branch = Branch(branch.coins)
            new_branch.update(coins[i])
            var_gen_2(mod, i, new_branch)


# Slow
def var_gen_3(amount: int, index: int = 0, branch: dict = {}) -> None: # populates vars with dictionaries
    for i in range(index, len(coins)):
        dif = amount - coins[i]
        if dif < 0:
            continue
        elif dif == 0:
            new_branch = branch.copy()
            if coins[i] in new_branch: new_branch[coins[i]] += 1
            else: new_branch[coins[i]] = 1
            vars.append(new_branch)
        else:
            new_branch = branch.copy()
            if coins[i] in new_branch: new_branch[coins[i]] += 1
            else: new_branch[coins[i]] = 1
            var_gen_3(dif, i, new_branch)


#Fastest (Still not fast enough)
def changes(amount, coins):
    coins = sorted(coins, reverse=True)
    vars = []

    def var_gen_3_2(amount: int, index: int = 0, branch: dict = {}) -> None: # populates vars with dictionaries
        for i in range(index, len(coins)):

            if index == len(coins) - 1:
                new_branch = branch.copy()
                if coins[i] in new_branch: new_branch[coins[i]] += amount
                else: new_branch[coins[i]] = amount
                # print(f"Last index: adding {new_branch}")
                vars.append(new_branch)
                break

            dif = amount - coins[i]
            # print(f"{amount} - {coins[i]} = {dif}. Index {i}. Branch {branch}")
            
            if dif < 0:
                continue
            elif dif == 0:
                new_branch = branch.copy()
                if coins[i] in new_branch: new_branch[coins[i]] += 1
                else: new_branch[coins[i]] = 1
                # print(f"Adding {new_branch}")
                vars.append(new_branch)
            else:
                new_branch = branch.copy()
                if coins[i] in new_branch: new_branch[coins[i]] += 1
                else: new_branch[coins[i]] = 1
                var_gen_3_2(dif, i, new_branch)
    
    
    var_gen_3_2(amount)
    # print(vars)
    return len(vars)



if __name__ == "__main__":
    coins = (1, 2, 5, 10, 20, 50, 100, 200, 500)
    amount = 200
    print(changes(amount, coins))