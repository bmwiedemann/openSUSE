#
# spec file for package lal
#
# Copyright (c) 2021 SUSE LLC
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


# NEP 29: numpy, scipy do not have a python36 flavor package in TW
%define skip_python36 1

%define shliblal liblal20
%define shliblalsupport liblalsupport14

# No support for octave >= 6
%bcond_with octave
Name:           lal
Version:        7.1.2
Release:        0
Summary:        A collection of various gravitational wave data analysis routines
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/LALSuite
Source:         http://software.ligo.org/lscsoft/source/lalsuite/lal-%{version}.tar.xz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  bc
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(zlib)
Requires:       python-freezegun
Requires:       python-numpy
Requires:       python-python-dateutil
Requires:       python-scipy
Requires:       python-six
Recommends:     python-ligo-lw
Recommends:     python-ligo-segments
ExcludeArch:    %{ix86}
%if %{with octave}
BuildRequires:  octave-devel
BuildRequires:  swig >= 4.0
%else
BuildRequires:  swig >= 3.0
%endif
# SECTION For tests (only the default python3 flavor)
BuildRequires:  python3-freezegun
BuildRequires:  python3-ligo-lw
BuildRequires:  python3-ligo-segments
BuildRequires:  python3-pytest
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-scipy
# /SECTION

%python_subpackages

%description
The LSC Algorithm Library Suite (LALSuite) is comprised of various
gravitational wave data analysis routines written in C following the ISO/IEC
9899:1999 standard.

%package -n %{shliblal}
Summary:        Shared library for LAL
Group:          System/Libraries

%description -n %{shliblal}
The LSC Algorithm Library Suite (LALSuite) is comprised of various
gravitational wave data analysis routines written in C following the ISO/IEC
9899:1999 standard.

This package provides the shared library for lal.

%package -n %{shliblalsupport}
Summary:        Shared library for LALSupport
Group:          System/Libraries

%description -n %{shliblalsupport}
The LSC Algorithm Library Suite (LALSuite) is comprised of various
gravitational wave data analysis routines written in C following the ISO/IEC
9899:1999 standard.

This package provides the shared library for lalsupport.

%package -n %{name}-devel
Summary:        Headers and source files for building against lal
Group:          Productivity/Scientific/Physics
Requires:       %{shliblalsupport} = %{version}
Requires:       %{shliblal} = %{version}
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(zlib)

%description -n %{name}-devel
The LSC Algorithm Library Suite (LALSuite) is comprised of various
gravitational wave data analysis routines written in C following the ISO/IEC
9899:1999 standard.

This package provides the header files and sources need for building software against lal.

%package -n octave-lal
Summary:        Octave module for lal
Group:          Productivity/Scientific/Physics
%requires_eq    octave-cli

%description -n octave-lal
The LSC Algorithm Library Suite (LALSuite) is comprised of various
gravitational wave data analysis routines written in C following the ISO/IEC
9899:1999 standard.

This package provides the octave module for lal.

%prep
%autosetup -p1

%build
%{python_expand # Necessary to run %%configure with all python flavors
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
%{python_expand #  all python flavors as configured above
export PYTHON=$python
pushd ../${PYTHON}_build
%make_install
popd
}

rm %{buildroot}%{_sysconfdir}/*

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_libdir} -name "*.a" -delete -print

%python_expand %fdupes %{buildroot}%{$python_sitearch}/

%{python_expand # FIX env HASHBANGS
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lal/gpstime.py
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lal/series.py
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" %{buildroot}%{$python_sitearch}/lal/antenna.py
}
%{?python_compileall}

%check
%{python_expand # Run tests from the build dir of the primary python3 flavor only
if [ "$python_" = "python3_" -o "%{$python_provides}" = "python3" ]; then
export PYTHON=$python
pushd ../${PYTHON}_build
%make_build check
popd
fi
}

%post -n %{shliblal} -p /sbin/ldconfig
%post -n %{shliblalsupport} -p /sbin/ldconfig
%postun -n %{shliblal} -p /sbin/ldconfig
%postun -n %{shliblalsupport} -p /sbin/ldconfig

%files %{python_files}
%{python_sitearch}/lal

%files -n %{shliblal}
%{_libdir}/liblal.so.*

%files -n %{shliblalsupport}
%{_libdir}/liblalsupport.so.*

%files -n %{name}-devel
%doc AUTHORS README.md
%license COPYING
%{_bindir}/*
%{_includedir}/lal/
%{_libdir}/liblal.so
%{_libdir}/liblalsupport.so
%{_libdir}/pkgconfig/*.pc

%if %{with octave}
%files -n octave-lal
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%endif

%changelog
