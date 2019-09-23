#
# spec file for package cool-retro-term
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           cool-retro-term
Version:        1.1.1
Release:        0
Summary:        Terminal emulator which mimics old screens
License:        GPL-3.0-or-later
Group:          System/X11/Terminals
URL:            https://github.com/Swordfish90/cool-retro-term
Source:         https://github.com/Swordfish90/cool-retro-term/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cool-retro-term-disable-bundled-qmltermwidget.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       qmltermwidget >= 0.2.0
Recommends:     int10h-oldschoolpc-fonts

%description
cool-retro-term is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup -q
%patch0 -p1

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

%changelog
