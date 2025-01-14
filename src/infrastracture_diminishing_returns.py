import numpy as np

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastracturediminishingReturns(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.infrastructure_initial_capacity = 0.15
    self.current_infrastructure_capacity.equation = \
        self.infrastructure_initial_capacity + \
        np.log(self.public_investment_in_mobility + 1)
