from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationExponentialGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.population.equation = \
        self.carrying_capacity * sd.exp(0.01 * sd.time())

