#
# spec file for package lockdev
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


%bcond_with lockdev_debug

Name:           lockdev
Summary:        A library for locking devices
License:        LGPL-2.0-only
Group:          System/Base
Version:        1.0.3_git201003141408
Release:        0
Url:            http://packages.debian.org/unstable/source/lockdev
#Source0:        http://ftp.debian.org/debian/pool/main/l/lockdev/%{name}_%{version}.orig.tar.gz
Source0:        http://ftp.debian.org/debian/pool/main/l/lockdev/%{name}-%{version}.tar.bz2
Source90:       baselibs.conf
Patch0:         lockdev-drop-baudboy.h.diff
Patch1:         lockdev-fix-implicit-declarations.diff
Patch2:         lockdev-reserve-some-space-to-avoid-buffer-overflow.diff
Patch3:         lockdev-pie.diff
Patch4:         sysmacros.patch
#
Requires(pre):  pwdutils permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
BuildRequires:  libtool
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package -n liblockdev1
Summary:        The header files for the lockdev library
Group:          System/Base
Requires:       /usr/sbin/lockdev
Requires(post): glibc
Requires(postun): glibc

%description -n liblockdev1
Lockdev provides a reliable way to put an exclusive lock to devices
using both FSSTND and SVr4 methods.

%package devel
Summary:        A library for locking devices
Group:          Development/Libraries/C and C++
Requires:       lockdev = %{version}
Recommends:     pkg-config

%description devel
The lockdev library provides a reliable way to put an exclusive lock
on devices using both FSSTND and SVr4 methods. The lockdev-devel
package contains the development headers.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
cat > VERSION <<EOF
Package: lockdev
Version: %version
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

%check
objdump -p src/.libs/lockdev | grep -q "NEEDED.*liblockdev.so.1"

%install
%makeinstall
#
# no need for this
rm -f %{buildroot}/%{_libdir}/*.la
#
mkdir -p $RPM_BUILD_ROOT/var/lock

%pre
getent group lock >/dev/null || groupadd -r lock || :

%post
%set_permissions /usr/sbin/lockdev

%post -n liblockdev1 -p /sbin/ldconfig

%postun -n liblockdev1 -p /sbin/ldconfig

%verifyscript
%verify_permissions -e /usr/sbin/lockdev

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING AUTHORS
%verify(not mode) %attr(2755,root,lock) %{_sbindir}/lockdev
%{_mandir}/man8/*

%files -n liblockdev1
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/lockdev.pc
%{_mandir}/man3/*
%{_includedir}/*

%changelog
