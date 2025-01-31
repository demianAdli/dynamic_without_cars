from BPTK_Py import sd_functions as sd
from src.population_base import PopulationBase


class PopulationOscillatory(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()
    self.amplitude_variability.equation = 0.02
    self.cycle_length.equation = 60
    self.amplitude.equation = \
        self.average_population * \
        self.amplitude_variability

    self.population.equation = \
        self.average_population + \
        self.amplitude * \
        sd.sin(self.frequency * sd.time())
