#
# spec file for package tellico
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
%define qt6_version 6.4.0

Name:           tellico
Version:        4.1
Release:        0
Summary:        A Collection Manager
License:        GPL-2.0-or-later
URL:            https://tellico-project.org/
Source0:        https://tellico-project.org/files/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libcsv-devel >= 3.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KCddb6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KSaneWidgets6)
BuildRequires:  cmake(Qt6Charts) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(yaz) >= 2.0
# Needs QtWebEngine
ExclusiveArch:  x86_64 aarch64 riscv64

%description
Tellico is an application for organizing your collections. It provides
default templates for books, bibliographies, videos, music, video games, coins,
stamps, trading cards, comic books, and wines.

%lang_package

%prep
%autosetup -p1

# E: env-script-interpreter
sed -i 's#env perl$#perl#' src/config/*-update.pl
sed -i 's#env python$#python3#' src/fetch/scripts/*.py

%build
%cmake_kf6 -DENABLE_WEBCAM:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang tellico tellico.lang --with-html

%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%doc %lang(en) %{_kf6_htmldir}/en/tellico/
%config %{_kf6_configdir}/tellico*
%{_kf6_applicationsdir}/org.kde.tellico.desktop
%{_kf6_appstreamdir}/org.kde.tellico.appdata.xml
%{_kf6_bindir}/tellico
%{_kf6_configkcfgdir}/tellico_config.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/tellico.png
%{_kf6_iconsdir}/hicolor/*/mimetypes/application-x-tellico.png
%{_kf6_knsrcfilesdir}/tellico-template.knsrc
%{_kf6_sharedir}/kconf_update/tellico*
%{_kf6_sharedir}/mime/packages/tellico.xml
%{_kf6_sharedir}/tellico/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/tellico/

%changelog
