#
# spec file for package kgamma5
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without released
Name:           kgamma5
Version:        5.26.4
Release:        0
Summary:        Display gamma configuration
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kgamma5-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kgamma5-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xxf86vm)
%if %{with released}
Recommends:     %{name}-lang
%endif
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Provides:       kgamma = %{version}
Obsoletes:      kgamma < %{version}
%endif

%description
This package contains a KDE system settings module to configure display
gamma.

%lang_package

%prep
%setup -q -n %{name}-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

%files
%license LICENSES/*
%{_kf5_plugindir}/
%{_kf5_sharedir}/kgamma/
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
%doc %{_kf5_htmldir}/en/*/

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
