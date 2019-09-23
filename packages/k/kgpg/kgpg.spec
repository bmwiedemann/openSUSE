#
# spec file for package kgpg
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kgpg
Version:        19.08.1
Release:        0
Summary:        Encryption Tool
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch1:         kgpg-autostart.diff
BuildRequires:  akonadi-contact-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kcalcore-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kservice-devel
BuildRequires:  ktexteditor-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libgpgme-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       gpg2
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Kgpg is a simple GUI for gpg

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kgpg-%{version}
%patch1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
#suse_update_desktop_file org.kde.kgpg.deskt Utility Security

%files
%license COPYING
%doc AUTHORS
%config %{_kf5_configdir}/autostart/org.kde.kgpg.desktop
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/kgpg/
%{_kf5_applicationsdir}/org.kde.kgpg.desktop
%{_kf5_appstreamdir}/org.kde.kgpg.appdata.xml
%{_kf5_bindir}/kgpg
%{_kf5_configkcfgdir}/kgpg.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kgpg.Key.xml
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kgpg/
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_sharedir}/kgpg/
%{_kf5_debugdir}/kgpg.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
