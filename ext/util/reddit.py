import aiohttp

class SortType:
	HOT = 1
	NEW = 2
	RISING = 3
	CONTROVERSIAL = 4
	TOP = 5

	TOP_DAY = 6
	TOP_WEEK = 7
	TOP_MONTH = 8
	TOP_YEAR = 9
	TOP_ALL = 10

class Submission:
	"""Represents a post in a Reddit community."""
	def __init__(self):
		"""Initializing a submission directly is a bad idea."""
		self.title = "Title"
		self.content = ""
		self.media = None

		self.score = 0
		self.author = ""
		self.pinned = False

class Subreddit:
	"""Represents a Reddit community."""
	def __init__(self, name: str):
		"""Create an instance to view submissions."""
		self.name = name

	def get(self, limit: int = 1, sort: int = SortType.HOT):
		"""Get submission objects from a Reddit community."""
		submission = Submission()
		submission.title = ""
		submission.content = ""
		submission.media = None

		submission.score = 0
		submission.author = ""