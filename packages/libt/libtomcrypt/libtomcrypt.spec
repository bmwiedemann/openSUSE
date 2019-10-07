#
# spec file for package libtomcrypt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2009 Exata T.I., Maringa, PR, Brasil.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         soname libtomcrypt1
Name:           libtomcrypt
Version:        1.18.2
Release:        0
Summary:        Cryptographic Toolkit Written in Portable C
License:        SUSE-Public-Domain
Group:          Development/Libraries/C and C++
Url:            http://libtom.org
Source0:        https://github.com/libtom/libtomcrypt/releases/download/v%{version}/crypt-%{version}.tar.xz
Source1:        https://github.com/libtom/libtomcrypt/releases/download/v%{version}/crypt-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source4:        baselibs.conf
BuildRequires:  libtommath-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
LibTomCrypt is a fairly comprehensive, modular and portable cryptographic
toolkit that provides developers with a vast array of well known published
block ciphers, one-way hash functions, chaining modes, pseudo-random number
generators, public key cryptography and a plethora of other routines.

%package -n %{soname}
Summary:        Cryptographic toolkit with ciphers, hashes, PRNG and PKI
Group:          System/Libraries

%description -n %{soname}
LibTomCrypt is a fairly comprehensive, modular and portable cryptographic
toolkit that provides developers with a vast array of well known published
block ciphers, one-way hash functions, chaining modes, pseudo-random
numbergenerators, public key cryptography and a plethora of other routines.

This package contains shared libraries

%package devel
Summary:        Development Files for LibTomCrypt
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}

%description devel
LibTomCrypt is a fairly comprehensive, modular and portable cryptographic
toolkit that provides developers with a vast array of well known published
block ciphers, one-way hash functions, chaining modes, pseudo-random
numbergenerators, public key cryptography and a plethora of other routines.

This package contains headers and other development files.

%package examples
Summary:        Example Files for LibTomCrypt
Group:          Documentation/Other
Requires:       %{name}-devel = %{version}

%description examples
LibTomCrypt is a fairly comprehensive, modular and portable cryptographic
toolkit that provides developers with a vast array of well known published
block ciphers, one-way hash functions, chaining modes, pseudo-random
numbergenerators, public key cryptography and a plethora of other routines.

This package contains example *.c files showing how to use TomCrypt library.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="%{optflags} -DLTM_DESC -DUSE_LTM"
make %{?_smp_mflags} LIBPATH=%{_libdir} EXTRALIBS="-ltommath" -f makefile.shared

%install
%make_install -f makefile.shared DESTDIR=%{buildroot} LIBPATH=%{_libdir} NODOCS=0 PREFIX=%{_prefix}
# Remove static libraries (It's upstream bug in makefile.shared I think.)
rm %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print

%check

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%{_libdir}/libtomcrypt.so.*
%license LICENSE
%doc README.md

%files devel
%attr(0644,root,root) %{_includedir}/tomcrypt*.h
%{_libdir}/libtomcrypt.so
%{_libdir}/pkgconfig/libtomcrypt.pc

%files examples
%doc demos

%changelog
