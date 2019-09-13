#
# spec file for package finger
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           finger
Version:        1.3
Release:        0
Summary:        Show User Information (Client)
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
Source:         finger-bsd-%{version}.tar.bz2
Source3:        finger.socket
Source4:        finger@.service
Patch1:         finger-utf8_segfault.patch
Patch2:         finger-memory-leak.patch
Requires:       netcfg
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Finger is a utility that allows users to see information about system
users (login name, home directory, name, and more) on local and remote
systems.

%package server
Summary:        A Server for Showing User Information
Group:          Productivity/Networking/Other
Requires:       netcfg
%{?systemd_requires}

%description server
The finger daemon implements a simple protocol based on RFC1196 that
provides an interface to the Name and Finger programs at several
network sites. The program is supposed to return a friendly
human-oriented status report on either the system at the moment or a
particular person.

%prep
%setup -q -n finger-bsd-%{version}
%patch1
%patch2 -p1

%build
export CFLAGS="%{optflags} -fpie" LDFLAGS="-pie"
%configure
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_mandir}/man3
install -d -m 755 %{buildroot}%{_mandir}/man5
install -d -m 755 %{buildroot}%{_mandir}/man8
make install DESTDIR=%{buildroot} INSTALL_PROGRAM="install -m 755"

install -D -m 0644 %{SOURCE3} %{buildroot}/%{_unitdir}/finger.socket
install -D -m 0644 %{SOURCE4} %{buildroot}/%{_unitdir}/finger@.service
%find_lang finger-bsd

%pre server
%service_add_pre finger.socket

%post server
%service_add_post finger.socket

%preun server
%service_del_preun finger.socket

%postun server
%service_del_postun finger.socket

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/finger
%{_mandir}/man1/finger.1%{ext_man}

%files server -f finger-bsd.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_unitdir}/finger.socket
%{_unitdir}/finger@.service
%{_mandir}/man8/fingerd.8%{ext_man}
%{_mandir}/man8/in.fingerd.8%{ext_man}
%{_sbindir}/in.fingerd

%changelog
