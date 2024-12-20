#
# spec file for package sddm-conf
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


%define  _name  sddm_conf
Name:           sddm-conf
Version:        0.2.0
Release:        0
Summary:        SDDM configuration editor
License:        MIT
URL:            https://github.com/qtilities/sddm-conf
Source0:        https://github.com/qtilities/sddm-conf/archive/refs/tags/%{version}.tar.gz
BuildRequires:  extra-cmake-modules >= 6.0
BuildRequires:  cmake >= 3.15
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  qtilitools
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
Conflicts:      sddm-config-editor

%description
Configuration editor for SDDM similar to sddm-config-editor, but written in
C++.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DPROJECT_QT_VERSION=6
%kf6_build

%install
%kf6_install
%suse_update_desktop_file -r -G "Display Manager Configuration" -N "SDDM Configuration" %{_name} Qt Settings System

%find_lang %{name} --with-qt

%files
%license COPYING
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/metainfo/%{_name}.appdata.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations

%changelog
