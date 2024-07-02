#
# spec file for package kdiff3
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
Name:           kdiff3
Version:        1.11.2
Release:        0
Summary:        Code Comparison Utility
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kdiff3
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        kdiff3.keyring
%endif
BuildRequires:  boost-devel >= 1.71
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KDiff3 is a program that:

* Compares or merges two or three text input files or directories
* Shows the differences line-by-line and character-by-character
* Provides an automatic merge facility and an integrated editor for
  solving merge conflicts
* Supports KDE's KIO framework (allows accessing ftp, sftp, fish, smb, etc.)

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%suse_update_desktop_file -r org.kde.kdiff3 Qt KDE Utility TextEditor X-KDE-Utilities-File

%find_lang %{name} --all-name --with-man --with-html

%fdupes %{buildroot}

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kdiff3/
%doc %lang(en) %{_kf6_mandir}/man1/kdiff3.1%{?ext_man}
%{_kf6_applicationsdir}/org.kde.kdiff3.desktop
%{_kf6_appstreamdir}/org.kde.kdiff3.appdata.xml
%{_kf6_bindir}/kdiff3
%{_kf6_iconsdir}/hicolor/*/apps/kdiff3.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kdiff3.svgz
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/kdiff3fileitemaction.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kdiff3

%changelog
