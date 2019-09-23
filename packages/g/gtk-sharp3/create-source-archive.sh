#!/bin/bash
#

git_commit_fallback="master"
git_commit="$1"
name="gtk-sharp3"
git_remote="https://github.com/mono/gtk-sharp.git"

script_dir="$( cd "$( dirname "$0" )" && pwd )"
repo_dir="$name-tmp"
[[ -z $git_commit ]] && git_commit="$git_commit_fallback"

set -e

cd "$script_dir"
mkdir -p "$repo_dir"
cd "$repo_dir"
git init
git remote add ext "$git_remote"

echo "fetching"
git fetch -f --all
git checkout -f "$git_commit" || git_commit_failed="true"

if [[ $git_commit_failed = true ]]; then
  echo "failed to checkout requested commit, trying to use branch $git_commit instead"
  git branch -f "temp" "ext/$git_commit"
  git checkout -f "temp"
  git_commit=`git rev-parse HEAD`
fi

cdate=`git show -s --format=%ci $git_commit | cut -d' ' -f 1 | sed 's|-|.|g'`
hash=`git show -s --format=%h $git_commit`
repo_dir_r="$name-git.$cdate.$hash"

git submodule update --init
rm -rf .git
rm -f .gitattributes
rm -f .gitignore
rm -f .gitmodules
cd "$script_dir"
mv "$repo_dir" "$repo_dir_r"
tar cf "$repo_dir_r.tar" "$repo_dir_r" --owner=0 --group=0
rm -fv "$repo_dir_r.tar.xz"
xz -9e "$repo_dir_r.tar"
rm -rf "$repo_dir_r"
