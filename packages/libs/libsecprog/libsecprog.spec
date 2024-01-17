#
# spec file for package libsecprog
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           libsecprog
%define lname	libsecprog0
URL:            http://www.suse.de/~thomas/projects/secproglib/index.html
Summary:        Secure Replacements for Problematic C Functions
Version:        0.8
Release:        142
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Patch1:         %{name}-%{version}_str-with-n-equal-zero.diff
Patch2:         %{name}-%{version}_strliteralcmp.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool

%description
The "Secure Programming Library" provides several functions that should
serve as a replacement for problematic C functions from glibc. Besides
the replacement functions, there are some helper functions, such as
safe_reopen() or sigprotection(), that can be used for developing
exposed applications.

%package -n %lname
Summary:        Secure Replacements for Problematic C Functions
Group:          System/Libraries
# O/P added 2011-11-27
Obsoletes:      libsecprog < %version-%release
Provides:       libsecprog = %version-%release

%description -n %lname
The "Secure Programming Library" provides several functions that should
serve as a replacement for problematic C functions from glibc. Besides
the replacement functions, there are some helper functions, such as
safe_reopen() or sigprotection(), that can be used for developing
exposed applications.

%package devel
Group:          Development/Libraries/C and C++
Summary:        Secure Replacements for Problematic C Functions
Requires:       %lname = %version, glibc-devel

%description devel
The "Secure Programming Library" provides several functions that should
serve as a replacement for problematic C functions from glibc. Besides
the replacement functions there are some helper-functions (like:
safe_reopen() or sigprotection()) that can be used for developing
exposed applications.

%prep
%setup -q -n libsecprog
%patch1 -p1
%patch2 -p0

%build
autoreconf --install
export CFLAGS="$RPM_OPT_FLAGS"
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_libdir/libsecprog.so.0*

%files devel
%defattr(-,root,root)
%_libdir/libsecprog.so
%_includedir/secprog.h
%_mandir/man*/*

%changelog
