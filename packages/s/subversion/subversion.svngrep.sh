#!/bin/sh
find \( -path '*/.pc' -o -path '*/.svn' -o -path '*/.git' -o -path '*/.hg' \) -prune -o -type f -print0 | xargs -0 grep "$@"
