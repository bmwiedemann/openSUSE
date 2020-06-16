#
# spec file for package tuned
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


%{!?_tmpfilesdir:%global _tmpfilesdir %{_libexecdir}/tmpfiles.d}

%define         profile_dir %{_prefix}/lib/%{name}

Name:           tuned
Version:        2.13.0
Release:        0
Summary:        A dynamic adaptive system tuning daemon
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/redhat-performance/tuned
Source0:        https://github.com/redhat-performance/tuned/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        tuned.rpmlintrc
# PATCH-FIX-OPENSUSE fix-allow-receive_sender-default.patch <allow receive_sender="com.redhat.com"/> allow receive_* is normally
# not needed as that is the default --<p.drouand@gmail.com>
Patch0:         fix-allow-receive_sender-default.patch
Patch1:         adjust_README_path_in_manpage.patch
BuildRequires:  bash-completion
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(systemd)
# need perf_bias now
Requires:       cpupower >= 4.19
Requires:       ethtool
Requires:       gawk
Requires:       hdparm
Requires:       polkit
Requires:       python3-configobj
Requires:       python3-dbus-python
Requires:       python3-decorator
Requires:       python3-gobject
Requires:       python3-linux-procfs
Requires:       python3-pyudev
Requires:       util-linux
Requires:       virt-what
BuildArch:      noarch
%{?systemd_requires}

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%package gtk
Summary:        Disk and net statistic monitoring systemtap scripts - GTK GUI
Group:          System/Base
Requires:       %{name} = %{version}
Requires:       powertop

%description gtk
GTK GUI that can control tuned and provide simple profile editor.

# Do not ship SAP profiles for SLE and Leap, there are other packages
# providing these profiles
%if !0%{?sle_version}
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

%package profiles-atomic
Summary:        Additional tuned profiles targeted to Atomic
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-atomic
Additional profile(s) for the tuned daemon, targeted to Atomic host and guest.

%package profiles-realtime
Summary:        Additional tuned profiles targeted to realtime
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-realtime
Additional profile(s) for the tuned daemon, targeted to realtime.

%package profiles-oracle
Summary:        Additional tuned profiles targeted to Oracle loads
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-oracle
Additional profile(s) for the tuned daemon,  targeted to Oracle loads.

%package profiles-nfv
Summary:        Additional tuned profiles targeted to Network Function Virtualization (NFV)
Group:          System/Base
Requires:       %{name} = %{version}

%description profiles-nfv
Additional profile(s) for the tuned daemon, targeted to Network Function Virtualization (NFV).

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

%prep
%setup -q
%autopatch -p1

%build
# The tuned daemon is written in pure Python. Nothing requires to be built.
# Just a hack to avoid installation in a wrong directory
sed -i 's|usr/libexec/tuned|%{profile_dir}|' Makefile

%install
%make_install TUNED_PROFILESDIR=%{profile_dir}
%py3_compile %{buildroot}/%{python3_sitelib}
rm -rf %{buildroot}/%{_datadir}/doc
# Remove unwanted stuff instead of excluding them in files list
rm -rf %{buildroot}%{profile_dir}/{default,desktop-powersave,laptop-ac-powersave,server-powersave,laptop-battery-powersave,enterprise-storage,spindown-disk}
rm %{buildroot}%{_mandir}/man7/tuned-profiles-compat.7
ln -sf service %{buildroot}%{_sbindir}/rctuned

%post
%service_add_post %{name}.service
%if 0%{?suse_version} <= 1320
    systemd-tmpfiles --create %{_tmpfilesdir}/%{name}.conf >/dev/null 2>&1 || :
%else
    %tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%endif
# convert active_profile from full path to name (if needed)
sed -i 's|.*/\([^/]\+\)/[^\.]\+\.conf|\1|' %{_sysconfdir}/tuned/active_profile
%if 0%{?suse_version} < 1500
%desktop_database_post
%endif

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
%if 0%{?suse_version} < 1500
%desktop_database_postun
%endif

%files
%dir %_sysconfdir/dbus-1
%dir %_sysconfdir/dbus-1/system.d
%dir %{_sysconfdir}/modprobe.d
%license COPYING
%doc AUTHORS README
%{_datadir}/bash-completion/completions/tuned-adm
%{_datadir}/polkit-1/actions/com.redhat.tuned.policy
%exclude %{python3_sitelib}/tuned/gtk
%{python3_sitelib}/tuned
%{_sbindir}/tuned
%{_sbindir}/tuned-adm
%{_sbindir}/rctuned
%exclude %{_sysconfdir}/tuned/realtime-variables.conf
%exclude %{_sysconfdir}/tuned/realtime-virtual-guest-variables.conf
%exclude %{_sysconfdir}/tuned/realtime-virtual-host-variables.conf
%exclude %{profile_dir}/realtime-virtual-guest
%exclude %{profile_dir}/realtime-virtual-host
%exclude %{profile_dir}/sap-netweaver
%exclude %{profile_dir}/sap-hana
%exclude %{_mandir}/man7/tuned-profiles-sap*.7.gz
%exclude %{profile_dir}/atomic-host
%exclude %{profile_dir}/atomic-guest
%exclude %{profile_dir}/oracle
%exclude %{profile_dir}/realtime
%exclude %{profile_dir}/defirqaffinity*
%{profile_dir}/pmqos-static.py
%{profile_dir}
# active_profile might be empty when built via build service, but typically
# not on a real install -> better do not mark it %%ghost
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/active_profile
%config(noreplace) %{_sysconfdir}/modprobe.d/tuned.conf
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/tuned-main.conf
%config(noreplace) %{_sysconfdir}/tuned/profile_mode
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/tuned/bootcmdline
%dir %{_sysconfdir}/dbus-1
%dir %{_sysconfdir}/dbus-1/system.d
%config %{_sysconfdir}/dbus-1/system.d/com.redhat.tuned.conf
%{_sysconfdir}/grub.d
%{_tmpfilesdir}/tuned.conf
%{_unitdir}/tuned.service
%attr(750, root, root) %dir %{_localstatedir}/log/tuned
%dir %{_sysconfdir}/tuned
%{_mandir}/man5/tuned*
%{_mandir}/man7/tuned-profiles-cpu-partitioning.7%{?ext_man}
%{_mandir}/man7/tuned-profiles.7%{?ext_man}
%{_mandir}/man7/tuned-profiles-mssql.7%{?ext_man}
%{_mandir}/man8/tuned*
%dir %{_datadir}/tuned
%ghost %dir /run/tuned
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

%if !0%{?sle_version}
%files profiles-sap
%{profile_dir}/sap-netweaver
%{_mandir}/man7/tuned-profiles-sap.7%{?ext_man}

%files profiles-sap-hana
%{profile_dir}/sap-hana
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

%changelog
