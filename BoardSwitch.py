from gpiozero import LED

class smartPin(LED):

	def __init__(self, pin_no):
		super().__init__(pin_no)

	def switch_on(self):
		if not self.is_active:
			super().on()

	def switch_off(self):
		if self.is_active:
			super().off()



