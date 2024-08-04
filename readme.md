# Process and Update Submissions

This project automates the processing and updating of Markdown table links in a `submissions.md` file. The script converts plain URL text into clickable links and integrates with GitHub Actions for continuous deployment.

## Features

- **Automated Link Conversion**: Converts plain URLs in Markdown tables into clickable links.
- **Continuous Deployment**: Uses GitHub Actions to automatically run the script and commit changes on every push to the master branch.

## File Structure

```plaintext
docs/
├── submissions.md
├── submissions.py
.github/
└── workflows/
    └── submissions.yml
requirement.txt
readme.md