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
Version:        1.7.5
Release:        0
Summary:        A graphical IRC client by KDE
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            https://konversation.kde.org/
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-with-Qt-5.13.patch
Patch1:         add-missing-includes.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel >= %{kf5_version}
BuildRequires:  kbookmarks-devel >= %{kf5_version}
BuildRequires:  kconfig-devel >= %{kf5_version}
BuildRequires:  kconfigwidgets-devel >= %{kf5_version}
BuildRequires:  kcoreaddons-devel >= %{kf5_version}
BuildRequires:  kcrash-devel >= %{kf5_version}
BuildRequires:  kdbusaddons-devel >= %{kf5_version}
BuildRequires:  kdoctools-devel >= %{kf5_version}
BuildRequires:  kemoticons-devel >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  kglobalaccel-devel >= %{kf5_version}
BuildRequires:  ki18n-devel >= %{kf5_version}
BuildRequires:  kiconthemes-devel >= %{kf5_version}
BuildRequires:  kidletime-devel >= %{kf5_version}
BuildRequires:  kio-devel >= %{kf5_version}
BuildRequires:  kitemviews-devel >= %{kf5_version}
BuildRequires:  knotifications-devel >= %{kf5_version}
BuildRequires:  knotifyconfig-devel >= %{kf5_version}
BuildRequires:  kparts-devel >= %{kf5_version}
BuildRequires:  kwallet-devel >= %{kf5_version}
BuildRequires:  kwidgetsaddons-devel >= %{kf5_version}
BuildRequires:  kwindowsystem-devel >= %{kf5_version}
BuildRequires:  libqca-qt5-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  solid-devel >= %{kf5_version}
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.5.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.5.0
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
%autosetup -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS COPYING-DOCS ChangeLog NEWS README
%dir %{_kf5_appstreamdir}
%dir %{_kf5_sharedir}/kconf_update/
%doc %{_kf5_htmldir}/en/konversation/
%{_kf5_applicationsdir}/org.kde.konversation.desktop
%{_kf5_appstreamdir}/org.kde.konversation.appdata.xml
%{_kf5_bindir}/konversation
%{_kf5_iconsdir}/hicolor/*/actions/konv_message.*
%{_kf5_iconsdir}/hicolor/*/apps/konversation.*
%{_kf5_notifydir}/konversation.notifyrc
%{_kf5_sharedir}/kconf_update/konversation*
%{_kf5_sharedir}/konversation/
%{_kf5_kxmlguidir}/konversation/

%files lang -f %{name}.lang
%dir %{_kf5_htmldir}/pt_BR/
%doc %{_kf5_htmldir}/*/konversation/
%exclude %{_kf5_htmldir}/en/konversation

%changelog
