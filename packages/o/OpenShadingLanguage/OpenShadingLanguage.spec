#
# spec file for package OpenShadingLanguage
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


# The library soname versions follow the package version major and minor numbers.
%define sover %(echo %{version} | cut -d . -f 1,2)
%define sufx %(echo %{sover}|tr . _)
# Required for the plugin directory name, see https://github.com/OpenImageIO/oiio/issues/2583
%define oiio_major_minor_ver %(rpm -q --queryformat='%%{version}' OpenImageIO-devel | cut -d . -f 1-2)

Name:           OpenShadingLanguage
Version:        1.11.4.1
Release:        0
Summary:        A language for programmable shading
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            https://github.com/imageworks/OpenShadingLanguage
Source0:        https://github.com/imageworks/OpenShadingLanguage/archive/Release-%{version}-dev.tar.gz#/%{name}-Release-%{version}.tar.gz
Source1:        https://creativecommons.org/licenses/by/3.0/legalcode.txt
# PATCH-FIX-UPSTREAM
Patch0:         0001-LLVM-10-odds-and-ends-1135.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Some-SPI-build-fixes-for-finding-the-right-llvm.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-typo-in-the-.pc.in-files-that-botched-the-versio.patch
# PATCH-FIX-UPSTREAM - https://github.com/imageworks/OpenShadingLanguage/pull/1171
Patch3:         0001-Use-single-shared-clang-cpp-library-starting-with-LL.patch
BuildRequires:  OpenEXR-devel
BuildRequires:  bison
BuildRequires:  clang-devel >= 7
BuildRequires:  cmake >= 3.12
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  cmake(OpenImageIO) >= 2.0
BuildRequires:  cmake(pugixml)
Requires:       %{name}-common-headers = %{version}
Recommends:     %{name}-doc = %{version}

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

%package MaterialX-shaders-source
Summary:        MaterialX shader nodes
License:        BSD-3-Clause
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-common-headers

%description MaterialX-shaders-source
Open Shading Language (OSL) is a language for programmable shading
in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.

This package contains the code for the MaterialX shader nodes.

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
%setup -q -n %{name}-Release-%{version}-dev
%autopatch -p1
find . -iname CMakeLists.txt -exec sed "-i" "-e s/COMMAND python/COMMAND python3/" "{}" \;

%build
%cmake \
      -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
      -DOSL_SHADER_INSTALL_DIR:PATH=%{_datadir}/%{name}/shaders/ \
      -DCMAKE_CXX_STANDARD:STRING=14
%cmake_build

%install
%cmake_install
# Add Creative Commons license for documentation
cp -v %{SOURCE1} .
# Move the OpenImageIO plugin into its default search path
mkdir %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}
mv %{buildroot}%{_libdir}/osl.imageio.so %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/

find %{buildroot} -name LICENSE -print -delete
find %{buildroot} -name README.md -print -delete
find %{buildroot} -name CHANGES.md -print -delete

%post -n liboslcomp%{sufx} -p /sbin/ldconfig
%postun -n liboslcomp%{sufx} -p /sbin/ldconfig

%post -n liboslexec%{sufx} -p /sbin/ldconfig
%postun -n liboslexec%{sufx} -p /sbin/ldconfig

%post -n liboslnoise%{sufx} -p /sbin/ldconfig
%postun -n liboslnoise%{sufx} -p /sbin/ldconfig

%post -n liboslquery%{sufx} -p /sbin/ldconfig
%postun -n liboslquery%{sufx} -p /sbin/ldconfig

%post -n libtestshade%{sufx} -p /sbin/ldconfig
%postun -n libtestshade%{sufx} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/*

%files doc
%license legalcode.txt
%doc %{_docdir}/%{name}/

%files MaterialX-shaders-source
%{_datadir}/%{name}/shaders/MaterialX

%files example-shaders-source
%{_datadir}/%{name}/shaders/*.osl
%{_datadir}/%{name}/shaders/*.oso

%files common-headers
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shaders
%{_datadir}/%{name}/shaders/*.h

%files -n liboslcomp%{sufx}
%license LICENSE
%{_libdir}/liboslcomp.so.%{sover}*

%files -n liboslexec%{sufx}
%license LICENSE
%{_libdir}/liboslexec.so.%{sover}*

%files -n liboslnoise%{sufx}
%license LICENSE
%{_libdir}/liboslnoise.so.%{sover}*

%files -n liboslquery%{sufx}
%license LICENSE
%{_libdir}/liboslquery.so.%{sover}*

%files -n libtestshade%{sufx}
%license LICENSE
%{_libdir}/libtestshade.so.%{sover}*

%files -n OpenImageIO-plugin-osl
%license LICENSE
%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/osl.imageio.so

%files devel
%license LICENSE
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/cmake/
%{_libdir}/pkgconfig/

%changelog
