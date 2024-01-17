#
# spec file for package bumblebee
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           bumblebee
Version:        3.2.1
Release:        0
Summary:        NVidia Optimus support for GNU/Linux aimed at stability
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/Bumblebee-Project/bumblebee
Source0:        http://bumblebee-project.org/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch0:         nvidia-uvm-modeset-drm-support.patch
Patch1:         bumblebee-decimal-pciid.patch
# PATCH-FIX-UPSTREAM
Patch2:         Fix_build_with_GCC10.patch
BuildRequires:  glib2-devel
BuildRequires:  help2man
BuildRequires:  pciutils
BuildRequires:  pkgconfig
BuildRequires:  pwdutils
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  pkgconfig(systemd)
Requires:       VirtualGL
Requires:       pciutils
Requires:       primus
Requires:       shadow
Requires:       sudo
Requires:       xorg-x11-libX11
Recommends:     bbswitch
%{?systemd_requires}
# Always want 32b version on 64b system
%ifarch x86_64
Recommends:     VirtualGL-32bit
%endif
# Always want 32b version on 64b system
%ifarch x86_64
Recommends:     primus-32bit
%endif
%if 0%{?suse_version} < 1315
Requires:       module-init-tools
%else
Requires:       kmod-compat
%endif

%description
The Bumblebee daemon is a rewrite of the original Bumblebee service,
providing a means of managing Optimus hybrid graphics chipsets. This
project not only enables use of the discrete GPU for rendering, but
also smart power management of the dGPU when it is not in use.

%prep
%autosetup -p1

%build
%configure \
	--without-pidfile \
	--with-udev-rules=%{_udevrulesdir}/ \
	CONF_DRIVER_MODULE_NVIDIA=nvidia CONF_LDPATH_NVIDIA=%{_libdir}/nvidia:%{_prefix}/lib/nvidia \
	CONF_MODPATH_NVIDIA=%{_libdir}/nvidia/xorg/,%{_libdir}/xorg/modules \
	CONF_PRIMUS_LD_PATH=%{_libdir}/primus:%{_prefix}/lib/primus

make %{?_smp_mflags}

%install
%make_install
install -d 755 %{buildroot}%{_prefix}/lib/systemd
install -D -m644 "%{_builddir}/%{name}-%{version}/scripts/systemd/bumblebeed.service" "%{buildroot}%{_unitdir}/bumblebeed.service"
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcbumblebeed
# Fix service to run after dkms and modules leading service
sed -i '3i After=dkms.service systemd-modules-load.service' %{buildroot}%{_unitdir}/bumblebeed.service
# according to rpmlint error suse-filelist-forbidden-bashcomp-userdirs
install -d -m 0755 %{buildroot}/%{_datadir}/bash-completion/completions/
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/bumblebee %{buildroot}/%{_datadir}/bash-completion/completions/

%pre
getent group bumblebee >/dev/null || groupadd -r bumblebee
%service_add_pre bumblebeed.service

%post
%udev_rules_update
%service_add_post bumblebeed.service
# Notify user about the groups
mkdir -p %{_localstatedir}/adm/update-messages
cat > %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF
INFO: Please ensure that users using bublebee/video card are in following group(s):
INFO:     gpasswd -a <USER> bumblebee
INFO:   If going to use nvidia binary driver:
INFO:     gpasswd -a <USER> video
INFO: Also ensure the nouveau module is blacklisted (even if you plan to use it):
INFO:     echo "blacklist nouveau" >> %{_sysconfdir}/modprobe.d/50-blacklist.conf
INFO:     mkinitrd
EOF

%preun
%service_del_preun bumblebeed.service

%postun
%service_del_postun bumblebeed.service

%files
%license COPYING
%doc README.markdown
%dir %{_sysconfdir}/bumblebee
%config(noreplace) %{_sysconfdir}/bumblebee/xorg.conf.nouveau
%config(noreplace) %{_sysconfdir}/bumblebee/xorg.conf.nvidia
%config(noreplace) %{_sysconfdir}/bumblebee/bumblebee.conf
%dir %{_sysconfdir}/bumblebee/xorg.conf.d
%config %{_sysconfdir}/bumblebee/xorg.conf.d/10-dummy.conf
%{_unitdir}/bumblebeed.service
%{_sbindir}/rcbumblebeed
%{_udevrulesdir}/99-bumblebee-nvidia-dev.rules
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/bumblebee
%{_datadir}/doc/bumblebee
%{_sbindir}/bumblebeed
%{_bindir}/optirun
%{_bindir}/bumblebee-bugreport
%{_mandir}/man1/bumblebeed.1%{?ext_man}
%{_mandir}/man1/optirun.1%{?ext_man}

%changelog
