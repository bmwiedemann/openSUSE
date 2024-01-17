#!/bin/bash
# This script should be called before checkin.
sed -e 's/%bcond_with mini/%bcond_without mini/' \
    -e '/^Name:/s/$/-mini/' \
  gettext-runtime.spec > gettext-runtime-mini.spec
cp gettext-runtime.changes gettext-runtime-mini.changes
