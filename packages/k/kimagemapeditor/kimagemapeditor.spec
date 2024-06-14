#
# spec file for package kimagemapeditor
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

%bcond_without released
Name:           kimagemapeditor
Version:        24.05.1
Release:        0
Summary:        HTML Image Map Editor
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kimagemapeditor
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# No QtWebEngine for other archs
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
A tool to edit image maps of HTML files

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file -r org.kde.kimagemapeditor Office WebDevelopment

%fdupes -s %{buildroot}

%files
%license COPYING*
%doc %lang(en) %{_kf6_htmldir}/en/kimagemapeditor/
%{_kf6_applicationsdir}/org.kde.kimagemapeditor.desktop
%{_kf6_appstreamdir}/org.kde.kimagemapeditor.appdata.xml
%{_kf6_bindir}/kimagemapeditor
%{_kf6_debugdir}/kimagemapeditor.categories
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_plugindir}/kf6/parts/kimagemapeditorpart.so
%{_kf6_sharedir}/kimagemapeditor/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kimagemapeditor/

%changelog
