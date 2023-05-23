#
# spec file for package cool-retro-term
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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


Name:           cool-retro-term
Version:        1.2.0
Release:        0
Summary:        Terminal emulator which mimics old screens
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/Swordfish90/cool-retro-term
Source:         https://github.com/Swordfish90/cool-retro-term/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     int10h-oldschoolpc-fonts
Conflicts:       qmltermwidget

%description
cool-retro-term is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup -q

%build
%qmake5
%make_jobs

%install
%qmake5_install
install -Dpm 0644 cool-retro-term.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -Dpm 0644 packaging/debian/cool-retro-term.1 %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%license gpl-2.0.txt gpl-3.0.txt
%doc README.md
%{_bindir}/cool-retro-term
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_libdir}/qt5/qml/QMLTermWidget/*
%dir %{_libdir}/qt5/qml/QMLTermWidget

%changelog
