#
# spec file for package qt6-tasktree
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


%define real_version 6.11.0
%define short_version 6.11
%define tar_name qttasktree-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-tasktree%{?pkg_suffix}
Version:        6.11.0
Release:        0
Summary:        Generic framework for automatic management of asynchronous tasks
License:        GPL-2.0-only OR LGPL-3.0-only OR GPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
BuildRequires:  cmake(Qt6Concurrent) = %{real_version}
BuildRequires:  cmake(Qt6Core) = %{real_version}
BuildRequires:  cmake(Qt6CorePrivate) = %{real_version}
BuildRequires:  cmake(Qt6Network) = %{real_version}
BuildRequires:  cmake(Qt6Widgets) = %{real_version}
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt Task tree is a generic framework for automatic management of asynchronous tasks.

%if !%{qt6_docs_flavor}

%package -n libQt6TaskTree6
Summary:        Qt 6 TaskTree library

%description -n libQt6TaskTree6
Qt Task tree is a generic framework for automatic management of asynchronous tasks.

%package devel
Summary:        Qt 6 TaskTree library - Development files
Requires:       libQt6TaskTree6 = %{version}
Requires:       cmake(Qt6Concurrent) = %{real_version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}

%description devel
Development files for the Qt 6 TaskTree library.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6 \
  -DQT_GENERATE_SBOM:BOOL=FALSE

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%ldconfig_scriptlets -n libQt6TaskTree6

%files -n libQt6TaskTree6
%license LICENSES/*
%{_qt6_libdir}/libQt6TaskTree.so.*

%files devel
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtTaskTreeTestsConfig.cmake
%{_qt6_cmakedir}/Qt6TaskTree/
%{_qt6_cmakedir}/Qt6TaskTreePrivate/
%{_qt6_descriptionsdir}/TaskTree.json
%{_qt6_includedir}/QtTaskTree/
%{_qt6_libdir}/libQt6TaskTree.prl
%{_qt6_libdir}/libQt6TaskTree.so
%{_qt6_metatypesdir}/qt6tasktree_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_tasktree_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_tasktree.pri
%{_qt6_pkgconfigdir}/Qt6TaskTree.pc

%endif

%changelog
