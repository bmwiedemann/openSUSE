#
# spec file for package qt6-shadertools
#
# Copyright (c) 2023 SUSE LLC
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


%define real_version 6.7.2
%define short_version 6.7
%define tar_name qtshadertools-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-shadertools%{?pkg_suffix}
Version:        6.7.2
Release:        0
Summary:        Qt 6 ShaderTools library
License:        GPL-3.0-or-later
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-shadertools-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6Gui) = %{real_version}
Requires:       spirv-tools
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
The Qt 6 ShaderTools library and tools.

%if !%{qt6_docs_flavor}

%package -n libQt6ShaderTools6
Summary:        Qt 6 ShaderTools library

%description -n libQt6ShaderTools6
The Qt 6 ShaderTools library.

%package devel
Summary:        Qt 6 ShaderTools library - Development files
Requires:       libQt6ShaderTools6 = %{version}
# qsb is required
Requires:       qt6-shadertools = %{version}
Requires:       cmake(Qt6Gui) = %{real_version}

%description devel
Development files for the Qt 6 ShaderTools library

%package private-devel
Summary:        Non-ABI stable API for the Qt 6 ShaderTools library
Requires:       cmake(Qt6ShaderTools) = %{real_version}
%requires_eq    qt6-gui-private-devel

%description private-devel
This package provides private headers of libQt6ShaderTools that do not have any
ABI or API guarantees.

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%{qt6_link_executables}

%ldconfig_scriptlets -n libQt6ShaderTools6

%files
%{_qt6_bindir}/qsb
%{_bindir}/qsb6

%files -n libQt6ShaderTools6
%license LICENSES/*
%{_qt6_libdir}/libQt6ShaderTools.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%{_qt6_cmakedir}/Qt6ShaderTools/
%{_qt6_cmakedir}/Qt6ShaderToolsTools/
%{_qt6_descriptionsdir}/ShaderTools.json
%{_qt6_includedir}/QtShaderTools/
%{_qt6_libdir}/libQt6ShaderTools.prl
%{_qt6_libdir}/libQt6ShaderTools.so
%{_qt6_metatypesdir}/qt6shadertools_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_shadertools.pri
%{_qt6_pkgconfigdir}/Qt6ShaderTools.pc
%exclude %{_qt6_includedir}/QtShaderTools/%{real_version}/

%files private-devel
%{_qt6_includedir}/QtShaderTools/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_shadertools_private.pri

%endif

%changelog
