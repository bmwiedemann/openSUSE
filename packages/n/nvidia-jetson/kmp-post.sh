flavor=%1

# Create symlinks for udev so these devices will get user ACLs by logind later (bnc#1000625)
mkdir -p /run/udev/static_node-tags/uaccess
mkdir -p /usr/lib/tmpfiles.d
ln -snf /dev/nvidia-modeset /run/udev/static_node-tags/uaccess/nvidia-modeset
ln -snf /dev/nvidiactl      /run/udev/static_node-tags/uaccess/nvidiactl
ln -snf /dev/nvidia0        /run/udev/static_node-tags/uaccess/nvidia0
cat >  /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf << EOF
L /run/udev/static_node-tags/uaccess/nvidia-modeset - - - - /dev/nvidia-modeset
L /run/udev/static_node-tags/uaccess/nvidiactl - - - - /dev/nvidiactl
L /run/udev/static_node-tags/uaccess/nvidia0 - - - - /dev/nvidia0
EOF

# needs to be hardcoded so it's already known in initrd
GID=$(getent group video | cut -d: -f3)
sed -i "s/REALGID/$GID/" /lib/modprobe.d/50-nvidia-$flavor.conf

# IGX needs 0 for modeset
if dmidecode |grep "Product Name"|grep -q IGX; then
  sed -i "s/modeset=1/modeset=0/" /lib/modprobe.d/50-nvidia-$flavor.conf
fi

# Preset the service to follow the system's policy
%systemd_post load-nvidia-drm-${flavor}.service
# the official way above doesn't seem to work ;-(
/usr/bin/systemctl preset load-nvidia-drm-${flavor}.service
