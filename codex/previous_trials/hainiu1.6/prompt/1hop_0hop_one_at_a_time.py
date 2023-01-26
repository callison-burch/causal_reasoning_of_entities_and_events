# python

class Wash_Hands:
  # Init
  # Turn on the tap water.
  # Put hands under running water.
  # Apply soap and rub hands.
  # Turn off the tap water.
  # Dry my hands using a towel.
  def init(self, event):
    self.hands = Hands()
    self.event = event # I can safely touch a light switch.
  def turn_on_tap_water(self):
    self.hands.wet = False
    self.event.change = "equally likely" # I can safely touch a light switch.
  def put_hands_under_running_water(self):
    self.hands.wet = True
    self.event.change = "less likely" # I can safely touch a light switch.
  def apply_soap_and_rub_hands(self):
    self.hands.wet = True
    self.event.change = "equally likely" # I can safely touch a light switch.
  def turn_off_tap_water(self):
    self.hands.wet = True
    self.event.change = "equally likely" # I can safely touch a light switch.
  def dry_hands_with_towel(self):
    self.hands.wet = False
    self.event.change = "more likely" # I can safely touch a light switch.

class Wash_Hands:
  # Init
  # Turn on the tap water.
  # Put hands under running water.
  # Apply soap and rub hands.
  # Turn off the tap water.
  # Dry my hands using a towel.
  def init(self, event):
    self.water = Water()
    self.event = event # Water streaming sound can be heard.
  def turn_on_tap_water(self):
    self.water.on = True
    self.event.change = "more likely" # Water streaming sound can be heard.
  def put_hands_under_running_water(self):
    self.water.on = True
    self.event.change = "equally likely" # Water streaming sound can be heard.
  def apply_soap_and_rub_hands(self):
    self.water.on = True
    self.event.change = "equally likely" # Water streaming sound can be heard.
  def turn_off_tap_water(self):
    self.water.on = False
    self.event.change = "less likely" # Water streaming sound can be heard.
  def dry_hands_with_towel(self):
    self.water.on = False
    self.event.change = "equally likely" # Water streaming sound can be heard.

class Change_Battery_of_TV_Remote_Control:
  # Init
  # Pop open the battery cover.
  # Take out the old batteries.
  # Put in the new batteries.
  # Close the battery cover.
  def init(self, event):
    self.battery_cover = Battery_Cover()
    self.event = event # I can see inside the battery compartment
  def pop_open_battery_cover(self):
    self.battery_cover.removed = True
    self.event.change = "more likely" # I can see inside the battery compartment
  def take_out_old_batteries(self):
    self.battery_cover.removed = True
    self.event.change = "equally likely" # I can see inside the battery compartment
  def put_in_new_batteries(self):
    self.battery_cover.removed = True
    self.event.change = "equally likely" # I can see inside the battery compartment
  def close_battery_cover(self):
    self.battery_cover.removed = False
    self.event.change = "less likely" # I can see inside the battery compartment

class Change_Battery_of_TV_Remote_Control:
  # Init
  # Pop open the battery cover.
  # Take out the old batteries.
  # Put in the new batteries.
  # Close the battery cover.
  def init(self, event):
    self.remote = Remote()
    self.event = event # The remote can turn on a TV.
  def pop_open_battery_cover(self):
    self.remote.has_battery = True
    self.event.change = "equally likely" # The remote can turn on a TV.
  def take_out_old_batteries(self):
    self.remote.has_battery = False
    self.event.change = "less likely" # The remote can turn on a TV.
  def put_in_new_batteries(self):
    self.remote.has_battery = True
    self.event.change = "more likely" # The remote can turn on a TV.
  def close_battery_cover(self):
    self.remote.has_battery = True
    self.event.change = "equally likely" # The remote can turn on a TV.

class Cook_Salmon_In_Oven:
  # Init
  # Pat dry the salmon.
  # Brush the salmon with sauce.
  # Put the salmon on the foil.
  # Put the salmon in an oven preheated to 350 degrees for 20 minutes.
  # Serve the salmon.
  def init(self, event):
    self.salmon = Salmon()
    self.event = event # The salmon can be easliy flaked by a fork.
  def pat_dry_salmon(self):
    self.salmon.cooked = False
    self.event.change = "equally likely" # The salmon can be easliy flaked by a fork.
  def brush_salmon_with_sauce(self):
    self.salmon.cooked = False
    self.event.change = "equally likely" # The salmon can be easliy flaked by a fork.
  def cover_salmon_with_foil(self):
    self.salmon.cooked = False
    self.event.change = "equally likely" # The salmon can be easliy flaked by a fork.
  def put_salmon_in_oven_preheated_to_350_degrees_for_20_minutes(self):
    self.salmon.cooked = True
    self.event.change = "more likely" # The salmon can be easliy flaked by a fork.
  def serve_salmon(self):
    self.salmon.cooked = True
    self.event.change = "equally likely" # The salmon can be easliy flaked by a fork.

class Cook_Salmon_In_Oven:
  # Init
  # Pat dry the salmon.
  # Brush the salmon with sauce.
  # Put the salmon on the foil.
  # Put the salmon in an oven preheated to 350 degrees for 20 minutes.
  # Serve the salmon.
  def init(self, event):
    self.salmon = Salmon()
    self.event = event # I touch the salmon and my fingers get wet.
  def pat_dry_salmon(self):
    self.salmon.wet = False
    self.event.change = "less likely" # I touch the salmon and my fingers get wet.
  def brush_salmon_with_sauce(self):
    self.salmon.wet = True
    self.event.change = "more likely" # I touch the salmon and my fingers get wet.
  def cover_salmon_with_foil(self):
    self.salmon.wet = True
    self.event.change = "equally likely" # I touch the salmon and my fingers get wet.
  def put_salmon_in_oven_preheated_to_350_degrees_for_20_minutes(self):
    self.salmon.wet = False
    self.event.change = "less likely" # I touch the salmon and my fingers get wet.
  def serve_salmon(self):
    self.salmon.wet = False
    self.event.change = "equally likely" # I touch the salmon and my fingers get wet.
