from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationPowerLawGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.population.equation = \
        self.initial_population * sd.time() ** self.alpha
