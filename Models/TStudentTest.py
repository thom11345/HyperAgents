import pandas as pd
from scipy import stats
experiment_results = pd.read_csv('data/experimentMatrix.csv')

agents = experiment_results.drop(columns=['Game Name', 'Iteration']).columns

games = experiment_results['Game Name'].drop_duplicates().tolist()

ttest = pd.DataFrame(index=agents, columns=agents)
for a1 in range(len(agents)):
    for a2 in range(a1, len(agents)):
        agent1 = agents[a1]
        agent2 = agents[a2]
        
        if a1 == a2:
            ttest.loc[agent1, agent2] = 'N/A'
        else:
            t_stat, p_value = stats.ttest_ind(experiment_results[agent1], experiment_results[agent2], equal_var=True)
            ttest.loc[agent1, agent2] = f"T: {t_stat:.3f}\nP: {p_value:.3f}"
            ttest.loc[agent2, agent1] = f"T: {-1*t_stat:.3f}\nP: {p_value:.3f}"
ttest.to_csv(f'analysis/ttest.csv')
