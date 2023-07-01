# Reddit Backups

Backups for various reddit communities.

## Backup Script

There is a backup script for Lemmy compatibility found at `/src/reddit-export.py`. The script will pull subreddit data from the [pushshift.io](https://pushshift.io) API. You will need to manually edit this script until environment variables are implemented. The script inserts data into a mongo database `mongodb://localhost:27017`.

```bash
# Change directory into project
cd reddit-backups
# Create environment file
cp .env.example .env
# Install requirements
pyenv install
# Change into shell
pyenv shell
# Run Script
python ./src/reddit-export.py
```

## /r/usenet

[/r/usenet docs](./docs/usenet/README.md)
