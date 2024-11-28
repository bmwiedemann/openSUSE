#
# spec file for package nasc
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid com.github.parnold-x.nasc
Name:           nasc
Version:        0.5.4
Release:        0
Summary:        Do maths like a normal person
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://github.com/parnoldx/nasc
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM nasc-fix_gcc9_build.patch
Patch0:         nasc-fix_gcc9_build.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(cln)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libqalculate)
BuildRequires:  pkgconfig(libsoup-2.4)
Requires:       qalculate
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libcln.so) --qf '%%{NAME} >= %%{VERSION}')

%description
This is an application where you do calculations "like a normal
person". It lets you type whatever you want, smartly figures out what
computations are needed, and outputs an answer on the right pane.
Then you can plug those answers in to future equations and if that
answer changes, so does the equations it is used in.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wno-implicit-function-declaration"
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/qalculate/

%changelog
