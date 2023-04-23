#
# spec file for package kpimtextedit
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


%define libname libKPim5TextEdit5
%bcond_without released
Name:           kpimtextedit
Version:        23.04.0
Release:        0
Summary:        KDE PIM Libraries: Text edit functionality
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DesignerPlugin)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Widgets)

%description
This package contains the basic packages for KDE PIM applications, in
particular those related to editing text, like email messages.

%package -n %{libname}
Summary:        KDE PIM Libraries: Text editing functionality
Requires:       kpimtextedit
# Renamed
Obsoletes:      kpimtextedit-lang <= 23.04.0

%description  -n %{libname}
This package provides text editing functionality for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       %{libname} = %{version}
Requires:       cmake(KF5SyntaxHighlighting)
Requires:       cmake(KF5TextWidgets)
Requires:       cmake(KF5TextEditTextToSpeech)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n %{libname}

%prep
%autosetup -p1 -n kpimtextedit-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%{_kf5_debugdir}/kpimtextedit.categories

%files -n %{libname}
%license LICENSES/*
%{_kf5_libdir}/libKPim5TextEdit.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KPIMTextEdit/
%{_kf5_cmakedir}/KF5PimTextEdit/
%{_kf5_cmakedir}/KPim5TextEdit/
%{_kf5_libdir}/libKPim5TextEdit.so
%{_kf5_mkspecsdir}/qt_KPIMTextEdit.pri
%{_kf5_plugindir}/designer/kpimtextedit5widgets.so

%files -n %{libname}-lang -f %{libname}.lang

%changelog
