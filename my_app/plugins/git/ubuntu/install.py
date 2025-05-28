import subprocess


def install():
    steps = [
        ["sudo", "apt", "install", "lazygit"]
    ]

    for step in steps:
        subprocess.run(step)
