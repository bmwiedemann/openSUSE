#
# spec file for package mpc-qt
#
# Copyright (c) 2025 SUSE LLC
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


Name:           mpc-qt
Version:        24.12.1
Release:        0
Summary:        Media Player Classic Qute Theater
License:        GPL-2.0-only
URL:            https://github.com/mpc-qt/mpc-qt
Source0:        https://github.com/mpc-qt/mpc-qt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# For dirs ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt6-tools-linguist
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(mpv) >= 1.101.0

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
qmake6 \
  PREFIX=%{_prefix} MPCQT_VERSION=%{version} \
  mpc-qt.pro
%qmake6_build

%install
%qmake6_install

# Use %%doc instead
rm -r %{buildroot}%{_datadir}/doc/mpc-qt

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/io.github.mpc-qt.mpc-qt.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
