#
# spec file for package fipscheck
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


%define lname libfipscheck1
%global soversion 1.2.1
%global somajor 1
Name:           fipscheck
Version:        1.5.0
Release:        0
Summary:        A library for integrity verification of FIPS validated modules
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://releases.pagure.org/%{name}/
Source0:        https://releases.pagure.org/fipscheck/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch1:         fipscheck-dont_generate_manpages.patch
Patch2:         fipscheck-fips.h_not_needed.patch
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
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static --libdir=/%{_lib}

make %{?_smp_mflags} LDFLAGS="-Wl,-z,relro"

# Add generation of HMAC checksums of the final stripped binaries
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %__os_install_post \
    %{buildroot}%{_bindir}/fipshmac %{buildroot}%{_bindir}/fipscheck \
    %{buildroot}%{_bindir}/fipshmac %{buildroot}/%{_lib}/libfipscheck.so.%{soversion} \
    ln -s .libfipscheck.so.%{soversion}.hmac %{buildroot}/%{_lib}/.libfipscheck.so.%{somajor}.hmac \
%{nil}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_libdir}
ln -s  /%{_lib}/libfipscheck.so.%{soversion} %{buildroot}%{_libdir}/libfipscheck.so
rm %{buildroot}/%{_lib}/libfipscheck.so

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README AUTHORS
%{_bindir}/fipscheck
%{_bindir}/.fipscheck.hmac
%{_bindir}/fipshmac

%files -n %{lname}
/%{_lib}/libfipscheck.so.*
/%{_lib}/.libfipscheck.so.*
%{_mandir}/man8/*.8%{?ext_man}

%files devel
%{_includedir}/fipscheck.h
%{_libdir}/libfipscheck.so
%{_mandir}/man3/*.3%{?ext_man}

%changelog
