#
# spec file for package markdownpart
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
Name:           markdownpart
Version:        24.05.1
Release:        0
Summary:        KPart for rendering Markdown content
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
A(nother) Markdown viewer KParts plugin, which allows
KParts-using applications to display files in
Markdown format in the rendered target format.
Examples are Ark, Krusader, Kate's preview plugin & Konqueror.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%{_kf6_appstreamdir}/org.kde.markdownpart.metainfo.xml
%{_kf6_plugindir}/kf6/parts/markdownpart.so

%files lang -f %{name}.lang

%changelog
