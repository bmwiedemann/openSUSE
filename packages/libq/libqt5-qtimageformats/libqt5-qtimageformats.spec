#
# spec file for package libqt5-qtimageformats
#
# Copyright (c) 2020 SUSE LLC
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


%define qt5_snapshot 1
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtimageformats-everywhere-src-%{version}
Name:           libqt5-qtimageformats
Version:        5.15.8+kde6
Release:        0
Summary:        Qt 5 Image Format Plugins
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libmng-devel
BuildRequires:  libtiff-devel
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Gui) >= %{real_version}
BuildRequires:  pkgconfig(libwebp)
%requires_ge    libQt5Gui5

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%package devel
Summary:        Qt Development Kit
Group:          Development/Libraries/X11
Requires:       %{name} = %{version}
Requires:       libmng-devel
Requires:       libtiff-devel
Requires:       pkgconfig(Qt5Gui) >= %{real_version}
Requires:       pkgconfig(libwebp)

%description devel
Qt is a set of libraries for developing applications.

This package contains qtimageformats.

You need this package, if you want to compile programs with qtimageformats.

%prep
%autosetup -p1 -n %{tar_version}

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5 -- -system-tiff -system-webp -mng
%make_jobs

%install
%qmake5_install

%files
%license LICENSE.*
%dir %{_libqt5_archdatadir}
%dir %{_libqt5_plugindir}
%{_libqt5_plugindir}/imageformats/*.so

%files devel
%license LICENSE.*
%{_libqt5_libdir}/cmake/Qt5Gui/Qt5Gui_Q*Plugin.cmake

%changelog
