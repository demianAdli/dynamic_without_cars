from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationOscillatory(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()
    self.amplitude_variability = 0.02
    self.cycle_length = 60  # Solve the cycle length problem
    self.amplitude = self.average_population * self.amplitude_variability

    self.population = \
        self.average_population + \
        self.amplitude * \
        sd.sin(self.frequency * sd.time())


po = PopulationOscillatory()
print(po.population)