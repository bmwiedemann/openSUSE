#
# spec file for package npth
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


%define lname	libnpth0
Name:           npth
Version:        1.8
Release:        0
Summary:        GNU Portable Threads library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://gnupg.org/software/npth/
#Git-Clone:	git://git.gnupg.org/npth
#DL-URL:        https://gnupg.org/download/index.html#npth
Source:         https://gnupg.org/ftp/gcrypt/%name/%name-%version.tar.bz2
Source2:        https://gnupg.org/ftp/gcrypt/%name/%name-%version.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source4:        https://gnupg.org/signature_key.asc#/%name.keyring
Source99:       %name.changes

%description
nPth is a non-preemptive threads implementation using an API
similar to the one in GNU Pth. In contrast to Pth, nPth is
based on the system's standard threads implementation. Thus, nPth
allows the use of libraries which are not compatible to GNU Pth.

%package -n %lname
Summary:        GNU Portable Threads library
Group:          System/Libraries

%description -n %lname
nPth is a non-preemptive threads implementation using an API
similar to the one in GNU Pth. In contrast to Pth, nPth is
based on the system's standard threads implementation. Thus, nPth
allows the use of libraries which are not compatible to GNU Pth.

%package devel
Summary:        Development files for the GNU New Portable Threads library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
nPth is a non-preemptive threads implementation using an API
similar to the one in GNU Pth.

This subpackage contains the headers for npth.

%prep
%autosetup -p1

%build
date=$(date -u "+%%Y-%%m-%%dT%%H:%%M+0000" -r %SOURCE99)
%configure \
	--enable-build-timestamp="$date"
%make_build

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING.LIB
%_libdir/libnpth.so.*

%files devel
%license COPYING.LIB
%doc AUTHORS ChangeLog NEWS README
%_libdir/libnpth.so
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/aclocal/*

%changelog
