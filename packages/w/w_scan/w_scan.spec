#
# spec file for package w_scan
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


Name:           w_scan
Version:        20170107
Release:        0
Summary:        Tool for scanning DVB transponders
License:        GPL-2.0-only
Group:          Hardware/TV
URL:            http://wirbel.htpc-forum.de/w_scan/index2.html
Source0:        http://wirbel.htpc-forum.de/w_scan/w_scan-%{version}.tar.bz2
BuildRequires:  linux-kernel-headers

%description
w_scan is a small command line utility used to perform frequency scans for
DVB and ATSC transmissions. It is capable of creating channels.conf files
(in different output formats !) as well as initial tuning data for scan.
It's based on the utility scan from linuxtv-dvb-apps, but meanwhile it was
heavily changed and has different features.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fcommon"
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%doc doc/README.file_formats doc/README_VLC_DVB doc/rotor.conf
%{_bindir}/w_scan
%{_mandir}/man1/w_scan.1%{?ext_man}

%changelog
