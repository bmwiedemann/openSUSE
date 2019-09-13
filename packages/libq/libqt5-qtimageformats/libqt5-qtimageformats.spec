#
# spec file for package libqt5-qtimageformats
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           libqt5-qtimageformats
Version:        5.13.1
Release:        0
Summary:        Qt 5 Image Format Plugins
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-only
Group:          Development/Libraries/X11
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.13.1
%define so_version 5.13.1
%define tar_version qtimageformats-everywhere-src-5.13.1
Source:         https://download.qt.io/official_releases/qt/5.13/%{real_version}/submodules/%{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libmng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig(Qt5Gui) >= %{version}
BuildRequires:  pkgconfig(libwebp)
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  xz
%requires_ge libQt5Gui5

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %name = %version
Requires:       libmng-devel
Requires:       libtiff-devel
Requires:       pkgconfig(Qt5Gui) >= %{version}
Requires:       pkgconfig(libwebp)

%description devel
Qt is a set of libraries for developing applications.

This package contains qtimageformats.

You need this package, if you want to compile programs with qtimageformats.


%prep
%setup -q -n %{tar_version}

%build
%if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5 -- -system-tiff -system-webp -mng
%make_jobs

%install
%qmake5_install

%files
%doc LICENSE.*
%dir %{_libqt5_archdatadir}
%dir %{_libqt5_plugindir}
%{_libqt5_plugindir}/imageformats/*.so

%files devel
%doc LICENSE.*
%{_libqt5_libdir}/cmake/Qt5Gui/Qt5Gui_Q*Plugin.cmake

%changelog
