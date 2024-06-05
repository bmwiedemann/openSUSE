#
# spec file for package qterminal
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


Name:           qterminal
Version:        2.0.0
Release:        0
Summary:        A Qt-based terminal emulator
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/lxqt/qterminal
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  utempter-devel
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(qtermwidget6)
Recommends:     %{name}-lang = %{version}-%{release}

%description
The lightweight Qt terminal emulator.

%lang_package

%prep
%autosetup -p1

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%check
%ctest

%files
%doc AUTHORS CHANGELOG README.md CONTRIBUTING.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-drop.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/%{name}.metainfo.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}_bookmarks_example.xml
%license LICENSE

%files lang -f %{name}.lang
%dir %{_datadir}/qterminal
%dir %{_datadir}/qterminal/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
