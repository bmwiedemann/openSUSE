#
# spec file for package qml-box2d
#
# Copyright (c) 2021 SUSE LLC
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


Name:           qml-box2d
Version:        0+git.1523004651.b7212d5
Release:        0
Summary:        QML Box2D plugin
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/%{name}/%{name}
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Quick)

%description
This plugin is meant to be installed to your Qt/imports directory, or shipped
in a directory of which the parent is added as import path.

The goal is to expose the functionality of Box2D as QML components, in order
to make it easy to write physics-based games in QML.

%prep
%setup -q

%build
# FIXME: you should use the %%qmake5 macro
qmake-qt5 QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags}" QMAKE_STRIP="/bin/true";
%make_build

%install
make VERBOSE=1 %{?_smp_mflags} INSTALL_ROOT=%{buildroot} install

rm -rf "%{buildroot}%{_libdir}/qt5/tests"

%files
%license COPYING
%doc README.md
%{_libdir}/qt5/

%changelog
