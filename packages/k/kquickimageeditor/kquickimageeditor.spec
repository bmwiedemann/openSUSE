#
# spec file for package kquickimageeditor
#
# Copyright (c) 2021 SUSE LLC
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


%define _kf5_version 5.70.0
%define _tar_path 0.1
%bcond_without  lang
Name:           kquickimageeditor
Version:        0.1.3
Release:        0
Summary:        A set of QtQuick components for image editing
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/kquickimageeditor/%{_tar_path}/%{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.5
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
%if %{with lang}
Source1:        https://download.kde.org/stable/kquickimageeditor/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package imports
Summary:        A set of QtQuick components for image editing
Group:          System/GUI/KDE

%description imports
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary:        Development files for KQuickImageEditor
Group:          Development/Libraries/KDE
Requires:       %{name}-imports = %{version}
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Quick)

%description devel
Development files for KQuickImageEditor, a set of QtQuick components providing
basic image editing capabilities.

%prep
%autosetup

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%files imports
%license LICENSES/*
%doc README*
%dir %{_kf5_qmldir}/org
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/kquickimageeditor
%{_kf5_qmldir}/org/kde/kquickimageeditor/libkquickimageeditorplugin.so
%{_kf5_qmldir}/org/kde/kquickimageeditor/plugins.qmltypes
%{_kf5_qmldir}/org/kde/kquickimageeditor/qmldir
%{_kf5_qmldir}/org/kde/kquickimageeditor/qmldir.license
%{_kf5_qmldir}/org/kde/kquickimageeditor/BasicResizeHandle.qml

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KQuickImageEditor/
%{_kf5_mkspecsdir}/qt_KQuickImageEditor.pri

%changelog
