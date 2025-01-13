from BPTK_Py import sd_functions as sd

from src.private_cars_base import PrivateCarsBase


class PrivateCarsLinear(PrivateCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.private_cars_num.equation = \
        self.initial_private_cars_num + \
        self.private_cars_growth_rate * sd.time()
