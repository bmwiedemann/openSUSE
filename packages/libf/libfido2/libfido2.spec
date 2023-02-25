#
# spec file for package libfido2
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


%define sover  1
Name:           libfido2
Version:        1.13.0
Release:        0
Summary:        FIDO U2F and FIDO 2.0 protocols
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/libfido2/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/libfido2/Releases/%{name}-%{version}.tar.gz.sig
BuildRequires:  cmake
BuildRequires:  gcc-c++
%if 0%{?suse_version} >= 1540 || 0%{?sle_version} >= 150400
BuildRequires:  libopenssl-3-devel
%else
BuildRequires:  pkgconfig(openssl)
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hidapi-hidraw)
BuildRequires:  pkgconfig(libcbor)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(zlib)

%description
Provides library functionality for communicating with a FIDO device
over USB as well as verifying attestation and assertion signatures.

%package     -n %{name}-%{sover}
Summary:        FIDO U2F and FIDO 2.0 protocols
Group:          Development/Libraries/C and C++
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{name}-%{sover}
This library supports the FIDO U2F and FIDO 2.0 protocols for
communicating with a USB authenticator via the
Client-to-Authenticator Protocol (CTAP 1 and 2).

%package     -n %{name}-devel
Summary:        Development files for FIDO U2F and FIDO 2.0 protocols
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{sover} = %{version}
Requires:       openssl-devel
Conflicts:      libfido2-0_4_0
Conflicts:      libfido2-1_0_0

%description -n %{name}-devel
This package contains the header file needed to develop applications that
use FIDO U2F and FIDO 2.0 protocols.

%package     -n %{name}-utils
Summary:        Utility programs making use of libfido2, a library for FIDO U2F and FIDO 2.0
Group:          Hardware/Other
Conflicts:      libfido2-0_4_0
Conflicts:      libfido2-1_0_0

%description -n %{name}-utils
This package contains utilities to use FIDO U2F and FIDO 2.0 protocols.

%package      -n %{name}-udev
Summary:        Udev rules for libfido2
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description -n %{name}-udev
This package contains the udev rules for FIDO2 compatible devices.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCBOR_LIBRARY_DIRS=%{_libdir} \
    -DBUILD_EXAMPLES=OFF \
    -DUSE_HIDAPI=ON \
    -DNFC_LINUX=ON
%cmake_build

%install
%cmake_install

# Remove Debian specific plugdev setting from udev rules
sed -i -e 's/, GROUP="plugdev"//g ; s/, MODE="0660"//g' udev/70-u2f.rules
# u2f-host has the same udev rule, use a different name
mkdir -p %{buildroot}%{_udevrulesdir}
install -m 0644 udev/70-u2f.rules %{buildroot}%{_udevrulesdir}/70-fido2.rules

find %{buildroot} -type f -name "*.a" -delete -print

%post   -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

%post udev
%{udev_rules_update}

%postun udev
%{udev_rules_update}

%files -n %{name}-%{sover}
%license LICENSE
%doc README.adoc
%{_libdir}/%{name}.so.*

%files -n %{name}-devel
%{_includedir}/*.h
%dir %{_includedir}/fido
%{_includedir}/fido/*.h
%{_libdir}/%{name}.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/*

%files udev
%{_udevrulesdir}/70-fido2.rules

%files -n %{name}-utils
%{_bindir}/fido2-*
%{_mandir}/man1/*

%changelog
