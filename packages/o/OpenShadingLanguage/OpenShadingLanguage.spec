#
# spec file for package OpenShadingLanguage
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


# The library soname versions follow the package version major and minor numbers.
%define sover %(echo %{version} | cut -d . -f 1,2)
%define sufx %(echo %{sover}|tr . _)
# Required for the plugin directory name, see https://github.com/OpenImageIO/oiio/issues/2583
%define oiio_major_minor_ver %(rpm -q --queryformat='%%{version}' OpenImageIO-devel | cut -d . -f 1-2)

# we could have a minimum of 9 here. but to more easily switch to C++17 we set the minium to 16
%global min_llvm_version 16
%global max_llvm_version 18.9

%if 0%{?suse_version} >= 1600
%bcond_without qt
%else
%bcond_with    qt
%endif

%if 0%{?suse_version} == 1500
%global force_boost_version 1_75_0
%endif

Name:           OpenShadingLanguage
Version:        1.13.11.0
Release:        0
Summary:        A language for programmable shading
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
Source0:        https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://creativecommons.org/licenses/by/3.0/legalcode.txt#/CC-BY-3.0.txt
Patch0:         fix-install-paths.patch
BuildRequires:  OpenEXR-devel >= 2.4
BuildRequires:  bison
BuildRequires:  cmake >= 3.15
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem%{?force_boost_version}-devel
BuildRequires:  libboost_system%{?force_boost_version}-devel
BuildRequires:  libboost_thread%{?force_boost_version}-devel
BuildRequires:  (OpenImageIO >= 2.4 with OpenImageIO < 3)
BuildRequires:  (cmake(Clang) >= %{min_llvm_version} with cmake(Clang) =< %{max_llvm_version})
BuildRequires:  (cmake(LLVM)  >= %{min_llvm_version} with cmake(LLVM)  =< %{max_llvm_version})
%if %{with qt}
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
%endif
%ifnarch %{arm}
# Build fails with partio on armv7/armv6
BuildRequires:  partio-devel
%endif
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
BuildRequires:  (cmake(OpenImageIO) >= 2.0 with cmake(OpenImageIO) < 3)
BuildRequires:  cmake(pugixml)
Requires:       %{name}-common-headers = %{version}
Recommends:     %{name}-doc = %{version}
ExcludeArch:    %{ix86}

%description
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the standalone oslc compiler and some
utilities.

%package doc
Summary:        Documentation for OpenShadingLanguage
License:        CC-BY-3.0
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.
This package contains documentation.

%package example-shaders-source
Summary:        OSL shader examples
License:        BSD-3-Clause
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-common-headers

%description example-shaders-source
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains some OSL example shaders.

%package common-headers
Summary:        OSL standard library and auxiliary headers
License:        BSD-3-Clause
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description common-headers
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the OSL standard library headers, as well
as some additional headers useful for writing shaders.

%package -n liboslcomp%{sufx}
Summary:        OpenShadingLanguage's compiler component library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n liboslcomp%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n liboslexec%{sufx}
Summary:        OpenShadingLanguage's execution component library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n liboslexec%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n liboslnoise%{sufx}
Summary:        OpenShadingLanguage's image noise generation library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n liboslnoise%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n liboslquery%{sufx}
Summary:        Osl library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n liboslquery%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n libtestshade%{sufx}
Summary:        Osl library
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libtestshade%{sufx}
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

%package -n OpenImageIO-plugin-osl
Summary:        OpenImageIO input plugin
License:        BSD-3-Clause
Group:          System/Libraries
Obsoletes:      osl.imageio < 1.11.4.1
Provides:       osl.imageio = %{version}

%description -n OpenImageIO-plugin-osl
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This is a plugin to access OSL from OpenImageIO.

%package        devel
Summary:        Development files for %{name}
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       liboslcomp%{sufx} = %{version}
Requires:       liboslexec%{sufx} = %{version}
Requires:       liboslnoise%{sufx} = %{version}
Requires:       liboslquery%{sufx} = %{version}
Requires:       libtestshade%{sufx} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1
find . -iname CMakeLists.txt -exec sed "-i" "-e s/COMMAND python/COMMAND python3/" "{}" \;

%build
%define _lto_cflags %{nil}
%cmake \
%if %{without qt}
      -DUSE_QT:BOOL=FALSE \
%endif
      -DCMAKE_SKIP_RPATH:BOOL=TRUE \
      -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
      -DOSL_SHADER_INSTALL_DIR:PATH=%{_datadir}/%{name}/shaders/ \
      -DCMAKE_CXX_STANDARD:STRING=17
%cmake_build

%install
%cmake_install
# Add Creative Commons license for documentation
cp -v %{SOURCE1} .

find %{buildroot} -name LICENSE.md -print -delete
# add top level markdowns to the doc package
cp -p *.md %{buildroot}%{_docdir}/%{name}/
# TODO: package python module
find %{buildroot}%{python3_sitearch} -name oslquery.so -print -delete
rm %{buildroot}%{_datadir}/build-scripts/serialize-bc.py

%ldconfig_scriptlets -n liboslcomp%{sufx}
%ldconfig_scriptlets -n liboslexec%{sufx}
%ldconfig_scriptlets -n liboslnoise%{sufx}
%ldconfig_scriptlets -n liboslquery%{sufx}
%ldconfig_scriptlets -n libtestshade%{sufx}

%files
%license LICENSE.md
%{_bindir}/*

%files doc
%license CC-BY-3.0.txt
%doc %{_docdir}/%{name}/

%files example-shaders-source
%{_datadir}/%{name}/shaders/*.osl
%{_datadir}/%{name}/shaders/*.oso

%files common-headers
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shaders
%{_datadir}/%{name}/shaders/*.h

%files -n liboslcomp%{sufx}
%license LICENSE.md
%{_libdir}/liboslcomp.so.%{sover}*

%files -n liboslexec%{sufx}
%license LICENSE.md
%{_libdir}/liboslexec.so.%{sover}*

%files -n liboslnoise%{sufx}
%license LICENSE.md
%{_libdir}/liboslnoise.so.%{sover}*

%files -n liboslquery%{sufx}
%license LICENSE.md
%{_libdir}/liboslquery.so.%{sover}*

%files -n libtestshade%{sufx}
%license LICENSE.md
%{_libdir}/libtestshade.so.%{sover}*

%files -n OpenImageIO-plugin-osl
%license LICENSE.md
%{_libdir}/osl.imageio.so

%files devel
%license LICENSE.md
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/OSL
%{_libdir}/pkgconfig/osl*.pc

%changelog
