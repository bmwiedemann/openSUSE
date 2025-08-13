flavor=%1
%if 0%{?suse_version} >= 1550
modprobedir=%{_prefix}/lib/modprobe.d
%else
modprobedir=%{_sysconfdir}/modprobe.d
%endif

# get rid of rule of older KMPs not to load nvidia_drm module
# which are still installed in parallel and therefore still active;
# see also boo#1247923
if test -f ${modprobedir}/60-nvidia-${flavor}.conf; then
  rm ${modprobedir}/60-nvidia-${flavor}.conf
fi
