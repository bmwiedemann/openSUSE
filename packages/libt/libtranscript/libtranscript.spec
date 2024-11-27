#
# spec file for package libtranscript
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


Name:           libtranscript
%define lname	libtranscript1
Version:        0.3.4
Release:        0
Summary:        A character set conversion library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://os.ghalkes.nl/libtranscript.html
#Git-Clone:	https://github.com/gphalkes/transcript
Source:         https://os.ghalkes.nl/dist/%name-%version.tar.bz2
Source2:        https://os.ghalkes.nl/dist/%name-%version.tar.bz2.sig
Source3:        %name.keyring
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
libtranscript is a character set conversion library which allows
great control over the conversion.

%package -n %lname
Summary:        A character conversion library
Group:          System/Libraries

%description -n %lname
libtranscript is a character set conversion library which allows
great control over the conversion.

%package devel
Summary:        Development files for libtranscript, a character conversion library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libtranscript is a character set conversion library which allows
great control over the conversion.

This subpackage contains libraries and header files for developing
applications that want to make use of libtranscript.

%prep
%autosetup -p1

%build
export CC=gcc
# not autoconf :-/
# includedir intentional, cf. bugzilla.opensuse.org/795968
./configure --prefix="%_prefix" --includedir="%_includedir/transcript" \
	--libdir="%_libdir" --docdir="%_docdir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libtranscript.so.1*
%_libdir/transcript1/
%license COPYING

%files devel
%_includedir/transcript/
%_libdir/libtranscript.so
%_libdir/pkgconfig/libtranscript.pc
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%changelog
