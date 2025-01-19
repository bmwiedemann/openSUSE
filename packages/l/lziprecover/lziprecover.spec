#
# spec file for package lziprecover
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without tests
Name:           lziprecover
Version:        1.25
Release:        0
Summary:        Utility to repair broken lzip files
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            http://www.nongnu.org/lzip/lunzip.html
Source:         http://download.savannah.gnu.org/releases/lzip/lziprecover/%name-%version.tar.gz
Source2:        http://download.savannah.gnu.org/releases/lzip/lziprecover/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  gcc-c++
%if %{with tests}
BuildRequires:  lzip >= 1.16
%endif
Requires(post): info
Requires(preun):info

%description
Lziprecover is a data recovery tool and decompressor for files in the
lzip compressed data format (.lz) able to repair slightly damaged
files, recover badly damaged files from two or more copies, extract
undamaged members from multi-member files, decompress files and test
integrity of files.

Lziprecover is able to recover or decompress files produced by any of
the compressors in the lzip family; lzip, plzip, minilzip/lzlib,
clzip and pdlzip. This recovery capability contributes to make the
lzip format one of the best options for long-term data archiving.

Lziprecover is able to efficiently extract a range of bytes from a
multi-member file, because it only decompresses the members
containing the desired data.

Lziprecover can print correct total file sizes and ratios even for
multi-member files.

%prep
%autosetup -p1

%build
# not autoconf
mkdir build
pushd build/
../configure --prefix="%_prefix" --bindir="%_bindir" --datadir="%_datadir" \
	--infodir="%_infodir" --mandir="%_mandir" --sysconfdir="%_sysconfdir" \
	CFLAGS="%optflags"
%make_build
popd

%install
pushd build/
%make_install
popd

%if %{with tests}
%check
pushd build/
%make_build check
popd
%endif

%post
%install_info --info-dir="%_infodir" "%_infodir/%name".info*

%postun
%install_info_delete --info-dir="%_infodir" "%_infodir/%name".info*

%files
%doc ChangeLog README
%license COPYING
%_bindir/lziprecover
%_mandir/man1/lziprecover.1*
%_infodir/lziprecover.info*

%changelog
