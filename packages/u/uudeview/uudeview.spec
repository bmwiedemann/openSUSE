#
# spec file for package uudeview
#
# Copyright (c) 2025 SUSE LLC
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


Name:           uudeview
BuildRequires:  autoconf
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
URL:            http://www.fpx.de/fp/Software/UUDeview
Suggests:       /sbin/sendmail
Version:        0.5.20
Release:        0
Summary:        The Nice and Friendly Decoder
License:        GPL-2.0-or-later
Group:          Productivity/Networking/News/Utilities
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}.patch
Patch1:         %{name}-matherr.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The UUDeview package contains a very smart decoder and an encoder for
Base64 (MIME), uuencoded, xxencoded, Binhex, and yEnc files. Its
ultimate goal is to fully replace the "standard", but dumb uudecode and
uuencode utilities.

%prep
%setup -q
%patch -P 0
%patch -P 1 -p2

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
autoconf
CFLAGS="$RPM_OPT_FLAGS -fPIC -DUSE_NON_CONST" \
./configure --prefix=%_prefix \
	--libdir=%_libdir \
	--disable-minews \
	--enable-sendmail=/sbin/sendmail \
	--enable-tcl=%_libdir \
	--enable-tk=%_libdir
make

%install
make prefix=%buildroot%_prefix MANDIR=%buildroot%_mandir install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
cp -pf uulib/libuu.a %buildroot%_libdir
cp -pf uulib/uudeview.h %buildroot%_includedir

%files
%defattr(-,root,root)
%_libdir/lib*
%_includedir/*
/usr/bin/uudeview
/usr/bin/uuenview
/usr/bin/uuwish
/usr/bin/xdeview
%doc HISTORY README
%doc %{_mandir}/man1/uudeview.1.gz
%doc %{_mandir}/man1/uuenview.1.gz
%doc %{_mandir}/man1/xdeview.1.gz

%changelog
