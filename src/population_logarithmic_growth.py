import numpy as np
from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationLogarithmicGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()
    this_time = self.converter('Model\'s Time')
    this_time.equation = sd.time()
    numeric_time = float(this_time.equation)
    self.population.equation = self.carrying_capacity * np.log(numeric_time + 1)
