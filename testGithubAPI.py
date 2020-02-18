

import unittest

from githubAPI import getGithubInfo

class TestGithubAPI(unittest.TestCase):

	def testUsernameInput(self):
		self.assertEqual("Error: Username must be a valid, non-empty string", getGithubInfo(""))
		self.assertEqual("Error: Username must be a valid, non-empty string", getGithubInfo(123))

	def testValidGithubUser(self):
		self.assertEqual("User fakeuser123456 has no repositories or does not exist", getGithubInfo("fakeuser123456"))
		self.assertEqual("Error: Data not found", getGithubInfo("fakeuser123 456"))

	def testCommitCount(self):
		self.assertEqual("Repo: InterviewPrep Number of Commits: 26\nRepo: PersonalWebsite Number of Commits: 15\n",getGithubInfo("MarkSwanson4887"))

if __name__ == '__main__':
	print('Running unit tests')
	unittest.main()