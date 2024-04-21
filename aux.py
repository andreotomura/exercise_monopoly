
def impulsive(balance, price, rent): 
    return True

def demanding(balance, price, rent):
    if rent > 50:
        return True
    else:
        return False

def cautious(balance, price, rent):
    if balance - price >= 80:
        return True
    else:
        return False

def rand(balance, price, rent):
    probability = random.random()
    if probability >= 0.5:
        return True
    else:
        return False

def create_players():
    players = {
        impulsive: {
            "position": 0,
            "balance": 300,
            "order": 0,
            "turn": 0
        },
        demanding: {
            "position": 0,
            "balance": 300,
            "order": 0,
            "turn": 0
        },
        cautious: {
            "position": 0,
            "balance": 300,
            "turn": 0
        },
        rand: {
            "position": 0,
            "balance": 300,
            "turn": 0
        },
    }
    return players



# def check_balances(players): # redo!
#     balances = []

#     player_1_balance = players["player_1"]["balance"]
#     player_2_balance = players["player_2"]["balance"]
#     player_3_balance = players["player_3"]["balance"]
#     player_4_balance = players["player_4"]["balance"]

#     balances.append(player_1_balance)
#     balances.append(player_2_balance)
#     balances.append(player_3_balance)
#     balances.append(player_4_balance)

#     max_balance = max(balances)
#     max_balance_player = balances.index(max_balance)

#     print(max_balance_player)

#     # for first_level_key in players.keys():
#     #     print(first_level_key)
#     #     for second_level_key in players[first_level_key]:
#     #         print(second_level_key["balance"])

#     return max(balances)
