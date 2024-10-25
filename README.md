# Ludii Hyper Agents

## Overview

### Ludii AI

AI directory contains the Ludii Hyper-agents, created as an Eclipse project

Create PMML model files for the Ludii Hyper-agents by running CreatePMMLs.py in the Models folder

main/LaunchLudii.java launches the Ludii UI

### Python Models and Analysis

Models directory contains code for training evaluating and exporting the portfolio models

## Requirements

### Python

### AI

Java project in the AI folder, developed in eclipse.
Portfolio
Ensemble

### Ludii

Built with Ludii version 1.3.12

#### Modifications to the Ludii source code

AI/src/search/minimax/AlphaBetaSearch.java

- Add provedWin() getter

Core/src/other/trial/Trial.java

- Set null endData, RNGStats to new ArrayList in the copy constructor : Trial(Trial) -> was breaking MCTS in the ensemble

Player/src/app/views/players/PlayerViewUser.java

- Add drawEnsembleFace() for ensemble agent in the UI
