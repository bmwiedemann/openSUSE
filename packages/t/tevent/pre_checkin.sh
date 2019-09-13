#!/bin/bash

sed 's/%define.*build_man.*0/%define build_man 1/' tevent.spec > tevent-man.spec
cp -a tevent.changes tevent-man.changes
