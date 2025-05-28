import subprocess


def install():
    steps = [
        ["dnf", "copr", "enable", "atim/lazygit", "-y"],
        ["dnf", "-qy", "install", "git", "lazygit"],
        ["dnf", "-qy", "install", "git-lfs"],
    ]

    for step in steps:
        subprocess.run(step)
