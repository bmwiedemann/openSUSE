#
# spec file for package slop
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           slop
%define lname	libslopy7_6
Version:        7.6
Release:        0
Summary:        Tool to query for a screen region selection
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/naelstrof/slop
Source0:        https://github.com/naelstrof/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         slop-glew_config_compat.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  glm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(xrandr)

%description
slop (Select Operation) queries for a selection from the user and prints
the region to stdout. It grabs the mouse and turns it into a crosshair,
lets the user click and drag to make a selection (or click on a window)
while drawing a pretty box around it, then finally prints the selection's
dimensions to stdout.

%package -n %{lname}
Summary:        Screen region selection library
Group:          System/Libraries
# slop 7.6 wrongly called this package libslopy7_5
Conflicts:      libslopy7_5 = 7.6

%description -n %{lname}
This library implements the slop utility's functionality to mark a
region ont the screen.

%package devel
Summary:        Development files for the slop library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Header files for the slop library.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{lname}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/*.1%{?ext_man}

%files -n %{lname}
%{_libdir}/libslopy.so.7*

%files devel
%{_includedir}/*
%{_libdir}/libslopy.so

%changelog
