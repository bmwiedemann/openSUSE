#
# spec file for package lal
#
# Copyright (c) 2024 SUSE LLC
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

# NEP 29: numpy, scipy do not have a python36 flavor package in TW
%define skip_python36 1
# Py2 no longer supported by upstream
%define skip_python2 1

%define shliblal liblal20
%define shliblalsupport liblalsupport14

# No support for octave >= 6
%bcond_with octave
Name:           lal%{psuffix}
Version:        7.6.0
Release:        0
Summary:        A collection of various gravitational wave data analysis routines
License:        GPL-2.0-only
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/LALSuite
Source:         https://software.igwn.org/sources/source/lalsuite/lal-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         https://git.ligo.org/lscsoft/lalsuite/-/commit/9dba245ab3692ecf691247a442704f13c075ed34.patch#/lalsuite_fix_swig_4_3_0_compat.patch
# PATCH-FIX-UPSTREAM
Patch1:         https://git.ligo.org/lscsoft/lalsuite/-/commit/e12d57e893882c1603778018139ed9060579c8a7.patch#/lalsuite_fix_swig_4_3_0_compat_2.patch
# PATCH-FIX-UPSTREAM lal-disable-erroneous-test.patch badshah400@gmail.com -- Disable a test that gives 'SystemError: error return without exception set'
Patch2:         lal-disable-erroneous-test.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module xml}
BuildRequires:  bc
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(zlib)
# Section Patch2 requirements
BuildRequires:  libtool
# /Section
Requires:       python-freezegun
Requires:       python-numpy
Requires:       python-python-dateutil
Requires:       python-scipy
Recommends:     python-ligo-lw
Recommends:     python-ligo-segments
%if %{with octave}
BuildRequires:  octave-devel
BuildRequires:  swig >= 4.0
%else
BuildRequires:  swig >= 3.0
%endif
%if %{with test}
# SECTION For tests (only the default python3 flavor)
BuildRequires:  python3-freezegun
BuildRequires:  python3-ligo-lw
BuildRequires:  python3-ligo-segments
# python3-py - remove with next update -- https://git.ligo.org/lscsoft/lalsuite/-/merge_requests/2033
BuildRequires:  python3-py
BuildRequires:  python3-pytest
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-scipy
# /SECTION
%endif

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
%if %{with octave}
%requires_eq    octave-cli
%endif

%description -n octave-lal
The LSC Algorithm Library Suite (LALSuite) is comprised of various
gravitational wave data analysis routines written in C following the ISO/IEC
9899:1999 standard.

This package provides the octave module for lal.

%prep
# Upstream patches are -p2, non-upstreamed patch is -p1
%autosetup -N -n lal-%{version}
%patch -P0 -p2
%patch -P1 -p2
%patch -P2 -p1

%build
autoreconf -fvi
%{python_expand # Necessary to run configure with all python flavors
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
%if %{without test}
%{python_expand #  all python flavors as configured above
export PYTHON=$python
pushd ../${PYTHON}_build
%make_install
popd
}

rm %{buildroot}%{_sysconfdir}/*

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_libdir} -name "*.a" -delete -print

%{python_expand # FIX env HASHBANGS
sed -Ei "1{/^#!\/usr\/bin\/env python/d}" \
    %{buildroot}%{$python_sitearch}/lal/{gpstime,series,antenna}.py
rm %{buildroot}%{$python_sitearch}/lal/__pycache__/{gpstime,series,antenna}*.pyc

# Only compileall >= 3.9 has '-s strip_prefix' option
if [ %{$python_version_nodots} -ge 39 ]; then \
  for d in %{buildroot}%{$python_sitelib} %{buildroot}%{$python_sitearch}; do \
    if [ -d $d ]; then \
      $python -m compileall -s %{buildroot} $d; \
      $python -O -m compileall -s %{buildroot} $d; \
    fi; \
  done \
fi;
}
# python_compileall is broken, see https://github.com/openSUSE/python-rpm-macros/issues/150
#%%{?python_compileall}

%{python_expand # Verify we don't have broken cache files
# "-exec false {} +" makes the return code nonzero on match
find %{buildroot}%{$python_sitearch} -iname \*pyc -type f \( -exec grep 'home/abuild' '{}' \; -and -exec false '{}' \+ \)
}

%python_expand %fdupes %{buildroot}%{$python_sitearch}/

# Fix broken hashbang
sed -Ei "1{s|(python3\.?[0-9]*)|%{_bindir}/\1|}" %{buildroot}%{_bindir}/lal_{path2cache,searchsum2cache}
%endif

%check
%if %{with test}
%{python_expand # Run tests from the build dir of the primary python3 flavor only
if [ "$python_" = "python3_" -o "%{$python_provides}" = "python3" ]; then
export PYTHON=$python
pushd ../${PYTHON}_build
%make_build check
popd
fi
}
%endif

%if %{without test}
%post -n %{shliblal} -p /sbin/ldconfig
%post -n %{shliblalsupport} -p /sbin/ldconfig
%postun -n %{shliblal} -p /sbin/ldconfig
%postun -n %{shliblalsupport} -p /sbin/ldconfig

%files %{python_files}
%{python_sitearch}/lal/

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
%{_mandir}/man7/*.7%{?ext_man}

%if %{with octave}
%files -n octave-lal
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%endif

%endif

%changelog
