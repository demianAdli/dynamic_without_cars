from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureExponential(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.infrastructure_initial_capacity = 0.15
    self.current_infrastructure_capacity.equation = \
        self.initial_capacity * \
        sd.exp(self.infrastracture_growth_rate * sd.time())
