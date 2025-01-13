from BPTK_Py import sd_functions as sd

from src.shift_base import ShiftBase


class ShiftPolicyDriven(ShiftBase):
  def __init__(self):
    super().__init__()
    self.policy_year = self.constant('Policy Year')
    self.policy_shift = self.constant('Policy Shift')
    self.post = self.constant('Post')

    self.initialize()

  def initialize(self):
    super().initialize()

    self.policy_year = 1
    self.policy_shift = 1
    self.post = 1

    self.shift_to_sustainable_modes.equation = \
        sd.If(sd.time() <= self.policy_year,
              self.initial_shift + self.shift_growth_rate * sd.time(),
              self.post - self.policy_shift + self.shift_growth_rate *
              (sd.time() - self.policy_year))
