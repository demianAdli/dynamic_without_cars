from BPTK_Py import Model
from BPTK_Py import sd_functions as sd

from src.less_cars_base_dynamics import LessCarsBaseDynamics


class PopulationLogisticGrowth(LessCarsBaseDynamics):
  def __init__(self):
    Model.__init__(self, starttime=0.0, stoptime=25.0, dt=1.0, name='population_logistic_growth')
    self.private_cars_num = self.stock('Number of Private Cars')
    self.population = self.converter('Population')
    self.carrying_capacity = self.constant('Carrying Capacity')

    self.initialize()

  def initialize(self):
    self.carrying_capacity.equation = 17100
    self.population.equation = self.carrying_capacity / (1 + sd.exp(-(0.02 * (sd.time() - 15))))
