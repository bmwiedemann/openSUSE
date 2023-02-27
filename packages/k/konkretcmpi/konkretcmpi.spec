#
# spec file for package konkretcmpi
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


# 1 for python3, 0 for python2
%if 0%{?suse_version} >= 1500
%define python3 1
%else
%define python3 0
%endif
%if %{python3}
%define pythonpackagename python3
%else
%define pythonpackagename python
%endif

Name:           konkretcmpi
%define         libname   lib%{name}
%define         libsoname %{libname}0
Version:        0.9.2
Release:        0
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if %{python3}
BuildRequires:  python3-devel
%else
BuildRequires:  python-devel
%endif
BuildRequires:  sblim-cmpi-devel
BuildRequires:  swig
URL:            https://github.com/rnovacek/konkretcmpi
# Increment the version every time the source code changes.
Summary:        A tool for developing CMPI providers in the C programming language
# This is necessary to build the RPM as a non-root user.
License:        MIT
Group:          Development/Libraries/C and C++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#Source0:        https://github.com/rnovacek/konkretcmpi/archive/%{version}/konkretcmpi-%{version}.tar.gz
Source0:        konkretcmpi-%{version}.tar.gz

# PATCH-FIX-UPSTREAM
# Fix for cim-schema 2.40.0 compatiblity
# See https://github.com/rnovacek/konkretcmpi/issues/3
Patch1:         0001-Honor-that-string-properties-with-EmbeddedInstance-q.patch
# PATCH-FIX-UPSTREAM
Patch2:         0002-Don-t-optimize-out-module-registration.patch
# PATCH-FIX-UPSTREAM
Patch3:         0003-Fix-returning-instance-as-an-output-argument-from-me.patch
# PATCH-FIX-UPSTREAM
Patch4:         0004-Fix-missing-rpath.patch
# PATCH-FIX-UPSTREAM
Patch5:         0005-konkretreg-ignore-KONKRET_REGISTRATION-macro-in-libr.patch
# PATCH-FIX-UPSTREAM
# stolen from Fedora
Patch8:         konkretcmpi-0.9.2-fix-segfault-mofelement.patch

# PATCH-FIX-OPENSUSE, kkaempf@suse.de
# Adapt for older cmake versions
Patch6:         older-cmake.patch

# PATCH-FIX-OPENSUSE, SWIG/Python on SLE 11 and below needs -classic switch, kkaempf@suse.de
#   See http://stackoverflow.com/questions/14192288/how-to-make-multiple-properties-valid-to-one-file-by-set-source-files-properties
#   why set_source_files_properties cannot be used (recognizes string as single property)
# CMake on SLE10 defines PYTHON_INCLUDE_PATH, not PYTHON_INCLUDE_DIR, kkaempf@suse.de
Patch7:         sle10.patch

%description
An open-source tool for rapidly developing CMPI providers in the C
programming language. KonkretCMPI makes CMPI provider development
easier by generating type-safe concrete CIM interfaces from MOF
definitions and by providing default implementations for many of the
provider operations.

%package -n %{libsoname}
Summary:        Shared library of konkretcmpi
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{libsoname}
This package contains the shared libkonkretcmpi library.

%package devel
Summary:        Development files for konkretcmpi
Group:          Development/Libraries/C and C++
Requires:       cim-schema >= 2.17
Requires:       cmake
Requires:       sblim-cmpi-devel

%description devel
An open-source tool for rapidly developing CMPI providers in the C
programming language. KonkretCMPI makes CMPI provider development
easier by generating type-safe concrete CIM interfaces from MOF
definitions and by providing default implementations for many of the
provider operations.

%package %{pythonpackagename}
Summary:        Python bindings for konkretcmpi
Group:          Development/Libraries/Python
%if 0%{?suse_version}
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%if %{python3}
%{!?py3_requires: %define py3_requires Requires: python3}
%{py3_requires}
%else
%{!?py_requires: %define py_requires Requires: python}
%{py_requires}
%endif
%else
Requires:       python2
%endif

%description %{pythonpackagename}
This package contains python binding for konkretcmpi.

%prep
# Untar the sources.
%setup -n konkretcmpi-%{version}
%if 0%{?suse_version} > 0
%if 0%{?suse_version} < 1320
%patch6 -p1
%if 0%{?suse_version} < 1020
%patch7 -p1
%endif
%endif
%endif
%if 0%{?rhel_version} > 0 && 0%{?rhel_version} < 700
%patch6 -p1
%endif
%if 0%{?centos_version} > 0 && 0%{?centos_version} < 700
%patch6 -p1
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch8 -p1

%build
rm -rf build
mkdir build
pushd build
# --with-schema=%{_datadir}/mof/cim-current
cmake \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DCMAKE_VERBOSE_MAKEFILE=TRUE \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_C_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS -fstack-protector -fno-delete-null-pointer-checks" \
  -DCMAKE_CXX_FLAGS_RELEASE:STRING="$RPM_OPT_FLAGS -fstack-protector -fno-delete-null-pointer-checks" \
  -DCMAKE_SKIP_RPATH=1 \
  -DPACKAGE_ARCHITECTURE=`uname -m` \
  -DEXPLICIT_TARGET="$EXPLICIT_TARGET" \
  -DLIB=%{_lib} \
  -DWITH_PYTHON=ON \
  ..
popd
make %{?_smp_mflags} -C build

%install
make DESTDIR=$RPM_BUILD_ROOT install/fast -C build
# Don't package .la object
rm -rf $RPM_BUILD_ROOT/usr/lib*/libkonkret.la

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post -n %{libsoname} -p /sbin/ldconfig

%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/libkonkret.so.*
%{_libdir}/libkonkretmof.so.*
%doc README
%license COPYING

%files devel
%defattr(-,root,root)
%dir %{_includedir}/konkret
%{_includedir}/konkret/*.h
%{_libdir}/libkonkret.so
%{_libdir}/libkonkretmof.so
%{_bindir}/konkret
%{_bindir}/konkretreg
%{_datadir}/cmake/Modules/*

%files %{pythonpackagename}
%defattr(-,root,root)
%{python_sitearch}/*.so
%if 0%{?suse_version} > 0 && 0%{?suse_version} < 1020
%{python_sitelib}/*.py*
%else
%if %{python3}
%{python_sitearch}/*.py*
%else
%{python2_sitearch}/*.py*
%endif
%endif

%changelog
