#
# spec file for package ser2net
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ser2net
Version:        3.5
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            https://github.com/cminyard/ser2net.git
Source:         %{name}-%{version}.tar.xz
Source2:        ser2net.service
Summary:        Serial port to network proxy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  systemd-rpm-macros
Patch0:         ser2net-config.patch
%{?systemd_requires}

%description
ser2net provides a way for a user to connect from a network connection to a 
serial port. It provides all the serial port setup, a configuration file to 
configure the ports, a control login for modifying port parameters, 
monitoring ports, and controlling ports.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
autoreconf -i
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
install -D -m 0644 %{name}.conf %{buildroot}/%{_sysconfdir}/%{name}.conf
install -D -m 0644 %{S:2} %{buildroot}/%{_unitdir}/ser2net.service

%pre
%service_add_pre ser2net.service

%post
%service_add_post ser2net.service

%preun
%service_del_preun ser2net.service

%postun
%service_del_postun ser2net.service

%files
%defattr(-,root,root)
%doc COPYING ChangeLog AUTHORS README
%{_unitdir}/ser2net.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}*

%changelog
