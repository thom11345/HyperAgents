# Ludii Hyper Agents

## Overview

## Requirements

### Java

### Python

### JPY

### Ludii

Built with Ludii version 1.3.12

#### Modifications to the Ludii source code

AI/src/search/minimax/AlphaBetaSearch.java

- Add provedWin() getter

AI/src/search/minimax/BRSPlus.java

- Add heuristic constructor BRSPlus(Heuristics)
- Add provedWin property
- Set provedWin to true when finding a proved win
- Add provedWin() getter

Core/src/other/trial/Trial.java

- Set null endData, RNGStats to new ArrayList in the copy constructor : Trial(Trial) -> was breaking MCTS in the ensemble

Player/src/app/views/players/PlayerViewUser.java

- Add drawEnsembleFace() for ensemble agent in the UI
