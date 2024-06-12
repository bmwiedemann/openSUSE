#
# spec file for package cutecom
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


Name:           cutecom
Version:        0.60.0
Release:        0
Summary:        A graphical serial terminal
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://gitlab.com/cutecom/cutecom
Source:         https://gitlab.com/%{name}/%{name}/-/archive/v%{version}-RC1/%{name}-v%{version}-RC1.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Widgets)

%description
CuteCom is a graphical serial terminal, similar to minicom. It is
written using the Qt library.

It is aimed mainly at hardware developers or other people who need a
terminal to talk to their devices.

%prep
%autosetup -n %{name}-v%{version}-RC1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc Changelog TODO CREDITS README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/com.gitlab.%{name}.%{name}.appdata.xml

%changelog
