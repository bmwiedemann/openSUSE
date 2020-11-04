#
# spec file for package lalsimulation
#
# Copyright (c) 2020 SUSE LLC
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


%define shlib liblalsimulation23
%bcond_without octave
Name:           lalsimulation
Version:        2.2.1
Release:        0
Summary:        LSC Algorithm Simulation Library
License:        GPL-2.0-only
URL:            https://wiki.ligo.org/Computing/DASWG/LALSuite
Source:         http://software.ligo.org/lscsoft/source/lalsuite/lalsimulation-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lal >= 6.22.0}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  lal-devel >= 6.22.0
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
BuildRequires:  swig >= 3.0.7
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(zlib)
%if %{with octave}
BuildRequires:  pkgconfig(octave)
BuildRequires:  octave-lal >= 6.22.0
%endif
# SECTION For tests
BuildRequires:  python3-pytest
# /SECTION
Requires:       python-lal >= 6.22.0
Requires:       python-numpy
Requires:       python-six
# FOR PYTHON PACKAGE
Requires:       lalsimulation-data = %{version}
ExcludeArch:    %{ix86}

%python_subpackages

%description
The LSC Algorithm Simulation Library for gravitational wave data analysis. This
package contains the shared-object libraries needed to run applications
that use the LAL Simulation library.

%package -n %{shlib}
Summary:        Shared library for LALSimulation

%description -n %{shlib}
This package provides the shared library for LALSimulation.

%package -n %{name}-devel
Summary:        Headers and source files for building against LALSimulation
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(lal)
Requires:       pkgconfig(zlib)
Requires:       %{name}-data = %{version}

%description -n %{name}-devel
This package provides the header and sources for coding against LALSimulation.

%package -n %{name}-data
Summary:        Data files required for analyses using lalsimulation

%description -n %{name}-data
This package provides the data files used when running analyses involving
lalsimulation.

%package -n octave-lalsimulation
Summary:        Octave bindings for LALSimulation
Requires:       octave-lal
Requires:       %{name}-data = %{version}
%requires_eq    octave-cli

%description -n octave-lalsimulation
This package provides the necessary files for using LALSimulation with octave.

%prep
%autosetup -p1

%build
%{python_expand # Necessary to run %%configure with both py2 and py3
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
# FIXME: Failures because XLAL_ERROR implictly converts to function return type
export CFLAGS+=" -Wno-enum-conversion"
%configure \
  %{?with_octave:--enable-swig-octave} \
  %{!?with_octave:--disable-swig-octave}
%make_build
popd
}

%install
%{python_expand # py2 and py3 make_install
export PYTHON=$python
pushd ../${PYTHON}_build
%make_install
popd
}

# SECTION EXPORT LAL SPECIFIC ENV VARIABLES
# We do not use upstream's env files because they also set more generic
# variables (e.g. PATH) which may ruin setups

# NUKE UPSTREAM ENV SCRIPTS
rm %{buildroot}%{_sysconfdir}/%{name}-user-env.*

cat << EOF >> %{name}.sh
export LALSIMULATION_PREFIX=%{_prefix}
export LALSIMULATION_DATADIR=%{_datadir}/%{name}
EOF

cat << EOF >> %{name}.csh
setenv LALSIMULATION_PREFIX "%{_prefix}"
setenv LALSIMULATION_DATADIR "%{_datadir}/%{name}"
EOF

cat << EOF >> %{name}.fish
set LALSIMULATION_PREFIX (echo "%{_prefix}" | %{_bindir}/sed -e 's| |:|g;')
set LALSIMULATION_DATADIR (echo "%{_datadir}/%{name}" | %{_bindir}/sed -e 's| |:|g;')
EOF

install -D -m0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -m0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -m0644 %{name}.fish %{buildroot}%{_sysconfdir}/profile.d/%{name}.fish

# /SECTION

find %{buildroot} -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}/%{name}
%python_expand %fdupes %{buildroot}%{$python_sitearch}/%{name}/

%check
pushd ../python3_build
make %{?_smp_mflags} check || cat test/python/test-suite.log
popd

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files -n %{name}-devel
%license COPYING
%doc AUTHORS README.md
%config %{_sysconfdir}/profile.d/%{name}.*
%{_bindir}/*
%{_libdir}/*.so
%{_includedir}/lal/
%{_libdir}/pkgconfig/*
%{_mandir}/man1/*.1%{?ext_man}

%files -n %{name}-data
%{_datadir}/%{name}/

%files %{python_files}
%{python_sitearch}/lalsimulation/

%if %{with octave}
%files -n octave-%{name}
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%endif

%changelog
