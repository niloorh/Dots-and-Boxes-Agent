# Dots and Boxes AI

## Overview

This project implements an AI agent for the classic **Dots and Boxes** game.

The agent evaluates available moves, detects scoring opportunities, estimates risky moves, and selects moves using a heuristic adversarial decision strategy. A random agent is also included for comparison and testing.

## Project Description

### Game Representation

The board is represented as a grid of points, where each move adds an edge between two adjacent points.

The implementation keeps track of the current set of edges and determines which moves are still valid at each stage of the game.

### AI Agents

The project includes two agents:

- **Heuristic AI Agent**: evaluates candidate moves and prioritizes moves that can complete boxes while avoiding moves that may create favorable opportunities for the opponent.
- **Random Agent**: selects a valid move randomly and is used as a baseline opponent.

### Move Evaluation

The AI evaluates moves using two main ideas:

- **Immediate score**: detects whether a move completes one or more boxes.
- **Risk estimation**: considers whether a move leaves a box close to completion and may benefit the opponent on a later turn.

Moves are ranked according to this evaluation before the agent selects its action.

### Decision Strategy

The decision logic uses heuristic scoring and limited look-ahead structure to compare candidate moves.

The implementation prioritizes moves that maximize the agent's immediate advantage while reducing opportunities for the opponent.

### Simulation

The script includes a complete game simulation where the heuristic AI plays against the random agent.

During execution, it records:

- Selected moves
- Current board state
- Scores of both players
- Average decision time
- Maximum decision time

## Purpose

This project demonstrates core concepts in adversarial game-playing AI, including:

- State representation
- Legal move generation
- Heuristic evaluation
- Competitive decision-making
- Baseline comparison against a random agent
