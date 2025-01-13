from src.less_cars_base_dynamics import LessCarsBaseDynamics


class ShiftBase(LessCarsBaseDynamics):
  def __init__(self):
    super().__init__(starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')

    self.initialize()

  def initialize(self):
    self.shift_to_sustainable_modes.equation = None
