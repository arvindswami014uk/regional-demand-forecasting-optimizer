REPO_PATH = "/content/regional-demand-forecasting-optimizer"
GITHUB_BASE = "https://raw.githubusercontent.com/arvindswami014uk/regional-demand-forecasting-optimizer/main"

import os
import subprocess
from getpass import getpass

def run_cmd(cmd, label="command", cwd=REPO_PATH):
    print(f"[CMD] {label}: {cmd}")
    result = subprocess.run(
        cmd,
        shell=True,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"Command failed for {label}: {cmd}")
    return result

def main():
    if not os.path.exists(REPO_PATH):
        raise FileNotFoundError(f"Repo path not found: {REPO_PATH}")

    print("============================================================")
    print("DAY 11 GITHUB PUSH HELPER")
    print("Repo:", REPO_PATH)
    print("============================================================")

    github_username = "arvindswami014uk"
    git_name = input("Enter git user.name (example: Arvind Swami): ").strip()
    git_email = input("Enter git user.email: ").strip()
    github_token = getpass("Enter GitHub Personal Access Token: ").strip()

    if not git_name:
        raise ValueError("git user.name cannot be empty")
    if not git_email:
        raise ValueError("git user.email cannot be empty")
    if not github_token:
        raise ValueError("GitHub token cannot be empty")

    clean_remote = f"https://github.com/{github_username}/regional-demand-forecasting-optimizer.git"
    authed_remote = f"https://{github_username}:{github_token}@github.com/{github_username}/regional-demand-forecasting-optimizer.git"

    run_cmd(f'git config user.name "{git_name}"', label="set local git user.name", cwd=REPO_PATH)
    run_cmd(f'git config user.email "{git_email}"', label="set local git user.email", cwd=REPO_PATH)

    run_cmd("git status", label="git status before add", cwd=REPO_PATH)
    run_cmd("git add .", label="git add", cwd=REPO_PATH)

    try:
        run_cmd(
            'git commit -m "Day 11: green-fast fulfillment layer, carbon proxy, scenarios, and governance outputs"',
            label="git commit",
            cwd=REPO_PATH
        )
    except Exception as e:
        print("Commit may have been skipped because there were no new changes.")
        print(e)

    run_cmd(f'git remote set-url origin "{authed_remote}"', label="set authenticated remote", cwd=REPO_PATH)
    run_cmd("git push origin main", label="git push origin main", cwd=REPO_PATH)
    run_cmd(f'git remote set-url origin "{clean_remote}"', label="reset clean remote", cwd=REPO_PATH)

    print("============================================================")
    print("Push complete.")
    print("Remote reset to clean HTTPS URL.")
    print("============================================================")

if __name__ == "__main__":
    main()