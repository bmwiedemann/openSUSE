#
# spec file for package kquickimageeditor
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


%define kf5_version 5.91.0
%define qt5_version 5.15.0

%bcond_without  lang
Name:           kquickimageeditor
Version:        0.3.0
Release:        0
Summary:        A set of QtQuick components for image editing
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/kquickimageeditor/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/kquickimageeditor/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}

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
Requires:       kquickimageeditor-imports = %{version}
Requires:       cmake(Qt5Core)

%description devel
Development files for KQuickImageEditor, a set of QtQuick components providing
basic image editing capabilities.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%files imports
%license LICENSES/*
%doc README*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kquickimageeditor/

%files devel
%{_kf5_cmakedir}/KQuickImageEditor/
%{_kf5_mkspecsdir}/qt_KQuickImageEditor.pri

%changelog
