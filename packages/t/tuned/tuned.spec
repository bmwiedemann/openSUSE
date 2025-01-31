#
# spec file for package tuned
#
# Copyright (c) 2025 SUSE LLC
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


%define         system_dir %{_prefix}/lib/%{name}/
%define         profile_dir %{system_dir}profiles/
Name:           tuned
Version:        2.24.1.50+git.13dfc68
Release:        0
Summary:        A dynamic adaptive system tuning daemon
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/redhat-performance/tuned
Source0:        tuned-%{version}.tar.xz
Source1:        tuned.rpmlintrc
# PATCH-FIX-OPENSUSE fix-allow-receive_sender-default.patch <allow receive_sender="com.redhat.com"/> allow receive_* is normally
# not needed as that is the default --<p.drouand@gmail.com>
Patch0:         fix-allow-receive_sender-default.patch
Patch1:         0001-tuned-consts-Fix-grub.cfg-path-in-SLE.patch
BuildRequires:  bash-completion
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-dbus-python
# needed by check section
BuildRequires:  python3-pyudev
BuildRequires:  pkgconfig(systemd)
# need perf_bias now
Requires:       ethtool
Requires:       gawk
Requires:       hdparm
Requires:       polkit
Requires:       python3-configobj
Requires:       python3-dbus-python
Requires:       python3-decorator
Requires:       python3-linux-procfs
Requires:       python3-pyinotify
Requires:       python3-pyudev
Requires:       util-linux
Requires:       virt-what
Conflicts:      laptop-mode-tools
Conflicts:      tlp
BuildArch:      noarch
%{?systemd_requires}

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%package utils
Summary:        Disk and net statistic monitoring systemtap scripts
Group:          System/Base
Requires:       %{name} = %{version}
Requires:       powertop

%description utils
This package contains utilities that can help you to fine tune your
system and manage tuned profiles.

%package utils-systemtap
Summary:        Disk and net statistic monitoring systemtap scripts
Group:          System/Base
Requires:       %{name} = %{version}
Requires:       systemtap

%description utils-systemtap
This package contains several systemtap scripts to allow detailed
manual monitoring of the system. Instead of the typical IO/sec it collects
minimal, maximal and average time between operations to be able to
identify applications that behave power inefficient (many small operations
instead of fewer large ones).

%package gtk
Summary:        Disk and net statistic monitoring systemtap scripts - GTK GUI
Group:          System/Base
Requires:       %{name} = %{version}
Requires:       powertop
Requires:       python3-gobject

%description gtk
GTK GUI that can control tuned and provide simple profile editor.

%package profiles-atomic
Summary:        Additional tuned profiles targeted to Atomic
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-atomic
Additional profile(s) for the tuned daemon, targeted to Atomic host and guest.

%package profiles-nfv
Summary:        Additional tuned profiles targeted to Network Function Virtualization (NFV)
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-nfv
Additional profile(s) for the tuned daemon, targeted to Network Function Virtualization (NFV).

%package profiles-openshift
Summary:        Additional tuned profile(s) optimized for the OpenShift platform
Requires:       %{name} = %{version}

%description profiles-openshift
Additional 3 profiles for the Openshift platform:
A parent profile containing tuning shared by OpenShift control plane and worker nodes.
One profile optimized for OpenShift control plane.
And a third profile optimized for general workloads on OpenShift worker nodes.

%package profiles-oracle
Summary:        Additional tuned profiles targeted to Oracle loads
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-oracle
Additional profile(s) for the tuned daemon,  targeted to Oracle loads.

%package profiles-postgresql
Summary:        Additional tuned profile(s) targeted to PostgreSQL server loads
Requires:       %{name} = %{version}

%description profiles-postgresql
Additional tuned profile(s) targeted to PostgreSQL server loads.

%package profiles-realtime
Summary:        Additional tuned profiles targeted to realtime
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-realtime
Additional profile(s) for the tuned daemon, targeted to realtime.

# Do not ship SAP profiles for SLE and Leap, there are other packages
# providing these profiles (starting with ALP these are included again)
%if !0%{?sle_version} || %{?suse_version} >= 1599
%package profiles-sap
Summary:        Additional tuned profile(s) targeted to SAP NetWeaver loads
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-sap
Additional profile(s) for the tuned daemon, targeted to SAP NetWeaver loads.

%package profiles-sap-hana
Summary:        Additional tuned profile(s) targeted to SAP HANA loads
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-sap-hana
Additional profile(s) for the tuned daemon, targeted to SAP HANA loads.
%endif

%package profiles-spectrumscale
Summary:        Additional tuned profile(s) optimized for IBM Spectrum Scale
Requires:       %{name} = %{version}

%description profiles-spectrumscale
Additional tuned profile(s) optimized for IBM Spectrum Scale.

%package ppd
Summary:        PPD compatibility daemon
Requires:       %{name} = %{version}
Conflicts:      ppd-service
# The compatibility daemon is swappable for power-profiles-daemon
Provides:       ppd-service

