from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase

# Question: what is horizon


class PopulationLinearGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.population.equation = \
        sd.min(self.carrying_capacity,
               self.carrying_capacity * sd.time() / self.horizon)
