#
# spec file for package lockdev
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


%bcond_with lockdev_debug
Name:           lockdev
Version:        1.0.3_git201003141408
Release:        0
Summary:        A library for locking devices
License:        LGPL-2.0-only
Group:          System/Base
URL:            https://packages.debian.org/unstable/source/lockdev
#Source0:        http://ftp.debian.org/debian/pool/main/l/lockdev/%{name}_%{version}.orig.tar.gz
Source0:        http://ftp.debian.org/debian/pool/main/l/lockdev/%{name}-%{version}.tar.bz2
Source21:       tmpfiles-lockdev.conf
Source90:       baselibs.conf
Patch0:         lockdev-drop-baudboy.h.diff
Patch1:         lockdev-fix-implicit-declarations.diff
Patch2:         lockdev-reserve-some-space-to-avoid-buffer-overflow.diff
Patch3:         lockdev-pie.diff
Patch4:         sysmacros.patch
Patch5:         lockdev-debug.diff
#
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires(pre):  permissions
Requires(pre):  group(lock)

%description
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package -n liblockdev1
Summary:        The header files for the lockdev library
Group:          System/Base
Requires:       %{_sbindir}/lockdev
Requires(post): glibc
Requires(postun):glibc

%description -n liblockdev1
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package devel
Summary:        A library for locking devices
Group:          Development/Libraries/C and C++
Requires:       lockdev = %{version}
Recommends:     pkgconfig

%description devel
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods. The lockdev-devel
package contains the development headers.

%prep
%autosetup -p1

%build
cat > VERSION <<EOF
Package: lockdev
Version:        %{version}
Release-Date: Unreleased
Released-By: Unreleased
EOF
touch ChangeLog
mkdir -p m4
autoreconf -f -i
%configure \
	--disable-silent-rules \
	--enable-helper \
	%{?with_lockdev_debug:--enable-debug}
#
make %{?_smp_mflags}
#

%check
objdump -p src/.libs/lockdev | grep -q "NEEDED.*liblockdev.so.1"

%install
%make_install
#
# no need for this
find %{buildroot} -type f -name "*.la" -delete -print
#
install -D -m644 %{SOURCE21} %{buildroot}%{_tmpfilesdir}/lockdev.conf

%post
%tmpfiles_create lockdev.conf
%set_permissions %{_sbindir}/lockdev

%post -n liblockdev1 -p /sbin/ldconfig
%postun -n liblockdev1 -p /sbin/ldconfig

%verifyscript
%verify_permissions -e %{_sbindir}/lockdev

%files
%license COPYING
%doc AUTHORS
%verify(not mode) %attr(2755,root,lock) %{_sbindir}/lockdev
%{_mandir}/man8/*
%{_tmpfilesdir}/lockdev.conf

%files -n liblockdev1
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/lockdev.pc
%{_mandir}/man3/*
%{_includedir}/*

%changelog
