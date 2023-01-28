#
# spec file for package qt6ct
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


Name:           qt6ct
Version:        0.7
Release:        0
Summary:        Qt 6 Configuration Tool
License:        BSD-2-Clause
Group:          Development/Libraries/X11
URL:            https://github.com/trialuser02/qt6ct
Source:         https://github.com/trialuser02/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
Requires:       libQt6Svg6

%description
This program allows users to configure Qt6 settings (theme, font, icons,
etc.) under DE/WM without Qt integration.

%prep
%autosetup -p1

%build
%cmake_qt6
%qt6_build

%install
%qt6_install

%files
%license COPYING
%doc AUTHORS ChangeLog README
%dir %{_qt6_pluginsdir}/styles
%{_bindir}/qt6ct
%{_qt6_sharedir}/qt6ct/
%{_qt6_pluginsdir}/platformthemes/libqt6ct.so
%{_qt6_pluginsdir}/styles/libqt6ct-style.so
%{_datadir}/applications/qt6ct.desktop

%changelog
