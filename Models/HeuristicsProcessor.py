
import DataProcessor

heuristics = DataProcessor.load_heuristics_data()

heuristic_names = heuristics.drop(columns=['GameName']).columns

results = {}
for name in heuristic_names:
    results[name] = 0


total = 0
for index, row in heuristics.iterrows():
    total += 1
    for name in heuristic_names:
        if row[name] == row['NullHeuristicPos']:
            results[name] += 1


print(results, total)