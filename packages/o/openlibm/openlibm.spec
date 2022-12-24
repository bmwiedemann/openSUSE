#
# spec file for package openlibm
#
# Copyright (c) 2022 SUSE LLC
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


%define so_ver  4
%define libname lib%{name}%{so_ver}
Name:           openlibm
Version:        0.8.1
Release:        0
Summary:        Standalone C mathematical library
License:        BSD-2-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/JuliaLang/openlibm/
Source0:        https://github.com/JuliaLang/openlibm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
ExcludeArch:    ppc riscv64

%description
OpenLibm is an implementation of a standalone C mathematical library
(libm). It can be used standalone in applications and programming
language implementations.

%package     -n %{libname}
Summary:        Standalone C mathematical library
Group:          System/Libraries

%description -n %{libname}
OpenLibm is an implementation of a standalone C mathematical library
(libm). It can be used standalone in applications and programming
language implementations.

The OpenLIBM code derives from the FreeBSD msun implementation,
which in turn derives from FDLIBM 5.3. As a result, it has a number of
fixes and updates that have accumulated over the years in msun,
and also optimized assembly versions of many functions.

%package        devel
Summary:        Development files for openlibm
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
OpenLibm is an implementation of a standalone C mathematical library
(libm). It can be used standalone in applications and programming
language implementations.

This package provides libraries and header files for developing applications
that use OpenLIBM.

%prep
%setup -q

%build
%make_build \
     FFLAGS="%{optflags}" \
     CFLAGS="%{optflags}" \
     LDFLAGS="-Wl,-z,noexecstack" \
%ifarch armv6hl
     MARCH="armv6" \
%endif
%ifarch armv7hl
     MARCH="armv7" \
%endif
     ARCH="%{_arch}"

%install
make install DESTDIR=%{buildroot} \
             prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir}

rm %{buildroot}/%{_libdir}/libopenlibm.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{so_ver}*

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/openlibm/
%{_libdir}/libopenlibm.so
%{_libdir}/pkgconfig/openlibm.pc

%changelog
