
url = input("Please enter a URL starting with http://www.: ")

url = url.replace("http://www.", "", 1)

user_url = url.split("/")[0]

user_url += ".com"
print("Converted URL: ", user_url)
