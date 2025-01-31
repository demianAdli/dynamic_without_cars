from src.less_cars_base_dynamics import LessCarsBaseDynamics


class NewCarsBase(LessCarsBaseDynamics):
  def __init__(self):
    super().__init__(starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')
    self.initial_new_cars_num = self.constant('Initial Number of New Cars')
    self.average_income = self.constant('Average Income')
    self.initial_income = self.constant('Initial Income')
    self.elasticity = self.constant('Elasticity (New Cars)')
    self.replacement_rate = self.constant('Replacement Rate')
    self.demand_growth = self.constant('Demand Growth')
    self.max_new_cars_num = self.constant('Maximum Number of New Cars')
    self.policy_impact_factor = self.constant('Policy Impact Factor')

    self.initialize()

  def initialize(self):
    self.initial_new_cars_num.equation = 1
    self.new_cars_num.equation = None
