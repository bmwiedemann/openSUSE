#
# spec file for package lalmetaio
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


%define shlib lib%{name}8
%bcond_without octave
Name:           lalmetaio
Version:        1.6.1
Release:        0
Summary:        LSC Algorithm MetaIO Library
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/DASWG/LALSuite
Source:         http://software.ligo.org/lscsoft/source/lalsuite/%{name}-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module lal >= 6.21.0}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} < 1550
BuildRequires:  python-xml
%endif
BuildRequires:  swig
BuildRequires:  pkgconfig(lal) >= 6.21.0
BuildRequires:  pkgconfig(libmetaio)
%if %{with octave}
BuildRequires:  pkgconfig(octave)
BuildRequires:  octave-lal >= 6.21.0
%endif
# SECTION For tests
BuildRequires:  python3-pytest
# /SECTION
Requires:       python-lal >= 6.21.0
Requires:       python-numpy

%python_subpackages

%description
The LSC Algorithm MetaIO Library for gravitational wave data analysis.

%package -n %{shlib}
Summary:        Shared library for libmetaio - LIGO Light-Weight XML library
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package contains the shared-object libraries needed to run applications
that use the LAL MetaIO library.

%package -n %{name}-devel
Summary:        Development files for LAL metaio
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(lal)
Requires:       pkgconfig(libmetaio)

%description  -n %{name}-devel
This package contains sources and header files needed to build applications
that use the LAL MetaIO library.

%package -n octave-lalmetaio
Summary:        Octave bindings for LAL MetaIO
Group:          Productivity/Scientific/Physics
Requires:       octave-lal
%requires_eq    octave-cli

%description -n octave-lalmetaio
This package provides the necessary files for using LAL MetaIO with octave.

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
make %{?_smp_mflags}
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
export LALMETAIO_PREFIX=%{_prefix}
export LALMETAIO_DATADIR=%{_datadir}/%{name}
EOF

cat << EOF >> %{name}.csh
setenv LALMETAIO_PREFIX "%{_prefix}"
setenv LALMETAIO_DATADIR "%{_datadir}/%{name}"
EOF

cat << EOF >> %{name}.fish
set LALMETAIO_PREFIX (echo "%{_prefix}" | %{_bindir}/sed -e 's| |:|g;')
set LALMETAIO_DATADIR (echo "%{_datadir}/%{name}" | %{_bindir}/sed -e 's| |:|g;')
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

%check
pushd ../python3_build
make %{?_smp_mflags} check
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
