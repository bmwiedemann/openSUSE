#
# spec file for package vlan
#
# Copyright (c) 2023 SUSE LLC
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
Version:        1.9
Release:        0
Summary:        802.1q VLAN Implementation for Linux
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://www.candelatech.com/~greear/vlan.html
# online url http://www.candelatech.com/~greear/vlan/vlan.1.9.tar.gz but tarball is broken there
# this is a bz2 version of it
Source:         vlan.%{version}.tar.bz2
# from now offline       http://scry.wanfear.com/~greear/vlan/cisco_howto.html, accessible through https://web.archive.org/web/20070429115150/http://scry.wanfear.com/~greear/vlan/cisco_howto.html
Source1:        cisco_howto.html.bz2
BuildRequires:  gcc-c++

%description
An 802.1q vlan implementation for Linux. See
http://www.candelatech.com/~greear/vlan.html for more information.

%prep
%setup -q -n vlan
cp -p %{SOURCE1} .

%build
%make_build clean
%make_build CCFLAGS="%{optflags} -D_GNU_SOURCE -Wall" STRIP=true

%install
make DESTDIR=%{buildroot}
mkdir -p %{buildroot}/{sbin,%{_sbindir},%{_mandir}/man8/}
install -m755 vconfig   %{buildroot}/%{_sbindir}
install -m644 vconfig.8 %{buildroot}%{_mandir}/man8/
%if 0%{?suse_version} < 1550
ln -sf %{_sbindir}/vconfig %{buildroot}/sbin
%endif

%files
%defattr(644,root,root,755)
%doc *.html *.pl CHANGELOG README
%{_mandir}/man8/vconfig.8%{?ext_man}
%attr(755,root,root) %{_sbindir}/vconfig
%if 0%{?suse_version} < 1550
%attr(755,root,root) /sbin/vconfig
%endif

%changelog
