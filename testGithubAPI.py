

import unittest
from unittest import mock
import requests
import json

from githubAPI import getGithubRepos, getCommitNumber, getTotalCommitNumber



class TestGithubAPI(unittest.TestCase):

	@mock.patch('requests.get')
	def testUsernameInput(self, mockedReq):
		mockedReq = mock.MagicMock(return_value = {"message": "Not Found","documentation_url": "https://developer.github.com/v3"})
		self.assertEqual("Error: Username must be a valid, non-empty string", getGithubRepos(""))
		self.assertEqual("Error: Username must be a valid, non-empty string", getGithubRepos(123))

	@mock.patch('requests.get')
	def testValidGithubUser(self, mockedReq):
		mockedReq.return_value = mock.Mock(status_code = 200)
		mockedReq.return_value.json.return_value = {}
		result = getGithubRepos("fakeuser123456")
		self.assertEqual("User fakeuser123456 has no repositories or does not exist", result)

	@mock.patch('requests.get')
	def testValidGithubUser2(self, mockedReq):
		mockedReq = mock.MagicMock(return_value = {"message": "Not Found","documentation_url": "https://developer.github.com/v3/repos/#list-user-repositories"})
		self.assertEqual("Error: Data not found", getGithubRepos("fakeuser123 456"))

	@mock.patch('requests.get')
	def testCommitNumber(self, mockedReq):
		mockedReq.return_value = mock.Mock(status_code = 200)
		mockedReq.return_value.json.return_value = [{"commit1":"one"},{"commit2":"two"}, {"commit3":"three"}, {"commit4":"four"}, {"commit5":"five"}]
		self.assertEqual(5, getCommitNumber("fakeaccountjohn", "repo1"))

	@mock.patch('requests.get')
	def testCommitNumber2(self, mockedReq):
		mockedReq.return_value = mock.Mock(status_code = 200)
		mockedReq.return_value.json.return_value = {"commit1":"one"}
		self.assertEqual(1, getCommitNumber("fakeaccountjohn", "repo2"))


if __name__ == '__main__':
	print('Running unit tests')
	unittest.main()