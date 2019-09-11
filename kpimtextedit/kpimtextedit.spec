#
# spec file for package kpimtextedit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.44.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kpimtextedit
Version:        19.08.0
Release:        0
Summary:        KDE PIM Libraries: Text edit functionality
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  grantlee5-devel
BuildRequires:  kcodecs-devel >= %{kf5_version}
BuildRequires:  kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kdesignerplugin-devel >= %{kf5_version}
BuildRequires:  kemoticons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kiconthemes-devel >= %{kf5_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  ktextwidgets-devel >= %{kf5_version}
BuildRequires:  kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  kxmlgui-devel >= %{kf5_version}
BuildRequires:  pkgconfig
BuildRequires:  sonnet-devel >= %{kf5_version}
BuildRequires:  syntax-highlighting-devel >= %{kf5_version}
BuildRequires:  pkgconfig(Qt5Designer) >= 5.8.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.8.0
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.8.0
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.34
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

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
Requires:       ktextwidgets-devel >= %{kf5_version}
Requires:       libKF5PimTextEdit5 = %{version}
Requires:       syntax-highlighting-devel >= %{kf5_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kpimtextedit-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %make_jobs

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
