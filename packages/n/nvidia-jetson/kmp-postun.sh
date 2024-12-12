flavor=%1

if [ "$1" = 0 ] ; then
    # cleanup of bnc# 1000625
    rm -f /usr/lib/tmpfiles.d/nvidia-logind-acl-trick-G06.conf
fi

# Cleanup after uninstallation
%systemd_postun_with_restart load-nvidia-drm-${flavor}.service
