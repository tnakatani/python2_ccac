# On Git

## 3 Regions in a Git Repo

1. Working Directory - The only human-viewable component of git
2. Staging Area - Add files to this individually with ```git add [file]``` or, in root directory ```git add .```
3. Index - Where commited files are stored in a tree structure

## Merging

Merge operation is, "grab changes from anotehr branch, and integrate into my own branch"

1. Checkout the branch in which you wish to merge your changes
2. Run ```git merge [branch or commit name]``` 
3. Best scenario: changes are synchronized, and new commit will automatically be added to file history.
  - if conflicts exists, a merge operation will appear

## Fetch / Merge / Pull

```git fetch``` retrieves all commits on a given branch from a remote repo and those changes will be stored in the remote tracking branch named by default ```[remote_repo_name]/[branch_name]```.

A remote tracking is special, because we never manually change with the remote tracking branch -- it's a local branch designed to synchronize with the remote, allowing for a controlled merge into any other specified branch.

A ```git pull``` automatically updates the remote tracking branch AND merges those changes into your current branch without asking.

Best practice: Get in the habit of separately running ```git fetch``` and ```git pull```.
