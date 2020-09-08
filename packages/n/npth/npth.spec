#
# spec file for package npth
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.6
Release:        0
Summary:        GNU Portable Threads library
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://gnupg.org/
#Git-Clone:	git://git.gnupg.org/npth
#DL-URL:        ftp://ftp.gnupg.org/gcrypt/npth/
Source:         ftp://ftp.gnupg.org/gcrypt/npth/%name-%version.tar.bz2
Source2:        ftp://ftp.gnupg.org/gcrypt/npth/%name-%version.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source4:        %name.keyring
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

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnpth.so.0*

%files devel
%license COPYING.LIB
%doc AUTHORS NEWS ChangeLog README
%_bindir/npth-config
%_includedir/npth.h
%_libdir/libnpth.so
%_datadir/aclocal/

%changelog
