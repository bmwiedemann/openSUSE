#
# spec file for package kdebugsettings
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdebugsettings
Version:        19.08.3
Release:        0
Summary:        Program to set debug verbosity for KDE applications
License:        LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      kdebugsettings5 < %{version}
Provides:       kdebugsettings5 = %{version}
Recommends:     %{name}-lang

%description
This program allows to tune the debug output of KDE applications, ranging
from verbose to completely silent.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kdebugsettings-%{version}

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%suse_update_desktop_file org.kde.kdebugsettings Utility DesktopUtility

%files
%license COPYING*
%{_kf5_debugdir}/kde.categories
%{_kf5_debugdir}/kde.renamecategories
%{_kf5_applicationsdir}/org.kde.kdebugsettings.desktop
%{_kf5_bindir}/kdebugsettings
%{_kf5_debugdir}/kdebugsettings.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
