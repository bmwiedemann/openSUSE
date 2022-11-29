if test "$(id -u)" -gt "0" && test -d "$HOME"; then
    if test ! -e "$HOME"/.config/containers/storage.conf && \
            test ! -e "$HOME"/.local/share/containers/storage/libpod && \
            grep -qx "driver = .*btrfs.*" /etc/containers/storage.conf ; then
        if test "$(findmnt -o FSTYPE -l --target "$HOME" | grep -v FSTYPE)" != "btrfs"; then
            # Home partition is not btrfs, but system wide setting is to use btrfs, this won't work
            # default to 'overlay' then
            export STORAGE_DRIVER=overlay
        fi
    fi
fi
