#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%define pname lalinspiral

%define shlib lib%{name}17
# NEP 29: python36-numpy and co. in TW are no more
%define skip_python36 1
# Py2 dropped by upstream
%define skip_python2 1
# octave >= 6 not supported
%bcond_with octave
Name:           %{pname}%{?psuffix}
Version:        3.0.0
Release:        0
Summary:        LSC Algorithm Inspiral Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/LALSuite
Source:         https://software.igwn.org/sources/source/lalsuite/%{pname}-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.7}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lal) >= 7.2.0
BuildRequires:  pkgconfig(lalburst) >= 1.6.0
BuildRequires:  pkgconfig(lalframe) >= 2.0.0
BuildRequires:  pkgconfig(lalmetaio) >= 3.0.0
BuildRequires:  pkgconfig(lalsimulation) >= 4.0.0
Requires:       python-glue
Requires:       python-lal >= 7.2.0
Requires:       python-lalburst >= 1.6.0
Requires:       python-lalframe >= 2.0.0
Requires:       python-lalmetaio >= 3.0.0
Requires:       python-lalsimulation >= 4.0.0
Requires:       python-numpy >= 1.7
ExcludeArch:    %{ix86}
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
%if %{with octave}
BuildRequires:  octave-lal >= 7.2.0
BuildRequires:  octave-lalburst >= 1.6.0
BuildRequires:  octave-lalframe >= 2.0.0
BuildRequires:  octave-lalmetaio >= 3.0.0
BuildRequires:  octave-lalsimulation >= 4.0.0
BuildRequires:  pkgconfig(octave)
%endif
# SECTION For tests (python3 only)
%if %{with test}
BuildRequires:  %{python_module glue}
BuildRequires:  %{python_module lal >= 7.2.0}
BuildRequires:  %{python_module lalburst >= 1.6.0}
BuildRequires:  %{python_module lalframe >= 2.0.0}
BuildRequires:  %{python_module lalinspiral >= 3.0.0}
BuildRequires:  %{python_module lalmetaio >= 3.0.0}
BuildRequires:  %{python_module lalsimulation >= 4.0.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  pkgconfig(lalinspiral) = %{version}
%endif
# /SECTION
%python_subpackages

%description
The LSC Algorithm Inspiral Library for gravitational wave data analysis.

%package -n %{shlib}
Summary:        Shared library for LAL Inspiral
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package contains the shared-object libraries needed to run applications
that use the LAL Inspiral library.

%package -n %{name}-devel
Summary:        Development files for LAL Inspiral
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(lal) >= 7.2.0
Requires:       pkgconfig(lalframe) >= 2.0.0
Requires:       pkgconfig(lalmetaio) >= 3.0.0
Requires:       pkgconfig(lalsimulation) >= 4.0.0
%if %{with octave}
Requires:       pkgconfig(octave)
%endif

%description -n %{name}-devel
This package contains sources and header files needed to build applications
that use the LAL Inspiral library.

%package -n octave-lalinspiral
Summary:        Octave bindings for LAL Inspiral
Group:          Productivity/Scientific/Physics
Requires:       octave-lal >= 7.2.0
Requires:       octave-lalframe >= 2.0.0
Requires:       octave-lalmetaio >= 3.0.0
Requires:       octave-lalsimulation >= 4.0.0
%requires_eq    octave-cli

%description -n octave-lalinspiral
This package provides the necessary files for using LAL Inspiral with octave.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%{python_expand # Necessary to run configure with multiple py3 flavors
export PYTHON=%{_bindir}/$python
builddir=../`basename ${PYTHON}`_build
mkdir ${builddir}
cp -pr ./ ${builddir}
pushd ${builddir}
export CFLAGS="%{optflags} -Wno-error=address"
export CXXFLAGS=${CFLAGS}
%configure \
  %{?with_octave:--enable-swig-octave} \
  %{!?with_octave:--disable-swig-octave}
%make_build %{?with_test:test}
popd
}

%install
%if %{without test}
%{python_expand # py2 and py3 make_install
export PYTHON=%{_bindir}/$python
builddir=../`basename ${PYTHON}`_build
pushd ${builddir}
%make_install
popd
}

# SECTION EXPORT LAL SPECIFIC ENV VARIABLES
# We do not use upstream's env files because they also set more generic
# variables (e.g. PATH) which may ruin setups

# NUKE UPSTREAM ENV SCRIPTS
rm %{buildroot}%{_sysconfdir}/%{name}-user-env.*

cat << EOF >> %{name}.sh
export LALINSPIRAL_PREFIX=%{_prefix}
export LALINSPIRAL_DATADIR=%{_datadir}/%{name}
EOF

cat << EOF >> %{name}.csh
setenv LALINSPIRAL_PREFIX "%{_prefix}"
setenv LALINSPIRAL_DATADIR "%{_datadir}/%{name}"
EOF

cat << EOF >> %{name}.fish
set LALINSPIRAL_PREFIX (echo "%{_prefix}" | %{_bindir}/sed -e 's| |:|g;')
set LALINSPIRAL_DATADIR (echo "%{_datadir}/%{name}" | %{_bindir}/sed -e 's| |:|g;')
EOF

install -D -m0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -m0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -m0644 %{name}.fish %{buildroot}%{_sysconfdir}/profile.d/%{name}.fish

# /SECTION

# SECTION REMOVE STATIC LIB AND LIBTOOL ARCHIVE
find %{buildroot}%{_libdir}/ -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
# /SECTION

%python_expand sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lalinspiral/sbank/bank.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}/%{name}/

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files -n %{name}-devel
%doc AUTHORS README.md
%license COPYING
%{_bindir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%config %{_sysconfdir}/profile.d/%{name}.*

%if %{with octave}
%files -n octave-%{name}
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%endif

%files %{python_files}
%{python_sitearch}/*

%else

%check
%{python_expand export PYTHON=%{_bindir}/$python
%make_build -C ../`basename ${PYTHON}`_build check
}

%endif

%changelog
