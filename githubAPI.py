import requests
import json


def getGithubInfo(username):
	if(isinstance(username, str) == False):
		return "Error: Username must be a valid string"

	response = requests.get("https://api.github.com/users/" + username + "/repos")

	if(response.status_code != 200):
		return "Error: Data not found"

	finalResult = ""

	if(len(response.json()) < 1):
		finalResult = "User " + username + " has no repositories"
	else:
		for repo in response.json():
			repoResponse = requests.get("https://api.github.com/repos/" + username + "/" + repo['name'] + "/commits")
			finalResult = finalResult + "Repo: " + repo['name'] + " Number of Commits: " + str(len(repoResponse.json())) + "\n"
	
	return finalResult
