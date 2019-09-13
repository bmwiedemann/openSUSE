#
# spec file for package yate-bts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           yate-bts
Version:        6.1.0
Release:        0
Summary:        GSM BTS based on Yet Another Telephony Engine
# MBTS radio component and the radio transceiver, released under the AGPLv3 license
License:        GPL-2.0-or-later AND AGPL-3.0-only
Group:          Productivity/Telephony/Servers
URL:            https://yatebts.com
Source0:        http://yate.null.ro/tarballs/yatebts6/yate-bts-%{version}-1.tar.gz
Source99:       yate-bts.rpmlintrc
Patch0:         yate-dont-mess-with-cflags.patch
Patch1:         yatebts-sgsnggsn-inetutils-hostname-fix.diff
Patch2:         yatebts-5.0.0-gcc6.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  yate >= 6.0.0
BuildRequires:  pkgconfig(yate) >= 6.0.0
Requires:       yate-scripts >= 6.0.0

%description
Yate is a telephony engine designed to implement PBX and IVR solutions
for small to large scale projects.
This module implements a 2G GSM BTS for Yate.
At least one transceiver package must also be installed for
interfacing with the hardware.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{_sourcedir}/%{name}.changes")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find . -type f -regex ".*\.c\|.*\.cpp\|.*\.h" -exec sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" {} +

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc/
rm -f %{buildroot}/%{_datadir}/yate/nipc_web/.htaccess

%files
%license COPYING
%doc README
%config(noreplace) %{_sysconfdir}/yate/subscribers.conf
%config(noreplace) %{_sysconfdir}/yate/ybts.conf
%dir %{_libdir}/yate/server/bts
%{_libdir}/yate/server/bts/mbts
%{_libdir}/yate/server/gsmtrx.yate
%{_libdir}/yate/server/ybts.yate
%{_datadir}/yate/scripts
%{_datadir}/yate/sounds
%{_datadir}/yate/nipc_web

%changelog
