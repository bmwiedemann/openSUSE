#
# spec file for package libjansson
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


%define lname   libjansson4
Name:           libjansson
Version:        2.14
Release:        0
Summary:        C library for encoding, decoding and manipulating JSON data
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://digip.org/jansson/
#Git-Clone:     git://github.com/akheron/jansson
Source0:        https://github.com/akheron/jansson/releases/download/v%{version}/jansson-%{version}.tar.bz2
Source1:        baselibs.conf
Source2:        https://github.com/akheron/jansson/releases/download/v%{version}/jansson-%{version}.tar.bz2.asc
Source3:        %{name}.keyring
BuildRequires:  pkgconfig

%description
Jansson is a C library for encoding, decoding and manipulating JSON data.
It features:
 * Simple and intuitive API and data model
 * Comprehensive documentation
 * No dependencies on other libraries
 * Full Unicode support (UTF-8)
 * Extensive test suite

%package -n %{lname}
Summary:        C library for encoding, decoding and manipulating JSON data
Group:          Development/Libraries/C and C++

%description -n %{lname}
Jansson is a C library for encoding, decoding and manipulating JSON data.
It features:
 * Simple and intuitive API and data model
 * Comprehensive documentation
 * No dependencies on other libraries
 * Full Unicode support (UTF-8)
 * Extensive test suite

%package devel
Summary:        Development files for libjansson
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Jansson is a C library for encoding, decoding and manipulating JSON data.
It features:
 * Simple and intuitive API and data model
 * Comprehensive documentation
 * No dependencies on other libraries
 * Full Unicode support (UTF-8)
 * Extensive test suite

%prep
%setup -q -n jansson-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libjansson.so.4*

%files devel
%{_includedir}/jansson.h
%{_includedir}/jansson_config.h
%{_libdir}/libjansson.so
%{_libdir}/pkgconfig/jansson.pc

%changelog
