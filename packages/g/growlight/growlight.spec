#
# spec file for package growlight
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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


%ifarch %{ix86} %{arm}
%bcond_with  pandoc
%else
%bcond_without  pandoc
%endif
Name:           growlight
Version:        1.2.38
Release:        0
Summary:        Disk manipulation and system setup tool
License:        GPL-3.0-or-later
Group:          System/Monitoring
URL:            https://nick-black.com/dankwiki/index.php/Growlight
Source:         https://github.com/dankamongmen/growlight/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if %{with pandoc}
BuildRequires:  pandoc
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blkid) >= 2.20.1
BuildRequires:  pkgconfig(devmapper) >= 1.02.74
BuildRequires:  pkgconfig(doctest) >= 2.3.5
BuildRequires:  pkgconfig(libatasmart) >= 0.19
BuildRequires:  pkgconfig(libcap) >= 2.24
BuildRequires:  pkgconfig(libcryptsetup) >= 2.0.2
BuildRequires:  pkgconfig(libpci) >= 3.1.9
BuildRequires:  pkgconfig(libudev) >= 175
BuildRequires:  pkgconfig(nettle) >= 3.5.1
BuildRequires:  pkgconfig(notcurses) >= 2.4.4
BuildRequires:  pkgconfig(pciaccess) >= 0.13.1
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib) >= 1.2.11
Recommends:     btrfsprogs
Recommends:     dosfstools
Recommends:     e2fsprogs
Recommends:     f2fs-tools
Recommends:     hdparm
Recommends:     hfsutils
Recommends:     ipmctl
Recommends:     mdadm
Recommends:     ntfs-3g
Recommends:     nvme-cli
Recommends:     xfsprogs

%description
growlight can manipulate both physical (NVMe, SATA, etc.) and virtual (mdadm,
device-mapper, etc.) block devices, help identify bottlenecks in a storage
topology, create and destroy filesystems, and prepare a machine for initial
boot when run in an installer context. Both full-screen and REPL readline UIs
are available.

%prep
%setup -q

%build
%cmake -DUSE_LIBZFS=OFF -DUSE_PANDOC=%{with pandoc}
%make_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_sbindir}/growlight
%{_sbindir}/growlight-readline
%dir %{_datadir}/growlight
%{_datadir}/growlight/growlight.jpg
%if %{with pandoc}
%{_mandir}/man8/growlight-readline.8%{?ext_man}
%{_mandir}/man8/growlight.8%{?ext_man}
%endif

%changelog
