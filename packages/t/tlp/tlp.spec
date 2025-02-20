#
# spec file for package tlp
#
# Copyright (c) 2024 SUSE LLC
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


%define _name TLP
%define systemd_sleepdir %{_systemd_util_dir}/system-sleep
%if 0%{?suse_version} > 01500
%define _udevdir %(pkg-config --variable udev_dir udev || echo %{_prefix}/lib/udev)
%else
%{!?_udevdir: %define _udevdir %{_prefix}/lib/udev}
%endif
%{!?_udevrulesdir: %define _udevrulesdir %{_udevdir}/rules.d}
Name:           tlp
Version:        1.8.0
Release:        0
Summary:        Tools to save battery power on laptops
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Hardware/Mobile
URL:            https://linrunner.de/tlp
Source:         https://github.com/linrunner/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source10:       tlp-rpmlintrc
BuildRequires:  gzip
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(udev)
Requires:       hdparm
Requires:       iw
Requires:       pciutils
Requires:       rfkill
Requires:       usbutils
Requires:       util-linux >= 2.17
Requires(pre):  systemd
Recommends:     %{name}-rdw = %{version}
Recommends:     ethtool
Recommends:     lsb-release
Recommends:     smartmontools
Conflicts:      laptop-mode-tools
Conflicts:      power-profiles-daemon
Conflicts:      tuned
BuildArch:      noarch
%{?systemd_ordering}

%description
TLP implements advanced power management for Linux.
TLP is a pure command line tool with automated background tasks.
It does not contain a GUI.

%package rdw
Summary:        TLP Radio Device Wizard
Group:          Hardware/Mobile
Requires:       NetworkManager >= 1.20
Requires:       tlp = %{version}
Requires(pre):  systemd
BuildArch:      noarch

%description rdw
TLP implements advanced power management for Linux.
TLP is a pure command line tool with automated background tasks.
It does not contain a GUI.

Switch radios upon network connect/disconnect and dock/undock.

%prep
%setup -q -n %{_name}-%{version}

%build
%make_build \
  TLP_ULIB=%{_udevdir} \
  TLP_SYSD=%{_unitdir}

%install
%make_install \
  TLP_WITH_SYSTEMD=1           \
  TLP_WITH_ELOGIND=0           \
  TLP_NO_INIT=1                \
  TLP_ULIB=%{_udevdir} \
  TLP_SYSD=%{_unitdir} \
  TLP_SDSL=%{systemd_sleepdir}

make install-man      DESTDIR=%{buildroot}
make install-man-rdw  DESTDIR=%{buildroot}

ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rctlp

%pre
%service_add_pre tlp.service

%post
%service_add_post tlp.service
%{_bindir}/systemctl mask systemd-rfkill.service
%{_bindir}/systemctl mask systemd-rfkill.socket
%{_bindir}/systemctl mask power-profiles-daemon.service

%postun
%service_del_postun tlp.service
if [ $1 -eq 0 ] ; then
    %{_bindir}/systemctl unmask systemd-rfkill.service
    %{_bindir}/systemctl unmask systemd-rfkill.socket
    %{_bindir}/systemctl unmask power-profiles-daemon.service
fi

%preun
%service_del_preun tlp.service

%post rdw
%{_bindir}/systemctl enable NetworkManager-dispatcher.service >/dev/null 2>&1 || :

%files
%license COPYING LICENSE
%doc AUTHORS changelog README.rst
%dir %{_sysconfdir}/%{name}.d
%dir %{systemd_sleepdir}
%dir %{_datadir}/metainfo/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.d/00-template.conf
%{_sysconfdir}/%{name}.d/README
%{systemd_sleepdir}/tlp
%{_bindir}/bluetooth
%{_bindir}/run-on-{ac,bat}
%{_bindir}/%{name}-stat
%{_bindir}/nfc
%{_bindir}/wifi
%{_bindir}/wwan
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%{_datadir}/%{name}/
%{_datadir}/metainfo/de.linrunner.tlp.metainfo.xml
%{_udevdir}/%{name}-usb-udev
%{_udevrulesdir}/85-%{name}.rules
%{_localstatedir}/lib/%{name}/
%{_datadir}/bash-completion/completions/*
%exclude %{_datadir}/bash-completion/completions/tlp-rdw
%{_datadir}/zsh/site-functions/*
%exclude %{_datadir}/zsh/site-functions/_tlp-rdw
%{_mandir}/man?/*.?%{?ext_man}
%exclude %{_mandir}/man8/%{name}-rdw.8%{?ext_man}
%{_datadir}/fish/vendor_completions.d/*
%exclude %{_datadir}/fish/vendor_completions.d/tlp-rdw.fish

%files rdw
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%attr(0755,root,root) %{_prefix}/lib/NetworkManager/dispatcher.d/99tlp-rdw-nm
%{_bindir}/%{name}-rdw
%{_udevrulesdir}/85-%{name}-rdw.rules
%{_udevdir}/%{name}-rdw-udev
%{_mandir}/man8/%{name}-rdw.8%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}-rdw
%{_datadir}/zsh/site-functions/_%{name}-rdw
%{_datadir}/fish/vendor_completions.d/%{name}-rdw.fish

%changelog
