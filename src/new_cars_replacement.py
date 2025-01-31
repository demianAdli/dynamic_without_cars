from BPTK_Py import sd_functions as sd

from src.new_cars_base import NewCarsBase


class NewCarsReplacement(NewCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.replacement_rate.equation = 0.083
    # Demand Growth: based on population and income growth, adjusted for car ownership trends.
    self.demand_growth = 0.01
    self.new_cars_num.equation = \
        self.replacement_rate * self.private_cars_num + self.demand_growth
