class Course:
	def __init__(self, code, name, max_num, permission, time, loc):
		self._code = code
		self._name = name
		self._max_num = max_num
		self._permission = permission
		self._time = time
		self._loc = loc	

	def get_code(self):
		return self._code

	def get_name(self):
		return self._name

	def get_limit(self):
		return self._max_num

	def get_permit(self):
		return self._permission

	def get_time(self):
		return self._time

	def get_loc(self):
		return self._loc