from BPTK_Py import sd_functions as sd

from src.new_cars_base import NewCarsBase


class NewCarsPolicyInfluenced(NewCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    # minimal impact = 0.01 to 0.05
    # moderate impact = 0.05 to 0.1
    # high impact = 0.1 to 0.3
    self.policy_impact_factor.equation = 0.01
    self.new_cars_num.equation = \
        self.initial_new_cars_num * \
        (1 - ((self.policy_impact_factor * sd.time()) / 100))
