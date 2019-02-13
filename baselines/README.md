# Formal Language Constraints for Markov Decision Processes (OpenAI Baselines fork)
d
This folder is a fork of the [OpenAI Baselines]() library. Most modifications are in a new folder called `constraints`, though changes were made to the code in `deepq` in order to fit constraints into the code used for DQN and in `run.py` and `common/cmd_util.py` in order to make constraints specifiable from the command line.

Experiments using constraints can be run with commands similar to 
```
python run.py --env Reacher-v2 --augmentation constraint_state --constraints reacher_actuation_counting --rewards -1
```

or

```
python run.py --env HalfCheetah-v2 --augmentation constraint_state --constraints half_cheetah_dithering_0 half_cheetah_dithering_1 half_cheetah_dithering_2 half_cheetah_dithering_3 half_cheetah_dithering_4 half_cheetah_dithering_5 --rewards -1 -1 -1 -1 -1 -1
```
