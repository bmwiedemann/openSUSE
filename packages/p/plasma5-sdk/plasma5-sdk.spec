#
# spec file for package plasma5-sdk
#
# Copyright (c) 2023 SUSE LLC
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
Name:           plasma5-sdk
Version:        5.26.5
Release:        0
Summary:        Plasma SDK
License:        GPL-2.0-only AND LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://cgit.kde.org/plasma-sdk.git
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-sdk-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-sdk-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  breeze5-icons
BuildRequires:  extra-cmake-modules >= 1.8.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive) >= 5.98.0
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5PlasmaQuick)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Requires:       bash
Requires:       kirigami2
Requires:       plasmaengineexplorer5
Conflicts:      plasmate
Recommends:     %{name}-lang

%description
Plasma SDK taylored for development of Plasma components,
such as Widgets, Runners, Dataengines.

%package -n plasmaengineexplorer5
Summary:        Provides direct access to plasma data engines
License:        GPL-2.0-only
Group:          Development/Tools/Other
Conflicts:      plasmate

%description -n plasmaengineexplorer5
Plasmaengineexplorer is a graphical tool allowing developers to
test Plasma data engines without writing a Plasma applet.

%lang_package

%prep
%setup -q -n plasma-sdk-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

  mkdir -p %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
  cp -L %{_kf5_iconsdir}/breeze/apps/22/plasma.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
  cp -L %{_kf5_iconsdir}/breeze/apps/48/cuttlefish.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/
  cp -L %{_kf5_iconsdir}/breeze/actions/24/tools-wizard.svg %{buildroot}%{_kf5_iconsdir}/hicolor/scalable/apps/

  # Workaround for kde#382275, "The following applications are going to be removed: Cuttlefish".
  # The package contains two appdata files with the same Name, which libzypp can't handle (boo#1038368)
  rm %{buildroot}%{_kf5_appstreamdir}/org.kde.plasma.cuttlefish.appdata.xml

%if %{with released}
%find_lang cuttlefish %{name}.lang
%find_lang plasma_shell_org.kde.plasmoidviewershell %{name}.lang
%find_lang org.kde.plasma.themeexplorer %{name}.lang
%find_lang org.kde.plasma.lookandfeelexplorer %{name}.lang
%find_lang plasmoidviewer %{name}.lang
%find_lang plasmaengineexplorer %{name}.lang
%find_lang cuttlefish_editorplugin %{name}.lang
%endif

%if %{with released}
%files lang -f %{name}.lang
%endif

%files
%license LICENSES/*
%{_kf5_bindir}/cuttlefish
%{_kf5_bindir}/plasmoidviewer
%{_kf5_bindir}/plasmathemeexplorer
%{_kf5_bindir}/lookandfeelexplorer
%{_kf5_sharedir}/plasma/
%{_kf5_sharedir}/kpackage/
%{_kf5_plugindir}/
%{_kf5_applicationsdir}/org.kde.plasma.cuttlefish.desktop
%{_kf5_applicationsdir}/org.kde.plasma.themeexplorer.desktop
%{_kf5_applicationsdir}/org.kde.plasma.lookandfeelexplorer.desktop
%{_kf5_applicationsdir}/org.kde.plasmoidviewer.desktop
%dir %{_kf5_iconsdir}/hicolor/*
%dir %{_kf5_iconsdir}/hicolor/*/*
%{_kf5_iconsdir}/*/*/*/*.*
%{_mandir}/man1/plasmoidviewer.1%{ext_man}
%{_kf5_appstreamdir}/org.kde.plasmoidviewer.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.plasmoidviewershell.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.themeexplorer.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.lookandfeelexplorer.appdata.xml
%{_kf5_servicesdir}/plasma-shell-org.kde.plasma.plasmoidviewershell.desktop

%files -n plasmaengineexplorer5
%license LICENSES/*
%{_kf5_bindir}/plasmaengineexplorer
%{_mandir}/man1/plasmaengineexplorer.1%{ext_man}
%{_kf5_applicationsdir}/org.kde.plasmaengineexplorer.desktop
%{_kf5_appstreamdir}/org.kde.plasmaengineexplorer.appdata.xml

%changelog
