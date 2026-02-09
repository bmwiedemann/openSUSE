#
# spec file for package avogadrolibs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{suse_version} >= 1550
%bcond_without spglib
%bcond_without python
%bcond_without tests
%else
# Needs <filesystem>
%define gcc_ver 8
%bcond_with spglib
%bcond_with python
%bcond_with tests
%endif

# Requires genXrdPattern
%bcond_with vtk

%define sonum 1
%define libname libAvogadro%{sonum}
%define molecules_rev 1.98.0
%define crystals_rev  1.98.0
%define fragments_rev 1.99.0
Name:           avogadrolibs
Version:        1.100.0
Release:        0
Summary:        Avogadro libraries for computational chemistry
License:        Apache-2.0 AND BSD-3-Clause AND CDDL-1.0 AND GPL-3.0-or-later
URL:            https://two.avogadro.cc/
Source0:        https://github.com/OpenChemistry/avogadrolibs/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/OpenChemistry/molecules/archive/%{molecules_rev}.tar.gz#/molecules-%{molecules_rev}.tar.gz
Source2:        https://github.com/OpenChemistry/crystals/archive/%{crystals_rev}.tar.gz#/crystals-%{crystals_rev}.tar.gz
Source3:        https://github.com/OpenChemistry/fragments/archive/refs/tags/%{fragments_rev}.tar.gz#/fragments-%{fragments_rev}.tar.gz
# PATCH-FIX-UPSTREAM not-install-gwavi.patch -- Library only used locally so no need to install this helper
Patch0:         not-install-gwavi.patch
# PATCH-FIX-UPSTREAM fix-cmake-dependencies.patch -- Fix CMake dependencies
Patch1:         fix-cmake-dependencies.patch
Patch2:         assert.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  eigen3-devel >= 2.91.0
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  hdf5-devel
BuildRequires:  mmtf-cpp-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(libmsym) >= 0.2.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
%endif
%if %{with spglib}
BuildRequires:  spglib-devel
%endif
%if %{with tests}
BuildRequires:  cmake(GTest)
BuildRequires:  cmake(Qt6Test)
%endif
%if 0%{?suse_version} <= 1500
BuildRequires:  pkgconfig(glu)
%endif
%if %{with vtk}
BuildRequires:  genXrdPattern
BuildRequires:  cmake(vtk)
%endif

%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular
modeling, bioinformatics, materials science, and related areas.

%package -n %{libname}
Summary:        Avogadro libraries for computational chemistry
Recommends:     %{name}-plugins >= %{version}
Recommends:     avogadro2-data >= %{version}

%description -n %{libname}
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular
modeling, bioinformatics, materials science, and related areas.

%package plugins
Summary:        Plugins for Avogadro2libs

%description plugins
This package contains the vendor provided plugins for Avogadro2

%package -n avogadro2-data
Summary:        Data files for Avogadro2 and Avogadro2libs
BuildArch:      noarch

%description -n avogadro2-data
This package contains:
  * Crystallographic files of common materials, elements, oxides, for visualization in Avogadro.
  * Common molecule fragments for visualization in Avogadro

%package devel
Summary:        Header files for Avogadro libraries
Requires:       %{libname} = %{version}
Requires:       %{name}-plugins = %{version}
Requires:       eigen3-devel >= 2.91.0
Requires:       cmake(Qt6Concurrent)
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6OpenGLWidgets)
Requires:       cmake(Qt6Widgets)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glew)
%if 0%{?suse_version} <= 1500
Requires:       pkgconfig(glu)
%endif

%description devel
Header files for Avogadro libraries.

%if %{with python}
%package -n python3-avogadro
Summary:        Python bindings for Avogadro libraries

%description -n python3-avogadro
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular
modeling, bioinformatics, materials science, and related areas.
%endif

%prep
%setup -q -b 1 -b 2 -b 3
%autopatch -p1
[ -e ../crystals ] && rm -rfv ../crystals; mv ../crystals-%{crystals_rev} ../crystals
[ -e ../molecules ] && rm -rfv ../molecules; mv ../molecules-%{molecules_rev} ../molecules
[ -e ../fragments ] && rm -rfv ../fragments; mv ../fragments-%{fragments_rev} ../fragments
%ifarch aarch64 %{arm}
# Workaround for Qt GLES builds on ARM, until overlayaxes fixed upstream - https://github.com/OpenChemistry/avogadrolibs/issues/810
# Type of function prototypes differ between GLEW and GLES
sed -i 's/add_subdirectory(overlayaxes)//' avogadro/qtplugins/CMakeLists.txt
%endif

%build
# Note: Molequeue is abandonware, see https://github.com/OpenChemistry/avogadroapp/issues/561
%cmake \
  -DCMAKE_CXX_COMPILER:STRING=g++%{?gcc_ver:-%{gcc_ver}} \
  -DINSTALL_DOC_DIR:PATH=%{_defaultdocdir} \
  -DBUILD_STATIC_PLUGINS:BOOL=OFF \
  -DBUILD_MOLEQUEUE:BOOL=OFF \
  -DENABLE_TESTING:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
  -DQT_VERSION:STRING=6 \
  -DUSE_EXTERNAL_NLOHMANN:BOOL=ON \
  -DUSE_EXTERNAL_PUGIXML:BOOL=ON \
  -DUSE_LIBMSYM:BOOL=ON \
  -DUSE_MMTF:BOOL=ON \
  -DUSE_HDF5:BOOL=ON \
  -DUSE_QT:BOOL=ON \
  -DUSE_VTK:BOOL=%{?with_vtk:ON}%{!?with_vtk:OFF} \
  -DUSE_PYTHON:BOOL=%{?with_python:ON}%{!?with_python:OFF} \
  -DUSE_SPGLIB:BOOL=%{?with_spglib:ON}%{!?with_spglib:OFF} \
  -DOpenGL_GL_PREFERENCE=GLVND \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  %{nil}
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_defaultdocdir}/avogadrolibs/LICENSE
%fdupes %{buildroot}%{_datadir}

sed -E -i '1{\@/usr/bin/env python@d}' %{buildroot}%{_datadir}/avogadro2/fragments/scripts/*.py

# Remove exec permissions from scripts not in $$PATH
chmod -x %{buildroot}%{_libdir}/avogadro2/scripts/formatScripts/zyx.py

rm %{buildroot}%{_datadir}/avogadro2/fragments/.gitignore

%if %{with tests}
%check
%ctest
%endif

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%{_libdir}/libAvogadro*.so.%{sonum}*

%files plugins
%dir %{_libdir}/avogadro2
%{_libdir}/avogadro2/{plugins,scripts}

%files devel
%dir %{_defaultdocdir}/avogadrolibs
%doc %{_defaultdocdir}/avogadrolibs/*.md
%{_includedir}/avogadro/
%{_libdir}/libAvogadro*.so
%{_libdir}/cmake/*

%files -n avogadro2-data
%dir %{_datadir}/avogadro2
%{_datadir}/avogadro2/crystals/
%{_datadir}/avogadro2/fragments/
%{_datadir}/avogadro2/molecules/

%if %{with python}
%files -n python3-avogadro
%{python3_sitearch}/avogadro/
%endif

%changelog