%description ppd
An API translation daemon that allows applications to easily transition
to TuneD from power-profiles-daemon (PPD).

%prep
%autosetup -p1

%build
# The tuned daemon is written in pure Python. Nothing requires to be built.
# Just a hack to avoid installation in a wrong directory
sed -i 's|usr/libexec/tuned|%{system_dir}|' Makefile
sed -i 's|$(SYSCONFDIR)/modprobe.d|%{_modprobedir}|' Makefile
sed -i 's|$(SYSCONFDIR)/dbus-1/system.d|%{_datadir}/dbus-1/system.d|' Makefile

%install
%make_install TUNED_PROFILES_DIR=%{profile_dir}
make install-ppd DESTDIR=%{buildroot} TUNED_PROFILES_DIR=%{profile_dir}
# we do not have the python perf module (see bsc #1217758)
rm %{buildroot}/%{python3_sitelib}/tuned/plugins/plugin_{scheduler,irqbalance}.py
%py3_compile %{buildroot}/%{python3_sitelib}
rm -rf %{buildroot}/%{_datadir}/doc
# Remove unwanted stuff instead of excluding them in files list
rm -rf %{buildroot}%{profile_dir}/{default,desktop-powersave,laptop-ac-powersave,server-powersave,laptop-battery-powersave,enterprise-storage,spindown-disk}
rm %{buildroot}%{_mandir}/man7/tuned-profiles-compat.7
%if 0%{?suse_version} < 1600
ln -sf service %{buildroot}%{_sbindir}/rctuned
%endif

%if 0%{?sle_version} && %{?suse_version} < 1599
rm -r %{buildroot}%{profile_dir}/sap-netweaver
rm -r %{buildroot}%{profile_dir}/sap-hana
rm %{buildroot}%{_mandir}/man7/tuned-profiles-sap.7
rm %{buildroot}%{_mandir}/man7/tuned-profiles-sap-hana.7
%endif

%check
make test PYTHON=python3

%post
%tmpfiles_create %{name}.conf
%systemd_post %{name}.service

