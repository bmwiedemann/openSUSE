#
# spec file for package tktable
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tktable
BuildRequires:  autoconf
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(x11)
Version:        2.10
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A Table/Matrix Widget Extension to Tcl/Tk
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Source:         http://sourceforge.net/projects/tktable/files/tktable/%version/Tktable%version.tar.gz
Requires:       tcl >= %{tcl_version}
Requires:       tk >= %{tcl_version}

%description
The basic features of the widgets are:

* multi-line cells

* support for embedded windows (one per cell)

* row & column spanning

* variable width/height columns/rows (interactively re-sizable)

* row and column titles

* multiple data sources ((Tcl array || Tcl command) &| internal
   caching)

* supports standard Tk reliefs, fonts, colors, etc.

* x/y scrollbar support

* 'tag' styles per row, column or cell to change visual appearance

* in-cell editing - returns value back to data source

* support for disabled (read-only) tables or cells (via tags)

* multiple selection modes, with "active" cell

* multiple drawing modes to get optimal performance for larger
   tables

* optional 'flashes' when things update

* cell validation support

* works everywhere Tk does (including Windows and Mac!)

* unicode support (Tk8.1+)



Authors:
--------
    Jeffrey Hobbs <jeff.hobbs@acm.org>

%prep
%setup -q -n Tktable%{version}
chmod 644 README* demos/tcllogo.gif

%build
autoconf
export CFLAGS="%optflags"
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	--with-tcl=%_libdir \
	--with-tk=%_libdir \
	--mandir=%_mandir
make

%install
make install DESTDIR=%buildroot pkglibdir=%tcl_archdir/%name%version
mkdir -p %buildroot%_mandir/mann
install -m 644 doc/tkTable.n %buildroot%_mandir/mann

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%_mandir/mann/*
%tcl_archdir/*
%doc ChangeLog README.blt README.txt
%doc TODO.txt license.txt
%doc demos doc/tkTable.html

%changelog
