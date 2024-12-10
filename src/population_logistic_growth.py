from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

from src.population_base import PopulationBase


class PopulationLogisticGrowth(PopulationBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

