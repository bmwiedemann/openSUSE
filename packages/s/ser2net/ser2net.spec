#
# spec file for package ser2net
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ser2net
Version:        4.3.11
Release:        0
Summary:        Serial port to network proxy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/cminyard/ser2net.git
Source:         https://sourceforge.net/projects/ser2net/files/ser2net/%{name}-%{version}.tar.gz
Source2:        ser2net.service
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libgensio) >= 2.2.0
BuildRequires:  pkgconfig(yaml-0.1)
%{?systemd_requires}

%description
ser2net provides a way for a user to connect from a network connection to a
serial port. It provides all the serial port setup, a configuration file to
configure the ports, a control login for modifying port parameters,
monitoring ports, and controlling ports.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
install -D -m 0644 %{name}.yaml %{buildroot}/%{_sysconfdir}/ser2net/%{name}.yaml
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/ser2net.service

%pre
%service_add_pre ser2net.service

%post
%service_add_post ser2net.service

%preun
%service_del_preun ser2net.service

%postun
%service_del_postun ser2net.service

%files
%license COPYING
%doc ChangeLog AUTHORS README
%{_sbindir}/%{name}
%dir %{_sysconfdir}/ser2net
%config(noreplace) %{_sysconfdir}/ser2net/%{name}.yaml
%{_unitdir}/ser2net.service
%{_mandir}/man5/ser2net.yaml.5%{?ext_man}
%{_mandir}/man8/ser2net.8%{?ext_man}

%changelog
