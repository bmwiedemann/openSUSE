#
# spec file for package gio-qt
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 Hillwood Yang <hillwood@opensuse.org>
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

%define   libver          0

Name:           gio-qt
Version:        0.0.9
Release:        0
Summary:        A Qt wrapper library for Gio
License:        GPL-3.0-or-later
Group:          System/GUI/Other
Url:            https://github.com/linuxdeepin/gio-qt
Source0:        https://github.com/linuxdeepin/gio-qt/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         drop-invalid-file.patch
BuildRequires:  fdupes
BuildRequires:  doxygen
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  cmake >= 3.12.4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a Qt wrapper library for Gio (or say it's a glib/glibmm wrapper mainly
focused on GIO module). This library is designed to be exception-free and avoid
Qt application developer do direct access to glib/glibmm (so they can use Gio in
a more Qt way).

%package -n lib%{name}%{libver}
Summary:        A Qt wrapper library for Gio
Group:          System/Libraries

%description -n lib%{name}%{libver}
This is a Qt wrapper library for Gio (or say it's a glib/glibmm wrapper mainly
focused on GIO module). This library is designed to be exception-free and avoid
Qt application developer do direct access to glib/glibmm (so they can use Gio in
a more Qt way).

%package devel
Summary:        Development tools for gio-qt
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{libver} = %{version}

%description devel
The gio-qt-devel package contains the header files and developer
docs for gio-qt.


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{libver} -p /sbin/ldconfig
%postun -n lib%{name}%{libver} -p /sbin/ldconfig


%files -n lib%{name}%{libver}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog

