#!/usr/bin/env python
import re
import os
import git
import argparse
import subprocess
from pathlib import Path
from git import Repo

tg_owt_url = 'https://github.com/desktop-app/tg_owt.git'
repo_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tg_owt-master")

def clone_repo(git_url, repo_dir):
    try:
        repo = Repo(repo_dir)
    except (git.exc.GitCommandError, git.exc.NoSuchPathError):
        Repo.clone_from(git_url, repo_dir)
        repo = Repo(repo_dir)
    return repo

def load_submodules(repo):
    for sms in repo.submodules:
        sms.update(init=True)

#def find_pipewire_path(repo):
#    "Return the relative path of pipewire (relative to repo path)"
#    sms = map(lambda x: x.name, repo.submodules)
#    sms = filter(lambda x: "pipewire" in x, sms)
#    sms = list(sms)
#    assert len(sms) == 1, f"find more than 1 pipewire submodule: {sms}"
#    return sms[0]
#
#def find_pipewire_ver(pipeware_path):
#    pw_build_file = os.path.join(pipeware_path, "meson.build")
#    with open(pw_build_file, "r") as pf:
#        pw_build = list(map(lambda x: x.strip(), pf.read().splitlines()))
#    version_re = "^version : '([0-9]+)\.([0-9]+)\.([0-9]+)',"
#    apiver_re = "^apiversion = '([0-9.]+)'"
#    ver_line = list(filter(lambda x: re.match(version_re, x), pw_build))
#    apiver_line = list(filter(lambda x: re.match(apiver_re, x), pw_build))
#    assert len(ver_line) == 1, f"Found more than one version line: {ver_line}"
#    assert len(apiver_line) == 1, f"Found more than one apiversion line: {apiver_line}"
#    ver  = re.match(version_re, ver_line[0]).groups()
#    api_ver  = re.match(apiver_re, apiver_line[0]).groups()[0]
#    return ver, api_ver
#
#def gen_pipewire_version_header(pipewire_path, pw_ver, pw_apiver):
#    pw_ver_major, pw_ver_minor, pw_ver_micro = pw_ver
#    replace_map = {
#        '@PIPEWIRE_API_VERSION@': pw_apiver,
#        '@PIPEWIRE_VERSION_MAJOR@': pw_ver_major,
#        '@PIPEWIRE_VERSION_MINOR@': pw_ver_minor,
#        '@PIPEWIRE_VERSION_MICRO@': pw_ver_micro,
#    }
#    part_header_file = os.path.join(pipewire_path, "src", "pipewire", "version.h.in")
#    with open(part_header_file, "r") as phf:
#        part_header = phf.read()
#    for k, v in replace_map.items():
#        part_header = part_header.replace(k, v)
#    header_file = os.path.join(pipewire_path, "src", "pipewire", "version.h")
#    with open(header_file, "w") as hf:
#        hf.write(part_header)

def compress_package(repo_dir):
    basename = os.path.basename(repo_dir)
    zipname = basename + ".zip"
    path = Path(repo_dir).parent
    command = ['zip', zipname, '-r', basename, '-x', '*.git*']
    subprocess.check_call(command, cwd=path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Package tg_owt for telegram-desktop build.")
    parser.add_argument('--repo-dir', required=True, help="Specify path to clone tg_owt master branch.")
    args = parser.parse_args()

    repo_dir = args.repo_dir
    repo = clone_repo(tg_owt_url, repo_dir)
    load_submodules(repo)
#    pipewire_path = find_pipewire_path(repo)
#    pipewire_path = os.path.join(repo_dir, pipewire_path)
#    pw_ver, pw_apiver = find_pipewire_ver(pipewire_path)
#    gen_pipewire_version_header(pipewire_path, pw_ver, pw_apiver)
    compress_package(repo_dir)
