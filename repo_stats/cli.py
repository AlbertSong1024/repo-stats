"""CLI interface for repo-stats."""

import json
import os
import sys

import click
from rich.console import Console
from rich.panel import Panel

from . import __version__
from .core import (
    display_contributors,
    display_languages,
    display_recent_commits,
    display_repo_info,
    fetch_commit_activity,
    fetch_contributors,
    fetch_languages,
    fetch_recent_commits,
    fetch_repo_info,
    generate_json_report,
)

console = Console()


def parse_repo_input(repo_input: str) -> tuple:
    """Parse repository input (owner/repo or URL)."""
    # Handle GitHub URLs
    if "github.com" in repo_input:
        parts = repo_input.rstrip("/").split("/")
        if len(parts) >= 2:
            return parts[-2], parts[-1]

    # Handle owner/repo format
    if "/" in repo_input:
        owner, repo = repo_input.split("/", 1)
        return owner, repo

    console.print("[red]Error: Invalid repository format. Use 'owner/repo' or GitHub URL.[/red]")
    sys.exit(1)


@click.command()
@click.version_option(version=__version__, prog_name="repo-stats")
@click.argument("repo")
@click.option(
    "--token", "-t",
    default=None,
    help="GitHub API token (or set GITHUB_TOKEN env var)",
)
@click.option(
    "--format", "-f",
    type=click.Choice(["text", "json"]),
    default="text",
    help="Output format (default: text)",
)
@click.option(
    "--contributors", "-c",
    default=10,
    help="Number of top contributors to show (default: 10)",
)
@click.option(
    "--commits", "-n",
    default=5,
    help="Number of recent commits to show (default: 5)",
)
@click.option(
    "--output", "-o",
    default=None,
    help="Output file path (for JSON format)",
)
def main(
    repo: str,
    token: str,
    format: str,
    contributors: int,
    commits: int,
    output: str,
):
    """Analyze GitHub repositories and generate statistics reports.

    Examples:

        repo-stats owner/repo

        repo-stats https://github.com/owner/repo

        repo-stats owner/repo --format json

        repo-stats owner/repo --output report.json
    """
    # Get token from env if not provided
    if not token:
        token = os.environ.get("GITHUB_TOKEN")

    # Parse repository input
    owner, repo_name = parse_repo_input(repo)

    console.print(f"\n[bold blue]Analyzing repository: {owner}/{repo_name}[/bold blue]\n")

    # Fetch data with loading indicator
    with console.status("[bold green]Fetching repository data..."):
        try:
            info = fetch_repo_info(owner, repo_name, token)
            languages = fetch_languages(owner, repo_name, token)
            top_contributors = fetch_contributors(owner, repo_name, token, contributors)
            recent_commits = fetch_recent_commits(owner, repo_name, token, commits)
        except Exception as e:
            console.print(f"[red]Error fetching data: {e}[/red]")
            sys.exit(1)

    # Output format
    if format == "json":
        report = generate_json_report(info, languages, top_contributors, recent_commits)

        if output:
            with open(output, "w") as f:
                json.dump(report, f, indent=2)
            console.print(f"[green]Report saved to {output}[/green]")
        else:
            console.print_json(json.dumps(report, indent=2))
    else:
        # Display text format
        console.print()
        display_repo_info(info)
        console.print()
        display_languages(languages)
        console.print()
        display_contributors(top_contributors)
        console.print()
        display_recent_commits(recent_commits)

        # Summary panel
        console.print()
        summary = f"""[bold]Repository Analysis Complete![/bold]

📊 Total Stars: {info['stargazers_count']:,}
🍴 Total Forks: {info['forks_count']:,}
💻 Primary Language: {info.get('language', 'N/A')}
👥 Contributors: {len(top_contributors):,}
🔗 URL: {info['html_url']}"""
        console.print(Panel(summary, title="Summary", border_style="green"))


if __name__ == "__main__":
    main()
