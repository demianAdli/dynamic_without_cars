from src.less_cars_base_dynamics import LessCarsBaseDynamics


class InfrastractureCapacityBase(LessCarsBaseDynamics):
  def __init__(self):
    super().__init__(starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')
    self.initial_capacity = self.constant('Initial Capacity')

    self.initialize()

  def initialize(self):
    self.current_infrastructure_capacity.equation = None
