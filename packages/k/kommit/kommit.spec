#
# spec file for package kommit
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2023 Matteo De Carlo
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
Name:           kommit
Version:        1.0.2
Release:        0
Summary:        Graphical Git Client
License:        GPL-3.0-only
URL:            https://apps.kde.org/kommit
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kommit.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(Qt5Test)

%description
Graphical Git Client

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

%ldconfig_scriptlets

%files
%doc README.md
%doc %lang(en) %{_kf5_htmldir}/en/*/
%license LICENSE
%{_kf5_bindir}/kommit
%{_kf5_bindir}/kommitdiff
%{_kf5_bindir}/kommitmerge
%{_kf5_libdir}/lib%{name}.so.*
%{_kf5_libdir}/lib%{name}diff.so.*
%{_kf5_libdir}/lib%{name}gui.so.*
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%dir %{_kf5_plugindir}/kf5/overlayicon
%{_kf5_plugindir}/kf5/kfileitemaction/kommititemaction.so
%{_kf5_plugindir}/kf5/overlayicon/kommitoverlayplugin.so
%{_kf5_iconsdir}/hicolor/*/apps/%{name}.*
%{_kf5_iconsdir}/hicolor/scalable/actions/*.svg
%{_kf5_applicationsdir}/org.kde.%{name}.desktop
%{_kf5_applicationsdir}/org.kde.%{name}.diff.desktop
%{_kf5_applicationsdir}/org.kde.%{name}.merge.desktop
%{_kf5_appstreamdir}/org.kde.%{name}.appdata.xml
%{_kf5_debugdir}/%{name}.categories

%files lang -f %{name}.lang

%changelog
