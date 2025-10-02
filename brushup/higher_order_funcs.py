# Regular funcs

def attack(character, x ):
    return f"The attack move from {character} is {x}"


def defender(character, x ):
    return f"The defence move from {character} is {x}"

# Higher order function
def ninja_moves(character, x ):
    return character("Jon bah", 5)


action_1 = ninja_moves(defender, 10)
print(action_1)

moves = ["kick", "jump", "punch"]

# Built-in higher order func

# -map(higher order func)

def make_move_powerfull(move ):
    return f"{move.upper()} !!!"

powerful_moves = map(make_move_powerfull, moves)
print(list(powerful_moves))

# Another built_in high order funcs

scores = [20, 30, 40, 50, 60, 70, 80, 90, 100]

def best_score_selector(score):
    return score > 50


best_scores = filter(best_score_selector, scores)
print(list(best_scores))

