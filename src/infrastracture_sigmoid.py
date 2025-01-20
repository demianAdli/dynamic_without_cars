from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureSigmoid(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.midtime.equation = 12
    self.current_infrastructure_capacity.equation = \
        self.carrying_capacity / \
        1 + sd.exp(
          -self.infrastracture_growth_rate * (sd.time() - self.midtime))
