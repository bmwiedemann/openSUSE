#
# spec file for package lalinference
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define shlib lib%{name}21
%bcond_without octave
Name:           lalinference
Version:        2.0.3
Release:        0
Summary:        LSC Algorithm Inference Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/DASWG/LALSuite
Source:         http://software.ligo.org/lscsoft/source/lalsuite/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM lalinference-printf-data-type-consistency.patch badshah400@gmail.com -- Cast data passed to printf from size_t to long to make it consistent with the format "%li"; this fixes build failures on i586
Patch0:         lalinference-printf-data-type-consistency.patch
BuildRequires:  %{python_module Shapely}
BuildRequires:  %{python_module astropy}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module glue}
BuildRequires:  %{python_module lal >= 6.19.2}
BuildRequires:  %{python_module lalburst >= 1.5.1}
BuildRequires:  %{python_module lalframe >= 1.4.0}
BuildRequires:  %{python_module lalinspiral >= 1.8.1}
BuildRequires:  %{python_module lalmetaio >= 1.5.0}
BuildRequires:  %{python_module lalpulsar >= 1.17.1}
BuildRequires:  %{python_module lalsimulation >= 2.2.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
BuildRequires:  swig
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lal)
BuildRequires:  pkgconfig(lalburst)
BuildRequires:  pkgconfig(lalframe)
BuildRequires:  pkgconfig(lalinspiral)
BuildRequires:  pkgconfig(lalmetaio)
BuildRequires:  pkgconfig(lalpulsar)
BuildRequires:  pkgconfig(lalsimulation)
BuildRequires:  pkgconfig(libmetaio)
%if %{with octave}
BuildRequires:  octave-lal
BuildRequires:  octave-lalburst
BuildRequires:  octave-lalframe
BuildRequires:  octave-lalinspiral
BuildRequires:  octave-lalmetaio
BuildRequires:  octave-lalpulsar
BuildRequires:  octave-lalsimulation
BuildRequires:  pkgconfig(octave)
%endif
Requires:       python-lal
Requires:       python-lalframe
Requires:       python-lalinspiral
Requires:       python-lalmetaio
Requires:       python-lalpulsar
Requires:       python-lalsimulation
Requires:       %{name}-data = %{version}

%python_subpackages

%description
The LSC Algorithm Inference Library for gravitational wave data analysis.

%package -n %{shlib}
Summary:        Shared library for LAL Inference
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package contains the shared-object libraries needed to run applications
that use the LAL Inference library.

%package -n %{name}-devel
Summary:        Development files for LAL Inference
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       %{name}-data = %{version}
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(lal)
Requires:       pkgconfig(lalburst)
Requires:       pkgconfig(lalframe)
Requires:       pkgconfig(lalinspiral)
Requires:       pkgconfig(lalmetaio)
Requires:       pkgconfig(lalpulsar)
Requires:       pkgconfig(lalsimulation)
Requires:       pkgconfig(libmetaio)

%description -n %{name}-devel
This package contains sources and header files needed to build applications
that use the LAL Inference library.

%package -n %{name}-data
Summary:        Data files for lalinference
Group:          Productivity/Scientific/Physics
Provides:       python2-lalinference-data
Provides:       python3-lalinference-data

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
%autosetup -p1

%build
%{python_expand # Necessary to run %%configure with both py2 and py3
export PYTHON=%{_bindir}/$python
mkdir ../$python
cp -pr ./ ../$python  
pushd ../$python
%configure \
  %{?with_octave:--enable-swig-octave} \
  %{!?with_octave:--disable-swig-octave}
make %{?_smp_mflags}
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
%python3_only %{_bindir}/*
%{python_sitearch}/*

%files -n %{name}-data
%{_datadir}/%{name}/

%changelog
