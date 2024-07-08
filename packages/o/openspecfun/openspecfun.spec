#
# spec file for package openspecfun
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


%define so_ver  2
%define libname lib%{name}%{so_ver}
Name:           openspecfun
Version:        0.5.6
Release:        0
Summary:        A collection of special mathematical functions
License:        MIT
Group:          System/Libraries
URL:            https://github.com/JuliaMath/openspecfun
Source0:        https://github.com/JuliaMath/openspecfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-fortran

%description
Openspecfun provides AMOS and Faddeeva. AMOS (from Netlib) is a portable package
for Bessel Functions of a Complex Argument and Nonnegative Order; it contains
subroutines for computing Bessel functions and Airy functions. Faddeeva allows
computing the various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled complementary
error function, imaginary error function, and Dawson function); given these,
one can also easily compute Voigt functions, Fresnel integrals, and similar
related functions as well.

%package     -n %{libname}
Summary:        A collection of special mathematical functions
Group:          System/Libraries

%description -n %{libname}
Openspecfun provides AMOS and Faddeeva. AMOS (from Netlib) is a portable package
for Bessel Functions of a Complex Argument and Nonnegative Order; it contains
subroutines for computing Bessel functions and Airy functions. Faddeeva allows
computing the various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled complementary
error function, imaginary error function, and Dawson function); given these,
one can also easily compute Voigt functions, Fresnel integrals, and similar
related functions as well.

%package        devel
Summary:        A collection of special mathematical functions
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description    devel
Openspecfun provides AMOS and Faddeeva. AMOS (from Netlib) is a portable package
for Bessel Functions of a Complex Argument and Nonnegative Order; it contains
subroutines for computing Bessel functions and Airy functions. Faddeeva allows
computing the various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled complementary
error function, imaginary error function, and Dawson function); given these,
one can also easily compute Voigt functions, Fresnel integrals, and similar
related functions as well.

%prep
%setup -q

%build
%make_build \
     FFLAGS="%{optflags}" \
     CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot} \
             prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir}

rm %{buildroot}/%{_libdir}/libopenspecfun.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libopenspecfun.so.%{so_ver}*

%files devel
%license LICENSE.md
%doc README.md
%{_libdir}/libopenspecfun.so
%{_includedir}/Faddeeva.h

%changelog