# migrate all user-defined profiles from /etc/tuned/ to /etc/tuned/profiles/
for f in %{_sysconfdir}/tuned/*; do
  if [ -e "$f/tuned.conf" ]; then
    mv -n "$f" %{_sysconfdir}/tuned/profiles/
  fi
done

%post ppd
%systemd_post %{name}-ppd.service

%pre
%systemd_pre %{name}.service
# Avoid restoring outdated stuff in posttrans
[ ! -f "%{_sysconfdir}/modprobe.d/tuned.conf.rpmsave" ] || \
  mv -f "%{_sysconfdir}/modprobe.d/tuned.conf.rpmsave" "%{_sysconfdir}/modprobe.d/tuned.conf.rpmsave.old" || :

%pre ppd
%systemd_pre %{name}-ppd.service

%posttrans
# Migration of modprobe.conf files to _modprobedir
[ ! -f "%{_sysconfdir}/modprobe.d/tuned.conf.rpmsave" ] || \
  mv -fv "%{_sysconfdir}/modprobe.d/tuned.conf.rpmsave" "%{_sysconfdir}/modprobe.d/tuned.conf" || :

%preun
%service_del_preun %{name}.service

%preun ppd
%service_del_preun %{name}-ppd.service

%postun
%service_del_postun %{name}.service

%postun ppd
%service_del_postun %{name}-ppd.service

%files
%license COPYING
%doc AUTHORS README.md
%{_datadir}/bash-completion/completions/tuned-adm
%{_datadir}/polkit-1/actions/com.redhat.tuned.policy
%{python3_sitelib}/tuned
%{_sbindir}/tuned
%{_sbindir}/tuned-adm
%if 0%{?suse_version} < 1600
%{_sbindir}/rctuned
%endif
%dir %{system_dir}
%dir %{system_dir}/recommend.d
%exclude %{python3_sitelib}/tuned/gtk

# General files
%{system_dir}/pmqos-static.py
%{system_dir}/functions
%{system_dir}/recommend.d/50-tuned.conf
%{system_dir}/defirqaffinity.py

%if 0%{?sle_version} && %{?suse_version} < 1599
%exclude %{profile_dir}/sap-netweaver
%exclude %{profile_dir}/sap-hana
%exclude %{profile_dir}/sap-hana-kvm-guest
%exclude %{_mandir}/man7/tuned-profiles-sap.7%{?ext_man}
%exclude %{_mandir}/man7/tuned-profiles-sap-hana.7%{?ext_man}
%endif

# Profiles included in main package - alphabetically sorted
%dir %{profile_dir}
%{profile_dir}/accelerator-performance
%{profile_dir}/aws
%{profile_dir}/balanced
%{profile_dir}/balanced-battery
%{profile_dir}/cpu-partitioning
%{profile_dir}/cpu-partitioning-powersave
%{profile_dir}/desktop
%{profile_dir}/hpc-compute
%{profile_dir}/intel-sst
%{profile_dir}/latency-performance
%{profile_dir}/mssql
%{profile_dir}/network-latency
%{profile_dir}/network-throughput
%{profile_dir}/optimize-serial-console
%{profile_dir}/powersave
%{profile_dir}/throughput-performance
%{profile_dir}/virtual-guest
%{profile_dir}/virtual-host

# active_profile might be empty when built via build service, but typically
# not on a real install -> better do not mark it %%ghost
%config(noreplace) %{_sysconfdir}/tuned/active_profile
%config(noreplace) %{_sysconfdir}/tuned/ppd_base_profile
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-powersave-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/tuned-main.conf
%config(noreplace) %{_sysconfdir}/tuned/profile_mode
%config(noreplace) %{_sysconfdir}/tuned/profiles
%config(noreplace) %{_sysconfdir}/tuned/post_loaded_profile
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/bootcmdline
%config %{_sysconfdir}/grub.d
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/tuned.service
%{_modprobedir}/tuned.conf
%{_datadir}/dbus-1/system.d/com.redhat.tuned.conf
%attr(750, root, root) %dir %{_localstatedir}/log/tuned
%dir %{_sysconfdir}/tuned
%{_mandir}/man5/tuned*
%{_mandir}/man7/tuned-profiles-cpu-partitioning.7%{?ext_man}
%{_mandir}/man7/tuned-profiles.7%{?ext_man}
%{_mandir}/man7/tuned-profiles-mssql.7%{?ext_man}
%{_mandir}/man8/tuned*
%dir %{_datadir}/tuned
%ghost %dir /run/tuned
%dir %{_prefix}/lib/kernel
%dir %{_prefix}/lib/kernel/install.d
%{_prefix}/lib/kernel/install.d/92-tuned.install

%files gtk
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/tuned-gui.desktop
%{_sbindir}/tuned-gui
%{python3_sitelib}/tuned/gtk
%{_datadir}/tuned/ui

%if !0%{?sle_version} || %{?suse_version} >= 1599
%files profiles-sap
%{profile_dir}/sap-netweaver
%{_mandir}/man7/tuned-profiles-sap.7%{?ext_man}

%files profiles-sap-hana
%{profile_dir}/sap-hana
%{profile_dir}/sap-hana-kvm-guest
%{_mandir}/man7/tuned-profiles-sap-hana.7%{?ext_man}
%endif

%files profiles-atomic
%{profile_dir}/atomic-host
%{profile_dir}/atomic-guest
%{_mandir}/man7/tuned-profiles-atomic.7%{?ext_man}

%files profiles-realtime
%config(noreplace) %{_sysconfdir}/tuned/realtime-variables.conf
%{profile_dir}/realtime
%{_mandir}/man7/tuned-profiles-realtime.7%{?ext_man}

%files profiles-oracle
%{profile_dir}/oracle
%{_mandir}/man7/tuned-profiles-oracle.7%{?ext_man}

%files profiles-nfv
%config(noreplace) %{_sysconfdir}/tuned/realtime-virtual-guest-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/realtime-virtual-host-variables.conf
%{profile_dir}/realtime-virtual-guest
%{profile_dir}/realtime-virtual-host
%{_mandir}/man7/tuned-profiles-nfv-*.7%{?ext_man}

%files profiles-postgresql
%defattr(-,root,root,-)
%{profile_dir}/postgresql
%{_mandir}/man7/tuned-profiles-postgresql.7*

%files profiles-spectrumscale
%defattr(-,root,root,-)
%{profile_dir}/spectrumscale-ece
%{_mandir}/man7/tuned-profiles-spectrumscale-ece.7*

%files profiles-openshift
%defattr(-,root,root,-)
%{profile_dir}/openshift-control-plane
%{profile_dir}/openshift-node
%{profile_dir}/openshift
%{_mandir}/man7/tuned-profiles-openshift.7%{?ext_man}

%files utils
%license COPYING
%{_bindir}/powertop2tuned

%files utils-systemtap
%license COPYING
%doc doc/README.utils doc/README.scomes
%{_sbindir}/varnetload
%{_sbindir}/netdevstat
%{_sbindir}/diskdevstat
%{_sbindir}/scomes
%{_mandir}/man8/varnetload.*
%{_mandir}/man8/netdevstat.*
%{_mandir}/man8/diskdevstat.*
%{_mandir}/man8/scomes.*

%files ppd
%{_sbindir}/tuned-ppd
%{_unitdir}/tuned-ppd.service
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/polkit-1/actions/net.hadess.PowerProfiles.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/polkit-1/actions/org.freedesktop.UPower.PowerProfiles.policy
%config(noreplace) %{_sysconfdir}/tuned/ppd.conf

%changelog
