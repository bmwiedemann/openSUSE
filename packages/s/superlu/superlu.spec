#
# spec file for package superlu
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _sover 7
%define libname lib%{name}%{?_sover}

Name:           superlu
Summary:        A general purpose library for the direct solution of linear equations
License:        BSD-3-Clause
Group:          Productivity/Scientific/Math
Version:        7.0.1
Release:        0
URL:            https://portal.nersc.gov/project/sparse/superlu/
Source0:        %{name}-%{version}.tar.gz
# Tarball above is generated with the script below
Source1:        get-tarball.sh
Source2:        README.SUSE
Source3:        superlu.rpmlintrc
# PATCH-FIX-OPENSUSE superlu-remove-mc64ad.patch [bnc#796236]
# The Harwell Subroutine Library (HSL) routine mc64ad.c have been removed
# from the original sources for legal reasons. This patch disables the inclusion of
# this routine in the library which, however, remains fully functional
Patch0:         superlu-remove-mc64ad.patch
Patch1:         superlu-make.linux.patch
# PATCH upstream from https://github.com/xiaoyeli/superlu/pull/169
Patch2:         superlu-restore-compatibility-v6.patch
BuildRequires:  blas-devel
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  gcc-fortran
BuildRequires:  tcsh

%description
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

Documentation can be found in the %{name}-doc package or on
https://portal.nersc.gov/project/sparse/superlu/.

%package -n %libname
Summary:        SuperLU matrix solver
Group:          System/Libraries

%description -n %libname
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

%package        devel
Summary:        Headers and development library for lib%{name}%{?_sover}
Group:          Development/Libraries/C and C++
Requires:       %libname = %version
Recommends:     %name-doc

%description    devel
SuperLU headers and libraries files needed for development

%package        doc
Summary:        Documentation for %name
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
Documentation (HTML/PDF) for SuperLU.
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

%package        examples
Summary:        Examples for %name
Group:          Documentation/Other
Recommends:     %name-devel
BuildArch:      noarch

%description    examples
Example programs for SuperLU.
SuperLU is an algorithm that uses group theory to optimize LU
decomposition of sparse matrices.

%prep
%setup -q -n superlu-%{version}
%autopatch -p1
cp %SOURCE2 ./
# Create baselibs.conf dynamically
cat > %{_sourcedir}/baselibs.conf  <<EOF
lib%{name}%{?_sover}
EOF

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release -DUSE_XSDK_DEFAULTS='TRUE' \
  -Denable_tests=ON -Denable_examples=OFF
make %{?_smp_mflags}

%install
%cmake_install
#fix permissions
chmod 644 MATLAB/* EXAMPLE/*

cp FORTRAN/README README.fortran
cp -r EXAMPLE examples
cp MAKE_INC/make.linux examples/make.inc
sed -i -e 's&@superlu_home@&%_prefix&' -e 's&@superlu_lib@&%_libdir&' examples/make.inc
rm -f examples/.gitignore

%fdupes -s examples

%check
%ctest
# remove all build examples
rm -fr EXAMPLE

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%doc README MATLAB README.SUSE
%{_libdir}/*.so.*

%files devel
%doc README.fortran
%{_includedir}/slu_*.h
%{_includedir}/superlu_*.h
%{_includedir}/supermatrix.h
%{_libdir}/*.so
%dir %{_libdir}/cmake/
%dir %{_libdir}/cmake/superlu/
%{_libdir}/cmake/superlu/*.cmake
%{_libdir}/pkgconfig/superlu.pc

%files doc
%doc DOC/html DOC/ug.pdf

%files examples
%doc examples

%changelog
