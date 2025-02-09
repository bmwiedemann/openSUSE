#
# spec file for package liberasurecode
#
# Copyright (c) 2021 SUSE LLC
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


%define libsoname liberasurecode1
Name:           liberasurecode
Version:        1.6.5
Release:        0
Summary:        Erasure Code API library with pluggable Erasure Code backends
License:        BSD-3-Clause
URL:            https://github.com/openstack/liberasurecode
Source0:        https://github.com/openstack/liberasurecode/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
liberasurecode is an Erasure Code API library written in C with
pluggable Erasure Code backends.

%package -n %{libsoname}
Summary:        Erasure Code API library with pluggable Erasure Code backends

%description -n %{libsoname}
liberasurecode is an Erasure Code API library written in C with
pluggable Erasure Code backends.

%package devel
Summary:        Development files for liberasurecode
Requires:       %{libsoname} = %{version}

%description devel
Development files for the Unified Erasure Coding interface.

%prep
%autosetup -p1

%build
./autogen.sh
%configure \
	--disable-static \
	--disable-mmi \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build test

%ldconfig_scriptlets -n %{libsoname}

%files -n %{libsoname}
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libXorcode.so.*
%{_libdir}/liberasurecode.so.*
%{_libdir}/libnullcode.so.*
%{_libdir}/liberasurecode_rs_vand.so.*

%files devel
%license COPYING
%{_includedir}/liberasurecode
%{_includedir}/config_liberasurecode.h
%{_includedir}/erasurecode*.h
%{_libdir}/libXorcode.so
%{_libdir}/liberasurecode.so
%{_libdir}/libnullcode.so
%{_libdir}/liberasurecode_rs_vand.so
%{_libdir}/pkgconfig/erasurecode-1.pc

%changelog
