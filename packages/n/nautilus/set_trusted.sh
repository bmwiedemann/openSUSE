#!/bin/bash

DIR=$HOME/Desktop

for f in $(ls $DIR)
do
    gio set -t string $DIR/$f "metadata::trusted" true
done

if [ -f $HOME/.config/autostart/set_trusted.desktop ]; then
    rm $HOME/.config/autostart/set_trusted.desktop
fi

