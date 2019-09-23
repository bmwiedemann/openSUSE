#
# spec file for package qml-box2d
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qml-box2d
Version:        0+git.1451747535.1b37be7
Release:        0
Summary:        QML Box2D plugin
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            https://github.com/%{name}/%{name}
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libBox2D-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Quick)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin is meant to be installed to your Qt/imports directory, or shipped
in a directory of which the parent is added as import path.

The goal is to expose the functionality of Box2D as QML components, in order
to make it easy to write physics-based games in QML.

%prep
%setup -q

%build
qmake-qt5 DEFINES+=BOX2D_SYSTEM  QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags" QMAKE_STRIP="/bin/true";
make VERBOSE=1 %{?_smp_mflags}

%install
make VERBOSE=1 %{?_smp_mflags} INSTALL_ROOT="%{buildroot}" install

rm -rf "%{buildroot}%{_libdir}/qt5/tests"

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/qt5/

%changelog
