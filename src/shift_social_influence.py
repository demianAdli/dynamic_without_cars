from src.shift_base import ShiftBase


class ShiftSocialInfluence(ShiftBase):
  def __init__(self):
    super().__init__()
    self.current_shift = self.constant('Current Shift')
    self.social_influence_factor = self.constant('Social Influence Factor')

    self.initialize()

  def initialize(self):
    super().initialize()

    self.current_shift = 1
    # Three scenarios each has more than one scenarios
    # (Pages 6 and 7 sd_scenarios in content folder)
    self.social_influence_factor = 0.01
    self.shift_to_sustainable_modes.equation = \
        self.current_shift * \
        (1 + self.social_influence_factor * (1 - self.current_shift))
