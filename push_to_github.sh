#!/bin/bash

# Remove existing remote if it exists
git remote remove origin 2>/dev/null

# Set the branch to main
git branch -M main

# Add the new remote with SSH
git remote add origin git@github.com:g-k-virdi/portfolio-website.git

# Push to GitHub
git push -u origin main 