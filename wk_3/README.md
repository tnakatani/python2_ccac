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
