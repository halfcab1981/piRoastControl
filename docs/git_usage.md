# Git Usage Guide

## Initial Setup

1. Open Terminal in your project folder.
2. Type `git init` to start a new Git repository.
3. Type `git config --global user.name "Your Name"` to set your name.
4. Type `git config --global user.email "your.email@example.com"` to set your email.

## Basic Workflow

### Checking Status
- Type `git status` to see which files have changed.

### Adding Changes
- Type `git add filename` to stage a specific file.
- Type `git add .` to stage all changed files.

### Committing Changes
- Type `git commit -m "Your message here"` to commit staged changes.

### Viewing History
- Type `git log` to see commit history.

## Branching

### Creating a New Branch
- Type `git branch branch-name` to create a new branch.
- Type `git checkout -b branch-name` to create and switch to a new branch.

### Switching Branches
- Type `git checkout branch-name` to switch to an existing branch.

### Merging Branches
1. Switch to the branch you want to merge into (usually main).
2. Type `git merge branch-name` to merge changes from another branch.

## Remote Repositories

### Adding a Remote
- Type `git remote add origin https://github.com/username/repo-name.git`

### Pushing Changes
- Type `git push -u origin branch-name` for the first push of a branch.
- For subsequent pushes, just type `git push`.

### Pulling Changes
- Type `git pull` to fetch and merge changes from the remote.

## Other Useful Commands

### Discarding Changes
- Type `git checkout -- filename` to discard changes in a file.

### Creating Tags
- Type `git tag v1.0.0` to create a tag for the current commit.

### Viewing Differences
- Type `git diff` to see changes before staging.

Remember, always commit your changes before switching branches or pulling from remote!