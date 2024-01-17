#!/bin/bash
# Reset lang list for spec file.
# Usage:
# When build fails on missing on superfluous language packages, call:
# 1. sh ./translation-update-reset-lang-list.sh
# 2. osc build # it will fail
# 3. sh ./translation-update-generate-lang-list.sh

grep %package *.spec | sed 's/%package -n //' | LANG=C sort -u >pkglist-pre.lst
sed -i '
/^%package -n/,/^%prep$/c \
%prep

/^%files -n/,/^%changelog$/c \
%changelog
' translation-update.spec
