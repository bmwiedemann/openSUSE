#
# spec file for package xxhash
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xxhash
Version:        0.8.0
Release:        0
Summary:        Non-cryptographic hash algorithm
License:        GPL-2.0-only AND BSD-2-Clause
Group:          Productivity/Security
URL:            https://github.com/Cyan4973/xxHash
Source0:        https://github.com/Cyan4973/xxHash/archive/v%{version}.tar.gz#/xxHash-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig

%description
xxHash is a hash algorithm. It completes the SMHasher test suite which
evaluates collision, dispersion and randomness qualities of hash functions.
Hashes are identical on all platforms.

%package -n libxxhash0
Summary:        Shared library for xxHash - a non-cryptographic hash algorithm
License:        BSD-2-Clause
Group:          System/Libraries

%description -n libxxhash0
Shared library for xxHash - a hash algorithm. It completes the SMHasher test
suite which evaluates collision, dispersion and randomness qualities of hash
functions. Hashes are identical on all platforms.

%package devel
Summary:        Development files for xxHash - a non-cryptographic hash algorithm
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libxxhash0 = %{version}

%description devel
Development files for xxHash - a hash algorithm. It completes the SMHasher test
suite which evaluates collision, dispersion and randomness qualities of hash
functions. Hashes are identical on all platforms.

%prep
%setup -q -n xxHash-%{version}

%build
make %{?_smp_mflags} prefix=%{_prefix} libdir=%{_libdir}

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
rm -rf %{buildroot}%{_libdir}/libxxhash.a

%check
make test

%post -n libxxhash0 -p /sbin/ldconfig
%postun -n libxxhash0 -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_bindir}/xxhsum
%{_bindir}/xxh32sum
%{_bindir}/xxh64sum
%{_bindir}/xxh128sum
%{_mandir}/man1/xxh32sum.*
%{_mandir}/man1/xxh64sum.*
%{_mandir}/man1/xxh128sum.*
%{_mandir}/man1/xxhsum.*

%files -n libxxhash0
%{_libdir}/libxxhash.so.*

%files devel
%{_includedir}/xxhash.h
%{_includedir}/xxh3.h
%{_libdir}/pkgconfig/libxxhash.pc
%{_libdir}/libxxhash.so

%changelog
