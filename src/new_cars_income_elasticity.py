from BPTK_Py import sd_functions as sd

from src.new_cars_base import NewCarsBase


class NewCarsIncomeElasticity(NewCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()
    self.initial_new_cars_num.equation = 1
    self.average_income.equation = 1
    self.initial_income.equation = 1
    # The elasticity is between 0.5 and 1.5
    self.elasticity.equation = 0.5
    self.new_cars_num.equation = \
        self.initial_new_cars_num * \
        ((self.average_income / self.initial_income) ** self.elasticity)
