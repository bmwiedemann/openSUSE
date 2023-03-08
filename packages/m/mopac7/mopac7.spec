#
# spec file for package mopac7
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


%define         libname  libmopac7-1
Name:           mopac7
Version:        1.15
Release:        0
Summary:        Semi-empirical quantum mechanics suite
License:        SUSE-Public-Domain
Group:          Productivity/Scientific/Chemistry
URL:            https://sourceforge.net/projects/mopac7/
Source0:        http://www.bioinformatics.org/ghemical/download/current/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
Patch1:         mopac7-1.14-random_data.patch
Patch2:         mopac7-1.14-libdir.patch
# PATCH-FEATURE-OPENSUSE mopac7-fortify.patch -- fix for building with gcc7
Patch3:         mopac7-fortify.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-fortran
BuildRequires:  libtool
BuildRequires:  pkgconfig
%{?suse_build_hwcaps_libs}

%description
MOPAC7 is a semi-empirical quantum-mechanics code written by James J. P.
Stewart and co-workers. The purpose of this project is to maintain MOPAC7 as
a stand-alone program as well as a library that provides the functionality
of MOPAC7 to other programs.

%package -n	%{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries

%description -n	%{libname}
MOPAC7 is a semi-empirical quantum-mechanics code written by James J. P.
Stewart and co-workers. The purpose of this project is to maintain MOPAC7 as
a stand-alone program as well as a library that provides the functionality
of MOPAC7 to other programs.

This package contains dynamic libraries.

%package    -n %{libname}-devel
Summary:        Header files and static libraries from %{name}
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}

%description -n %{libname}-devel
MOPAC7 is a semi-empirical quantum-mechanics code written by James J. P.
Stewart and co-workers. The purpose of this project is to maintain MOPAC7 as
a stand-alone program as well as a library that provides the functionality
of MOPAC7 to other programs.

This package contains development files.

%prep
%autosetup -p1

%build
autoreconf -fiv
# http://www.bioinformatics.org/pipermail/ghemical-devel/2008-August/000763.html
export FFLAGS="%{optflags} -std=legacy -fno-automatic"
%ifarch aarch64 %{arm}
export FFLAGS="%{optflags} -fPIC"
%endif
%configure \
  --disable-static
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_bindir}
libtool --mode=install install -m 755 fortran/%{name} %{buildroot}%{_bindir}/%{name}
sed -e "s|\./src|%{_bindir}|g" run_mopac7 > %{buildroot}%{_bindir}/run_mopac7
rm tests/Makefile*
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog NEWS README tests
%attr(755,root,root) %{_bindir}/run_mopac7
%{_bindir}/%{name}

%files -n %{libname}
%license COPYING
%{_libdir}/libmopac7.so.*

%files -n %{libname}-devel
%{_includedir}/%{name}
%{_libdir}/libmopac7.so
%{_libdir}/pkgconfig/libmopac7.pc

%changelog
