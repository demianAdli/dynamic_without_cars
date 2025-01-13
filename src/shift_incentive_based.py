from BPTK_Py import sd_functions as sd

from src.shift_base import ShiftBase


class ShiftIncentiveBased(ShiftBase):
  def __init__(self):
    super().__init__()
    self.incentive_effect = self.constant('Incentive Effect')

    self.initialize()

  def initialize(self):
    super().initialize()

    # Three scenarios each has more than three scenarios
    # (Page 6 sd_scenarios in content folder)
    self.incentive_effect = 0.01
    self.shift_to_sustainable_modes.equation = \
        self.base_shift * sd.exp(self.incentive_effect * sd.time())
