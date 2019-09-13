#
# spec file for package tlp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   TLP
Name:           tlp
Version:        1.2.2
Release:        0
Summary:        Tools to save battery power on laptops
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Hardware/Mobile
URL:            http://linrunner.de/tlp
Source:         https://github.com/linrunner/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildRequires:  gzip
BuildRequires:  systemd-rpm-macros
Requires:       hdparm
Requires:       iw
Requires:       pciutils
Requires:       rfkill
Requires:       usbutils
Requires:       util-linux >= 2.17
Recommends:     %{name}-rdw = %{version}
Recommends:     ethtool
Recommends:     lsb-release
Recommends:     smartmontools
Suggests:       acpi-call-kmp
Suggests:       tp-smapi-kmp
Conflicts:      laptop-mode-tools
BuildArch:      noarch
%{?systemd_ordering}

%description
TLP implements advanced power management for Linux.
TLP is a pure command line tool with automated background tasks.
It does not contain a GUI.

%package rdw
Summary:        TLP Radio Device Wizard
Group:          Hardware/Mobile
Requires:       NetworkManager
Requires:       tlp = %{version}

%description rdw
TLP implements advanced power management for Linux.
TLP is a pure command line tool with automated background tasks.
It does not contain a GUI.

Switch radios upon network connect/disconnect and dock/undock.

%prep
%setup -q -n %{_name}-%{version}

%build
make %{?_smp_mflags} V=1 \
  TLP_ULIB=%{_libexecdir}/udev \
  TLP_SYSD=%{_unitdir}

%install
%make_install \
  TLP_WITH_SYSTEMD=1           \
  TLP_WITH_ELOGIND=0           \
  TLP_NO_INIT=1                \
  TLP_ULIB=%{_libexecdir}/udev \
  TLP_SYSD=%{_unitdir}
make install-man \
  DESTDIR=%{buildroot}
make install-man-rdw \
  DESTDIR=%{buildroot}

for rc in rc%{name} rc%{name}-sleep; do
    ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/$rc
done

%pre
%service_add_pre %{name}.service %{name}-sleep.service

%post
%service_add_post %{name}.service %{name}-sleep.service

%postun
%service_del_postun %{name}.service %{name}-sleep.service

%preun
%service_del_preun %{name}.service %{name}-sleep.service

%files
%license COPYING LICENSE
%doc AUTHORS changelog README.md
%config(noreplace) %{_sysconfdir}/default/%{name}
%{_bindir}/bluetooth
%{_bindir}/run-on-*
%{_bindir}/%{name}-*list
%{_bindir}/%{name}-stat
%{_bindir}/wifi
%{_bindir}/wwan
%{_sbindir}/*%{name}*
%{_unitdir}/%{name}*.service
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*%{name}.metainfo.xml
%dir %{_libexecdir}/udev/
%dir %{_libexecdir}/udev/rules.d/
%{_libexecdir}/udev/%{name}-usb-udev
%{_libexecdir}/udev/rules.d/85-%{name}.rules
%{_localstatedir}/lib/%{name}/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/bluetooth
%{_datadir}/bash-completion/completions/%{name}*
%{_datadir}/bash-completion/completions/wifi
%{_datadir}/bash-completion/completions/wwan
%{_mandir}/man?/*.?%{?ext_man}
%exclude %{_mandir}/man8/%{name}-rdw.8%{?ext_man}

%files rdw
%{_sysconfdir}/NetworkManager/
%{_bindir}/%{name}-rdw
%dir %{_libexecdir}/udev/
%dir %{_libexecdir}/udev/rules.d/
%{_libexecdir}/udev/rules.d/85-%{name}-rdw.rules
%{_libexecdir}/udev/%{name}-rdw-udev
%{_mandir}/man8/%{name}-rdw.8%{?ext_man}

%changelog
