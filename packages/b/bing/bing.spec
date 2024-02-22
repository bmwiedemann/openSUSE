#
# spec file for package bing
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


Name:           bing
PreReq:         permissions
Url:            http://fgouget.free.fr/bing/index-en.shtml
Summary:        A Point-to-Point Bandwidth Measurement Tool
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
Version:        1.0.5
Release:        0
Source:         bing-%{version}.tar.bz2
Patch0:         bing-%{version}.dif
Patch1:         %{name}-%{version}-permissions.patch
Patch2:         %{name}-%{version}-includes.diff
Patch3:         %{name}-%{version}-moresecure.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bing determines the real (raw, as opposed to available or average)
throughput of a link by measuring ICMP echo request round trip times
for different packet sizes for each end of the link.

%prep
%setup
%patch -P 0
%patch -P 1
%patch -P 2
%patch -P 3 -p1

%build
make CC="%__cc" CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/{%{_mandir}/man8,usr/sbin}
make install MANDIR=$RPM_BUILD_ROOT/%{_mandir} BINDIR=$RPM_BUILD_ROOT/usr/sbin

%files
%defattr(-,root,root)
%attr(0755,root,root) /usr/sbin/bing
%doc %{_mandir}/man8/bing.*
%doc bing.ps
%doc ChangeLog README

%changelog
