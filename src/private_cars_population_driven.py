from src.private_cars_base import PrivateCarsBase


class PrivateCarsPopulationDriven(PrivateCarsBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.private_cars_num.equation = \
        self.new_cars_num - self.shift_to_sustainable_modes
