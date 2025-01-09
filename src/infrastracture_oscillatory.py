from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureOscillatory(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.current_infrastructure_capacity.equation = \
        100 / (1 + sd.exp(-(0.05 * (sd.time() - 15))))

