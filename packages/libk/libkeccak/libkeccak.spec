#
# spec file for package libkeccak
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


%define lname libkeccak1
Name:           libkeccak
Version:        1.3.1.2
Release:        0
Summary:        Keccak family hashing library, including SHA-3
License:        ISC
Group:          Development/Libraries/C and C++
URL:            https://github.com/maandree/libkeccak
Source:         https://github.com/maandree/libkeccak/archive/refs/tags/%version.tar.gz

%description
libkeccak is a bit-oriented lanewise implementation of the Keccak
family with support for extend output size, state marshalling,
algorithm tuning with implicit parameters, secure erasure of
sensitive data, and HMAC.

A subset of Keccak was specified by NIST as SHA-3 (Secure Hash Algorithm 3).

%package devel
Summary:        Development files for %name
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libkeccak is a bit-oriented lanewise implementation of the Keccak
family with support for extend output size, state marshalling,
algorithm tuning with implicit parameters, secure erasure of
sensitive data, and HMAC.

A subset of Keccak was specified by NIST as SHA-3 (Secure Hash Algorithm 3).
This package contains the files required for development with %name.

%package -n %lname
Summary:        Keccak family hashing library, including SHA-3
Group:          System/Libraries

%description -n %lname
libkeccak is a bit-oriented lanewise implementation of the Keccak
family with support for extend output size, state marshalling,
algorithm tuning with implicit parameters, secure erasure of
sensitive data, and HMAC.

A subset of Keccak was specified by NIST as SHA-3 (Secure Hash Algorithm 3).

%prep
%autosetup -p1

%build
%make_build CFLAGS="%optflags" LDFLAGS="" LDOPTIMISE=""

%install
mkdir -p %buildroot%_libdir
%make_install PREFIX=%_prefix
find %buildroot -type f -iname '*.a' -print -delete
if [ "%_lib" != lib ]; then
	mv %buildroot/%_libdir/../lib/* %buildroot/%_libdir/
fi
# packaged via macro
rm -rvf %buildroot%_datadir/licenses/%name

%post -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files devel
%doc DEPENDENCIES README TODO
%license LICENSE
%_libdir/%name.so
%_includedir/*
%_mandir/man3/*.3%{?ext_man}
%_mandir/man7/*.7%{?ext_man}

%files -n %lname
%license LICENSE
%_libdir/%name.so.*

%changelog
