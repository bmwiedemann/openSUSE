#
# spec file for package ghostwriter
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
Name:           ghostwriter
Version:        23.04.0
Release:        0
Summary:        A distraction-free Markdown editor
License:        GPL-3.0-or-later
URL:            https://ghostwriter.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(hunspell)
Recommends:     multimarkdown
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
ghostwriter is a text editor for Markdown, which is a plain text
markup format. For more information about Markdown, please visit John
Gruber’s website at http://www.daringfireball.net. ghostwriter
provides a relaxing, distraction-free writing environment.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-qt --with-man

%files
%license LICENSES/*
%doc README.md
%{_kf5_applicationsdir}/org.kde.ghostwriter.desktop
%{_kf5_appstreamdir}/org.kde.ghostwriter.metainfo.xml
%{_kf5_bindir}/ghostwriter
%{_kf5_iconsdir}/hicolor/*/apps/ghostwriter.*
%{_kf5_mandir}/man1/ghostwriter.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
