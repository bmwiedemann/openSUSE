if [ "$1" = 0 ] ; then
    # remove Workaround needed to disable ast driver broken on aarch64
    pbl --del-option modprobe.blacklist=ast --config
    # remove plymouth Workaround needed to not hang serial console with
    # no monitor connected ...
    pbl --del-option plymouth.enable=0 --config
    # remove Workaround to prevent fatal "watchdog: BUG: soft lockup"
    # issue, which made it necessary to reboot the machine ...
    pbl --del-option preempt=full --config
fi
