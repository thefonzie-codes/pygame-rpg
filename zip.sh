#!/bin/bash

# Script to create a zip archive excluding files from .gitignore
# Usage: ./git-archive.sh [archive_name.zip]

# Check if we're in a git repository
if ! git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
  echo "Error: Not in a git repository"
  exit 1
fi

# Get the root directory of the git repository
GIT_ROOT=$(git rev-parse --show-toplevel)
cd "$GIT_ROOT" || exit 1

# Get the base name of the repository
REPO_NAME=$(basename "$GIT_ROOT")

# If no argument provided, prompt for suffix
if [ -z "$1" ]; then
  read -p "Enter archive name suffix (without .zip): " SUFFIX
  ARCHIVE_NAME="${REPO_NAME}_${SUFFIX}.zip"
else
  ARCHIVE_NAME="$1"
fi

# Check if archive name ends with .zip, if not append it
if [[ "$ARCHIVE_NAME" != *.zip ]]; then
  ARCHIVE_NAME="${ARCHIVE_NAME}.zip"
fi

echo "Creating archive: $ARCHIVE_NAME"

# Use git ls-files to get a list of tracked files and non-ignored untracked files
FILES=$(git ls-files --cached --others --exclude-standard)

# Create a temporary file listing
TMP_FILE=$(mktemp)
echo "$FILES" > "$TMP_FILE"

# Create the zip archive
zip -r "$ARCHIVE_NAME" -@ < "$TMP_FILE"

# Clean up
rm "$TMP_FILE"

echo "Archive created successfully: $ARCHIVE_NAME"