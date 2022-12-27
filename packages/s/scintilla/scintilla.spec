#
# spec file for package scintilla
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


%define so_ver 5.3
%define _ver %{so_ver}.2
%define tar_ver 532
%define libname libscintilla5
Name:           scintilla
Version:        %{_ver}
Release:        0
Summary:        A source code editing component
License:        MIT
URL:            http://www.scintilla.org
Source:         http://sourceforge.net/projects/scintilla/files/scintilla/%{version}/%{name}%{tar_ver}.tgz
Patch0:         %{name}-shared.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Scintilla is a code editing component. It includes features for
editing and debugging source code, such as syntax styling, error
indicators, code completion and call tips. The selection margin can
contain breakpoint markers and the current line. It can use
proportional fonts, multiple fonts and different colors at the same
time.

%package -n %{libname}
Summary:        A source code editing component

%description -n %{libname}
Scintilla is a code editing component. It includes features for
editing and debugging source code, such as syntax styling, error
indicators, code completion and call tips. The selection margin can
contain breakpoint markers and the current line. It can use
proportional fonts, multiple fonts and different colors at the same
time.

%package -n libscintilla-devel
Summary:        Development files for Scintilla, a code editing component
Requires:       %{libname} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gtk+-3.0)

%description -n libscintilla-devel
Scintilla is a code editing component. It includes features for
editing and debugging source code, such as syntax styling, error
indicators, code completion and call tips.

This subpackage contains the header files for developing
applications that want to make use of the Scintilla library.

%prep
%autosetup -p1 -n %{name}

%build
%make_build -C gtk GTK3=1 LIBDIR=%{_libdir} VERSION=`echo %{so_ver} | sed 's|\.0*|:|'` static

%install
mkdir -p %{buildroot}%{_includedir}/%{name}/src
cp include/* %{buildroot}%{_includedir}/%{name}
cp src/*.h %{buildroot}%{_includedir}/%{name}/src

mkdir -p %{buildroot}%{_libdir}
libtool --mode=install install bin/libscintilla.la %{buildroot}%{_libdir}
# Delete libtool archive and static lib
find %{buildroot}%{_libdir} -name "*.a" -delete -print
find %{buildroot}%{_libdir} -name "*.la" -delete -print

rmdir %{buildroot}%{_includedir}/%{name}/src || :

%post -n %{libname} -p %run_ldconfig
%postun -n %{libname} -p %run_ldconfig

%files -n %{libname}
%license License.txt
%{_libdir}/libscintilla.so.*

%files -n libscintilla-devel
%license License.txt
%doc doc
%{_libdir}/libscintilla.so
%{_includedir}/%{name}/

%changelog
