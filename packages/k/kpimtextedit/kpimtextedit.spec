#
# spec file for package kpimtextedit
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kpimtextedit
Version:        20.08.1
Release:        0
Summary:        KDE PIM Libraries: Text edit functionality
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DesignerPlugin)
BuildRequires:  cmake(KF5Emoticons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Widgets)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  libboost_headers-devel
Recommends:     %{name}-lang

%description
This package contains the basic packages for KDE PIM applications, in particular those related to editing text, like email messages.

%package -n libKF5PimTextEdit5
Summary:        KDE PIM Libraries: Text editing functionality
Group:          Development/Libraries/KDE
Requires:       %{name}

%description  -n libKF5PimTextEdit5
This package provides text editing functionality for KDE PIM applications

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       libKF5PimTextEdit5 = %{version}
Requires:       cmake(KF5SyntaxHighlighting)
Requires:       cmake(KF5TextWidgets)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%setup -q -n kpimtextedit-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5PimTextEdit5 -p /sbin/ldconfig
%postun -n libKF5PimTextEdit5 -p /sbin/ldconfig

%files
%{_kf5_debugdir}/kpimtextedit.categories

%files -n libKF5PimTextEdit5
%license COPYING.LIB
%{_kf5_libdir}/libKF5PimTextEdit.so.*

%files devel
%license COPYING.LIB
%{_kf5_cmakedir}/KF5PimTextEdit/
%{_kf5_includedir}/KPIMTextEdit/
%{_kf5_includedir}/kpimtextedit_version.h
%{_kf5_libdir}/libKF5PimTextEdit.so
%{_kf5_mkspecsdir}/qt_KPIMTextEdit.pri
%{_kf5_plugindir}/designer/kpimtexteditwidgets.so

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
