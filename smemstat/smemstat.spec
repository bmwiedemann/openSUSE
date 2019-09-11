#
# spec file for package smemstat
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           smemstat
Version:        0.02.03
Release:        0
Summary:        Memory usage monitoring tool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://kernel.ubuntu.com/~cking/smemstat/
Source:         https://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncursesw)

%description
Smemstat reports the physical memory usage taking into consideration shared
memory. The tool can either report a current snapshot of memory usage or
periodically dump out any changes in memory.

%prep
%setup -q

%build
export CFLAGS="%{optflags} $(pkg-config --cflags ncursesw) -fwhole-program"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/smemstat
%{_mandir}/man8/smemstat.8%{?ext_man}

%changelog
