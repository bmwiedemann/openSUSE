#
# spec file for package fipscheck
#
# Copyright (c) 2024 SUSE LLC
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


%define lname libfipscheck1
%global soversion 1.2.1
%global somajor 1
Name:           fipscheck
Version:        1.7.0
Release:        0
Summary:        A library for integrity verification of FIPS validated modules
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/LairdCP/fipscheck
Source0:        fipscheck-%version.tar.bz2
Source1:        baselibs.conf
Patch0:         fipscheck-fix_check_openssl_version.patch
Patch1:         fipscheck-fix_incorrect_length_type.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
Requires:       %{lname} = %{version}

%description
FIPSCheck is a library for integrity verification of FIPS validated
modules. The package also provides helper binaries for creation and
verification of the HMAC-SHA256 checksum files.

%package -n %{lname}
Summary:        Library files for %{name}
Group:          System/Libraries
Requires:       %{_bindir}/fipscheck

%description -n %{lname}
This package contains the FIPSCheck library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure --disable-static

make %{?_smp_mflags} LDFLAGS="-Wl,-z,relro"

# Add generation of HMAC checksums of the final stripped binaries
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %__os_install_post \
    %{buildroot}%{_bindir}/fipshmac %{buildroot}%{_bindir}/fipscheck \
    %{buildroot}%{_bindir}/fipshmac %{buildroot}/%{_libdir}/libfipscheck.so.%{soversion} \
    ln -s .libfipscheck.so.%{soversion}.hmac %{buildroot}/%{_libdir}/.libfipscheck.so.%{somajor}.hmac \
%{nil}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README AUTHORS
%{_bindir}/fipscheck
%{_bindir}/.fipscheck.hmac
%{_bindir}/fipshmac

%files -n %{lname}
%{_libdir}/libfipscheck.so.*
%{_libdir}/.libfipscheck.so.*
%{_mandir}/man8/*.8%{?ext_man}

%files devel
%{_includedir}/fipscheck.h
%{_libdir}/libfipscheck.so
%{_mandir}/man3/*.3%{?ext_man}

%changelog
