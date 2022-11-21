#
# spec file for package qt6-imageformats
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


%define real_version 6.4.1
%define short_version 6.4
%define short_name qtimageformats
%define tar_name qtimageformats-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
Name:           qt6-imageformats%{?pkg_suffix}
Version:        6.4.1
Release:        0
Summary:        Qt 6 ImageFormat Plugins
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
URL:            https://www.qt.io
Source:         https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-imageformats-rpmlintrc
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libwebp)
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Plugins for additional image formats: TIFF, MNG, TGA, WEBP, WBMP

%if !%{qt6_docs_flavor}

%package devel
Summary:        Qt 6 ImageFormats - Development files
Requires:       %{name} = %{version}
Requires:       libtiff-devel
Requires:       cmake(Qt6Gui)
Requires:       pkgconfig(libmng)
Requires:       pkgconfig(libwebp)

%description devel
Development files for the Qt 6 ImageFormats plugins.

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

%build
%cmake_qt6

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

%files
%license LICENSES/*
%{_qt6_pluginsdir}/imageformats/

%files devel
%{_qt6_cmakedir}/Qt6/FindLibmng.cmake
%{_qt6_cmakedir}/Qt6/FindWrapJasper.cmake
%{_qt6_cmakedir}/Qt6/FindWrapWebP.cmake
%{_qt6_cmakedir}/Qt6Gui/*

%endif

%changelog
