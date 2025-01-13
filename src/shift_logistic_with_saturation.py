from BPTK_Py import sd_functions as sd

from src.shift_base import ShiftBase


class ShiftLogisticWithSaturation(ShiftBase):
  def __init__(self):
    super().__init__()
    self.max_shift = self.constant('Maximum Shift')

    self.initialize()

  def initialize(self):
    super().initialize()

    self.max_shift = 1
    # midtime is undefined
    self.shift_to_sustainable_modes.equation = \
        self.max_shift / \
        (1 + sd.exp(-self.shift_growth_rate * (sd.time() - self.midtime)))
