#
# spec file for package plzip
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           plzip
Version:        1.11
Release:        0
Summary:        Parallel LZMA Data Compressor
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://www.nongnu.org/lzip/plzip.html
Source:         https://download.savannah.gnu.org/releases/lzip/plzip/%name-%version.tar.gz
Source2:        https://download.savannah.gnu.org/releases/lzip/plzip/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  c++_compiler
BuildRequires:  lzlib-devel
Requires(post): %install_info_prereq
Requires(preun):%install_info_prereq

%description
Plzip is a parallel version of the lzip data compressor. The files
produced by plzip are fully compatible with lzip-1.4 or newer. Plzip
is intended for faster compression/decompression of big files on
multiprocessor machines.

Lzip is a lossless data compressor based on the LZMA algorithm, with
very safe integrity checking and a user interface similar to the one
of gzip or bzip2. Lzip decompresses almost as fast as gzip and
compresses better than bzip2, which makes it well suited for software
distribution and data archiving.

%prep
%autosetup -p1

%build
mkdir build
pushd build/
# not autoconf
../configure --prefix="%_prefix" --bindir="%_bindir" --datadir="%_datadir" \
	--includedir="%_includedir" --infodir="%_infodir" --libdir="%_libdir" \
	--mandir="%_mandir" --sysconfdir="%_sysconfdir" --enable-shared \
	CFLAGS="%optflags" CXXFLAGS="%optflags"
%make_build
popd

%install
pushd build/
%make_install LDCONFIG=true
popd

%check
pushd build/
%make_build check
popd

%post
%install_info --info-dir="%_infodir" "%_infodir/%name.info%ext_info"

%preun
%install_info_delete --info-dir="%_infodir" "%_infodir/%name.info%ext_info"

%files
%license COPYING
%doc ChangeLog README
%_bindir/plzip
%_infodir/plzip.info*
%_mandir/man1/plzip.1*

%changelog
