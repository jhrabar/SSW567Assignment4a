
# John Hrabar
# I Pledge My Honor That I Have Abided By The Stevens Honor System

#John Hrabar
#I Pledge My Honor That I Have Abided By The Stevens Honor System
#I had to split my original code from assignment 4 into multiple functions.
#The core of the code is the same, but it was very difficult to test using mocks
#when it was all in one function due to the multiple different API calls

import requests
import json

def getCommitNumber(username, repo):
	repoResponse = requests.get("https://api.github.com/repos/" + username + "/" + repo + "/commits")
	return len(repoResponse.json())

def getGithubRepos(username):
	if(not username or not isinstance(username, str)):
		return "Error: Username must be a valid, non-empty string"

	response = requests.get("https://api.github.com/users/" + username + "/repos")

	if(response.status_code != 200):
		return "Error: Data not found"

	if(len(response.json()) < 1):
		return "User " + username + " has no repositories or does not exist"

	return response.json()


def getTotalCommitNumber(username):
	repositories = getGithubRepos(username)
	if(isinstance(repositories, str)):
		return repositories
	finalResult = ""
	for repo in repositories:
			commits = getCommitNumber(username, repo['name'])
			finalResult = finalResult + "Repo: " + repo['name'] + " Number of Commits: " + str(commits) + "\n"
	return finalResult