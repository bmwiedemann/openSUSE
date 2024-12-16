#
# spec file for package nfswatch
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


Name:           nfswatch
Version:        4.99.11
Release:        0
Summary:        An NFS traffic monitoring tool
License:        BSD-2-Clause
Group:          Productivity/Networking/NFS
URL:            http://nfswatch.sourceforge.net
Source:         %{name}-%{version}.tar.gz
Patch0:         makefile.patch
Patch1:         nfswatch-4.99.11-sysmacros.patch
Patch2:         nfswatch-fix-proto.patch
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  libtirpc-devel
%endif

%description
Nfswatch is a command-line tool for monitoring NFS traffic.
Nfswatch can capture and analyze the NFS packets on a particular
network interface or on all interfaces.

%prep
%setup -q
%if 0%{?suse_version} >= 1500
%patch -P 0 -p1
%endif
%patch -P 1 -p1
%patch -P 2 -p1

%build

make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
make STRIP= DESTDIR=%{buildroot} install

%files
%license LICENSE
%doc README
%{_sbindir}/nfswatch
%{_sbindir}/nfslogsum
%{_mandir}/man8/*

%changelog
