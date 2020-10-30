#
# spec file for package konversation
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


%define kf5_version 5.25.0
Name:           konversation
Version:        1.7.7
Release:        0
Summary:        A graphical IRC client by KDE
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://konversation.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libqca-qt5-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive) >= %{kf5_version}
BuildRequires:  cmake(KF5Bookmarks) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DocTools) >= %{kf5_version}
BuildRequires:  cmake(KF5Emoticons) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5IdleTime) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemViews) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5NotifyConfig) >= %{kf5_version}
BuildRequires:  cmake(KF5Parts) >= %{kf5_version}
BuildRequires:  cmake(KF5Solid) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core) >= 5.5.0
BuildRequires:  cmake(Qt5Gui) >= 5.5.0
BuildRequires:  cmake(Qt5Widgets) >= 5.5.0
Recommends:     %{name}-lang = %{version}

%description
Konversation is an Internet Relay Chat (IRC) client built on the
KDE Platform.

Features:

 SSL server support
 Bookmarking support
 Multiple servers and channels in one single window
 DCC file transfer
 Multiple identities for different servers
 Text decorations and colors
 OnScreen Display for notifications
 Automatic UTF-8 detection
 Per channel encoding support
 Theme support for nick icons

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS COPYING-DOCS ChangeLog NEWS README
%doc %{_kf5_htmldir}/en/konversation/
%dir %{_kf5_appstreamdir}
%dir %{_kf5_sharedir}/kconf_update/
%{_kf5_applicationsdir}/org.kde.konversation.desktop
%{_kf5_appstreamdir}/org.kde.konversation.appdata.xml
%{_kf5_bindir}/konversation
%{_kf5_iconsdir}/hicolor/*/actions/konv_message.*
%{_kf5_iconsdir}/hicolor/*/apps/konversation.*
%{_kf5_kxmlguidir}/konversation/
%{_kf5_notifydir}/konversation.notifyrc
%{_kf5_sharedir}/kconf_update/konversation*
%{_kf5_sharedir}/konversation/

%files lang -f %{name}.lang
%dir %{_kf5_htmldir}/pt_BR/
%doc %{_kf5_htmldir}/*/konversation/
%exclude %{_kf5_htmldir}/en/konversation

%changelog
