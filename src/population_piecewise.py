from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase
from src.population_exponential import PopulationExponential
from src.population_logistic import PopulationLogistic


class PopulationPiecewiseGrowth(PopulationBase):
  def __init__(self):
    super().__init__()
    self.population_threshold_time = self.constant('Population Threshold Time')

    self.initialize()

  def initialize(self):
    super().initialize()

    self.population_threshold_time = 13
    self.population.equation = \
        sd.If(sd.time() >= self.population_threshold_time,
              PopulationExponential().population.equation,
              PopulationLogistic().population.equation)
