#
# spec file for package spew
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


Name:           spew
Version:        1.0.8
Release:        0
Summary:        An I/O performance measurement and load generation tool
License:        GPL-2.0-only
Group:          System/Benchmark
URL:            http://freecode.com/projects/spew
Source:         https://fossies.org/linux/privat/old/%{name}-%{version}.tgz
Patch0:         fix-format-security.patch
Patch1:         fix-automake-1.13.patch
Patch2:         fix-ncurses-tinfo.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  popt-devel

%description
Spew is used to measure I/O performance of character devices, block devices,
and regular files. It can also be used to generate high I/O loads to stress
systems while verifying data integrity.

Spew is easy to use and is flexible. No configuration files or complicated
client/server configurations are needed. Spew also generates its own data
patterns that are designed to make it easy to find and debug data integrity
problems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS FAQ NEWS README TODO
%{_bindir}/spew
%{_bindir}/gorge
%{_bindir}/regorge
%{_mandir}/man1/spew.1%{?ext_man}
%{_mandir}/man1/gorge.1%{?ext_man}
%{_mandir}/man1/regorge.1%{?ext_man}
%config %{_sysconfdir}/spew.conf

%changelog
