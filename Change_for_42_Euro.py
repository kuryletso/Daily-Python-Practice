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


#Faster (Still not fast enough)
def changes_1(amount, coins):
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



# With memoization, slow
from copy import deepcopy

def changes(amount, coins):
    amount = (amount,)
    coins = sorted(coins, reverse=True)
    cache: dict[int, dict[str, list[int] | set[tuple[int]]]] = {coins[-1] : {"complete": [1] * len(coins), "vars": {(coins[-1],)}}}
    cache_template: dict = {"complete": [0] * len(coins), "vars": set()}
        

    def var_gen_5(memo: tuple = amount, coin_index: int = 0, branch: tuple = tuple()) -> None:
        rem: int = memo[-1]
        
        if rem not in cache:
            # 1 Create rem in cache with empty vars
            cache.update({rem: deepcopy(cache_template)})

        if rem in cache and all(cache[rem].get("complete", 0)):
            # 2.1 Create branches for each variant of rem in cache
            # 2.2 Update cache numbers with new branches

            for m in range(len(memo)-1):
                new_branches: set = set(map(lambda x: tuple(sorted(branch[m:] + x, reverse=True)), cache[rem]["vars"]))
                cache[memo[m]]["vars"] |= new_branches

        elif coin_index == len(coins) - 1:
            # 3.1 Finish branch by adding (rem // coin[-1]) amount of coin[-1]
            # 3.2 Update cache numbers with new branch

            if not rem % coins[-1]:
                new_branch: tuple = branch + (coins[-1],) * (rem // coins[-1])
                for m in range(len(memo)):
                    cache[memo[m]]["vars"].add(new_branch[m:])
        else:
            # 4.1 Substract each coin from rem, starting from coin_index' coin
            # 4.2 Mark this coin for rem in cache as completed
            # 4.3 IF dif < 0 : cancel this branch
            # 4.4 IF dif = 0 : finish this branch; Update numbers in cache, adding branch
            # 4.5 IF dif > 0 : add coin to branch; add dif to memo; run var_gen on rem  
            for c in range(coin_index, len(coins)):
                cache[rem]["complete"][c] = 1
                dif: int = rem - coins[c]
            
                if dif < 0:
                    continue
                elif dif == 0:
                    new_branch: tuple = branch + (coins[c],)
                    for m in range(len(memo)):
                        cache[memo[m]]["vars"].add(new_branch[m:])
                else:
                    new_branch: tuple = branch + (coins[c],)
                    new_memo: tuple = memo + (dif,)
                    var_gen_5(new_memo, c, new_branch)
        
    var_gen_5(amount)
    return len(cache[amount[0]]["vars"])



if __name__ == "__main__":
    coins = (1, 2, 5, 10, 20, 50, 100, 200, 500)
    amount = 200
    print(changes(amount, coins))