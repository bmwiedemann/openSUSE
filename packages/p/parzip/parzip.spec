#
# spec file for package parzip
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


Name:           parzip
Version:        1.3.0
Release:        0
Summary:        Parallel pkzip implementation
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://github.com/jpakkane/parzip
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM parzip-fix-missing-includes.patch
Patch0:         parzip-fix-missing-includes.patch
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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%license COPYING
%{_bindir}/parunzip
%{_bindir}/parzip
%{_mandir}/man1/parunzip.1%{?ext_man}
%{_mandir}/man1/parzip.1%{?ext_man}

%changelog
