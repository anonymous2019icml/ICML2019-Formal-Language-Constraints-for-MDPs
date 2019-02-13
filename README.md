# ICML2019 Formal Language Constraints for Markov Decision Processes

This repository contains the code used for experiments in the ICML 2019 paper under review, "Formal Language Constraints for Markov Decision Processes". It is split into two sections: a fork of [keras-rl](https://github.com/keras-rl/keras-rl) which was used for the Atari experiments, and a fork of [OpenAI baselines](https://github.com/openai/baselines) which was used for the Mujoco experiments.

There is no principled reason why the experiments were split. It just happened that experiments began on the `keras-rl` fork, and then switched to OpenAI's `baselines`. Although this happened accidentally, we hope that it can have the silver lining of demonstrating how easy it is to implement the methods outlined in the paper, and how robust they are.

Further, we apologize that we didn't manage to have 100% of the code uploaded immediately upon submission. There has been one update to this repository to upload the code forked from `keras-rl`, for completeness and to encourage replicability of all of the experimental results included in the paper.

More specific readmes are included the sub-folders corresponding to each fork.