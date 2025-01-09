from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationOscillatoryGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.population = \
        self.average_population * \
        self.amplitude * \
        sd.sin(self.frequency * sd.time())
