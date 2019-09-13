#
# spec file for package libtranscript
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


Name:           libtranscript
%define lname	libtranscript1
Version:        0.3.3
Release:        0
Summary:        A character set conversion library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            http://os.ghalkes.nl/libtranscript.html

#Git-Clone:	git://github.com/gphalkes/transcript
Source:         http://os.ghalkes.nl/dist/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%_libdir/libtranscript.so.1*
%doc COPYING
%_libdir/transcript1/

%files devel
%defattr(-,root,root)
%_includedir/transcript/
%_libdir/libtranscript.so
%_libdir/pkgconfig/libtranscript.pc
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%changelog
