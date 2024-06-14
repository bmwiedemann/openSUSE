#
# spec file for package kate
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
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           kate
Version:        24.05.1
Release:        0
Summary:        Advanced Text Editor
License:        GPL-3.0-or-later
URL:            https://kate-editor.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         0001-Defuse-root-block.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditor) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kate-plugins = %{version}
Recommends:     kuiviewer
Recommends:     markdownpart
Recommends:     svgpart
Obsoletes:      kate5 < %{version}
Provides:       kate5 = %{version}

%description
Kate is an advanced text editor by KDE.

%package -n kwrite
Summary:        KDE Text Editor
Requires:       kate-plugins = %{version}
Obsoletes:      kwrite5 < %{version}

%description -n kwrite
KWrite is a text editor by KDE.

%package plugins
Summary:        KDE Text Editor plugins
Obsoletes:      kate5-plugins < %{version}
Provides:       ktexteditorpreviewplugin = %{version}
Obsoletes:      ktexteditorpreviewplugin < %{version}

%description plugins
Kate is an advanced text editor by KDE. This package contains
plugins and data files for Kate and KWrite editors.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# Remove exotic icon sizes
rm -r %{buildroot}%{_kf6_iconsdir}/hicolor/{150x150,310x310,44x44}

%find_lang %{name} --with-man --with-html --all-name

%ldconfig_scriptlets

%files
%doc README.md
%doc %lang(en) %{_kf6_htmldir}/en/kate/
%doc %lang(en) %{_kf6_htmldir}/en/katepart/
%doc %{_kf6_mandir}/man1/kate.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.kate.desktop
%{_kf6_appstreamdir}/org.kde.kate.appdata.xml
%{_kf6_bindir}/kate
%{_kf6_iconsdir}/hicolor/*/apps/kate.*
%{_kf6_libdir}/libkateprivate.so.*

%files -n kwrite
%doc README.md
%{_kf6_applicationsdir}/org.kde.kwrite.desktop
%{_kf6_appstreamdir}/org.kde.kwrite.appdata.xml
%{_kf6_bindir}/kwrite
%{_kf6_iconsdir}/hicolor/*/apps/kwrite.*

%files plugins
%{_kf6_plugindir}/kf6/ktexteditor/
%{_kf6_sharedir}/kateproject/
%{_kf6_sharedir}/katexmltools/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kate/
%exclude %{_kf6_htmldir}/en/katepart/

%changelog
