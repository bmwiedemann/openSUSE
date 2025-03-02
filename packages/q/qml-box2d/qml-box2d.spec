#
# spec file for package qml-box2d
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


%define qt6_version 6.6.2

Name:           qml-box2d
Version:        0+git.1713207787.3a85439
Release:        0
Summary:        QML Box2D plugin
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/%{name}/%{name}
Source:         %{name}-%{version}.tar.xz
%if 0%{?suse_version} < 1599
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%endif
BuildRequires:  libbox2d-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This plugin is meant to be installed to your Qt/imports directory, or shipped
in a directory of which the parent is added as import path.

The goal is to expose the functionality of Box2D as QML components, in order
to make it easy to write physics-based games in QML.

%prep
%setup -q

%build
%if 0%{?suse_version} < 1599
export CC="/usr/bin/gcc-13"
export CXX="/usr/bin/g++-13"
%endif
%cmake
%cmake_build

%install
%cmake_install

rm -rf "%{buildroot}%{_libdir}/qt6/tests"

%files
%license COPYING
%doc README.md
%{_libdir}/Box2D
%{_libdir}/Box2D/qmldir
%{_libdir}/Box2D/libqmlbox2d.so

%changelog
