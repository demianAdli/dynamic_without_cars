from BPTK_Py import sd_functions as sd

from src.new_cars_base import NewCarsBase


class NewCarsLogisticWithSaturation(NewCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.new_cars_num.equation = \
        self.max_new_cars_num / \
        (1 +
         ((self.max_new_cars_num - self.initial_new_cars_num) /
          self.initial_new_cars_num) *
         sd.exp(- self.new_cars_growth_rate * sd.time()))
