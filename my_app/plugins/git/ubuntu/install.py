import json
import subprocess
import urllib.request

lazygit_dest = "/tmp/lazygit"


def install():
    install_lazygit()
    install_git_lfs()


def install_lazygit():
    lazygit_package_url = ""
    lazygit_releases_url = "https://api.github.com/repos/jesseduffield/lazygit/releases/latest"

    with urllib.request.urlopen(lazygit_releases_url) as response:
        json_data = json.loads(response.read().decode())
        lazygit_package_url = get_lazygit_linux_package_url(json_data)

    download_lazygit_linux_package(lazygit_package_url)

    subprocess.run(["tar",  "xf", lazygit_dest + ".tar.gz",  'lazygit'])
    subprocess.run(["mv",  'lazygit', lazygit_dest])
    subprocess.run(["sh", "-c", f'install {lazygit_dest} /usr/local/bin'])


def get_lazygit_linux_package_url(data):
    for asset in data['assets']:
        if asset['browser_download_url'].endswith("_Linux_x86_64.tar.gz"):
            return asset['browser_download_url']


def download_lazygit_linux_package(url: str):
    urllib.request.urlretrieve(url, lazygit_dest + ".tar.gz")


def install_git_lfs():
    subprocess.run([
        "curl", "-s", "https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh", "|", "bash"
    ])
    subprocess.run(["apt-get", "install", "git-lfs"])
