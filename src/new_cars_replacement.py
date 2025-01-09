from BPTK_Py import sd_functions as sd

from src.new_cars_base import NewCarsBase


class NewCarsReplacement(NewCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.new_cars_num.equation = \
        (1 - sd.time() / 25) * \
        (self.population - self.shift_to_sustainable_modes) * 0.84 * 0.9
