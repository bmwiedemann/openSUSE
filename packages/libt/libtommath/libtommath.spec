#
# spec file for package libtommath
#
# Copyright (c) 2024 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libtommath
%define libsoname %{name}1
Version:        1.3.0
Release:        0
Summary:        Routines For a Integer Based Number Theoretic Applications
License:        Unlicense
Group:          System/Libraries
URL:            https://github.com/libtom/libtommath
Source:         https://github.com/libtom/libtommath/releases/download/v%{version}/ltm-%{version}.tar.xz
Source2:        https://github.com/libtom/libtommath/releases/download/v%{version}/ltm-%{version}.tar.xz.asc
Source3:        %{name}.keyring
Source4:        baselibs.conf
Source5:        libtommath-rpmlintrc
BuildRequires:  dos2unix
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?suse_build_hwcaps_libs}

%description
LibTomMath provides highly optimized and portable routines for a vast
majority of integer based number theoretic applications (including public
key cryptography). LibTomMath is not a cryptographic toolkit itself but it
can be used to write one [Used in LibTomCrypt for RSA, DH and ECC public key
routines].

%package -n %{libsoname}
Summary:        Routines For a Integer Based Number Theoretic Applications
Group:          System/Libraries

%description -n %{libsoname}
LibTomMath provides highly optimized and portable routines for a vast
majority of integer based number theoretic applications (including public
key cryptography). LibTomMath is not a cryptographic toolkit itself but it
can be used to write one [Used in LibTomCrypt for RSA, DH and ECC public key
routines].

%package devel
Summary:        Development files for LibTomMath
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Provides:       libtommath0-devel = %{version}
Obsoletes:      libtommath0-devel < 1

%description devel
Headers and other development files for TomMath library.

LibTomMath provides highly optimized and portable routines for a vast
majority of integer based number theoretic applications (including public
key cryptography). LibTomMath is not a cryptographic toolkit itself but it
can be used to write one [Used in LibTomCrypt for RSA, DH and ECC public key
routines].

%package examples
Summary:        Example files for LibTomMath
Group:          Development/Libraries/Other
Provides:       libtommath0-examples = %{version}
Obsoletes:      libtommath0-examples < 1
BuildArch:      noarch

%description examples
Demo *.c files showing how to use TomMath library.

LibTomMath provides highly optimized and portable routines for a vast
majority of integer based number theoretic applications (including public
key cryptography). LibTomMath is not a cryptographic toolkit itself but it
can be used to write one [Used in LibTomCrypt for RSA, DH and ECC public key
routines].

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} LIBPATH=%{_libdir} -f makefile.shared

%check
make %{?_smp_mflags} test_standalone
./test
rm -f demo/*.o

%install
dos2unix etc/timer.asm
make DESTDIR=%{buildroot} LIBPATH=%{_libdir} INCPATH=%{_includedir} %{?_smp_mflags} -f makefile.shared install
# we don't want to ship any static libraries or .la files
find %{buildroot} -type f \( -name '*.a' -o -name '*.la' \) -delete -print
chmod +x %{buildroot}%{_libdir}/libtommath.so.*

%post -n %{libsoname} -p /sbin/ldconfig

%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root)
%if (0%{?suse_version} >= 1500) || (0%{?sle_version} >= 120300)
%license LICENSE
%else
%doc LICENSE
%endif
%doc changes.txt
%{_libdir}/libtommath.so.*

%files devel
%defattr(-,root,root)
%attr(0644,root,root) %{_includedir}/tommath*.h
%{_libdir}/libtommath.so
%{_libdir}/pkgconfig/libtommath.pc

%files examples
%defattr(-,root,root)
%doc demo etc mtest pre_gen

%changelog
