#
# spec file for package kf6-ktexteditor
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


%define qt6_version 6.6.0

%define rname ktexteditor
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-ktexteditor
Version:        6.3.0
Release:        0
Summary:        Embeddable text editor component
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(EditorConfig)
BuildRequires:  cmake(KF6Archive) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Parts) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Sonnet) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libgit2)
Requires:       kf6-syntax-highlighting >= %{_kf6_bugfix_version}

%description
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF6::TextEditor library.

%package -n libKF6TextEditor6
Summary:        Embeddable text editor component
Requires:       kf6-ktexteditor >= %{version}

%description -n libKF6TextEditor6
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF6::TextEditor library.

%package devel
Summary:        Header files for ktexteditor, an embeddable text editor component
Requires:       libKF6TextEditor6 = %{version}
Requires:       cmake(KF6Parts) >= %{_kf6_bugfix_version}
Requires:       cmake(KF6SyntaxHighlighting) >= %{_kf6_bugfix_version}

%description devel
KTextEditor provides a text editor component that can be embedded in
applications, either as a KPart or using the KF6::TextEditor library.

This subpackage provides the header files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE \
           -DENABLE_KAUTH:BOOL=FALSE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang ktexteditor6

%ldconfig_scriptlets -n libKF6TextEditor6

%files
%{_kf6_debugdir}/ktexteditor.categories
%{_kf6_debugdir}/ktexteditor.renamecategories
# TODO split
%dir %{_kf6_plugindir}/kf6/parts
%{_kf6_plugindir}/kf6/parts/katepart.so

%files -n libKF6TextEditor6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6TextEditor.so.*

%files devel
%doc %{_kf6_qchdir}/KF6TextEditor.*
%{_kf6_cmakedir}/KF6TextEditor/
%{_kf6_includedir}/KTextEditor/
%{_kf6_libdir}/libKF6TextEditor.so
%{_kf6_sharedir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2

%files -n kf6-ktexteditor-lang -f ktexteditor6.lang

%changelog
