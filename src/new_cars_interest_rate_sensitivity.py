from BPTK_Py import sd_functions as sd

from src.new_cars_base import NewCarsBase


class NewCarsInterestRateSensitivity(NewCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()
    # With an elasticity of 1.1, if the current rate drops by 10%,
    # new car purchases increase by 11%. (typically, between 0.5–1.5)
    self.initial_interest_rate = 1
    self.current_interest_rate = 1
    self.interest_elasticity = 1
    self.new_cars_num.equation = \
        self.initial_new_cars_num * \
        (self.initial_interest_rate / self.current_interest_rate) ** \
        self.interet_elasticity
