# studying git and git hub

command1 = 'get init'
new_repo = command1

# When you run command1, Git will create a new directory named .git in your project folder. 
# This directory contains all the information about your project's history and configuration.

command2 = 'git remote add origin '

repo_url = 'repository url.git'
connect_local_remote = command2 + repo_url

# We need to connect our local repository (folder on our computer) with our remote repository (the link on GitHub). 
# We use the 'remote add' command.

command3 = 'git branch -M main'

# We rename the branch to main using command3.
# This will be the branch we push code to, and will be default branch. 

command4 = 'git add'
command5 = 'git commit '

# Command4 tells git that 'I'm getting ready to go online!'
# It's a temporary area where you pick and choose what files you want to "commit", or send to the remote repository.
# Variation includes: git add .           (will add all the changed files to the staging area.)
#                     git add example.txt (will add the single file to the staging area, especially in cases you only want one of your working files to appear on GitHub)
#                     git add *.html      (will only stage files with a specified extension.)

# Committing files (command5) are about sharing the current code as a "snapshot" that GitHub online has access to. It likes saving our progress.
# It allows us to add helpful messages so we know and keep track of changes. Example:

the_message = 'Initial commit'
to_commit = command5 + '-m ' + the_message

