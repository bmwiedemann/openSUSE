#
# spec file for package kdesignerplugin
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


# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           kdesignerplugin
Version:        5.116.0
Release:        0
Summary:        Framework for integration of KDE frameworks widgets with Qt Designer
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  cmake(KF5Config) >= %{_kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Designer) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}

%description
This framework provides plugins for Qt Designer that allow it to display
the widgets provided by various KDE frameworks, as well as a utility
(kgendesignerplugin) that can be used to generate other such plugins
from ini-style description files.

%package devel
Summary:        Build environment for kdesignerplugin, a framework for integration of KDE frameworks widgets
Requires:       %{name} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

%description devel
This framework provides plugins for Qt Designer that allow it to display
the widgets provided by various KDE frameworks, as well as a utility
(kgendesignerplugin) that can be used to generate other such plugins
from ini-style description files. Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-qt --with-man --without-mo --all-name

%ldconfig_scriptlets

%files lang -f %{name}.lang

%files
%license COPYING*
%doc README*
%{_kf5_bindir}/kgendesignerplugin
%doc %lang(en) %{_kf5_mandir}/*/kgendesignerplugin.*

%files devel
%{_kf5_libdir}/cmake/KF5DesignerPlugin/

%changelog
