#
# spec file for package OpenImageDenoise
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 LISA GmbH, Bingen, Germany.
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


%define sover 0
%define libname lib%{name}%{sover}
%define pkgname oidn
Name:           OpenImageDenoise
Version:        1.2.2
Release:        0
Summary:        Open Image Denoise library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://openimagedenoise.github.io/
Source:         https://github.com/%{name}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.src.tar.gz
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  ispc
BuildRequires:  tbb-devel
ExclusiveArch:  x86_64

%description
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

%package -n %{libname}
Summary:        Open Image Denoise library
Group:          System/Libraries

%description -n %{libname}
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description	devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license LICENSE.txt
%{_bindir}/oidn*

%files -n %{libname}
%license LICENSE.txt
%{_libdir}/lib%{name}.so.*

%files devel
%license LICENSE.txt
%doc CHANGELOG.md README.md readme.pdf
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so

%changelog
