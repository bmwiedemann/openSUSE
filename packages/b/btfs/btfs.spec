#
# spec file for package btfs
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           btfs
Version:        3.1
Release:        0
Summary:        A BitTorrent file system based on FUSE
License:        GPL-3.0-or-later
URL:            https://github.com/johang/%{name}
Source:         https://github.com/johang/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_system-devel
%else
BuildRequires:  libboost_system1_75_0-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse3) >= 3.0
BuildRequires:  pkgconfig(libcurl) >= 7.22.0
BuildRequires:  pkgconfig(libtorrent-rasterbar) >= 1.0.0

%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp work as expected. Applications like media players can also work without changes.

%prep
%autosetup -p1
sed -i 's,env python,python,' scripts/btplay

%build
export CXXFLAGS="-std=c++14"
autoreconf -fi
%configure
%make_build

%install
%make_install V=1

%files
%doc README.md
%license LICENSE
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/btfs
%{_bindir}/btplay
%{_bindir}/btfsstat

%changelog
