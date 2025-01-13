from BPTK_Py import sd_functions as sd

from src.infrastracture_capacity_base import InfrastractureCapacityBase


class InfrastractureLogisticWithCarryingCapacity(InfrastractureCapacityBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.current_infrastructure_capacity.equation = \
        self.carrying_capacity / \
        (1 + (self.carrying_capacity - self.initial_population /
              self.initial_population)
         * sd.exp(-0.01 * sd.time()))

