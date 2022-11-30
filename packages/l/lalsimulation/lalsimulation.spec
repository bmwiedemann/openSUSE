#
# spec file for package lalsimulation
#
# Copyright (c) 2022 SUSE LLC
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


# NEP 29: python36-numpy and co. in TW are no more
%define skip_python36 1
# Py2 support dropped upstream
%define skip_python2 1

%define shlib liblalsimulation31
# octave >= 6 not supported
%bcond_with octave
Name:           lalsimulation
Version:        4.0.0
Release:        0
Summary:        LSC Algorithm Simulation Library
License:        GPL-2.0-only
URL:            https://wiki.ligo.org/Computing/DASWG/LALSuite
Source:         https://software.igwn.org/sources/source/lalsuite/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM swig_4_1_compat.patch badshah40@gmail.com -- Ensure compatibility with swig 4.1; patch taken from upstream
Patch0:         https://git.ligo.org/lscsoft/lalsuite/-/commit/17bdccd92ab76abfe617e3eb38edf85ab4dfe424.patch#/swig_4_1_compat.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lal >= 7.2.0}
BuildRequires:  %{python_module numpy >= 1.7}
BuildRequires:  %{python_module numpy-devel >= 1.7}
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
BuildRequires:  swig >= 3.0.10
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lal) >= 7.2.0
BuildRequires:  pkgconfig(zlib)
%if %{with octave}
BuildRequires:  octave-lal >= 7.2.0
BuildRequires:  pkgconfig(octave)
%endif
# SECTION For tests
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-lal >= 7.2.0
Requires:       python-numpy >= 1.7
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
Requires:       %{name}-data = %{version}
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(lal) >= 7.2.0
Requires:       pkgconfig(zlib)

%description -n %{name}-devel
This package provides the header and sources for coding against LALSimulation.

%package -n %{name}-data
Summary:        Data files required for analyses using lalsimulation
BuildArch:      noarch

%description -n %{name}-data
This package provides the data files used when running analyses involving
lalsimulation.

%package -n octave-lalsimulation
Summary:        Octave bindings for LALSimulation
Requires:       %{name}-data = %{version}
Requires:       octave-lal
%requires_eq    octave-cli

%description -n octave-lalsimulation
This package provides the necessary files for using LALSimulation with octave.

%prep
%autosetup -p2

%build
%{python_expand # Necessary to run configure with multiple py3 flavors
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
%configure \
  %{?with_octave:--enable-swig-octave} \
  %{!?with_octave:--disable-swig-octave}
%make_build
popd
}

%install
%{python_expand # py2 and py3 make_install
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
%{python_expand export PYTHON=%{_bindir}/$python
pushd ../$python
%make_build check
popd
}

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
