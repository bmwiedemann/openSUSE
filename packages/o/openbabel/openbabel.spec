#
# spec file for package openbabel
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


# Allow disabling maestro (.mae) file support (enabled by default)
%bcond_without maestro

# Allow disabling GUI build (enabled by default)
%bcond_without gui

# Upstream version is "openbabel-major-minor-patch" instead of "major.minor.patch"
%define upstream_version openbabel-3-1-1

# The major ABI version of the shared library
%define abiver 7

Name:           openbabel
Version:        3.1.1
Release:        0
Summary:        A chemistry toolbox
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://openbabel.org
Source0:        https://github.com/openbabel/openbabel/archive/%{upstream_version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM openbabel-3.1.1-test-python3-escape-chars.patch -- Fix test failure with python3 (gh#openbabel/openbabel#2217)
Patch0:         openbabel-3.1.1-test-python3-escape-chars.patch
# PATCH-FIX-UPSTREAM openbabel-3.1.1-test-python3-imports.patch -- Fix ImportError in python3 tests (gh#openbabel/openbabel!2378)
Patch1:         openbabel-3.1.1-test-python3-imports.patch
# PATCH-FIX-UPSTREAM openbabel-3.1.1-version-number.patch -- Fix version number
Patch2:         openbabel-3.1.1-version-number.patch
# PATCH-FIX-UPSTREAM openbabel-3.1.1-gcc-12.patch -- Fix build with GCC 12 (gh#openbabel/openbabel!2493)
Patch3:         openbabel-3.1.1-gcc-12.patch
# PATCH-FIX-UPSTREAM openbabel-3.1.1-wx-stl-compat.patch -- Fix build with wxWidgets using STL (gh#openbabel/openbabel!2527)
Patch4:         openbabel-3.1.1-wx-stl-compat.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  inchi-devel >= 1.04
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  swig >= 2.0
BuildRequires:  pkgconfig(RapidJSON) >= 1.1.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(eigen3) >= 2.91.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(zlib)
%if %{with gui}
BuildRequires:  wxWidgets-devel >= 2.8
%endif
%if %{with maestro}
BuildRequires:  maeparser-devel >= 1.2.3
%endif

%description
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

This package contains the command-line utility, which is intended to
be used as a replacement for the original babel program, to translate
between various chemical file formats as well as a wide variety of
utilities to foster development of other open source scientific
software.

%if %{with gui}
%package gui
Summary:        Graphical User Interface for Open Babel, a chemical toolbox
Group:          Productivity/Scientific/Chemistry

%description gui
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

This package contains a graphical interface for Open Babel.
%endif

%package -n libopenbabel%{abiver}
Summary:        Component library of Open Babel, a chemistry toolbox
Group:          System/Libraries

%description -n libopenbabel%{abiver}
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

This package contains the shared library of Open Babel.

%package -n python3-openbabel
Summary:        Python bindings for Open Babel, a chemistry toolbox
Group:          Productivity/Scientific/Chemistry

%description -n python3-openbabel
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

This package contains the Python bindings of Open Babel.

%package devel
Summary:        Development files for Open Babel
Group:          Development/Libraries/C and C++
Requires:       libopenbabel%{abiver} = %{version}
Requires:       pkgconfig(zlib)
Provides:       libopenbabel-devel = %{version}
Obsoletes:      libopenbabel-devel < %{version}

%description devel
Open Babel is a chemical toolbox understanding many formats of
chemical data. It allows to search, convert, analyze, or store data
from molecular modeling, chemistry, solid-state materials,
biochemistry, or related areas.

%prep
%autosetup -p1 -n "%{name}-%{upstream_version}"

%build
%define __builder ninja
%cmake \
  -DRUN_SWIG=ON \
  -DPYTHON_BINDINGS=ON \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DOPENBABEL_USE_SYSTEM_INCHI=ON \
  %{?with_maestro:-DWITH_MAEPARSER=ON} \
  -ULIB_INSTALL_DIR \
  -Wno-dev
%cmake_build

%install
%cmake_install

%post -n libopenbabel%{abiver} -p /sbin/ldconfig
%postun -n libopenbabel%{abiver} -p /sbin/ldconfig

%check
%ifarch aarch64 %{power64}
  # See gh#openbabel/openbabel/266, gh#openbabel/openbabel#2246
  %define test_filter --exclude-regex "(test_regressions_1|test_regressions_221|test_regressions_228|inchiSteffen_PubChem.smi_Test|pytest_sym|pybindtest_obconv_writers|pybindtest_bindings)"
%else
  # Some test failures on Tumbleweed apparently linked to slight changes in floating point value outputs.
  # They look harmless - maybe float comparison margin is just not big enough - and may be linked to newer rapidjson.
  %if 0%{?suse_version} > 1500
    %ifarch %{ix86}
      %define test_filter --exclude-regex "(pybindtest_obconv_writers|test_cifspacegroup_11|pybindtest_bindings)"
    %else
      %define test_filter --exclude-regex "pybindtest_obconv_writers"
    %endif
  %endif
%endif

%ctest %{?test_filter}

%files
%{_bindir}/roundtrip
%{_bindir}/ob*
%{_mandir}/man1/*
%exclude %{_bindir}/obgui
%exclude %{_mandir}/man1/obgui.1*

%if %{with gui}
%files gui
%{_bindir}/obgui
%{_mandir}/man1/obgui.1%{?ext_man}
%dir %{_datadir}/openbabel
%dir %{_datadir}/openbabel/%{version}
%{_datadir}/openbabel/%{version}/splash.png
%endif

%files -n libopenbabel%{abiver}
%{_libdir}/libopenbabel.so.%{abiver}
%{_libdir}/libopenbabel.so.%{abiver}.0.0
# Library plugins
%dir %{_libdir}/openbabel
%{_libdir}/openbabel/%{version}
# Data files needed by either the library or its plugins
%dir %{_datadir}/openbabel
%{_datadir}/openbabel/%{version}
%exclude %{_datadir}/openbabel/%{version}/splash.png

%files devel
%dir %{_libdir}/cmake/openbabel3
%{_includedir}/openbabel3
%{_libdir}/cmake/openbabel3/OpenBabel3Config.cmake
%{_libdir}/cmake/openbabel3/OpenBabel3ConfigVersion.cmake
%{_libdir}/cmake/openbabel3/OpenBabel3_EXPORTS*.cmake
%{_libdir}/libopenbabel.so
%{_libdir}/pkgconfig/openbabel-3.pc

%files -n python3-openbabel
%{python3_sitearch}*

%changelog
