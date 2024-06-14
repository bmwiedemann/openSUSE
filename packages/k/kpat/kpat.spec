#
# spec file for package kpat
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150400
%bcond_without bhsolver
%endif

%bcond_without released
Name:           kpat
Version:        24.05.1
Release:        0
Summary:        Patience card game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kpat
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  freecell-solver-devel
%if %{with bhsolver}
BuildRequires:  pkgconfig(libblack-hole-solver)
%endif
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kdegames-carddecks-default
Obsoletes:      kpat5 < %{version}
Provides:       kpat5 = %{version}

%description
KPatience is a collection of various patience games known all over the
world. It includes Klondike, Freecell, Yukon, Forty and Eight and many
more. The game has nice graphics and many different carddecks.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 \
%if %{with bhsolver}
  -DWITH_BH_SOLVER:BOOL=TRUE
%else
  -DWITH_BH_SOLVER:BOOL=FALSE
%endif

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name

%files
%license COPYING COPYING.DOC
%doc %lang(en) %{_kf6_htmldir}/en/kpat/
%{_kf6_applicationsdir}/org.kde.kpat.desktop
%{_kf6_appstreamdir}/org.kde.kpat.appdata.xml
%{_kf6_bindir}/kpat
%{_kf6_configkcfgdir}/kpat.kcfg
%{_kf6_debugdir}/kpat.categories
%{_kf6_iconsdir}/hicolor/*/*/kpat.*
%{_kf6_knsrcfilesdir}/kcardtheme.knsrc
%{_kf6_knsrcfilesdir}/kpat.knsrc
%{_kf6_libdir}/libkcardgame.so
%{_kf6_mandir}/man6/kpat.6.gz
%{_kf6_sharedir}/kpat/
%{_kf6_sharedir}/mime/packages/kpatience.xml

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kpat/

%changelog
