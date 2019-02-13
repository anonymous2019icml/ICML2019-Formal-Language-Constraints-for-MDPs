import argparse
import luigi

import pipeline.train_task as train_task
import pipeline.test_task as test_task


parser = argparse.ArgumentParser()
parser.add_argument('--env-name',
                    type=str,
                    choices=['BreakoutDeterministic-v4', 'SpaceInvadersDeterministic-v4', 'SeaquestDeterministic-v4', 'doom'])
parser.add_argument('--task',
                    type=str,
                    choices=['train', 'test'])
parser.add_argument('--contract',
                    type=str,
                    choices=['dithering', 'actuation', 'upto4'])
parser.add_argument('--doom_scenario', type=str, default=None,
                    choices=['DoomBasic-v0', 'DoomCorridor-v0',
                             'DoomDefendCenter-v0', 'DoomDefendLine-v0',
                             'DoomHealthGathering-v0', 'DoomMyWayHome-v0',
                             'DoomPredictPosition-v0', 'DoomTakeCover-v0'])
parser.add_argument('--arch',
                    type=str,
                    choices=['original', 'contract', 'contract_action_history', 'contract_dfa_state', 'contract_graph_emb'])
parser.add_argument('--train_seed', type=int)
parser.add_argument('--test_seed', type=int)
parser.add_argument('--steps', type=int, default=10000000)
parser.add_argument('--enforce_contract', type=bool, default=False)
args = parser.parse_args()


arch = args.arch
if arch == 'original':
    arch = 'contract'
    mode = 'off'
else:
    mode = 'punish'

if args.task=='train':
    tasks = [train_task.TrainTask(env_name=args.env_name, contract=args.contract, steps=args.steps, architecture=arch, contract_mode=mode, train_seed=args.train_seed, enforce_contract=args.enforce_contract, doom_scenario=args.doom_scenario)]
else:
    tasks = [test_task.TestTask(env_name=args.env_name, contract=args.contract, steps=args.steps, architecture=arch, contract_mode=mode, train_seed=args.train_seed, test_seed=args.test_seed, enforce_contract=args.enforce_contract, doom_scenario=args.doom_scenario)]

luigi.build(tasks, local_scheduler=True)
