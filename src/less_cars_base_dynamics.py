from abc import ABC, abstractmethod

from BPTK_Py import Model


class LessCarsBaseDynamics(ABC, Model):
  def __init__(self, *args, **kwargs):
    Model.__init__(
      self, starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')
    self.initial_private_cars_num = \
        self.converter('Initial Number of Private Cars')
    self.private_cars_num = self.stock('Number of Private Cars')
    self.new_cars_num = self.flow('Number of New Cars')
    self.shift_to_sustainable_modes = self.flow('Shift to Sustainable Modes')
    self.population = self.converter('Population')
    self.amplitude = self.converter('Amplitude')
    self.frequency = self.converter('Frequency')
    self.current_infrastructure_capacity = \
        self.converter('Current Infrastructure Capacity')
    self.education_level = self.converter('Education Level')
    self.sustainable_mode_preference = \
        self.converter('Mode Preference Towards Sustainable Modes')
    self.ride_sharing_trip_share = \
        self.converter('Share of Ride-Sharing Trips')
    self.public_transport_trip_share = \
        self.converter('Share of Public Transport Trips')
    self.active_transportation_trip_share =  \
        self.converter('Share of Active Transportation Trips')
    self.investment_in_rs = self.converter('Investment in RS')
    self.investment_in_pt = self.converter('Investment in PT')
    self.investment_in_at = self.converter('Investment in AT')
    self.initial_population = self.constant('Initial Population')
    self.carrying_capacity = self.constant('Carrying Capacity')
    self.tipping_point = self.constant('Tipping Point')
    self.average_population = self.constant('Average Population')
    self.amplitude_variability = self.constant('Amplitude Variability')
    self.cycle_length = self.constant('Cycle Length')
    self.alpha = self.constant('Alpha')
    self.horizon = self.constant('Horizon')
    self.public_investment_in_mobility =  \
        self.constant('Public Investment in Mobility')
    self.available_transportation_modes = \
        self.constant('Available Transportation Modes')
    self.economic_factor = self.constant('Economic Factor')

    self.population_growth_rate = self.constant('Population Growth Rate')
    self.infrastracture_growth_rate = self.constant('Infrastracture Capacity Growth Rate')
    self.private_cars_growth_rate = self.constant('Private Cars Growth Rate')
    self.shift_growth_rate = self.constant('Shift to Sustainable Modes Growth Rate')
    self.new_cars_growth_rate = self.constant('New Cars Growth Rate')

  @abstractmethod
  def initialize(self):
    pass

