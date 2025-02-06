#
# spec file for package lzip
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2008-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           lzip
Version:        1.25
Release:        0
Summary:        Lossless Data Compressor based on the LZMA Algorithm
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            https://www.nongnu.org/lzip/lzip.html
Source:         https://download.savannah.gnu.org/releases/lzip/%name-%version.tar.gz
Source2:        https://download.savannah.gnu.org/releases/lzip/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  gcc-c++
PreReq:         %install_info_prereq

%description
Lzip is a lossless data compressor based on the LZMA algorithm, with very safe
integrity checking and a user interface almost identical to the one of
bzip2. Lzip is only a data compressor, not an archiver. It has no facilities
for multiple files, encryption, or archive-splitting, but, in the Unix
tradition, relies instead on separate external utilities such as GNU Tar for
these tasks.

%prep
%autosetup -p1

%build
# not autoconf:
mkdir build
pushd build/
../configure --prefix="%_prefix" --bindir="%_bindir" --datadir="%_datadir" \
	--infodir="%_infodir" --mandir="%_mandir" --sysconfdir="%_sysconfdir" \
	CC="%__cc" CFLAGS="%optflags" CXX="%__cxx" CXXFLAGS="%optflags"
%make_build
popd

%install
pushd build/
%make_install
popd

%check
pushd build/
%make_build check
popd

%post
%install_info --info-dir="%_infodir" "%_infodir/lzip.info%ext_info"

%postun
%install_info_delete --info-dir="%_infodir" "%_infodir/lzip.info%ext_info"

%files
%doc ChangeLog README
%license COPYING
%_bindir/lzip
%_infodir/lzip.info%ext_info
%_mandir/man1/lzip.1%ext_man

%changelog
