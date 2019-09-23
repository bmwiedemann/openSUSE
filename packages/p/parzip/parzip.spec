#
# spec file for package parzip
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


Name:           parzip
Version:        1.2.0
Release:        0
Summary:        Parallel pkzip implementation
License:        GPL-3.0+
Group:          Productivity/Archiving/Compression
Url:            https://github.com/jpakkane/parzip
Source0:        https://github.com/jpakkane/parzip/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)

%description
A command line utility to pack and unpack zip archives using
multiple threads.

Supports
    both zipping and unzipping
    multithreading
    uncompressed (i.e. stored) files
    deflate and lzma compression and decompression
    ZIP64 extensions (i.e. >4 GB files)
    unix file attributes

Does not support
    modifying existing archives
    encryption (zip encryption is broken, use GPG instead)
    ancient compression methods
    archives split to multiple files

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license COPYING
%{_bindir}/parunzip
%{_bindir}/parzip
%{_mandir}/man1/parunzip.1%{ext_man}
%{_mandir}/man1/parzip.1%{ext_man}

%changelog
