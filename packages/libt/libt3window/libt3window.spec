#
# spec file for package libt3window
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libt3window
%define lname	libt3window0
Version:        0.3.2
Release:        0
Summary:        The Tilde Toolkit's window-based terminal program library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            http://os.ghalkes.nl/t3/libt3window.html

#Git-Clone:	git://github.com/gphalkes/t3widget
Source:         http://os.ghalkes.nl/dist/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libtranscript) >= 0.2.2

%description
libt3window library provides functions for manipulating the terminal
and for creating (possibly overlapping) windows on a terminal.
libt3window can be used instead of (n)curses for drawing on the
terminal.

%package -n %lname
Summary:        The Tilde Toolkit's window-based terminal program library
Group:          System/Libraries

%description -n %lname
libt3window library provides functions for manipulating the terminal
and for creating (possibly overlapping) windows on a terminal.
libt3window can be used instead of (n)curses for drawing on the
terminal.

%package devel
Summary:        Development files for libt3window, a library for window-based terminal drawing
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libt3window library provides functions for manipulating the terminal
and for creating (possibly overlapping) windows on a terminal.
libt3window can be used instead of (n)curses for drawing on the
terminal.

This subpackage contains libraries and header files for developing
applications that want to make use of libt3window.

%prep
%setup -q

%build
export CC=gcc
%configure --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post   -p /sbin/ldconfig -n %lname
%postun -p /sbin/ldconfig -n %lname

%files -n %lname
%defattr(-,root,root)
%_libdir/libt3window.so.0*
%doc COPYING

%files devel
%defattr(-,root,root)
%_includedir/t3/
%_libdir/libt3window.so
%_libdir/pkgconfig/libt3window.pc
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%changelog
