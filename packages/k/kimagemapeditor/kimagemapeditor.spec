#
# spec file for package kimagemapeditor
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kimagemapeditor
Version:        22.12.0
Release:        0
Summary:        HTML Image Map Editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kimagemapeditor
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
# Only build on archs where Qt5WebEngine is available
ExcludeArch:    ppc ppc64 ppc64le s390 s390x

%description
A tool to edit image maps of HTML files

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file -r org.kde.kimagemapeditor Office WebDevelopment

%fdupes -s %{buildroot}

%files
%license COPYING*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_applicationsdir}/org.kde.kimagemapeditor.desktop
%{_kf5_appstreamdir}/org.kde.kimagemapeditor.appdata.xml
%{_kf5_bindir}/kimagemapeditor
%{_kf5_debugdir}/kimagemapeditor.categories
%{_kf5_htmldir}/en/kimagemapeditor/
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_plugindir}/kf5/parts/kimagemapeditorpart.so
%{_kf5_servicesdir}/kimagemapeditorpart.desktop
%{_kf5_sharedir}/kimagemapeditor/

%files lang -f %{name}.lang

%changelog
