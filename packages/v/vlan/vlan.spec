#
# spec file for package vlan
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


Name:           vlan
BuildRequires:  gcc-c++
URL:            http://www.candelatech.com/~greear/vlan.html
Version:        1.9
Release:        0
Summary:        802.1q VLAN Implementation for Linux
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
Source:         http://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.bz2
Source1:        http://scry.wanfear.com/~greear/vlan/cisco_howto.html.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An 802.1q vlan implementation for Linux. See
http://www.candelatech.com/~greear/vlan.html for more information.



Authors:
--------
    Ben Greear <greearb@candelatech.com>

%prep
%setup -n vlan
cp -p %{S:1} .

%build
make clean
make CCFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -Wall" STRIP=true

%install
make DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{sbin,%_sbindir,%{_mandir}/man8/}
install -m755 vconfig   $RPM_BUILD_ROOT/%_sbindir
install -m644 vconfig.8 $RPM_BUILD_ROOT%{_mandir}/man8/
%if 0%{?suse_version} < 1550
ln -sf %_sbindir/vconfig $RPM_BUILD_ROOT/sbin
%endif

%files
%defattr(644,root,root,755)
%doc *.html *.pl CHANGELOG README
%doc %{_mandir}/man8/vconfig.8.gz
%attr(755,root,root) %_sbindir/vconfig
%if 0%{?suse_version} < 1550
%attr(755,root,root) /sbin/vconfig
%endif

%changelog
