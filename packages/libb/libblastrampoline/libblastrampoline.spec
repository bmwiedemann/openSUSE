#
# spec file for package libblastrampoline
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


%global somajor 5
%global libname libblastrampoline%{somajor}
Name:           libblastrampoline
Version:        5.4.0
Release:        0
Summary:        BLAS/LAPACK demuxer library using PLT trampolines
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/JuliaLinearAlgebra/libblastrampoline
Source:         https://github.com/JuliaLinearAlgebra/libblastrampoline/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  glibc-devel
ExclusiveArch:  x86_64 aarch64

%description
libblastrampoline is a BLAS/LAPACK demuxer library that uses PLT
trampolines and implements a consistent API atop BLAS implementations.

%package -n     %{libname}
Summary:        BLAS/LAPACK demuxer library using PLT trampolines
Group:          System/Libraries

%description -n %{libname}
libblastrampoline is a BLAS/LAPACK demuxer library that uses PLT
trampolines and implements a consistent API atop BLAS implementations
(like OpenBLAS, MKL, etc.) that differ in their function argument
types (e.g. 32-bit vs. 64-bit array indices) and/or function names
(dgemm vs. dgemm_).

%package        devel
Summary:        Headers for libblastrampline, a BLAS/LAPACK demuxer
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description    devel
libblastrampoline is a BLAS/LAPACK demuxer library that uses PLT
trampolines and implements a consistent API atop BLAS implementations.

This package contains the headers for libblastrampoline.

%prep
%autosetup

%build
cd src/
%make_build prefix=%{_prefix}

%install
cd src/
%make_install prefix=%{_prefix}

%fdupes %{buildroot}/%{_prefix}

# Workaround for 64-bit systems
%if "%{?_lib}" == "lib64"
mv -v %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}
%endif

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files devel
%doc README.md
%{_includedir}/%{name}/
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so

%files -n %{libname}
%license LICENSE
%{_libdir}/%{name}.so.%{somajor}*

%changelog
