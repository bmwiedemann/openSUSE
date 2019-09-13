#
# spec file for package libfido2
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


%define sover  1
Name:           libfido2
Version:        1.1.0
Release:        0
Summary:        FIDO U2F and FIDO 2.0 protocols
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
URL:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/libfido2/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/libfido2/Releases/%{name}-%{version}.tar.gz.sig
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libhidapi-devel
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcbor)

%description
Provides library functionality for communicating with a FIDO device
over USB as well as verifying attestation and assertion signatures.

%package     -n %{name}-%{sover}
Summary:        FIDO U2F and FIDO 2.0 protocols
Group:          System/Libraries
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
Requires:       libhidapi-devel
Requires:       libopenssl-1_1-devel
Conflicts:      libfido2-0_4_0

%description -n %{name}-devel
This package contains the header file needed to develop applications that
use FIDO U2F and FIDO 2.0 protocols.

%package     -n %{name}-utils
Summary:        Utility programs making use of libfido2, a library for FIDO U2F and FIDO 2.0
Group:          Development/Tools/Other
Conflicts:      libfido2-0_4_0

%description -n %{name}-utils
This package contains utilities to use FIDO U2F and FIDO 2.0 protocols.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCBOR_LIBRARY_DIRS=%{_libdir} -DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}

%install
pushd build
%make_install
popd
find %{buildroot} -type f -name "*.a" -delete -print

%post   -n %{name}-%{sover} -p /sbin/ldconfig
%postun -n %{name}-%{sover} -p /sbin/ldconfig

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

%files -n %{name}-utils
%{_bindir}/fido2-*
%{_mandir}/man1/*

%changelog
