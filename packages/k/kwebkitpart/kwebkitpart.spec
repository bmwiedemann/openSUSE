#
# spec file for package kwebkitpart
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kwebkitpart
Version:        1.3.4git.20171117T115813~cca571d
Release:        0
Summary:        KDE Webkit web browser component
License:        LGPL-2.0+ and LGPL-2.1+
Group:          System/GUI/KDE
Url:            https://cgit.kde.org/kwebkitpart.git
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-lang.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdewebkit-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kparts-devel
BuildRequires:  pkgconfig
BuildRequires:  sonnet-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     kwebkitpart-lang
Provides:       libkdenetwork1 = 4.3.0.svn1001692-36.1
Obsoletes:      libkdenetwork1 < 4.3.0.svn1001692-36.1
Provides:       kde4-webkitpart = 4.3.90.svn1072556
Obsoletes:      kde4-webkitpart < 4.3.90.svn1072556
Obsoletes:      kwebkitpart-devel < 1.2.0git20111013
Provides:       kwebkitpart-devel = 1.2.0git20111013
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A webkit web browser component for KDE (KPart).

%lang_package

%prep
%setup -q -n %{name}-%{version} -a 1
echo "ki18n_install(po)" >> CMakeLists.txt

%build
%cmake_kf5 -d build
%make_jobs

%install
pushd build
%kf5_makeinstall
popd
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_kf5_debugdir}/kwebkitpart.categories
%{_kf5_plugindir}
%{_kf5_servicesdir}/kwebkitpart.desktop
%{_kf5_appsdir}/kwebkitpart
%{_kf5_iconsdir}/hicolor/*/apps/webkit.*
%{_kf5_sharedir}/kxmlgui5/kwebkitpart
%dir %{_kf5_iconsdir}/hicolor/*
%dir %{_kf5_iconsdir}/hicolor/*/apps
%doc COPYING.LIB README

%files lang -f %{name}.lang

%changelog
