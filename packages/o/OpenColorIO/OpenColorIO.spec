#
# spec file for package OpenColorIO
#
# Copyright (c) 2025 SUSE LLC
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


%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == "ocio_tools"
%bcond_without ocio_tools
%else
%bcond_with    ocio_tools
%endif
# Ensure that libyaml-cpp version is the one that is built against
# See boo#1160171
%define yamlrequires %(rpm -q --requires yaml-cpp-devel | grep libyaml || echo aaa_base)
%define so_ver 2_4
%define pkg_name OpenColorIO
%if %{without ocio_tools}
Name:           OpenColorIO
%else
Name:           OpenColorIO-tools
%endif
Version:        2.4.1
Release:        0
Summary:        Color Management Solution Geared Towards Motion Picture Production
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://opencolorio.org/
Source0:        https://github.com/AcademySoftwareFoundation/OpenColorIO/archive/v%{version}.tar.gz
BuildRequires:  cmake >= 3.12
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libexpat-devel >= 2.2.8
BuildRequires:  liblcms2-devel >= 2.2
BuildRequires:  openexr-devel
BuildRequires:  pkgconfig
BuildRequires:  pystring-devel >= 1.1.3
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
BuildRequires:  yaml-cpp-devel >= 0.6.3
BuildRequires:  pkgconfig(minizip-ng) >= 4.0.4
Recommends:     %{pkg_name}-doc = %{version}
%if %{with ocio_tools}
BuildRequires:  OpenImageIO-plugin-osl
BuildRequires:  OpenShadingLanguage-devel
BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-Sphinx
BuildRequires:  python3-breathe
BuildRequires:  python3-recommonmark
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-sphinx-tabs
BuildRequires:  python3-sphinx_press_theme
BuildRequires:  python3-testresources
BuildRequires:  (OpenImageIO >= 2.1.9 with OpenImageIO < 3)
BuildRequires:  (OpenImageIO-devel >= 2.1.9 with OpenImageIO-devel < 3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glut)
%endif

%description
OpenColorIO (OCIO) is a color management solution geared towards motion picture
production with an emphasis on visual effects and computer animation.

OCIO is compatible with the Academy Color Encoding Specification (ACES) and is
LUT-format agnostic, supporting many popular formats.

%package devel
Summary:        Development Files for OpenColorIO
Group:          Development/Libraries/C and C++
Requires:       libOpenColorIO%{so_ver} = %{version}
Recommends:     %{pkg_name}-doc = %{version}

%description devel
This package provides development libraries and headers needed to build
software using OpenColorIO.

%package -n %{pkg_name}-doc
Summary:        Documentation for OpenColorIO
Group:          Documentation/Other
BuildArch:      noarch

%description -n %{pkg_name}-doc
This package contains documentation for OpenColorIO.

%package -n libOpenColorIO%{so_ver}
Summary:        Complete Color Management Solution Geared Towards Motion Picture Production
Group:          System/Libraries
Requires:       %{yamlrequires}
# this is unfortunate and a fallout of properly naming the lib after fixing so_ver
Conflicts:      libOpenColorIO2_0 = 2.1.1
Conflicts:      libOpenColorIO2_0 = 2.1.2

%description -n libOpenColorIO%{so_ver}
OpenColorIO (OCIO) is a color management solution geared towards motion picture
production with an emphasis on visual effects and computer animation.

OCIO is compatible with the Academy Color Encoding Specification (ACES) and is
LUT-format agnostic, supporting many popular formats.

%package -n python3-OpenColorIO
Summary:        Python Bindings for OpenColorIO
Group:          Development/Libraries/Python
# python-OpenColorIO was last used at version 1.1.1
Provides:       python-OpenColorIO = %{version}
Obsoletes:      python-OpenColorIO < %{version}

%description -n python3-OpenColorIO
This package contains python bindings for OpenColorIO.

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

# Fix library install location
sed -i 's|DESTINATION lib|DESTINATION %{_lib}|' src/OpenColorIO/CMakeLists.txt

%build
%cmake \
    -DCMAKE_CXX_STANDARD=17 \
    -DCMAKE_SKIP_RPATH=ON \
%ifnarch x86_64
    -DOCIO_USE_SSE=OFF \
%endif
%if %{with ocio_tools}
    -DOCIO_BUILD_DOCS=ON
%else
    -DOCIO_BUILD_APPS=OFF \
    -DOCIO_BUILD_DOCS=OFF
%endif
%cmake_build

%install
%cmake_install

# Remove stray static libs
rm -f %{buildroot}%{_libdir}/*.a

# Move documentation to the right location
mkdir -p %{buildroot}%{_docdir}/%{pkg_name}
cp *.md  %{buildroot}%{_docdir}/%{pkg_name}

# This shouldn't be needed
rm %{buildroot}%{_datadir}/ocio/setup_ocio.sh

%if %{without ocio_tools}
rm -rf %{buildroot}%{_docdir}/%{pkg_name}/
%else
mv %{buildroot}%{_datadir}/doc/OpenColorIO/html/ %{buildroot}%{_docdir}/%{pkg_name}/
rmdir %{buildroot}%{_datadir}/doc/OpenColorIO
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_includedir}
%endif

%post -n libOpenColorIO%{so_ver} -p /sbin/ldconfig
%postun -n libOpenColorIO%{so_ver} -p /sbin/ldconfig

%if %{with ocio_tools}
%files
%license LICENSE
%{_bindir}/*
%doc %{_docdir}/%{pkg_name}/
%exclude %{_docdir}/%{pkg_name}/html/
%{_datadir}/ocio/

%files -n %{pkg_name}-doc
%{_docdir}/%{pkg_name}/html/
%else

%files devel
%{_includedir}/OpenColorIO/
%{_libdir}/pkgconfig/OpenColorIO.pc
%{_libdir}/cmake/OpenColorIO/
%{_libdir}/libOpenColorIO.so

%files -n libOpenColorIO%{so_ver}
%license LICENSE
%{_libdir}/libOpenColorIO.so.*

%files -n python3-OpenColorIO
%license LICENSE
%{python3_sitearch}/PyOpenColorIO/
%endif

%changelog
