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
arr = np.empty((user.get_repos().totalCount, 3), dtype=object)

# Iterate through the list of repositories
for i in range(num_pages):
    repos = user.get_repos().get_page(i)
    repos = [repo for repo in repos if not repo.archived]

    for i, repo in enumerate(repos):
        # Get the list of topics for the repository
        pull_requests = repo.get_pulls()
        num_pulls = pull_requests.totalCount
        

        if num_pulls > 0:
            last_pull_request = None
            for pull_request in pull_requests:
                last_pull_request = pull_request
            last_pull_request_date = last_pull_request.created_at
        else:
            last_pull_request_date = "No pull requests found"
        
        if isinstance(last_pull_request_date, str):
        # Return the last pull request date as is if it is a string
            last_pull_request_date_str = last_pull_request_date
        else:
        # Convert the last pull request date to a datetime object and format it if it is not a string
            last_pull_request_date_str = last_pull_request_date.strftime("%Y-%m-%d %H:%M:%S")
      
        # Store the repository name and its topics in the array
        arr[i, 0] = repo.name
        arr[i, 1] = num_pulls
        arr[i, 2] = last_pull_request_date_str

# Print the array
print(arr)

# Create a new workbook object
workbook = xlsxwriter.Workbook('PRcount.xlsx')

# Create a new worksheet object
worksheet = workbook.add_worksheet('repos and PRs')

# Set the column width for the first and second columns
worksheet.set_column(0, 0, 30)
worksheet.set_column(1, 1, 50)
worksheet.set_column(2, 2, 100)

# Add the header row
worksheet.write(0, 0, "Repository Name")
worksheet.write(0, 1, "# of Pulls")
worksheet.write(0, 2, "Last Commit")

# Iterate through the array and write each row to the worksheet
for i, row in enumerate(arr):
    worksheet.write(i+1, 0, row[0])
    worksheet.write(i+1, 1, row[1])
    worksheet.write(i+1, 2, row[2])

# Close the workbook
workbook.close()






