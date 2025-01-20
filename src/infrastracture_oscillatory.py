from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureOscillatory(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()
    self.infrastructure_capacity_amplitude.equation = 50

    self.current_infrastructure_capacity.equation = \
        self.initial_capacity + \
        self.infrastructure_capacity_amplitude * \
        sd.sin(self.frequency * sd.time())
