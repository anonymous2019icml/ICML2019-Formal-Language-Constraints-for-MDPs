# Formal Language Constraints for Markov Decision Processes

# Source code of the Atari experiments

Use run_atari.py to run the training and testing jobs.

e.g.
python run_atari.py --task=train --env-name BreakoutDeterministic-v4 --contract dithering --arch contrac_dfa_state --train_seed 1 --enforce_contract True

# Experiemental Variables
---
# Models and Names used in the Result Files

Model Name (in Code and Result Files) | Model Description
--- | --- | --- | --- | ---
original | Without augmentation or negative reward shaping
contract | Without augmentation but with negative reward shaping
contract_action_history | State augmentation with constant action history and negative reward shaping
contract_dfa_state | State augmentation with One Hot Vector and negative reward shaping
contract_graph_emb | State augmentation with node2vec and negative reward shaping

---  
## Regular Expressions Used

Breakout: **'(23){2}'** and **'2{4}|3{4}'**  
Pong: **'((2|4)(3|5)){2}'** and **'((2|4){4}|(3|5){4})'**  
Space Invaders: **'((2|4)(3|5)){2}'** and **'((2|4){4}|(3|5){4})'**  

---
## Gamess Used
Breakout
Space Invaders
Seaquest

## Keras-RL
Keras-RL is a reinforcement learning library that we used in this project.
The 'src/rl' folder contrains this library with slight modification.
The original github repo is at: https://github.com/keras-rl/keras-rl
