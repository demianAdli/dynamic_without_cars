from abc import ABC, abstractmethod

from BPTK_Py import Model
from BPTK_Py import sd_functions as sd


class LessCarsBaseDynamics(ABC, Model):
  def __init__(self):
    Model.__init__(self, starttime=0.0, stoptime=25.0, dt=1.0, name='base_model')
    self.private_cars_num = self.stock('Number of Private Cars')
    self.new_cars_num = self.flow('Number of New Cars')
    self.shift_to_sustainable_modes = self.flow('Shift to Sustainable Modes')
    self.population = self.converter('Population')
    self.current_infrastructure_capacity = self.converter('Current Infrastructure Capacity')
    self.education_level = self.converter('Education Level')
    self.sustainable_mode_preference = self.converter('Mode Preference Towards Sustainable Modes')
    self.ride_sharing_trip_share = self.converter('Share of Ride-Sharing Trips')
    self.public_transport_trip_share = self.converter('Share of Public Transport Trips')
    self.active_transportation_trip_share = self.converter('Share of Active Transportation Trips')
    self.investment_in_rs = self.converter('Investment in RS')
    self.investment_in_pt = self.converter('Investment in PT')
    self.investment_in_at = self.converter('Investment in AT')
    self.carrying_capacity = self.constant('Carrying Capacity')
    self.public_investment_in_mobility = self.constant('Public Investment in Mobility')
    self.available_transportation_modes = self.constant('Available Transportation Modes')
    self.initial_private_cars_num = self.converter('Initial Number of Private Cars')

  @abstractmethod
  def initialize(self):
    self.public_investment_in_mobility.equation = 2e9
    self.available_transportation_modes.equation = 3.0
    self.carrying_capacity.equation = 17100
    self.population.equation = self.carrying_capacity / (1 + sd.exp(-(0.02 * (sd.time() - 15))))
    self.initial_private_cars_num.equation = (sd.If(sd.time() == 0, self.population, self.initial_private_cars_num)) * 0.84 * 0.9

    self.private_cars_num.initial_value = self.initial_private_cars_num

    self.private_cars_num.equation = self.new_cars_num - self.shift_to_sustainable_modes

    self.new_cars_num.equation = (1 - sd.time() / 25) * (self.population - self.shift_to_sustainable_modes) * 0.84 * 0.9
    self.education_level.equation = sd.time() / 25
    self.sustainable_mode_preference.equation = (self.available_transportation_modes / (self.available_transportation_modes + 1)) * (
            1 + self.education_level + 1.1)

    self.ride_sharing_trip_share.equation = self.sustainable_mode_preference * (
            1 + self.investment_in_rs / self.public_investment_in_mobility)
    self.public_transport_trip_share.equation = self.sustainable_mode_preference * (
            1 + self.investment_in_pt / self.public_investment_in_mobility)
    self.active_transportation_trip_share.equation = self.sustainable_mode_preference * (
            1 + self.investment_in_at / self.public_investment_in_mobility)
    self.investment_in_rs.equation = 2e8 + self.public_investment_in_mobility * 0.3
    self.investment_in_pt.equation = 8e8 + 0.6 * self.public_investment_in_mobility
    self.investment_in_at.equation = 5e7 + self.public_investment_in_mobility * 0.1
    self.current_infrastructure_capacity.equation = 100 / (1 + sd.exp(-(0.05 * (sd.time() - 15))))
    self.shift_to_sustainable_modes.equation = \
      ((min(1, self.current_infrastructure_capacity / 100) *
        (self.active_transportation_trip_share + self.public_transport_trip_share + self.ride_sharing_trip_share) /
        max(1, (
                self.active_transportation_trip_share + self.public_transport_trip_share + self.ride_sharing_trip_share))) / 100) * self.private_cars_num
