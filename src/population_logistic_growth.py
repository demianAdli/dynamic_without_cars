from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationLogisticGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.population.equation = \
        self.carrying_capacity / (1 + sd.exp(-(0.02 * (sd.time() - 15))))


