from src.shift_base import ShiftBase


class ShiftCostComparison(ShiftBase):
  def __init__(self):
    super().__init__()
    self.car_use_cost = self.constant('Cost of Car Use')
    self.sustainable_modes_cost = self.constant('Cost of Sustainable Modes')
    self.cost_sensitivity_factor = self.constant('Cost Sensitivity Factor')

    self.initialize()

  def initialize(self):
    super().initialize()

    self.car_use_cost.equation = 2900
    self.sustainable_modes_cost.equation = 1060
    # Three scenarios each has more than one scenarios
    # (Page 7 sd_scenarios in content folder)
    self.cost_sensitivity_factor.equation = 0.01
    self.shift_to_sustainable_modes.equation = \
        self.base_shift + \
        ((self.car_use_cost - self.sustainable_modes_cost) /
         self.cost_sensitivity_factor)
