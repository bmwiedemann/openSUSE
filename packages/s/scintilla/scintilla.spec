#
# spec file for package scintilla
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


%define tar_ver 375
%define so_ver 3.0
%define libname libscintilla3
Name:           scintilla
Version:        3.7.5
Release:        0
Summary:        A source code editing component
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://www.scintilla.org
Source:         http://sourceforge.net/projects/scintilla/files/scintilla/%{version}/%{name}%{tar_ver}.tgz
Patch0:         %{name}-shared.patch
BuildRequires:  fdupes
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
Group:          System/Libraries

%description -n %{libname}
Scintilla is a code editing component. It includes features for
editing and debugging source code, such as syntax styling, error
indicators, code completion and call tips. The selection margin can
contain breakpoint markers and the current line. It can use
proportional fonts, multiple fonts and different colors at the same
time.

%package -n libscintilla-devel
Summary:        Development files for Scintilla, a code editing component
Group:          Development/Libraries/C and C++
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
%setup -q -n %{name}
%patch0 -p1

%build
cd gtk
make CFLAGS="%{optflags}" GTK3=1 %{?_smp_mflags} LIBDIR=%{_libdir} -I%{_includedir}/glib-2.0 VERSION=`echo %{so_ver} | sed 's|\.0*|:|'`

%install
mkdir -p %{buildroot}%{_includedir}/%{name}/src
mkdir -p %{buildroot}%{_libdir}
cp include/* %{buildroot}%{_includedir}/%{name}
cp src/*.h %{buildroot}%{_includedir}/%{name}/src
mkdir -p lib
libtool --mode=install install bin/libscintilla.la `pwd`/lib
install -m755 lib/*.so.3 %{buildroot}%{_libdir}
ln -s libscintilla.so.3 %{buildroot}%{_libdir}/libscintilla.so
mkdir -p %{buildroot}/%{_defaultdocdir}
mv doc %{buildroot}/%{_defaultdocdir}/%{name}
cp License.txt %{buildroot}/%{_defaultdocdir}/%{name}
rmdir %{buildroot}%{_includedir}/%{name}/src || :
%fdupes -s %{buildroot}/%{_defaultdocdir}/%{name}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libscintilla.so.3

%files -n libscintilla-devel
%defattr(-,root,root)
%{_libdir}/libscintilla.so
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/*
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%changelog
