#!/bin/bash
for lang in $(ls -N openSUSE-welcome/data/i18n/qml_*.po | grep -o "_.*\.po" | sed -e "s/^_//" -e "s/\.po$//"); do echo "Recommends: (opensuse-welcome-lang if namespace:language($lang))"; done
