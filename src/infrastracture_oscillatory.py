from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureOscillatory(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.current_infrastructure_capacity.equation = \
        self.initial_capacity + \
        self.amplitude * \
        sd.sin(self.frequency * sd.time())
