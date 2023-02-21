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

%define pname lalpulsar

%define shlib lib%{name}26
# octave >= 6 is not supported
%bcond_with octave

# astropy and numy unsupported for python < 3.7 in TW
%define skip_python36 1
# Py2 support drop by upstream
%define skip_python2 1

Name:           %{pname}%{?psuffix}
Version:        5.0.0
Release:        0
Summary:        LSC Algorithm Pulsar Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/LALSuite
Source:         https://software.igwn.org/sources/source/lalsuite/%{pname}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM lalpulsar-printf-type-mismatch.patch badshah400@gmail.com -- Fix type mismatch when passing variables to printf
Patch0:         lalpulsar-printf-type-mismatch.patch
# PATCH-FIX-OPENSUSE lalpulsar-disable-test_ssbtodetector.patch badshah400@gmail.com -- Disable a test that requires packages not yet availabe on openSUSE
Patch1:         lalpulsar-disable-test_ssbtodetector.patch
# PATCH-FIX-UPSTREAM lalpulsar-fix-uninitialized-var.patch badshah400@gmail.com -- Fix an uninitialised variable
Patch2:         lalpulsar-fix-uninitialized-var.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lal >= 7.1.0}
BuildRequires:  %{python_module numpy-devel >= 1.7}
BuildRequires:  %{python_module numpy}
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lal) >= 7.2.0
BuildRequires:  pkgconfig(lalframe) >= 2.0.0
BuildRequires:  pkgconfig(lalinference) >= 4.0.0
BuildRequires:  pkgconfig(lalsimulation) >= 4.0.0
Requires:       python-lal >= 7.2.0
Requires:       python-lalframe >= 2.0.0
Requires:       python-lalinference >= 4.0.0
Requires:       python-lalsimulation >= 4.0.0
Requires:       python-numpy
Recommends:     %{name}-data = %{version}
ExcludeArch:    %{ix86}
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
%if %{with octave}
BuildRequires:  octave-lal
BuildRequires:  pkgconfig(octave)
%endif
# SECTION For tests
%if %{with test}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module lal >= 7.2.0}
BuildRequires:  %{python_module lalframe}
BuildRequires:  %{python_module lalinference >= 4.0.0}
BuildRequires:  %{python_module lalsimulation >= 4.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  bc
%endif
# /SECTION
%python_subpackages

%description
The LSC Algorithm Pulsar Library for gravitational wave data analysis.

%package -n %{shlib}
Summary:        Shared library for LAL Pulsar
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package contains the shared-object libraries needed to run applications
that use the LAL Pulsar library.

%package -n %{name}-devel
Summary:        Development files for LAL Pulsar
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(cfitsio)
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(lal) >= 7.2.0
Requires:       pkgconfig(lalframe) >= 2.0.0
Requires:       pkgconfig(lalinference) >= 4.0.0
Requires:       pkgconfig(lalsimulation) >= 4.0.0

%description  -n %{name}-devel
This package contains sources and header files needed to build applications
that use the LAL Pulsar library.

%package  -n %{name}-data
Summary:        Data files for use with LAL Pulsar
Group:          Productivity/Scientific/Physics
BuildArch:      noarch

%description  -n %{name}-data
This package provides auxiliary data useful for analyses with LAL Pulsar.

%package -n octave-lalpulsar
Summary:        Octave bindings for LAL Pulsar
Group:          Productivity/Scientific/Physics
Requires:       octave-lal
%requires_eq    octave-cli

%description -n octave-lalpulsar
This package provides the necessary files for using LAL Pulsar with octave.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
# Patch1 needs autoreconf
autoreconf -fvi
%{python_expand # Necessary to run configure with multiple py3 flavors
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
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
%{python_expand # Multiple py3 flavors make_install
export PYTHON=%{_bindir}/$python
pushd ../$python
%make_install
popd
}

# SECTION EXPORT LAL SPECIFIC ENV VARIABLES
# We do not use upstream's env files because they also set more generic
# variables (e.g. PATH) which may ruin setups

# NUKE UPSTREAM ENV SCRIPTS
rm %{buildroot}%{_sysconfdir}/%{name}-user-env.*

cat << EOF >> %{name}.sh
export LALPULSAR_PREFIX=%{_prefix}
export LALPULSAR_DATADIR=%{_datadir}/%{name}
EOF

cat << EOF >> %{name}.csh
setenv LALPULSAR_PREFIX "%{_prefix}"
setenv LALPULSAR_DATADIR "%{_datadir}/%{name}"
EOF

cat << EOF >> %{name}.fish
set LALPULSAR_PREFIX (echo "%{_prefix}" | %{_bindir}/sed -e 's| |:|g;')
set LALPULSAR_DATADIR (echo "%{_datadir}/%{name}" | %{_bindir}/sed -e 's| |:|g;')
EOF

install -D -m0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -m0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -m0644 %{name}.fish %{buildroot}%{_sysconfdir}/profile.d/%{name}.fish

# /SECTION

# SECTION REMOVE STATIC LIB AND LIBTOOL ARCHIVE
find %{buildroot}%{_libdir}/ -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
# /SECTION

sed -i "1s|/usr/bin/env tclsh|/usr/bin/tclsh|" %{buildroot}%{_bindir}/lalpulsar_CopySFTs

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

%files -n %{name}-data
%{_datadir}/%{name}/

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
pushd ../$python
%make_build check
popd
}

%endif

%changelog
