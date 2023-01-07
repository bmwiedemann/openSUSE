#
# spec file for package skanlite
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
Name:           skanlite
Version:        22.12.1
Release:        0
Summary:        Image Scanner Application
License:        LGPL-2.1-or-later
URL:            https://www.kde.org/applications/graphics/skanlite/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  libpng-devel
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sane)
BuildRequires:  cmake(KSaneCore)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}-doc < %{version}

%description
Skanlite is an image scanner application by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name
%{kf5_find_htmldocs}

# Fix rpmlint warning "script-without-shebang"
chmod 644 %{buildroot}%{_kf5_applicationsdir}/org.kde.skanlite.desktop

%files
%license LICENSES/*
%doc src/TODO
%doc %lang(en) %{_kf5_htmldir}/en/skanlite/
%{_kf5_applicationsdir}/org.kde.skanlite.desktop
%{_kf5_appstreamdir}/org.kde.skanlite.appdata.xml
%{_kf5_bindir}/skanlite
%{_kf5_iconsdir}/hicolor/48x48/apps/org.kde.skanlite.svg

%files lang -f %{name}.lang

%changelog
