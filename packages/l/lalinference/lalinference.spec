#
# spec file for package lalinference
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

%define pname lalinference

%define shlib lib%{name}23
# octave >= 6 not supported
%bcond_with octave

# astropy not supported for python < 3.7
%define skip_python2  1
%define skip_python36 1

Name:           %{pname}%{?psuffix}
Version:        4.0.0
Release:        0
Summary:        LSC Algorithm Inference Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/DASWG/LALSuite
Source:         https://software.igwn.org/sources/source/lalsuite/%{pname}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM lalinference-printf-data-type-consistency.patch badshah400@gmail.com -- Cast data passed to printf from size_t to long to make it consistent with the format "%li"; this fixes build failures on i586
Patch0:         lalinference-printf-data-type-consistency.patch
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
BuildRequires:  pkgconfig(lalinspiral) >= 3.0.0
BuildRequires:  pkgconfig(lalmetaio) >= 3.0.0
BuildRequires:  pkgconfig(lalsimulation) >= 4.0.0
# SECTION For tests
%if %{with test}
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module glue >= 1.54.1}
BuildRequires:  %{python_module h5py}
BuildRequires:  %{python_module healpy >= 1.9.1}
BuildRequires:  %{python_module lal >= 7.2.0}
BuildRequires:  %{python_module lalburst >= 1.6.0}
BuildRequires:  %{python_module lalframe >= 2.0.0}
BuildRequires:  %{python_module lalinspiral >= 3.0.0}
BuildRequires:  %{python_module lalmetaio >= 3.0.0}
BuildRequires:  %{python_module lalsimulation >= 4.0.0}
BuildRequires:  %{python_module matplotlib >= 1.2.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module scipy >= 0.9.0}
BuildRequires:  pkgconfig(lalinference) = %{version}
%endif
# /SECTION
%if %{with octave}
BuildRequires:  octave-lal
BuildRequires:  octave-lalframe
BuildRequires:  octave-lalinspiral
BuildRequires:  octave-lalmetaio
BuildRequires:  octave-lalpulsar
BuildRequires:  octave-lalsimulation
BuildRequires:  pkgconfig(octave)
%endif
Requires:       %{name}-data = %{version}
Requires:       python-lal >= 7.2.0
Requires:       python-lalburst >= 1.6.0
Requires:       python-lalframe >= 2.0.0
Requires:       python-lalinspiral >= 3.0.0
Requires:       python-lalmetaio >= 3.0.0
Requires:       python-lalsimulation >= 4.0.0
ExcludeArch:    %{ix86}

%python_subpackages

%description
The LSC Algorithm Inference Library for gravitational wave data analysis.

%package -n %{shlib}
Summary:        Shared library for LAL Inference
Group:          System/Libraries
Conflicts:      liblalinference21

%description -n %{shlib}
This package contains the shared-object libraries needed to run applications
that use the LAL Inference library.

%package -n %{name}-devel
Summary:        Development files for LAL Inference
Group:          Development/Libraries/C and C++
Requires:       %{name}-data = %{version}
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(lal) >= 7.2.0
Requires:       pkgconfig(lalburst) >= 1.6.0
Requires:       pkgconfig(lalframe) >= 2.0.0
Requires:       pkgconfig(lalinspiral) >= 3.0.0
Requires:       pkgconfig(lalmetaio) >= 3.0.0
Requires:       pkgconfig(lalsimulation) >= 4.0.0

%description -n %{name}-devel
This package contains sources and header files needed to build applications
that use the LAL Inference library.

%package -n %{name}-data
Summary:        Data files for lalinference
Group:          Productivity/Scientific/Physics
Provides:       %{python_module lalinference-data}
BuildArch:      noarch

%description -n %{name}-data
This package provides the data files for lalinference.

%package -n octave-lalinference
Summary:        Octave bindings for LAL Inference
Group:          Productivity/Scientific/Physics
Requires:       %{name}-data = %{version}
Requires:       octave-lal
Requires:       octave-lalburst
Requires:       octave-lalframe
Requires:       octave-lalinspiral
Requires:       octave-lalmetaio
Requires:       octave-lalpulsar
Requires:       octave-lalsimulation
%requires_eq    octave-cli

%description -n octave-lalinference
This package provides the necessary files for using LAL Inference with octave.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%{python_expand # Necessary to run %%configure with all python flavors
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%configure \
  %{?with_octave:--enable-swig-octave} \
  %{!?with_octave:--disable-swig-octave}
%make_build %{?with_test:test}
popd
}

%install
%if %{without test}
%{python_expand # install for all python flavors
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
export LALINFERENCE_PREFIX=%{_prefix}
export LALINFERENCE_DATADIR=%{_datadir}/%{name}
EOF

cat << EOF >> %{name}.csh
setenv LALINFERENCE_PREFIX "%{_prefix}"
setenv LALINFERENCE_DATADIR "%{_datadir}/%{name}"
EOF

cat << EOF >> %{name}.fish
set LALINFERENCE_PREFIX (echo "%{_prefix}" | %{_bindir}/sed -e 's| |:|g;')
set LALINFERENCE_DATADIR (echo "%{_datadir}/%{name}" | %{_bindir}/sed -e 's| |:|g;')
EOF

install -D -m0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -m0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -m0644 %{name}.fish %{buildroot}%{_sysconfdir}/profile.d/%{name}.fish

# /SECTION

# SECTION REMOVE STATIC LIB AND LIBTOOL ARCHIVE
find %{buildroot}%{_libdir}/ -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
# /SECTION

%{python_expand # FIX env HASHBANGS
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lalinference/tiger/make_injtimes.py
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lalinference/tiger/omegascans_dag.py
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lalinference/tiger/postproc.py
}

sed -E -i "1 s|^#\!\s*%{_bindir}/env\s*bash|#\!/bin/bash|" %{buildroot}%{_bindir}/lalinference_mpi_wrapper

%python_expand %fdupes %{buildroot}%{$python_sitearch}/%{name}/

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files -n %{name}-devel
%doc AUTHORS README.md
%license COPYING
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
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
%{_bindir}/*
%endif
%{python_sitearch}/*

%files -n %{name}-data
%{_datadir}/%{name}/

%else

%check
%{python_expand # check for all python flavors
export PYTHON=%{_bindir}/$python
%make_build -C ../$python check
}

%endif

%changelog
