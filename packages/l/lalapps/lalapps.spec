#
# spec file for package lalapps
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


%define skip_python2 1
Name:           lalapps
Version:        6.26.1
Release:        0
Summary:        LSC Algorithm Library Applications
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/DASWG/LALSuite
Source:         http://software.ligo.org/lscsoft/source/lalsuite/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM lalapps-fix-uninitialised-var.patch badshah400@gmail.com -- Fix usage of uninitialised variable
Patch0:         lalapps-fix-uninitialised-var.patch
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module glue}
BuildRequires:  %{python_module lal >= 6.21.0}
BuildRequires:  %{python_module lalburst >= 1.5.4}
BuildRequires:  %{python_module lalframe >= 1.5.0}
BuildRequires:  %{python_module lalinference >= 1.11.0}
BuildRequires:  %{python_module lalmetaio >= 1.6.0}
BuildRequires:  %{python_module lalpulsar >= 1.18.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  cfitsio-devel
BuildRequires:  fdupes
BuildRequires:  openmpi-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(framel)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lal) >= 6.21.0
BuildRequires:  pkgconfig(lalburst) >= 1.5.4
BuildRequires:  pkgconfig(lalframe) >= 1.5.0
BuildRequires:  pkgconfig(lalinference) >= 1.11.0
BuildRequires:  pkgconfig(lalinspiral) >= 1.10.0
BuildRequires:  pkgconfig(lalmetaio) >= 1.6.0
BuildRequires:  pkgconfig(lalpulsar) >= 1.18.0
BuildRequires:  pkgconfig(lalsimulation) >= 1.10.0
Requires:       python3-lal >= 6.21.0
Requires:       python3-lalburst >= 1.5.4
Requires:       python3-lalframe >= 1.5.0
Requires:       python3-lalinference >= 1.11.0
Requires:       python3-lalinspiral >= 1.10.0
Requires:       python3-lalmetaio >= 1.6.0
Requires:       python3-lalpulsar >= 1.18.0
Requires:       python3-lalsimulation >= 1.10.0
Requires:       python3-numpy
Requires:       python3-scipy
# 32-bit no longer supported upstream
ExcludeArch:    %{ix86}
%python_subpackages

%description
The LSC Algorithm Library Applications for gravitational wave data analysis.
This package contains applications that are built on tools in the LSC
Algorithm Library.

%prep
%autosetup -p1

# FIX env-BASED HASHBANGS
sed -Ei "1{s|/usr/bin/env python|%{_bindir}/python3|}" \
  src/pulsar/HeterodyneSearch/make_frame_cache

%build
%{python_expand # Necessary to run %%configure with both py2 and py3
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python
pushd ../$python
# FIXME: Failures because XLAL_ERROR implictly converts to function return type
export CFLAGS+=" -Wno-enum-conversion"
%configure \
%configure --enable-swig
%make_build
popd
}

%install
%{python_expand # py2 and py3 make_install
export PYTHON=$python
pushd ../$python
%make_install
popd
}

# env-based hashbang /usr/bin/env tclsh => /usr/bin/tclsh
sed -Ei "1{s/env //}" %{buildroot}%{_bindir}/lalapps_CopySFTs

# SECTION EXPORT LAL SPECIFIC ENV VARIABLES
# We do not use upstream's env files because they also set more generic
# variables (e.g. PATH) which may ruin setups

# NUKE UPSTREAM ENV SCRIPTS
rm %{buildroot}%{_sysconfdir}/%{name}-user-env.*

cat << EOF >> %{name}.sh
export LALAPPS_PREFIX=%{_prefix}
export LALAPPS_DATADIR=%{_datadir}/%{name}
EOF

cat << EOF >> %{name}.csh
setenv LALAPPS_PREFIX "%{_prefix}"
setenv LALAPPS_DATADIR "%{_datadir}/%{name}"
EOF

cat << EOF >> %{name}.fish
set LALAPPS_PREFIX (echo "%{_prefix}" | %{_bindir}/sed -e 's| |:|g;')
set LALAPPS_DATADIR (echo "%{_datadir}/%{name}" | %{_bindir}/sed -e 's| |:|g;')
EOF

install -D -m0644 %{name}.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
install -D -m0644 %{name}.csh %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh
install -D -m0644 %{name}.fish %{buildroot}%{_sysconfdir}/profile.d/%{name}.fish

# /SECTION

# SECTION REMOVE STATIC LIB AND LIBTOOL ARCHIVE
find %{buildroot}%{_libdir}/ -name "*.a" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
# /SECTION

%python_expand %fdupes %{buildroot}%{$python_sitearch}/%{name}/
%fdupes %{buildroot}/%{_datadir}/%{name}/

%files -n %{name}
%license COPYING
%{_bindir}/*
%{_datadir}/lalapps/
%{_mandir}/man1/*
%config %{_sysconfdir}/profile.d/%{name}.*

%files %{python_files}
%{python_sitearch}/*

%changelog
