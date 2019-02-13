from rl.callbacks import Callback


class ContractLogger(Callback):
    def __init__(self, filename, interval=1):
        self._interval = interval
        self._file = open(filename, 'w')

        
    def on_episode_begin(self, episode, logs):
        """Called at beginning of each episode"""
        self._action_list = []
        self._info_list = []
        pass

    
    def on_episode_end(self, episode, logs):
        """Called at end of each episode"""
        if episode % self._interval == 0:
            #assert len(self._action_list) == len(self._info_list)
            self._file.write('{}\t{}\t{}\t{}\n'.format(episode, logs, self._action_list, self._info_list))
            self._file.flush()
        pass

    
    def on_step_begin(self, step, logs):
        """Called at beginning of each step"""
        pass

    
    def on_step_end(self, step, logs):
        """Called at end of each step"""
        self._info_list += [logs['info']]

    
    def on_action_begin(self, action, logs):
        """Called at beginning of each action"""
        self._action_list += [action]


    def on_action_end(self, action, logs):
        """Called at end of each action"""
        pass
