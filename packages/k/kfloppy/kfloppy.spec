#
# spec file for package kfloppy
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
Name:           kfloppy
Version:        23.04.3
Release:        0
Summary:        Floppy Formatter
License:        GPL-2.0-only
URL:            https://apps.kde.org/kfloppy
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)

%description
KDE Floppy Disk Utility

%lang_package

%prep
%autosetup -p1 -n kfloppy-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kfloppy System Filesystem

%files
%license COPYING
%doc README TODO
%doc %lang(en) %{_kf5_htmldir}/en/kfloppy/
%{_kf5_applicationsdir}/org.kde.kfloppy.desktop
%{_kf5_appstreamdir}/org.kde.kfloppy.appdata.xml
%{_kf5_bindir}/kfloppy
%{_kf5_debugdir}/kfloppy.categories
%{_kf5_iconsdir}/hicolor/*/apps/kfloppy.png

%files lang -f %{name}.lang

%changelog
