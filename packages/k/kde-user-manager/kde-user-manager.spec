#
# spec file for package kde-user-manager
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


%bcond_without lang
Name:           kde-user-manager
Version:        5.19.90
Release:        0
Summary:        KDE System Settings module to manage users
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         user-manager-%{version}.tar.xz
%if %{with lang}
Source1:        user-manager-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.3.0
BuildRequires:  libpwquality-devel
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
Requires:       accountsservice
Recommends:     %{name}-lang

%description
A simple system settings module to manage the users of your systems.

%lang_package

%prep
%setup -q -n user-manager-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
%kf5_find_lang
%endif

%files
%license COPYING
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_sharedir}/user-manager/
%{_kf5_debugdir}/user-manager.categories

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
