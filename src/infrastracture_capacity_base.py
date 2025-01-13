from src.less_cars_base_dynamics import LessCarsBaseDynamics


class InfrastractureCapacityBase(LessCarsBaseDynamics):
  def __init__(self):
    super().__init__(starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')
    # if this must be defined, is it better to leave it here or put it in their specific class or in abc?
    self.threshold_time = self.constant('Threshold Time')
    self.threshold_capacity = self.constant('Capacity at Threshold')
    self.initial_capacity = self.constant('Initial Capacity')
    self.midtime = self.constant('Midtime')

    self.initialize()

  def initialize(self):
    self.current_infrastructure_capacity.equation = None
