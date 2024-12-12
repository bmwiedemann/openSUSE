flavor=%1

# Stop and disable the service before removal
%systemd_preun load-nvidia-drm-${flavor}.service
