#
# spec file for package kpimtextedit
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


%define kf6_version 6.19.0
%define qt6_version 6.9.0
%define ktextaddons_version 2.0.0

%bcond_without released
Name:           kpimtextedit
Version:        26.04.0
Release:        0
Summary:        KDE PIM Libraries: Text edit functionality
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAddonsWidgets) >= %{ktextaddons_version}
BuildRequires:  cmake(KF6TextCustomEditor) >= %{ktextaddons_version}
BuildRequires:  cmake(KF6TextEditTextToSpeech) >= %{ktextaddons_version}
BuildRequires:  cmake(KF6TextEmoticonsWidgets) >= %{ktextaddons_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This package contains the basic packages for KDE PIM applications, in
particular those related to editing text, like email messages.

%package -n libKPim6TextEdit6
Summary:        KDE PIM Libraries: Text editing functionality
Requires:       kpimtextedit >= %{version}

%description  -n libKPim6TextEdit6
This package provides text editing functionality for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKPim6TextEdit6 = %{version}
Requires:       cmake(KF6TextCustomEditor) >= %{ktextaddons_version}
Requires:       cmake(KF6TextEditTextToSpeech) >= %{ktextaddons_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package -n libKPim6TextEdit6

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang libKPim6TextEdit6 --all-name

%ldconfig_scriptlets -n libKPim6TextEdit6

%files
%{_kf6_debugdir}/kpimtextedit.categories

%files -n libKPim6TextEdit6
%license LICENSES/*
%{_kf6_libdir}/libKPim6TextEdit.so.*

%files devel
%{_includedir}/KPim6/KPIMTextEdit/
%{_kf6_cmakedir}/KPim6TextEdit/
%{_kf6_libdir}/libKPim6TextEdit.so

%files -n libKPim6TextEdit6-lang -f libKPim6TextEdit6.lang

%changelog
