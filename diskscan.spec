#
# spec file for package diskscan
#
# Copyright (c) 2021 SUSE LLC
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


Name:           diskscan
Version:        0.20
Release:        0
Summary:        Scan disk for bad or near failure sectors
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/baruch/diskscan
Source0:        https://github.com/baruch/diskscan/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0.2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3-Markdown
BuildRequires:  python3-PyYAML
BuildRequires:  python3-beautifulsoup4
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)

%description
DiskScan is a Unix/Linux tool to scan a block device and check
if there are unreadable sectors, in addition it uses read
latency times as an assessment for a near failure as sectors
that are problematic to read usually entail many retries. This
can be used to assess the state of the disk and maybe decide
on a replacement in advance to its imminent failure. The disk
self test may or may not pick up on such clues depending on
the disk vendor decision making logic.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install

%files
%license COPYING
%doc README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
