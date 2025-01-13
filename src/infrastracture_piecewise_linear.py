from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastracturePiecewiseLinear(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.threshold_time = 10  # this constant has not been defined
    self.threshold_capacity = 30
    self.current_infrastructure_capacity.equation = \
        (sd.If
         (sd.time() <= self.tipping_point,
          self.initial_capacity + self.infrastracture_growth_rate * sd.time(),
          self.threshold_capacity + self.infrastracture_growth_rate * (
                  sd.time() - self.threshold_time)))
