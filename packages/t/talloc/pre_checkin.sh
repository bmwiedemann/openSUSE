#!/bin/bash

sed 's/%define.*build_man.*0/%define build_man 1/' talloc.spec > talloc-man.spec
cp -a talloc.changes talloc-man.changes
