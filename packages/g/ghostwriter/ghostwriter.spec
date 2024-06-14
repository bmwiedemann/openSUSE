#
# spec file for package ghostwriter
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
Name:           ghostwriter
Version:        24.05.1
Release:        0
Summary:        A distraction-free Markdown editor
License:        GPL-3.0-or-later
URL:            https://ghostwriter.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebChannel) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(hunspell)
Recommends:     multimarkdown
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
ghostwriter is a text editor for Markdown, which is a plain text markup format.
For more information about Markdown, please visit John Gruber’s website at
http://www.daringfireball.net.
Ghostwriter provides a relaxing, distraction-free writing environment.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-qt --with-man

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_mandir}/man1/ghostwriter.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.ghostwriter.desktop
%{_kf6_appstreamdir}/org.kde.ghostwriter.metainfo.xml
%{_kf6_bindir}/ghostwriter
%{_kf6_iconsdir}/hicolor/*/apps/ghostwriter.*

%files lang -f %{name}.lang

%changelog
