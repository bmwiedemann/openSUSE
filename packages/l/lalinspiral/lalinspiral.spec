#
# spec file for package lalinspiral
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


%define shlib lib%{name}15
%bcond_without octave
Name:           lalinspiral
Version:        1.10.1
Release:        0
Summary:        LSC Algorithm Inspiral Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/LALSuite
Source:         http://software.ligo.org/lscsoft/source/lalsuite/%{name}-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module glue}
BuildRequires:  %{python_module lal >= 6.21.0}
BuildRequires:  %{python_module lalburst}
BuildRequires:  %{python_module lalframe}
BuildRequires:  %{python_module lalmetaio}
BuildRequires:  %{python_module lalsimulation >= 1.10.0}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lal) >= 6.21.0
BuildRequires:  pkgconfig(lalburst)
BuildRequires:  pkgconfig(lalframe)
BuildRequires:  pkgconfig(lalmetaio)
BuildRequires:  pkgconfig(lalsimulation) >= 1.10.0
Requires:       python-glue
Requires:       python-lal >= 6.21.0
Requires:       python-lalburst
Requires:       python-lalframe
Requires:       python-lalmetaio
Requires:       python-lalsimulation >= 1.10.0
Requires:       python-numpy
Requires:       python-scipy
ExcludeArch:    %{ix86}
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
%if %{with octave}
BuildRequires:  octave-lal >= 6.21.0
BuildRequires:  octave-lalburst
BuildRequires:  octave-lalframe
BuildRequires:  octave-lalmetaio
BuildRequires:  octave-lalsimulation >= 1.10.0
BuildRequires:  pkgconfig(octave)
%endif
# SECTION For tests (python3 only)
BuildRequires:  python3-pytest
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
Requires:       pkgconfig(lal)
Requires:       pkgconfig(lalframe)
Requires:       pkgconfig(lalmetaio)
Requires:       pkgconfig(lalsimulation)
Requires:       pkgconfig(libmetaio)
Requires:       pkgconfig(octave)

%description -n %{name}-devel
This package contains sources and header files needed to build applications
that use the LAL Inspiral library.

%package -n octave-lalinspiral
Summary:        Octave bindings for LAL Inspiral
Group:          Productivity/Scientific/Physics
Requires:       octave-lal
Requires:       octave-lalframe
Requires:       octave-lalmetaio
Requires:       octave-lalsimulation
%requires_eq    octave-cli

%description -n octave-lalinspiral
This package provides the necessary files for using LAL Inspiral with octave.

%prep
%autosetup -p1

%build
%{python_expand # Necessary to run %%configure with both py2 and py3
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
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

%check
pushd ../python3_build
export LD_LIBRARY_PATH+=%{buildroot}%{_libdir}
%make_build check
popd

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

%changelog
