from github import Github
from apikey import API_KEY
import numpy as np
import os 
import xlsxwriter


# API_KEY = os.environ["API_KEY"]

# Create a new Github object using your API token
gh = Github(API_KEY)

# Get the user object for the specified user
user = gh.get_user("ImanSM")

# Get a list of repositories for the user


# Print the names of the repositories
num_pages = user.get_repos().totalCount // 30 + 1



# Create an empty array with the same number of rows as the total number of repositories
# and 2 columns: the first column will store the repository name and the second column will
# store the list of topics for the repository
arr = np.empty((user.get_repos().totalCount, 2), dtype=object)

# Iterate through the list of repositories
for i in range(num_pages):
    repos = user.get_repos().get_page(i)
    repos = [repo for repo in repos if not repo.archived]
    for i, repo in enumerate(repos):
        # Get the list of topics for the repository
        topics = repo.get_topics()
        topics_str = ", ".join(topics)
        # Store the repository name and its topics in the array
        arr[i, 0] = repo.name
        arr[i, 1] = topics_str

# Print the array
print(arr)

# Create a new workbook object
workbook = xlsxwriter.Workbook('repos2.xlsx')

# Create a new worksheet object
worksheet = workbook.add_worksheet('repos and tags')

# Set the column width for the first and second columns
worksheet.set_column(0, 0, 30)
worksheet.set_column(1, 1, 50)

# Add the header row
worksheet.write(0, 0, "Repository Name")
worksheet.write(0, 1, "Topics")

# Iterate through the array and write each row to the worksheet
for i, row in enumerate(arr):
    worksheet.write(i+1, 0, row[0])
    worksheet.write(i+1, 1, row[1])

# Close the workbook
workbook.close()






