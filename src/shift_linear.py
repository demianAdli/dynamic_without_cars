from BPTK_Py import sd_functions as sd

from src.shift_base import ShiftBase


class ShiftLinear(ShiftBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.shift_to_sustainable_modes.equation = \
        self.initial_shift + self.shift_growth_rate * sd.time()
