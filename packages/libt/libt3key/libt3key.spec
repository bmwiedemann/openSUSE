#
# spec file for package libt3key
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


Name:           libt3key
%define lname	libt3key1
Version:        0.2.11
Release:        0
Summary:        The Tilde Toolkit's terminal key sequence database library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://os.ghalkes.nl/t3/libt3key.html
#Git-Clone:	https://github.com/gphalkes/t3key
Source:         https://os.ghalkes.nl/dist/%name-%version.tar.bz2
Source2:        https://os.ghalkes.nl/dist/%name-%version.tar.bz2.sig
Source3:        %name.keyring
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libt3config) >= 0.2.5
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

%description
libt3key is library that provides a database of mappings from escape
sequences as generated by different consoles and terminals or
emulators, to key symbols.

%package -n %lname
Summary:        The Tilde Toolkit's terminal key sequence database library
Group:          System/Libraries

%description -n %lname
libt3key is library that provides a database of mappings from escape
sequences as generated by different consoles and terminals or
emulators, to key symbols.

%package devel
Summary:        Development files for libt3key, a terminal key sequence db library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libt3key is library that provides a database of mappings from escape
sequences as generated by different consoles and terminals or
emulators, to key symbols.

This subpackage contains libraries and header files for developing
applications that want to make use of libt3key.

%package utils
Summary:        Utilities for working with libt3key terminal descriptions
Group:          System/Base

%description utils
libt3key is library that provides a database of mappings from escape
sequences as generated by different consoles and terminals or
emulators, to key symbols.

This subpackage contains the t3learnkeys and t3keyc programs.

%prep
%autosetup -p1

%build
export CC=gcc
# not autoconf :-/
./configure --prefix="%_prefix" --includedir="%_includedir/t3/key" \
	--libdir="%_libdir" --docdir="%_docdir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
chmod a+x "%buildroot/%_libdir"/*.so*
%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libt3key.so.1*
%_datadir/%lname/
%license COPYING

%files devel
%_includedir/t3/
%_libdir/libt3key.so
%_libdir/pkgconfig/libt3key.pc
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%files utils
%_bindir/t3*
%_mandir/man1/t3*.1*

%changelog
