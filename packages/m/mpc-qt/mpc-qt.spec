#
# spec file for package mpc-qt
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        26.01
Release:        0
Summary:        Media Player Classic Qute Theater
License:        GPL-2.0-only
URL:            https://github.com/mpc-qt/mpc-qt
Source0:        https://github.com/mpc-qt/mpc-qt/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
# For dirs ownership
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version} > 1600
BuildRequires:  libboost_headers-devel
%else
%if 0%{?suse_version} > 1500
BuildRequires:  libboost_system-devel
%else
BuildRequires:  gcc13-c++
BuildRequires:  libboost_system1_75_0-devel
%endif
%endif
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(mpv) >= 1.101.0

%description
A clone of Media Player Classic reimplemented in Qt.

%prep
%autosetup -p1
rm -rf mpv-dev

%build
export CXX=g++
test -x "$(type -p g++-13)" && export CXX=g++-13
%cmake \
  -DMPCQT_VERSION=%{version}
%cmake_build

%install
%cmake_install

# Use %%doc instead
rm -r %{buildroot}%{_datadir}/doc/mpc-qt

%files
%doc README.md DOCS/ipc.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/io.github.mpc_qt.mpc-qt.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/io.github.mpc_qt.mpc-qt.metainfo.xml

%changelog
