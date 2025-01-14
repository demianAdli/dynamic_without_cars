from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastracturePiecewiseLinear(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()
    self.infrastructure_threshold_time = \
        self.constant('Infrastructure Threshold Time')
    self.infrastructure_threshold_capacity = \
        self.constant('Infrastructure Capacity at Threshold')
    self.midtime = self.constant('Midtime')

    self.initialize()

  def initialize(self):
    super().initialize()

    self.infrastructure_threshold_time = 13
    self.infrastructure_initial_capacity = 0.15
    self.infrastructure_threshold_capacity = 30
    self.current_infrastructure_capacity.equation = \
        sd.If(
          sd.time() <= self.infrastructure_threshold_time,
          self.infrastructure_initial_capacity +
          self.infrastracture_growth_rate *
          sd.time(),
          self.infrastructure_threshold_capacity +
          self.infrastracture_growth_rate *
          (sd.time() - self.infrastructure_threshold_time))
