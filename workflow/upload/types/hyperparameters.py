from dataclasses import dataclass
from enum import Enum


class ExplorationType(Enum):
    """
  `categorical` (for clipped_ppo training algorithm) 
  or `additive_noise` (for sac training algorithm)
  """

    CATEGORICAL = 'categorical'
    ADDITIVE_NOISE = 'addtive_noise'


class LossType(Enum):
    """
  Type of loss technique used to minimize the error, two available on DeepRacer: MSE (Mean Squared Error) and Huber.
  """

    MSE = 'mean squared error'
    HUBER = 'huber'


@dataclass
class HyperParameters:
    """
  Structure to define hyperparametes from DeepRacer with default values from documentation
  `source: <https://github.com/aws-deepracer-community/deepracer-on-the-spot/tree/main/custom-files>`
  """

    batch_size: int = 64
    beta_entropy: float = 0.01
    discount_factor: float = 0.999
    e_greedy_value: float = 0.05
    epsilon_steps: int = 10000
    exploration_type: ExplorationType = ExplorationType.CATEGORICAL
    loss_type: LossType = LossType.HUBER
    lr: float = 0.0003
    num_episodes_between_training: int = 40
    num_epochs: int = 3
    stack_size: int = 1
    term_cond_avg_score: float = 100000
    term_cond_max_episodes: float = 100000
