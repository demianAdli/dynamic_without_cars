from src.less_cars_base_dynamics import LessCarsBaseDynamics


class ShiftBase(LessCarsBaseDynamics):
  def __init__(self):
    super().__init__(starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')
    self.initial_shift = self.constant('Initial Shift')
    self.base_shift = self.constant('Base Shift')

    self.initialize()

  def initialize(self):
    self.initial_shift.equation = 5
    self.base_shift.equation = 1
    self.shift_to_sustainable_modes.equation = None
