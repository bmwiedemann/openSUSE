#
# spec file for package milou5
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
Name:           milou5
Version:        5.20.0
Release:        0
Summary:        Dedicated search application built on top of Baloo
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://projects.kde.org/milou
Source:         milou-%{version}.tar.xz
%if %{with lang}
Source1:        milou-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons) >= 5.25.0
BuildRequires:  cmake(KF5Declarative) >= 5.25.0
BuildRequires:  cmake(KF5I18n) >= 5.25.0
BuildRequires:  cmake(KF5ItemModels) >= 5.25.0
BuildRequires:  cmake(KF5Plasma) >= 5.25.0
BuildRequires:  cmake(KF5Runner) >= 5.25.0
BuildRequires:  cmake(KF5Service) >= 5.25.0
BuildRequires:  cmake(KF5WindowSystem) >= 5.25.0
BuildRequires:  cmake(Qt5Qml) >= 5.4.0
BuildRequires:  cmake(Qt5Quick) >= 5.4.0
BuildRequires:  cmake(Qt5Test) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
Recommends:     %{name}-lang

%description
A dedicated search application built on top of Baloo

%lang_package

%prep
%autosetup -p1 -n milou-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif
  %fdupes -s %{buildroot}%{_kf5_localedir}/

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%license COPYING*
%{_kf5_libdir}/libmilou.so.*
%{_kf5_qmldir}/
%{_kf5_plasmadir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/
%{_kf5_plugindir}/
%{_kf5_appstreamdir}/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
