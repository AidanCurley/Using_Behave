class Coffee_Machine:
	def __init__(self, power_on = False):
		self.power_on = power_on
		self.menu = {1:'espresso', 2:'cappucino'}

	@property
	def menu_is_visible(self):
		return self.power_on and self.has_water

	@property
	def warning_is_visible(self):
		return not self.menu_is_visible

	def add_water(self):
		self.has_water = True

	def show_menu(self):
		if self.menu_is_visible:
			return True
		else:
			return False

	def show_warning(self):
		if self.warning_is_visible:
			return True
		else:
			return False
