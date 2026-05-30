# 📊 repo-stats

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()

> Analyze GitHub repositories and generate beautiful statistics reports.

## ✨ Features

- 📈 **Comprehensive Analysis** - Stars, forks, issues, contributors, languages
- 🎨 **Beautiful Output** - Rich terminal tables and formatting
- 📊 **JSON Export** - Export data for further analysis
- 🔍 **Detailed Insights** - Top contributors, recent commits, language breakdown
- ⚡ **Fast** - Fetches data directly from GitHub API
- 🔧 **CLI Interface** - Easy to use from command line
- 📦 **Pip Installable** - Install with a single command

- 🔄 **Compare Repos** - Compare two repositories side by side
## 📦 Installation

### From PyPI (recommended)

```bash
pip install repo-stats
```

### From source

```bash
git clone https://github.com/Alex-2Code/repo-stats.git
cd repo-stats
pip install -e .
```

## 🔧 Setup

1. Get a GitHub API token from [github.com/settings/tokens](https://github.com/settings/tokens)

2. Set the token (optional but recommended for higher rate limits):

```bash
export GITHUB_TOKEN="ghp_your-token-here"
```

## 🚀 Usage

### Compare Repositories

```bash
# Compare two repositories
repo-stats compare owner/repo1 owner/repo2

# Export comparison to JSON
repo-stats compare owner/repo1 owner/repo2 --format json
```

### Basic Usage

```bash
# Analyze a repository
repo-stats owner/repo

# Analyze using GitHub URL
repo-stats https://github.com/owner/repo

# Export to JSON
repo-stats owner/repo --format json --output report.json
```

### Command Options

```bash
repo-stats [OPTIONS] REPO

Options:
  --version                Show version
  -t, --token TEXT         GitHub API token (or set GITHUB_TOKEN env var)
  -f, --format [text|json] Output format (default: text)
  -c, --contributors INT   Number of top contributors to show (default: 10)
  -n, --commits INT        Number of recent commits to show (default: 5)
  -o, --output TEXT        Output file path (for JSON format)
  --help                   Show this message and exit
```

## 📖 Examples

### Example 1: Basic Analysis

```bash
$ repo-stats facebook/react

📊 Repository: facebook/react

┌─────────────────┬──────────────────────────────────────────┐
│ Property        │ Value                                    │
├─────────────────┼──────────────────────────────────────────┤
│ Description     │ The library for web and native user      │
│                 │ interfaces.                              │
│ ⭐ Stars         │ 230.5K                                   │
│ 🍴 Forks         │ 47.2K                                    │
│ 👀 Watchers      │ 6.8K                                     │
│ 📋 Open Issues   │ 756                                      │
│ 📦 Size          │ 22.5 MB                                  │
│ 🌐 Language      │ JavaScript                               │
│ 📜 License       │ MIT License                              │
│ 📅 Created       │ 2013-05-24                               │
│ 🔄 Updated       │ 2026-05-28                               │
└─────────────────┴──────────────────────────────────────────┘

💻 Languages

┌──────────────┬────────────┬────────────┐
│ Language     │     Bytes  │ Percentage │
├──────────────┼────────────┼────────────┤
│ JavaScript   │    3,245K  │     62.3%  │
│ TypeScript   │    1,892K  │     36.3%  │
│ CSS          │       45K  │      0.9%  │
└──────────────┴────────────┴────────────┘

👥 Top Contributors

┌─────┬─────────────┬───────────────────┐
│   # │ Username    │    Contributions  │
├─────┼─────────────┼───────────────────┤
│   1 │ gaearon     │             1,234 │
│   2 │ sophiebits  │               892 │
└─────┴─────────────┴───────────────────┘
```

### Example 2: JSON Export

```bash
$ repo-stats facebook/react --format json --output react-stats.json

Report saved to react-stats.json
```

### Example 3: Custom Limits

```bash
$ repo-stats facebook/react --contributors 20 --commits 10

# Shows top 20 contributors and 10 recent commits
```

## 📊 Output Formats

### Text Format (default)

Beautiful terminal output with tables and colors.

### JSON Format

```json
{
  "repository": {
    "name": "facebook/react",
    "description": "The library for web and native user interfaces.",
    "stars": 230500,
    "forks": 47200,
    "watchers": 6800,
    "open_issues": 756,
    "size_kb": 23040,
    "language": "JavaScript",
    "license": "MIT License",
    "created_at": "2013-05-24T16:01:50Z",
    "updated_at": "2026-05-28T10:30:00Z",
    "default_branch": "main",
    "url": "https://github.com/facebook/react"
  },
  "languages": {
    "JavaScript": 62.3,
    "TypeScript": 36.3,
    "CSS": 0.9
  },
  "top_contributors": [
    {"username": "gaearon", "contributions": 1234},
    {"username": "sophiebits", "contributions": 892}
  ],
  "recent_commits": [
    {
      "sha": "abc1234",
      "message": "Fix: resolve rendering issue",
      "author": "Dan Abramov",
      "date": "2026-05-28T10:00:00Z"
    }
  ]
}
```

## 🔑 Rate Limits

GitHub API has rate limits:
- **Unauthenticated**: 60 requests/hour
- **Authenticated**: 5,000 requests/hour

For best experience, set `GITHUB_TOKEN` environment variable.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GitHub API](https://docs.github.com/en/rest) for the data
- [Click](https://click.palletsprojects.com/) for the CLI framework
- [Rich](https://rich.readthedocs.io/) for beautiful terminal output

## 📧 Contact

- GitHub: [@Alex-2Code](https://github.com/Alex-2Code)

---

Made with ❤️ by [Alex-2Code](https://github.com/Alex-2Code)

---
<!-- last-updated -->
*Last updated: 2026-05-30*<!-- /last-updated -->
