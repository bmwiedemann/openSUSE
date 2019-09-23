#
# spec file for package tcpflow
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Sebastien Braun.
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


Name:           tcpflow
Version:        1.5.0
Release:        0
Summary:        Program for capturing and collecting TCP streams
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
Url:            http://afflib.org/software/tcpflow
Source:         http://www.digitalcorpora.org/downloads/tcpflow/%{name}-%{version}.tar.gz

%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
tcpflow is a program that captures data transmitted as part of TCP connections
(flows), and stores the data in a way that is convenient for protocol
analysis and debugging. Each TCP flow is stored in its own file. Thus, the
typical TCP flow will be stored in two files, one for each direction.
tcpflow can also process stored 'tcpdump' packet flows.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(0644,root,root)
%license COPYING
%doc AUTHORS NEWS TODO.txt ChangeLog
%attr(0755,root,root) %{_bindir}/tcpflow
%{_mandir}/man1/*.1.*

%changelog
