#
# spec file for package libtpms
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


%define lname libtpms0
Name:           libtpms
Version:        0.9.3
Release:        0
Summary:        Library providing Trusted Platform Module (TPM) functionality
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/stefanberger/libtpms
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  mozilla-nspr-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package -n %{lname}
Summary:        Library providing Trusted Platform Module (TPM) functionality
Group:          Development/Libraries/C and C++

%description -n %{lname}
A library providing TPM functionality for VMs. Targeted for integration
into Qemu.

%package        devel
Summary:        Include files for libtpms
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libopenssl-devel
Requires:       mozilla-nspr-devel

%description   devel
Libtpms header files and documentation.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure         \
    --with-tpm2    \
    --with-openssl \
    --disable-static

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}

%check
# fix check-local
# https://bugzilla.suse.com/show_bug.cgi?id=1204556#c9
sed -i "s@\(-L\./\.libs\)@\1 -Wl,--no-as-needed@" src/Makefile
%make_build check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%doc README CHANGES
%license LICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*%{?ext_man}

%changelog
