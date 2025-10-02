# They are called lambda or anonymous funcs
# They dont need a name nor a retrun key word but they have to be pre-fixed with lambda key word.

# replicating the best scores example

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

best_scores = filter(lambda score: score < 40, scores)
print(list(best_scores))