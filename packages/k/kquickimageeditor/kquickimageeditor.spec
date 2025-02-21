#
# spec file for package kquickimageeditor
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{flavor}" == "qt6"
  %define qt6 1
  %define pkg_suffix 6
  %define kf6_version 6.0.0
  %define qt6_version 6.6.0
%endif
%define rname kquickimageeditor

%bcond_without released
Name:           kquickimageeditor%{?pkg_suffix}
Version:        0.5.0
Release:        0
Summary:        A set of QtQuick components for image editing
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/kquickimageeditor/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kquickimageeditor/%{rname}-%{version}.tar.xz.sig
Source2:        kquickimageeditor.keyring
%endif
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
%endif

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package imports
Summary:        A set of QtQuick components for image editing

%description imports
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary:        Development files for KQuickImageEditor
Requires:       kquickimageeditor%{?pkg_suffix}-imports = %{version}
%if 0%{?qt6}
Requires:       cmake(Qt6Core) >= %{qt6_version}
# TODO: Remove after next update
Conflicts:      kquickimageeditor-devel
%endif

%description devel
Development files for KQuickImageEditor, a set of QtQuick components providing
basic image editing capabilities.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_kf6
%kf6_build
%endif

%install
%if 0%{?qt6}
%kf6_install
%endif

%files imports
%license LICENSES/*
%doc README.md
%if 0%{?qt6}
%{_kf6_qmldir}/org/kde/kquickimageeditor/
%endif

%files devel
%if 0%{?qt6}
%{_kf6_cmakedir}/KQuickImageEditor/
%{_kf6_mkspecsdir}/qt_KQuickImageEditor.pri
%endif

%changelog
