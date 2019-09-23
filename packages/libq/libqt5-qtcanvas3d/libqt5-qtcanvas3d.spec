#
# spec file for package libqt5-qtcanvas3d
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

%define qt5_snapshot 0

%define libname libQt5Canvas3D5

Name:           libqt5-qtcanvas3d
Version:        5.12.3
Release:        0
Summary:        Qt 5 Canvas3D Addon
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.12.3
%define so_version 5.12.3
%define tar_version qtcanvas3d-everywhere-src-5.12.3
Source:         https://download.qt.io/official_releases/qt/5.12/%{real_version}/submodules/%{tar_version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel >= %{version}
BuildRequires:  libQt5Gui-private-headers-devel >= %{version}
BuildRequires:  libqt5-qtbase-devel >= %{version}
BuildRequires:  libqt5-qtdeclarative-private-headers-devel >= %{version}
BuildRequires:  libQt5OpenGLExtensions-devel-static >= %{version}
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt Canvas 3D module provides a way to make OpenGL-like 3D drawing calls from Qt Quick JavaScript.

Qt Canvas3D is a fully supported Qt module starting from Qt 5.5. 
Just like WebGL, Canvas3D offers a low level OpenGL-like API that enables you to execute 3D drawing commands from JavaScript.
It allows easy porting of WebGL content from HTML to Qt Quick or even sharing the same WebGL code between Qt Quick and HTML applications.


%package examples
Summary:        Qt5 Canvas 3D examples
Group:          Development/Libraries/X11
Recommends:     %{name}

%description examples
Examples for libqt5-qtcanvas3d module.

%prep
%setup -q -n %{tar_version}

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

%files
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_archdatadir}/qml/

%files examples
%defattr(-,root,root,755)
%doc LICENSE.*
%{_libqt5_examplesdir}/

%changelog
