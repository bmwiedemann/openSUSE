if [ "$1" = 0 ] ; then
    # cleanup of bnc# 1000625
    rm -f /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf
    # remove TW Workaround for simpledrm during uninstall (boo#1201392)
    %if 0%{?suse_version} >= 1550
    pbl --del-option nosimplefb=1 --config
    %endif
fi
