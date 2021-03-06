import numpy as np

from .env import Env
from .vec_env import VecEnv

from .spaces import Discrete
from .spaces import Box


class EnvSpec(object):
    r"""Summarize the specifications of the environment. 
    
    It collects useful properties of an environment which can be very convenient for
    designing generic APIs to train RL agents, such as observation and action spaces, 
    maximum allowed horizon, discrete or continuous control type etc. 
    """
    def __init__(self, env):
        r"""Initialize the environment specification. 
        
        Args:
            env (Env/VecEnv): an environment object. 
        """
        assert isinstance(env, (Env, VecEnv)), f'expected Env or VecEnv dtype, got {type(env)}'
        
        self.env = env
    
    @property
    def observation_space(self):
        r"""Returns the observation space of the environment. """
        return self.env.observation_space
    
    @property
    def action_space(self):
        r"""Returns the action space of the environment. """
        return self.env.action_space
    
    @property
    def T(self):
        r"""Returns the maximum horizon of the environment. """
        return self.env.T
    
    @property
    def max_episode_reward(self):
        r"""Returns the maximum episodic rewards of the environment. """
        return self.env.max_episode_reward
    
    @property
    def reward_range(self):
        r"""Returns a tuple of min and max possible rewards. """
        return self.env.reward_range
    
    @property
    def control_type(self):
        r"""Returns a string to indicate if the environment is discrete or continuous control. 
        
        It returns one of the following strings:
        
        * 'Discrete': if the action space is of type :class:`Discrete`
        
        * 'Continuous': if the action space is of type :class:`Box`
        
        """
        if isinstance(self.env.action_space, Discrete):
            return 'Discrete'
        elif isinstance(self.env.action_space, Box):
            return 'Continuous'
        else:
            raise TypeError(f'expected type as Discrete or Box, got {type(self.env.action_space)}.')

    def __repr__(self):
        string = f'<{type(self).__name__}, {self.env}>\n'
        string += f'\tObservation space: {self.observation_space}\n'
        string += f'\tAction space: {self.action_space}\n'
        string += f'\tControl type: {self.control_type}\n'
        string += f'\tT: {self.T}\n'
        string += f'\tMax episode reward: {self.max_episode_reward}\n'
        string += f'\tReward range: {self.reward_range}'
        
        return string
