import pandas as pd

import ClusterProcessor
import DataProcessor
from DistanceProcessor import get_distances, maximise_min_distance_game


concepts = DataProcessor.load_concepts_data()
ludemes = DataProcessor.load_ludemes_data()
agents = DataProcessor.load_agents_data()
agents_columns = agents.columns

game_names = concepts['GameName']
concepts = DataProcessor.scale_data(DataProcessor.bi_symmetric_log_transform(concepts.drop(columns=['GameName'])))
concepts['GameName'] = game_names

features = pd.merge(concepts, ludemes, on='GameName')
games = features['GameName']

features_agents = pd.merge(features, agents, on='GameName')
filtered_games = features_agents['GameName']
filtered_features = features_agents.drop(columns=agents_columns)


features = features.drop(columns=['GameName'])

features_normalised = DataProcessor.scale_data(features)

distance_matrix = get_distances(filtered_features, 'cosine')

_, _, _, selected_games = maximise_min_distance_game(distance_matrix, filtered_games, 30)


indices = [index for index, value in enumerate(games) if value in selected_games]

X3_tsne = ClusterProcessor.apply_3d_tsne(features_normalised)


optimal_k = ClusterProcessor.calculate_optimal_k(*ClusterProcessor.get_k_wcss(features_normalised, 10))
clusters = ClusterProcessor.get_clusters(features_normalised, optimal_k)
available_indices = [index for index, value in enumerate(games) if value in list(filtered_games)]



for index in available_indices:
        clusters[index] += 4

clusters[indices] = 8

ClusterProcessor.plot_3d_tsne(X3_tsne, games, clusters, color_map='Full', write=True)