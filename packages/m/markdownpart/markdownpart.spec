#
# spec file for package markdownpart
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


%define kf5_version 5.91.0
%define qt5_version 5.15.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           markdownpart
Version:        22.12.0
Release:        0
Summary:        KPart for rendering Markdown content
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Parts) >= %{kf5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

%description
A(nother) Markdown viewer KParts plugin, which allows
KParts-using applications to display files in
Markdown format in the rendered target format.
Examples are Ark, Krusader, Kate's preview plugin & Konqueror.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name}

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%{_kf5_appstreamdir}/org.kde.markdownpart.metainfo.xml
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_plugindir}/kf5/parts/markdownpart.so
%{_kf5_servicesdir}/markdownpart.desktop

%files lang -f %{name}.lang

%changelog
