#
# spec file for package libt3config
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


Name:           libt3config
%define lname	libt3config0
Version:        0.2.11
Release:        0
Summary:        The Tilde Toolkit's library for reading and writing configuration files
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            http://os.ghalkes.nl/t3/libt3config.html

#Git-Clone:	git://github.com/gphalkes/t3config
Source:         http://os.ghalkes.nl/dist/%name-%version.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The libt3config library provides functions for reading and writing
simple structured configuration files.

%package -n %lname
Summary:        The Tilde Toolkit's library for reading and writing configuration files
Group:          System/Libraries

%description -n %lname
The libt3config library provides functions for reading and writing
simple structured configuration files.

%package devel
Summary:        Development files for libt3config, a library for reading/writing config files
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The libt3config library provides functions for reading and writing
simple structured configuration files.

This subpackage contains libraries and header files for developing
applications that want to make use of libt3config.

%prep
%setup -q

%build
# The default compiler we use is called 'gcc', not c99
export CC=gcc
# not autoconf, but at least it ignores unknown arguments
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
%_libdir/libt3config.so.0*
%doc COPYING

%files devel
%defattr(-,root,root)
%_includedir/t3/
%_libdir/libt3config.so
%_libdir/pkgconfig/libt3config.pc
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%changelog
