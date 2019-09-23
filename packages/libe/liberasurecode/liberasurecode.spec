#
# spec file for package liberasurecode
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libsoname liberasurecode1
Name:           liberasurecode
Version:        1.6.1
Release:        0
Summary:        Erasure Code API library with pluggable Erasure Code backends
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/openstack/liberasurecode
Source0:        https://github.com/openstack/liberasurecode/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(zlib)

%description
liberasurecode is an Erasure Code API library written in C with
pluggable Erasure Code backends.

%package -n %{libsoname}
Summary:        Erasure Code API library with pluggable Erasure Code backends
Group:          System/Libraries

%description -n %{libsoname}
liberasurecode is an Erasure Code API library written in C with
pluggable Erasure Code backends.

%package devel
Summary:        Development files for liberasurecode
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}

%description devel
Development files for the Unified Erasure Coding interface.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static --disable-mmi
make %{?_smp_mflags}

%install
%make_install

%check
make test

%post -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%if 0%{?suse_version} > 1315
%license COPYING
%else
%doc COPYING
%endif
%doc ChangeLog README.md
%{_libdir}/libXorcode.so.*
%{_libdir}/liberasurecode.so.*
%{_libdir}/libnullcode.so.*
%{_libdir}/liberasurecode_rs_vand.so.*

%files devel
%{_includedir}/liberasurecode
%{_includedir}/config_liberasurecode.h
%{_includedir}/erasurecode*.h
%{_libdir}/libXorcode.la
%{_libdir}/libXorcode.so
%{_libdir}/liberasurecode.la
%{_libdir}/liberasurecode.so
%{_libdir}/libnullcode.la
%{_libdir}/libnullcode.so
%{_libdir}/liberasurecode_rs_vand.la
%{_libdir}/liberasurecode_rs_vand.so
%{_libdir}/pkgconfig/erasurecode-1.pc

%changelog
