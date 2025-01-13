from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureLinear(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.current_infrastructure_capacity.equation = \
      sd.time() / self.horizon * 100
