from src.shift_base import ShiftBase


class ShiftLinear(ShiftBase):
  def __init__(self):
    super().__init__()

    self.initialize()

  def initialize(self):
    super().initialize()

    self.shift_to_sustainable_modes.equation = \
        ((min(1, self.current_infrastructure_capacity / 100) *
          (self.active_transportation_trip_share +
           self.public_transport_trip_share +
           self.ride_sharing_trip_share) /
          max(1,
              (self.active_transportation_trip_share +
               self.public_transport_trip_share +
               self.ride_sharing_trip_share))) / 100) * \
        self.private_cars_num
