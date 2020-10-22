class Scheduler:
	def __init__(self):
		self.tasks = []

	def clear(self):
		self.tasks.clear()
		return self

class Task:
	def __init__(self):
		pass

	def delete(self):
		"""Delete the task from the object and the scheduler."""
		del self.scheduler.find(self)
		del self