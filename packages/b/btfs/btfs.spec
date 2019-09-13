#
# spec file for package btfs
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


Name:           btfs
Version:        2.20
Release:        0
Summary:        A BitTorrent file system based on FUSE
License:        GPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/johang/%{name}
Source:         https://github.com/johang/%{name}/archive/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  libboost_system-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libtorrent-rasterbar) > 0.16

%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp work as expected. Applications like media players can also work without changes.

%prep
%setup -q
sed -i 's,env python,python,' scripts/btplay

%build
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
