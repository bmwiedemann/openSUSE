#
# spec file for package libite
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


%define sover 5
Name:           libite
Version:        2.0.2
Release:        0
Summary:        BSD function library
License:        MIT AND X11
Group:          Development/Languages/C and C++
URL:            https://github.com/troglobit/libite/
Source:         https://github.com/troglobit/libite/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
A library that extends the GNU libc with some functions and macros from BSD,
most notably the string functions strlcpy(3), strlcat(3) and the *BSD
sys/queue.h and sys/tree.h APIs.

glibc is not offering the _SAFE macros from the BSD sys/queue.h API —
recommended when traversing lists to delete/free nodes.

%package -n libite%{sover}
Summary:        BSD function library
Group:          System/Libraries

%description -n libite%{sover}
A library that extends the GNU libc with some functions and macros from BSD,
most notably the string functions strlcpy(3), strlcat(3) and the *BSD
sys/queue.h and sys/tree.h APIs.

glibc is not offering the _SAFE macros from the BSD sys/queue.h API —
recommended when traversing lists to delete/free nodes.

%package devel
Summary:        Header files for libite
Group:          Development/Libraries/C and C++
Requires:       libite%{sover} = %{version}

%description devel
Development and header files for libite.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}/%{_datadir}/doc

%post   -n libite%{sover} -p /sbin/ldconfig
%postun -n libite%{sover} -p /sbin/ldconfig

%files -n libite%{sover}
%doc ChangeLog.md HACKING.md README.md
%license LICENSE
%{_libdir}/libite.so.%{sover}*

%files devel
%{_includedir}/lite
%{_libdir}/libite.so
%{_libdir}/pkgconfig/libite.pc

%changelog
