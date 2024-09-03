# Workaround needed to disable ast driver broken on aarch64
pbl --add-option modprobe.blacklist=ast --config

# serial console hangs with plymouth spending 100% CPU load if no
# monitor is connected, so better disable plymouth; it never showed a logo
# on Jetson anyway ...
pbl --add-option plymouth.enable=0 --config

# prevent fatal "watchdog: BUG: soft lockup" issue, which made it
# necessary to reboot the machine ...
pbl --add-option preempt=full --config

# With newer kernels the hand-off of the frame-buffer from simple-drm
# to the NVIDIA display driver does not work and hence this needs to be
# disabled. It's tracked on NVIDIA side, but there is no ETA for fixing
# available. For now it is fine to set this configuration. Unfortunately,
# this needs to be done each time one upgrades the firmware. There is no
# way to configure this at flash time, but one can configure this via sysfs.
#
# The values that we can write to this variable are ...
#
# #define NVIDIA_SOC_DISPLAY_HANDOFF_MODE_NEVER   0
# #define NVIDIA_SOC_DISPLAY_HANDOFF_MODE_ALWAYS  1
# #define NVIDIA_SOC_DISPLAY_HANDOFF_MODE_AUTO    2
#
# These are defined here:
# https://github.com/NVIDIA/edk2-nvidia/blob/main/Silicon/NVIDIA/Include/NVIDIAConfiguration.h#L50
# So we want to switch from '2' (auto) to '0' (never). 

file=/sys/firmware/efi/efivars/SocDisplayHandoffMode-781e084c-a330-417c-b678-38e696380cb9
if test -f $file; then
  hexdump $file | head -n 1 | grep -q "0000000 0007 0000 0000"
  if test $? -ne 0; then
    chattr -i $file
    printf '\x07\x00\x00\x00\x00' | tee $file
  fi
fi

