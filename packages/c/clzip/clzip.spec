#
# spec file for package clzip
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           clzip
Version:        1.11
Release:        0
%define xversion	1.11
Summary:        Lossless Data Compressor based on LZMA
License:        GPL-2.0-or-later
Group:          Productivity/Archiving/Compression
URL:            http://www.nongnu.org/lzip/clzip.html
Source:         http://download.savannah.gnu.org/releases/lzip/clzip/%name-%xversion.tar.gz
Source2:        http://download.savannah.gnu.org/releases/lzip/clzip/%name-%version.tar.gz.sig
Source3:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): info
Requires(preun):info

%description
Clzip is a lossless data compressor based on the LZMA algorithm, with
very safe integrity checking and a user interface similar to that of
gzip or bzip2. Clzip decompresses almost as fast as gzip and
compresses better than bzip2, which makes it well suited for software
distribution and data archiving. Clzip uses the lzip file format; the
files produced by clzip are fully compatible with lzip-1.4 or newer.
Clzip is, in fact, a C language implementation of lzip, intended for
embedded devices or systems lacking a C++ compiler.

%prep
%autosetup -n %name-%xversion

%build
# not autoconf
mkdir build
pushd build/
../configure --prefix="%_prefix" --bindir="%_bindir" --datadir="%_datadir" \
	--infodir="%_infodir" --mandir="%_mandir" --sysconfdir="%_sysconfdir" \
	CC="%__cc" CFLAGS="%optflags"
make %{?_smp_flags}
popd

%install
pushd build/
%make_install
popd

%check
pushd build/
make %{?_smp_mflags} check
popd

%post
%install_info --info-dir="%_infodir" "%_infodir/clzip.info%ext_info"

%preun
%install_info_delete --info-dir="%_infodir" "%_infodir/clzip.info%ext_info"

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%_bindir/clzip
%_mandir/man1/clzip.1%ext_man
%_infodir/clzip.info%ext_info

%changelog
